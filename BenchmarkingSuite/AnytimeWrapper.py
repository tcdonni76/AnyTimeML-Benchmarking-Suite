import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
import importlib.util
import time
import threading
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
        print("Reached full time")
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
            classifier_name = f"./Classifiers/{dataset_name}_{model_name}.py"

        # Load in the generator to generate the if-else statements
        generator = RFPyAnytimeGenerator(model)
        # Generate the classifier for all samples to get the maximum time
        generator.generate(X, y, "random_forest_model.py")

        # Load in the classifier file from the current fold
        self.load_classifier("random_forest_model.py")

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
            f1_scores = []              # Store metrics for
            precision_scores = []       # each fold
            recall_scores = []          #
            all_y_true = []             #
            all_y_pred_proba = []       #

            for i in range(iters): # Iterate through to smooth out inconsistencies from threading
                print(f"ITERATION: {i+1}/{iters}")
                for train_index, test_index in kf.split(X, y):  # Pass both X and y to KFold.split()
                    X_train, X_test = X[train_index], X[test_index]
                    y_train, y_test = y[train_index], y[test_index]

                    # Train the model
                    generator.generate(X_train, y_train, f"classifier_fold.py")

                    # Load the classifier and voter
                    self.load_classifier("classifier_fold.py")

                    # Predict with a timeout
                    predictions, _ = self.predict_thread(X_test, timeout=time_limit)

                    # Collect the accuracy for this iteration of the fold
                    y_pred = np.array([pred[0] for pred in predictions])
                    accuracies.append(accuracy_score(y_test, y_pred))
                    
                    # Calculate the average number of trees processed per sample
                    n_trees = np.array([pred[1] for pred in predictions])
                    avg_trees.append(np.mean(n_trees))

                    # Calculate other metrics for this iteration of the fold
                    f1_scores.append(f1_score(y_test, y_pred, average='weighted', zero_division=0))
                    precision_scores.append(precision_score(y_test, y_pred, average='weighted', zero_division=0))
                    recall_scores.append(recall_score(y_test, y_pred, average='weighted', zero_division=0))
                    confusion_matrices.append(confusion_matrix(y_test, y_pred, labels=all_labels).tolist()) 

            # Calculate mean accuracy, standard deviation, and confidence interval
            mean_accuracy = np.mean(accuracies)
            std_accuracy = np.std(accuracies)
            conf_interval = 1.96 * std_accuracy / np.sqrt(len(accuracies))  # 95% confidence interval

            av_trees = np.mean(avg_trees)

            # Calculate other metrics
            mean_f1 = np.mean(f1_scores)
            mean_precision = np.mean(precision_scores)
            mean_recall = np.mean(recall_scores)

            # Construct the dictionary to pass to the JSON results file
            time_accuracies[time_limit] = {
                "accuracy": mean_accuracy, # Mean accuracy across the fold
                "std": std_accuracy, # Standard deviation of accuracies across the fold
                "avg_trees": av_trees, # The average number of trees processed per sample over the fold
                "conf. interval": conf_interval, # Confidence interval of the mean accuracy
                "upper_bound": min(mean_accuracy + conf_interval, 1.0),  # Upper bound of confidence interval
                "lower_bound": max(mean_accuracy - conf_interval, 0.0),   # Lower bound of confidence interval
                "confusion_matrices": confusion_matrices,  # Store confusion matrices for all folds
                "f1": mean_f1, # Average F1 score across the fold
                "precision": mean_precision, # Average precision across the fold
                "recall": mean_recall # Average recall across the fold
            }
            print(f"Accuracy: {mean_accuracy:.4f} ± {conf_interval:.4f}")
            count += 1


        return time_accuracies

    def fit(self, X, y):
        """Dummy method to comply with sklearn interface."""
        return self