import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
import importlib.util
import os
import time
import threading
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, confusion_matrix
from RFCPythonGenerator import RandomForestPythonGeneratorTime
import json
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

class GeneratedClassifierWrapperTime(BaseEstimator, ClassifierMixin):
    """Wrapper for dynamically generated classifier functions with anytime stopping support."""
    def __init__(self, flag=None):
        # If no flag is provided, create one.
        self.flag = flag if flag is not None else threading.Event()
        self.classifier_fn = None  # To be loaded from module
        self.voter_fn = None       # To be loaded from module

    def load_classifier(self, module_path):
        """Dynamically load the generated classifier function."""
        spec = importlib.util.spec_from_file_location("rfm", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.classifier_fn = module.classifier  # Expects: classifier(x, results, deadline, flag, [stop_time_recorder])

    def load_voter(self, module_path):
        """Dynamically load the generated voting logic."""
        spec = importlib.util.spec_from_file_location("rfm", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.voter_fn = module.vote_logic  # Expects: vote_logic(results) returns final prediction

    def predict_thread(self, X, timeout, record_stop_time=False):
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
            record_stop_time (bool): If True, pass a dictionary to record the actual stop time.
        
        Returns:
            predictions: Array of predictions.
            delays: Array of (actual_stop_time - deadline) for each sample (if record_stop_time is True), else None.
        """
        X = np.array(X, dtype=np.float32)  # Ensure correct data type
        num_samples = len(X)
        results = [[] for _ in range(num_samples)]  # Each sample’s partial tree results
        # If we want to record stop times, create a list of dictionaries.
        threads = []
        
        def wrapper(idx, sample, deadline, predictions, delays):
            # Call classifier_fn with the sample, results list, deadline, and the interrupt flag.
            self.classifier_fn(sample, results[idx], deadline, self.flag)
            np.append(predictions, self.voter_fn(results[idx])[0])
            delays.append(time.time() - deadline) # Get time between when it should have been stopped and when it actually stopped
                      
        deadlines = []
        predictions = np.empty((1, num_samples))
        delays = []
        for idx, sample in enumerate(X):
            deadlines.append(time.time() + timeout)
            t = threading.Thread(target=wrapper, args=(idx, sample, deadlines[idx], predictions, delays))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        # Perform voting logic on partial results for each sample.
        predictions = np.array([self.voter_fn(results[i]) for i in range(num_samples)])
        
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
        
        def full_run(idx, sample, predictions, latency, now):
            # Call classifier_fn with the sample, results list, deadline, and the interrupt flag.
            self.classifier_fn(sample, results[idx], np.inf, self.flag)
            np.append(predictions, self.voter_fn(results[idx]))
            latency.append(time.time() - now) # Get time it has taken to classify and predict on all 100 trees
                      
        predictions = np.empty((1, num_samples))
        max_latencies = []
        
        for i in range(iters):
            latency = []
            threads = []  # Reset threads for each iteration
            for idx, sample in enumerate(samples):
                now = time.time()
                t = threading.Thread(target=full_run, args=(idx, sample, predictions, latency, now))
                threads.append(t)
                t.start()
            
            # Wait for all threads to complete
            for t in threads:
                t.join()
            
            # Now calculate max latency after all threads have finished
            max_latencies.append(max(latency))
        
        return round(np.median(max_latencies), 2)

    def get_stats(self, X, y, model, generator, iters=5):
        """
        Args:
            X: Input samples.
            y: Target labels.
            model: The model to train.
            generator: The generator for creating classifier code.
            iters: Number of iterations for timing.
        
        Returns:
            time_accuracies: Dictionary of accuracies and statistics for different time limits.
        """
        X = np.array(X, dtype=np.float32)

        time_accuracies = {}
        max_time = 0.02  # Set a fixed max time for simplicity
        print(f'MAX TIME: {max_time}')
        times = np.linspace(0, max_time, 20)

        kf = KFold(n_splits=5, shuffle=True, random_state=42)  # 5-fold cross-validation
        count = 0
        for time_limit in times:
            print(f"TESTING TIME LIMIT: {time_limit}, {count}/{len(times)}")
            accuracies = []             #
            avg_trees = []              # Store for each fold
            confusion_matrices = []     #
            for train_index, test_index in kf.split(X, y):  # Pass both X and y to KFold.split()
                X_train, X_test = X[train_index], X[test_index]
                y_train, y_test = y[train_index], y[test_index]

                # Train the model
                model.fit(X_train, y_train)
                generator.generate(f"classifier_fold.py")

                # Load the classifier and voter
                self.load_classifier("classifier_fold.py")
                self.load_voter("classifier_fold.py")

                # Predict with a timeout
                predictions, _ = self.predict_thread(X_test, timeout=time_limit)
                y_pred = np.array([pred[0] for pred in predictions])
                accuracies.append(accuracy_score(y_test, y_pred))

                cm = confusion_matrix(y_test, y_pred)
                confusion_matrices.append(cm.tolist())  # Convert to list for JSON serialization


            # Calculate mean accuracy, standard deviation, and confidence interval
            mean_accuracy = np.mean(accuracies)
            std_accuracy = np.std(accuracies)
            conf_interval = 1.96 * std_accuracy / np.sqrt(len(accuracies))  # 95% confidence interval

            time_accuracies[time_limit] = {
                "accuracy": mean_accuracy,
                "std": std_accuracy,
                "avg_trees": np.mean(avg_trees),
                "conf. interval": conf_interval,
                "upper_bound": min(mean_accuracy + conf_interval, 1.0),  # Upper bound of confidence interval
                "lower_bound": max(mean_accuracy - conf_interval, 0.0),   # Lower bound of confidence interval
                "confusion_matrices": confusion_matrices  # Store confusion matrices for all folds
            }
            count += 1

        return time_accuracies

    def fit(self, X, y):
        """Dummy method to comply with sklearn interface."""
        return self


from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_openml

print("START")

clf = GeneratedClassifierWrapperTime()



# RUN THE BELOW TO GENERATE THE RESULTS FOR MNIST


# # module_filename = f"random_forest_model.py"

# print("LOADING MNIST. . .")
# mnist = fetch_openml('mnist_784', version=1, parser='auto')
# X = np.array(mnist["data"].astype('float32') / 255.0)
# y = np.array(mnist["target"].astype('int'))
# # Use a subset for speed
# X, y = X[:2000], y[:2000]
# print("MNIST LOADED")

# rfc = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# rfc.fit(X_train, y_train)

# # Initial model loading so we can get the maximum time needed to process all trees
# generator = RandomForestPythonGeneratorTime(rfc)
# generator.generate("random_forest_model.py")
# clf.load_classifier("random_forest_model.py")
# clf.load_voter("random_forest_model.py")

# time_acc = clf.get_stats(X, y, rfc, generator, iters=5)

# with open("time_acc.json", "w") as f:
#     json.dump(time_acc, f, indent=4)

# Load time_acc from the JSON file
with open("time_acc.json", "r") as f:
    time_acc = json.load(f)

# Extract data for plotting
times = list(time_acc.keys())
times = [float(t) for t in times]  # Convert times to float
times.sort()

accuracies = [time_acc[str(t)]["accuracy"] for t in times]
conf_intervals = [time_acc[str(t)]["conf. interval"] for t in times]
# conf_matrices = [time_acc[str(t)]["confusion_matrices"] for t in times]
upper_bounds = [time_acc[str(t)]["upper_bound"] for t in times]
lower_bounds = [time_acc[str(t)]["lower_bound"] for t in times]


# Plot Quality vs. Time with Confidence Intervals
plt.figure(figsize=(10, 6))
plt.plot(times, accuracies, label="Accuracy")
plt.fill_between(times, lower_bounds, upper_bounds, color='grey', alpha=0.3)
plt.xlabel("Time (s)")
plt.ylabel("Accuracy")
plt.title("Quality vs. Time with Confidence Intervals")
plt.legend()
plt.grid()
plt.show()

# Plot Confusion Matrices for Selected Time Points
# selected_times = [times[0], times[len(times) // 2], times[-1]]  # First, middle, and last time points
# for i, t in enumerate(selected_times):
#     cm = np.array(conf_matrices[times.index(t)])  # Convert to NumPy array
#     disp = ConfusionMatrixDisplay(confusion_matrix=cm)
#     disp.plot(cmap=plt.cm.Blues)
#     plt.title(f"Confusion Matrix at Time {t:.2f}s")
#     plt.show()