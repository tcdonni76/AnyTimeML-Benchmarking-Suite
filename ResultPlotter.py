import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay

# np.set_printoptions(suppress=True)

class ResultPlotter:
    def __init__(self):
        """
        Initialize the Plotter with the time_acc dictionary.

        Args:
            time_acc (dict): Dictionary containing accuracy, confidence intervals, and confusion matrices.
        """

    def plot_quality_map(self, results, dataset):
        """
        Plot accuracy vs. time with confidence intervals.
        """

        times = sorted([float(t) for t in results.keys()])
        accuracies = [results[str(t)]["accuracy"] for t in times]
        upper_bounds = [results[str(t)]["upper_bound"] for t in times]
        lower_bounds = [results[str(t)]["lower_bound"] for t in times]

        norm_times = [t / max(times) for t in times]

        plt.figure(figsize=(10, 6))
        plt.plot(norm_times, accuracies, label="Mean Accuracy", color="blue")
        plt.fill_between(norm_times, lower_bounds, upper_bounds, color="blue", alpha=0.2, label="95% Confidence Interval")
        plt.xlabel("% of Maximum Time")
        plt.ylabel("Accuracy")
        plt.title("Accuracy vs. Time for " + dataset)
        plt.legend()
        plt.grid()
        plt.show()

    def plot_confusion_matrices(self, results, dataset):
        """
        Plot confusion matrices for selected time points.

        Args:
            results (dict): Dictionary containing results, including confusion matrices.
            dataset (str): Name of the dataset.
        """
        from sklearn.metrics import ConfusionMatrixDisplay
        import numpy as np
        import matplotlib.pyplot as plt

        # Extract confusion matrices
        times = sorted([float(t) for t in results.keys()])
        selected_times = [times[len(times) // 4], times[len(times) // 2], times[3 * len(times) // 4], times[-1]]
        time_breaks = [25, 50, 75, 100]

        # Create subplots with a large figure size
        fig, axes = plt.subplots(1, len(selected_times), figsize=(40, 10))
        fig.suptitle("Confusion Matrices at Selected Time Points for " + dataset)

        max_rows = 0
        max_cols = 0
        for t in selected_times:
            for cm in results[str(t)]["confusion_matrices"]:
                max_rows = max(max_rows, len(cm))
                max_cols = max(max_cols, len(cm[0]))

        # Plot confusion matrices
        for count, t in enumerate(selected_times):
            confusion_matrices = results[str(t)]["confusion_matrices"]
            if not confusion_matrices:
                print(f"No confusion matrix available for time {t:.2f}s.")
                continue

            # Pad all matrices to the largest size
            padded_matrices = []
            for cm in confusion_matrices:
                padded_matrix = np.zeros((max_rows, max_cols))
                padded_matrix[:len(cm), :len(cm[0])] = cm  # Copy the original matrix into the padded one
                padded_matrices.append(padded_matrix)

            # Combine the padded matrices (e.g., sum them)
            combined_matrix = np.sum(padded_matrices, axis=0).astype(int)

            # Plot the combined matrix
            disp = ConfusionMatrixDisplay(confusion_matrix=combined_matrix)
            disp.plot(ax=axes[count], cmap=plt.cm.Blues, colorbar=False)

            # Add a title to each subplot
            axes[count].set_title(f"Time: {time_breaks[count]}%", fontsize=12)

            # Show X-axis label and ticks only for the first subplot
            if count == 0:
                axes[count].set_ylabel("True Labels", fontsize=12)
            else:
                axes[count].set_ylabel('')  # Remove X-axis label
                axes[count].set_yticks([])  # Remove X-axis ticks

        plt.subplots_adjust(wspace=0.4)  # Increase horizontal space between subplots
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for the overall title
        plt.show()

    def plot_all(self):
        """
        Plot all charts: accuracy vs. time and confusion matrices.
        """
        self.plot_accuracy_vs_time()
        self.plot_confusion_matrices()