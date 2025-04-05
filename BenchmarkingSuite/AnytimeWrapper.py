import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
import importlib.util
import time
import threading
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score

import sys
import os

# Add the parent directory to the Python path so there is seperation but can import generator
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

# Import the RFPyAnytimeGenerator class
from AnytimeMLGenerators.RFCPythonGenerator import RFPyAnytimeGenerator


class AnytimeBenchmarkTester(BaseEstimator, ClassifierMixin):
    """Wrapper for dynamically generated classifier functions with anytime stopping support."""
    def __init__(self, flag=None):
        # If no flag is provided, create one.
        self.flag = flag if flag is not None else threading.Event()
        self.classifier_fn = None  # To be loaded from module

    def load_classifier(self, module_path):
        """Dynamically load the generated classifier function."""
        spec = importlib.util.spec_from_file_location("rfm", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.classifier_fn = module.classifier  # Expects: classifier(x, results, deadline, flag)

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
        
        def wrapper(idx, sample, predictions, delays):
            deadline = time.time() + timeout
            # Call classifier_fn with the sample, results list, deadline, and the interrupt flag.
            result = self.classifier_fn(sample, results[idx], deadline, self.flag)
            predictions.append(result)
            delays.append(time.time() - deadline) # Get time between when it should have been stopped and when it actually stopped
                      
        deadlines = []
        delays = []
        for idx, sample in enumerate(X):
            deadlines.append(time.time() + timeout)
            t = threading.Thread(target=wrapper, args=(idx, sample, predictions, delays))
            threads.append(t)
            t.start()
        
        # Wait for all threads to finish
        for t in threads:
            t.join()
        
        return predictions, delays

    def get_full_time(self, samples, iters=5):
        """

        Args:
            X: Input samples.
        
        Returns:
        """
        samples = np.array(samples, dtype=np.float32)  # Ensure correct data type
        num_samples = len(samples)
        results = [[] for _ in range(num_samples)]  # Each sample’s partial tree results
        threads = []
        
        def full_run(idx, sample, predictions, latency):
            now = time.time()
            # Call classifier_fn with the sample, results list, deadline, and the interrupt flag.
            predictions.append(self.classifier_fn(sample, results[idx], np.inf, self.flag)[0])
            latency.append(time.time() - now) # Get time it has taken to classify and predict on all 100 trees
                      
        predictions = []
        max_latencies = []
        
        for i in range(iters):
            latency = []
            threads = []  # Reset threads for each iteration
            for idx, sample in enumerate(samples):
                t = threading.Thread(target=full_run, args=(idx, sample, predictions, latency))
                threads.append(t)
                t.start()
            
            # Wait for all threads to complete
            for t in threads:
                t.join()
            
            # Now calculate max latency after all threads have finished
            max_latencies.append(max(latency))
        median_latency = np.median(max_latencies)
        return median_latency

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
                    predictions, delays = self.predict_thread(X_test, timeout=time_limit)

                    # Collect the accuracy for this iteration of the fold
                    y_pred = np.array([pred[0] for pred in predictions])
                    accuracies.append(accuracy_score(y_test, y_pred))

                    # Calculate the maximum delay for this iteration
                    max_delays.append(np.max(delays))
                    
                    # Calculate the average number of trees processed per sample
                    n_trees = np.array([pred[1] for pred in predictions])
                    avg_trees.append(np.mean(n_trees))

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


        return time_accuracies

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