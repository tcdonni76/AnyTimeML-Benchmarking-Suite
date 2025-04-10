import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
import importlib.util
import time
import threading
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
import multiprocessing as mp
from multiprocessing import Pool

import sys
import os
import gc

# Add the parent directory to the Python path so there is seperation but can import generator
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

# Import the RFPyAnytimeGenerator class
from AnytimeMLGenerators.RFCPythonGenerator import RFPyAnytimeGenerator
from sklearn.datasets import fetch_openml
# from tensorflow.keras.datasets import cifar10

classifier_fn = None

class AnytimeBenchmarkTester(BaseEstimator, ClassifierMixin):

    def load_classifier(self, module_path):
        """Dynamically load the generated classifier function."""
        global classifier_fn
        spec = importlib.util.spec_from_file_location("rfm", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if not hasattr(module, 'classifier'):
            raise ValueError(f"Module {module_path} does not have a 'classifier' function.")
        classifier_fn = module.classifier  # Expects: classifier(x, result)
        print(f"Global classifier_fn: {classifier_fn}")

    def predict_thread(self, X, timeout):
        """
        Make predictions with a deadline (timeout) mechanism.
        
        For each sample, a separate thread is started. Each thread:
          - Computes its own deadline (current time + timeout)
          - Calls the classifier function, which processes trees until either the deadline is reached or the user-triggered interrupt flag is set.
          - Optionally, a dictionary is passed to record the actual stop time.
          
        After all threads join, the voting logic is applied to each sample’s partial results.
        
        Args:
            X: Input samples.
            timeout: Time limit per sample (in seconds).
        
        Returns:
            nothing but it does append to lists of the following:
                predictions: Array of predictions.
                delays: Array of (actual_stop_time - deadline) for each sample.
        """
        X = np.array(X, dtype=np.float32)  # Ensure correct data type
        num_samples = len(X)
        results = [[] for _ in range(num_samples)]  # Each sample’s partial tree results
        # If we want to record stop times, create a list of dictionaries.
        threads = []
        predictions = []  # List to store predictions for each sample
        
        classifier_path = './test_multiprocessing_classifier.py'  # Path to the classifier file
        manager = mp.Manager()
        res = manager.dict()  # Shared dictionary to store results   
        delays = []
        batch_size = len(X)
        for batch_start in range(0, len(X), batch_size):
            print(f"Batch start: {batch_start} / {len(X)}")
            batch_end = min(batch_start + batch_size, len(X))
            batch = X[batch_start:batch_end]
            # Create and start processes for the current batch
            processes = []
            for idx, sample in enumerate(batch, start=batch_start):
                p = mp.Process(target=self.worker, 
                            args=(sample, res, idx, timeout, classifier_path))
                processes.append(p)
                p.start()

            # Wait for all processes to complete
            for p in processes:
                deadline = time.time() + timeout
                p.join(deadline)
                if p.is_alive():
                    print(f"Process {p.pid} timed out, terminating.")
                    p.terminate()
                    p.join()
                print(time.time() - deadline)
        
        return predictions, delays

    def worker(self, sample, res, idx, timeout, classifier_path):
        try:
            self.load_classifier(classifier_path)

            res[idx] = []  # Initialize the result list for this sample
            # Calculate deadline
            deadline = time.time() + timeout
            # Process the sample - create an empty result list for this sample
            classifier_fn(sample, res[idx])  # Call the classifier function with the sample and result list
            print(res[idx], time.time() - deadline)
        except Exception as e:
            print(f"Error in worker process: {e}")

    def get_full_time(self, samples, iters=5, batch_size=10):
        """
        Calculate the maximum time needed to process all trees for a single sample using multiprocessing in batches.

        Args:
            samples: Input samples.
            iters: Number of iterations for timing.
            batch_size: Number of samples to process in each batch.

        Returns:
            median_latency: Minimum of the maximum latencies across all iterations.
        """
        samples = np.array(samples, dtype=np.float32)  # Ensure correct data type
        num_samples = len(samples)
        manager = mp.Manager()
        results = manager.dict()  # Shared dictionary to store results
        max_latencies = []

        # Process the dataset in batches
        for i in range(iters):
            print(f"Iteration {i+1}/{iters}")
            latency = manager.list()  # Shared list to store latencies for the current iteration
            for batch_start in range(0, num_samples, batch_size):
                batch_end = min(batch_start + batch_size, num_samples)
                batch = samples[batch_start:batch_end]

                # Create and start processes for the current batch
                processes = []
                for idx, sample in enumerate(batch, start=batch_start):
                    p = mp.Process(target=self.worker, args=(sample, idx, results, latency, classifier_fn))
                    processes.append(p)
                    p.start()

                # Wait for processes to complete or terminate them after timeout
                for p in processes:
                    p.join()
                    if p.is_alive():
                        print(f"Terminating process {p.pid} due to timeout.")
                        p.terminate()

            # Calculate the maximum latency for this iteration
            if latency:
                max_latencies.append(max(latency))

        # Calculate the median of the maximum latencies across all iterations
        median_latency = np.min(max_latencies) if max_latencies else 0
        return median_latency
    
    def full_run(self, idx, sample, predictions, latency, res):
        global classifier_fn
        now = time.time()
        # Call classifier_fn with the sample, results list, deadline, and the interrupt flag.
        predictions.append(classifier_fn(sample, res[idx], np.inf)[0])
        latency.append(time.time() - now) # Get time it has taken to classify and predict on all 100 trees

    def conduct_test(self, X, y, model, model_name, dataset_name, iters=5, classifier_name=None):
        """
        Args:
            X: Input samples.
            y: Target labels.
            model: The model to train.
            generator: The generator for creating classifier code.
            iters: Number of iterations for timing. The more iterations the smoother the metrics will be.
            dataset_name: Name of the dataset. Used to generate the file name.
            model_name: Name of the model. Used to generate the file name.
        
        Returns:
            time_accuracies: Dictionary of accuracies and statistics for different time limits.
        """
        print("Starting conduct_test...")
        # If no file name has been given
        if classifier_name is None:
            classifier_name = f"BenchmarkingSuite/Classifiers/{dataset_name}_{model_name}.py"

        # Load in the generator to generate the if-else statementsfor RFC
        if isinstance(model, RandomForestClassifier):
            generator = RFPyAnytimeGenerator(model, dataset_name)
        else:
            generator = None

        # This is ran so if RFC generator is uesed then it can generate for the current data, if not returns provided classifier name
        # This is ran first to get the max time
        self.determine_classifier(generator, X, y, model_name, dataset_name, classifier_name)

        # Load in the classifier file from the current fold
        self.load_classifier(classifier_name)

        time_accuracies = {}

        print("AT TESTING MAX TIME")

        # Train the model to get the maximum time
        max_time = self.get_full_time(X, iters=5)  # Get the maximum time needed to process all trees for a single sample
        print(f'MAX TIME: {max_time}')
        # Get evenly spaced time limits between 0 and calculated max time
        times = np.arange(0, max_time + 0.05 * max_time, 0.05 * max_time)

        all_labels = np.unique(y)

        kf = KFold(n_splits=5, shuffle=True, random_state=42)  # 5-fold cross-validation
        count = 1
        for time_limit in times:
            print(f"TESTING TIME LIMIT: {time_limit}, {count}/{len(times)}")
            accuracies = []             #
            avg_trees = []              # 
            confusion_matrices = []     #  
            f1_scores = []              #   
            precision_scores = []       # Store metrics for each iteration of each fold
            recall_scores = []          #   
            all_y_true = []             #  
            all_y_pred_proba = []       # 
            max_delays = []             # 

            for i in range(iters): # Iterate through to smooth out inconsistencies from threading
                print(f"ITERATION: {i+1}/{iters}")
                fold_count = 1
                for train_index, test_index in kf.split(X, y):  # Pass both X and y to KFold.split()
                    X_train, X_test = X[train_index], X[test_index]
                    y_train, y_test = y[train_index], y[test_index]

                    # This is ran so if RFC generator is uesed then it can generate for the current data, if not returns provided classifier name
                    self.determine_classifier(generator, X_train, y_train, model_name, dataset_name, classifier_name, fold_count)

                    # Load the classifier
                    self.load_classifier(classifier_name)

                    # Predict with a timeout
                    predictions, delays = self.predict_with_multiprocessing(X_test, timeout=time_limit)

                    # Collect the accuracy for this iteration of the fold
                    y_pred = np.array([pred[0] for pred in predictions])
                    accuracies.append(accuracy_score(y_test, y_pred))

                    # Calculate the maximum delay for this iteration
                    max_delays.append(np.max(delays))
                    
                    # Calculate the average number of trees processed per sample
                    n_trees = np.array([pred[1] for pred in predictions])
                    avg_trees.append(np.mean(n_trees))

                    print(f"Accuracy: {accuracies[-1]:.4f},\tTrees: {avg_trees[-1]:.4f},\tMax Delay: {max_delays[-1]:.4f}")

                    # Calculate other metrics for this iteration of the fold
                    f1_scores.append(f1_score(y_test, y_pred, average='weighted', zero_division=0))
                    precision_scores.append(precision_score(y_test, y_pred, average='weighted', zero_division=0))
                    recall_scores.append(recall_score(y_test, y_pred, average='weighted', zero_division=0))
                    confusion_matrices.append(confusion_matrix(y_test, y_pred, labels=all_labels).tolist()) 
                    fold_count += 1

            # Calculate mean accuracy, standard deviation, and confidence interval
            mean_accuracy = np.median(accuracies)
            std_accuracy = np.std(accuracies)
            conf_interval = 1.96 * std_accuracy / np.sqrt(len(accuracies))  # 95% confidence interval

            av_trees = np.median(avg_trees)

            # Calculate other metrics
            mean_f1 = np.median(f1_scores)
            std_f1 = np.std(f1_scores)
            conf_interval_f1 = 1.96 * std_f1 / np.sqrt(len(f1_scores))

            mean_precision = np.median(precision_scores)
            std_precision = np.std(precision_scores)
            conf_interval_precision = 1.96 * std_precision / np.sqrt(len(precision_scores))

            mean_recall = np.median(recall_scores)
            std_recall = np.std(recall_scores)
            conf_interval_recall = 1.96 * std_recall / np.sqrt(len(recall_scores))
            
            mean_max_delay = np.median(max_delays)
            std_max_delay = np.std(max_delays)
            conf_interval_max_delay = 1.96 * std_max_delay / np.sqrt(len(max_delays))

            confusion_matrices = np.round(np.mean(confusion_matrices, axis=0)).tolist()  # Average and round confusion matrices across folds

            # Construct the dictionary to pass to the JSON results file
            time_accuracies[time_limit] = {
                # Accuracy metrics
                "acc": mean_accuracy, # Mean accuracy across the fold
                "acc_std": std_accuracy, # Standard deviation of accuracies across the fold
                "acc_upper_bound": min(mean_accuracy + conf_interval, 1.0),  # Upper bound of confidence interval
                "acc_lower_bound": max(mean_accuracy - conf_interval, 0.0),   # Lower bound of confidence interval

                # Tree metrics
                "avg_trees": av_trees, # The average number of trees processed per sample over the fold

                # F1 metrics
                "f1": mean_f1, # Average F1 score across the fold
                "f1_std": std_f1, # Standard deviation of F1 scores across the fold
                "f1_upper_bound": mean_f1 + conf_interval_f1,  # Upper bound of confidence interval
                "f1_lower_bound": mean_f1 - conf_interval_f1,   # Lower bound of confidence interval

                # Precision metrics
                "precision": mean_precision, # Average precision across the fold
                "precision_std": std_precision, # Standard deviation of precision scores across the fold
                "precision_upper_bound": mean_precision + conf_interval_precision,  # Upper bound of confidence interval
                "precision_lower_bound": mean_precision - conf_interval_precision,   # Lower bound of confidence interval

                # Recall metrics
                "recall": mean_recall, # Average recall across the fold
                "recall_std": std_recall, # Standard deviation of recall scores across the fold
                "recall_upper_bound": mean_recall + conf_interval_recall,  # Upper bound of confidence interval
                "recall_lower_bound": mean_recall - conf_interval_recall,   # Lower bound of confidence interval

                # Delay metrics
                "max_delay": mean_max_delay, # Store the average max delay across the fold
                "max_delay_std": std_max_delay, # Standard deviation of max delays across the fold
                "max_delay_upper_bound": mean_max_delay + conf_interval_max_delay,  # Upper bound of confidence interval
                "max_delay_lower_bound": mean_max_delay - conf_interval_max_delay,   # Lower bound of confidence interval

                # Confusion matrices
                "confusion_matrices": confusion_matrices,  # Store confusion matrices for all folds
                "n": iters  # Amount of samples / iters in the fold
            }
            print(f"Accuracy: {mean_accuracy:.4f} ± {conf_interval:.4f}\t{av_trees} trees")
            count += 1
        print(mean_max_delay)
        return time_accuracies
    
    def predict_with_multiprocessing(self, X, timeout, batch_size=2, classifier_path=None):
        """
        Predict using multiprocessing in batches with a timeout for each sample.
        """
        manager = mp.Manager()
        results = manager.dict()  # Shared dictionary to store results
        predictions = []
        delays = []

        # Process the dataset in batches
        for batch_start in range(0, len(X), batch_size):
            batch_end = min(batch_start + batch_size, len(X))
            batch = X[batch_start:batch_end]

            # Create and start processes for the current batch
            processes = []
            for idx, sample in enumerate(batch, start=batch_start):
                p = mp.Process(target=self.worker, args=(sample, results, idx, timeout, classifier_path))
                processes.append(p)
                p.start()

            # Wait for processes to complete or terminate them after timeout
            for p in processes:
                p.join()
                if p.is_alive():
                    print(f"Terminating process {p.pid} due to timeout.")
                    p.terminate()

            # Collect results for the current batch
            for idx in range(batch_start, batch_end):
                if idx in results and results[idx] is not None:
                    predictions.append(results[idx])
                    delays.append(time.time() - timeout)
                else:
                    predictions.append(None)
                    delays.append(None)

            gc.collect()  # Clear memory after processing the batch

        return predictions, delays

    def worker(self, sample, results, idx, t, classifier_path):
        """Worker function to process a single sample."""
        # Load the classifier function in the worker process
        spec = importlib.util.spec_from_file_location("rfm", classifier_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if not hasattr(module, 'classifier'):
            raise ValueError(f"Module {classifier_path} does not have a 'classifier' function.")
        local_classifier_fn = module.classifier

        # Process the sample
        result = []
        deadline = time.time() + t
        local_classifier_fn(sample, result)
        results[idx] = result

    def determine_classifier(self, generator, X, y, model_name, dataset_name, classifier_name, fold_count=None):
        """
        Generate the classifier function dynamically based on the model type.

        Args:
            model: The model to generate the classifier for.
            model_name: Name of the model.
            dataset_name: Name of the dataset.
            classifier_name: File path to save the generated classifier.
            fold_count: Optional fold count for cross-validation.
        """
        if generator:
            generator.generate(X=X, y=y, fold_number=fold_count, fname=classifier_name)
        else:
            if not os.path.exists(classifier_name):
                raise ValueError(f"Classifier file {classifier_name} does not exist. Please provide.")

    def fit(self, X, y):
        """Dummy method to comply with sklearn interface."""
        return self
    
if __name__ == "__main__":
    wrapper = AnytimeBenchmarkTester()
    # Example usage:
    wrapper.load_classifier("./test_multiprocessing_classifier.py")
    from sklearn.datasets import load_iris
    X, y = load_iris(return_X_y=True)
    X, y = X[:100], y[:100]  # Use only the first 100 samples for testing
    # wrapper.conduct_test(X, y, RandomForestClassifier(), "RandomForestClassifier", "test_dataset", iters=5, classifier_name="test_multiprocessing_classifier.py")
    wrapper.predict_thread(X, 0.00000001)
