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

import psutil
# Get the number of logical cores
num_cores = psutil.cpu_count(logical=True)
print(num_cores)

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
        results = [[-1, 0] for _ in range(num_samples)]  # Give default values of -1 (bad prediction) and 0 (no estimators processed)

        # If we want to record stop times, create a list of dictionaries.
        threads = []
        predictions = []  # List to store predictions for each sample
        
        def wrapper(idx, sample, predictions, delays):
            deadline = time.time() + timeout
            # Call classifier_fn with the sample, results list, deadline, and the interrupt flag.
            self.classifier_fn(sample, results[idx], deadline, self.flag)
            predictions.append(results[idx])
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

    def get_full_time(self, samples, iters=3):
        """
        Calculate the maximum time required to classify all samples using the full set of estimators.

        This method runs the classifier function on all samples with no time limit (deadline set to infinity)
        and measures the time taken for each sample. It repeats the process for a specified number of iterations
        to smooth out inconsistencies caused by threading or system load.

        Args:
            samples (array-like): Input samples to classify.
            iters (int): Number of iterations to repeat the process for consistency. Default is 3.

        Returns:
            float: The minimum of the maximum latencies across all iterations. This represents the 
                   minimum time required to classify all samples using all trees.
        """
        # Ensure the input samples are in the correct data type
        samples = np.array(samples, dtype=np.float32)
        num_samples = len(samples)

        # Initialise results list to store partial tree results for each sample
        results = [[-1, 0] for _ in range(num_samples)]  # Give default values of -1 (bad prediction) and 0 (no estimators processed)

        # Function to run the classifier on a single sample and record its latency
        def full_run(idx, sample, predictions, latency):
            start_time = time.time()
            # Call the classifier function with no deadline (infinite time)
            self.classifier_fn(sample, results[idx], np.inf, self.flag)
            predictions.append(results[idx][0])
            # Record the time taken to classify the sample
            latency.append(time.time() - start_time)
        
        predictions = []  # List to store predictions for all samples
        max_latencies = []  # List to store the maximum latency for each iteration

        # Repeat the process for the specified number of iterations
        for i in range(iters):
            latency = []  # List to store latencies for the current iteration
            threads = []  # Reset threads for each iteration
            # Create and start a thread for each sample
            for idx, sample in enumerate(samples):
                t = threading.Thread(target=full_run, args=(idx, sample, predictions, latency))
                threads.append(t)
                t.start()
            # Wait for all threads to complete
            for t in threads:
                t.join()
            # Record the maximum latency for the current iteration
            max_latencies.append(max(latency))
        # Return the minimum of the maximum latencies across all iterations
        # This ensures we account for the fastest "worst-case" scenario
        lat = np.min(max_latencies)
        return lat

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
            f1_scores = []              # Store metrics for each iteration of each fold
            precision_scores = []       # 
            recall_scores = []          #   
            max_delays = []             # 
            usages = []

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
                    process = psutil.Process()  # Get the current process
                    cpu_before = process.cpu_percent(interval=None)  # CPU usage before prediction
                    predictions, delays = self.predict_thread(X_test, timeout=time_limit)
                    cpu_after = process.cpu_percent(interval=None)  # CPU usage after prediction

                    usages.append((cpu_after - cpu_before) / num_cores)  # Calculate CPU usage for this iteration

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

            # Calculate median accuracy, standard deviation, and confidence interval
            median_accuracy = np.median(accuracies)
            std_accuracy = np.std(accuracies)
            conf_interval = 1.96 * std_accuracy / np.sqrt(len(accuracies))  # 95% confidence interval

            av_trees = np.median(avg_trees)

            # Calculate other metrics
            median_f1 = np.median(f1_scores)
            std_f1 = np.std(f1_scores)
            conf_interval_f1 = 1.96 * std_f1 / np.sqrt(len(f1_scores))

            median_precision = np.median(precision_scores)
            std_precision = np.std(precision_scores)
            conf_interval_precision = 1.96 * std_precision / np.sqrt(len(precision_scores))

            median_recall = np.median(recall_scores)
            std_recall = np.std(recall_scores)
            conf_interval_recall = 1.96 * std_recall / np.sqrt(len(recall_scores))
            
            median_max_delay = np.median(max_delays)
            std_max_delay = np.std(max_delays)
            conf_interval_max_delay = 1.96 * std_max_delay / np.sqrt(len(max_delays))

            confusion_matrices = np.round(np.median(confusion_matrices, axis=0)).tolist()  # Average and round confusion matrices across folds

            # Construct the dictionary to pass to the JSON results file
            time_accuracies[time_limit] = {
                # Accuracy metrics
                "acc": median_accuracy, # median accuracy across the fold
                "acc_std": std_accuracy, # Standard deviation of accuracies across the fold
                "acc_upper_bound": min(median_accuracy + conf_interval, 1.0),  # Upper bound of confidence interval
                "acc_lower_bound": max(median_accuracy - conf_interval, 0.0),   # Lower bound of confidence interval

                # Tree metrics
                "avg_trees": av_trees, # The average number of trees processed per sample over the fold

                # F1 metrics
                "f1": median_f1, # Average F1 score across the fold
                "f1_std": std_f1, # Standard deviation of F1 scores across the fold
                "f1_upper_bound": median_f1 + conf_interval_f1,  # Upper bound of confidence interval
                "f1_lower_bound": median_f1 - conf_interval_f1,   # Lower bound of confidence interval

                # Precision metrics
                "precision": median_precision, # Average precision across the fold
                "precision_std": std_precision, # Standard deviation of precision scores across the fold
                "precision_upper_bound": median_precision + conf_interval_precision,  # Upper bound of confidence interval
                "precision_lower_bound": median_precision - conf_interval_precision,   # Lower bound of confidence interval

                # Recall metrics
                "recall": median_recall, # Average recall across the fold
                "recall_std": std_recall, # Standard deviation of recall scores across the fold
                "recall_upper_bound": median_recall + conf_interval_recall,  # Upper bound of confidence interval
                "recall_lower_bound": median_recall - conf_interval_recall,   # Lower bound of confidence interval

                # Delay metrics
                "max_delay": median_max_delay, # Store the average max delay across the fold
                "max_delay_std": std_max_delay, # Standard deviation of max delays across the fold
                "max_delay_upper_bound": median_max_delay + conf_interval_max_delay,  # Upper bound of confidence interval
                "max_delay_lower_bound": median_max_delay - conf_interval_max_delay,   # Lower bound of confidence interval

                # Confusion matrices
                "confusion_matrices": confusion_matrices,  # Store confusion matrices for all folds

                # Median energy consumption
                "energy": np.median(usages),  # Store the median energy consumption across the fold
                "energy_std": np.std(usages),  # Standard deviation of energy consumption across the fold

                "n": iters  # Amount of samples / iters in the fold
            }
            print(f"Accuracy: {median_accuracy:.4f} ± {conf_interval:.4f}\t{av_trees} trees")
            count += 1

        time_accuracies['auc'] = self.calc_auc(time_accuracies)  # Calculate AUC for the results

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

    def calc_auc(self, results):
        """
        Calculate the AUC (Area Under the Curve) for the given results.

        Args:
            results: Dictionary of results containing accuracy and time metrics.

        Returns:
            auc: The calculated AUC value.
        """
        # Extract time and accuracy values from the results
        times = sorted([float(t) for t in results.keys() if t != 'auc'])  # Exclude 'auc' key
        metrics = ["acc", "f1", "precision", "recall"]
        auc_values = {}

        # Normalize the time values to the range [0, 1]
        min_time = min(times)
        max_time = max(times)
        normalized_times = [(t - min_time) / (max_time - min_time) for t in times]

        for metric in metrics:
            # Extract accuracy values for the current metric
            accuracies = [results[(t)][metric] for t in times]

            # Calculate AUC using the trapezoidal rule
            if len(normalized_times) > 1 and len(accuracies) > 1:
                auc_values[metric] = np.trapezoid(accuracies, normalized_times)
            else:
                auc_values[metric] = 0  # Handle cases with insufficient data

        # Calculate the average AUC across all metrics
        average_auc = np.mean(list(auc_values.values()))
        return average_auc