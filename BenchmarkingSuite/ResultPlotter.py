import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay


class ResultPlotter:
    def __init__(self):
        """
        Initialize the Plotter with the time_acc dictionary.

        Args:
            time_acc (dict): Dictionary containing accuracy, confidence intervals, and confusion matrices.
        """

    def plot_accuracy_quality_map(self, results, dataset):
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

    def func(self, results, dataset):
        """
        Plot accuracy, F1 score, precision, and recall vs. time with confidence intervals in subplots.
        """

        metrics = ["acc", "f1", "precision", "recall"]
        metric_labels = ["Accuracy", "F1 Score", "Precision", "Recall"]

        times = sorted([float(t) for t in results.keys()])
        norm_times = [t / max(times) * 100 for t in times] 

        fig, axes = plt.subplots(1, len(metrics),figsize=(15, 5))
        fig.suptitle("Metrics vs. Time for " + model_name + ' evaluating ' + dataset)

        for i, metric in enumerate(metrics):
            values = [results[str(t)][metric] for t in times]
            upper_bounds = [results[str(t)][f"{metric}_upper_bound"] for t in times]
            lower_bounds = [results[str(t)][f"{metric}_lower_bound"] for t in times]

            axes[i].plot(norm_times, values, label=f"Mean {metric_labels[i]}", color="blue")
            axes[i].fill_between(norm_times, lower_bounds, upper_bounds, color="blue", alpha=0.2, label="95% Confidence Interval")
            axes[i].set_xlabel("% of Maximum Time")
            axes[i].set_ylabel(metric_labels[i])
            axes[i].set_title(metric_labels[i])
            axes[i].legend()
            axes[i].grid()

        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave space for the overall title
        plt.show()

    def plot_models(self, results_set, dataset_name):
        """
        Plot accuracy, F1 score, precision, and recall vs. time with confidence intervals in subplots for multiple models.
        """
        metrics = ["acc", "f1", "precision", "recall"]
        metric_labels = ["Accuracy", "F1 Score", "Precision", "Recall"]

        # Create a figure with an additional row for max times
        fig, axes = plt.subplots(2, len(metrics), figsize=(20, 10), gridspec_kw={"height_ratios": [4, 1]})
        fig.suptitle(f"Metrics vs. Time for Different Models on {dataset_name}")

        colors = plt.cm.tab10.colors  # Use a colormap for distinct colors
        max_times = []  # To store max times for each model

        # Plot metrics in the first row
        for i, run in enumerate(results_set):
            for j, metric in enumerate(metrics):
                results = run['results']
                times = sorted([float(t) for t in results.keys()])
                norm_times = [t / max(times) * 100 for t in times]

                values = [results[str(t)][metric] for t in times]
                upper_bounds = [results[str(t)][f"{metric}_upper_bound"] for t in times]
                lower_bounds = [results[str(t)][f"{metric}_lower_bound"] for t in times]

                axes[0, j].plot(norm_times, values, label=f"{run['model']}", color=colors[i % len(colors)])
                axes[0, j].fill_between(norm_times, lower_bounds, upper_bounds, color=colors[i % len(colors)], alpha=0.2)
                axes[0, j].set_xlabel("% of Maximum Time")
                axes[0, j].set_ylabel(metric_labels[j])
                axes[0, j].set_title(metric_labels[j])
                axes[0, j].legend()
                axes[0, j].grid()

            # Store max time for the model
            max_times.append((run['model'], max(times)))

        # Merge all axes in the second row into one
        for ax in axes[1, :]:
            ax.remove()  # Remove individual axes in the second row
        # Add a new axis below the plots for the max times
        ax_max_time = fig.add_axes([0.1, 0.05, 0.8, 0.1])  # [left, bottom, width, height]
        max_time_text = "Max time to process a single sample:\n" + "\n".join([f"{model}: {time:.5f}s" for model, time in max_times])
        ax_max_time.text(0.5, 0.5, max_time_text, ha="center", va="center", fontsize=12)
        ax_max_time.axis("off")  # Hide the axis lines and ticks

        plt.tight_layout(rect=[0, 0.15, 1, 0.95])  # Adjust layout to leave space for the text
        plt.show()

    def plot_roc_auc(self, results, dataset):
        """
        Plot ROC AUC vs. time with confidence intervals.

        Args:
            results (dict): Dictionary containing results, including ROC AUC values.
            dataset (str): Name of the dataset.
        """
        times = sorted([float(t) for t in results.keys()])
        roc_auc_values = [results[str(t)]["roc_auc"] for t in times]
        upper_bounds = [results[str(t)]["roc_auc_upper_bound"] for t in times]
        lower_bounds = [results[str(t)]["roc_auc_lower_bound"] for t in times]

        norm_times = [t / max(times) * 100 for t in times]

    def plot_confusion_matrices(self, results, dataset):
        """
        Plot confusion matrices for selected time points.

        Args:
            results (dict): Dictionary containing results, including confusion matrices.
            dataset (str): Name of the dataset.
        """


        # Extract confusion matrices
        times = sorted([float(t) for t in results.keys()])
        selected_times = [times[len(times) // 4], times[len(times) // 2], times[3 * len(times) // 4], times[-1]]
        time_breaks = [25, 50, 75, 100]

        # Create subplots with a large figure size
        fig, axes = plt.subplots(1, len(selected_times), figsize=(40, 10))
        fig.suptitle("Confusion Matrices at Selected Time Points for " + dataset)

        # Plot confusion matrices
        for count, t in enumerate(selected_times):
            confusion_matrix = np.array(results[str(t)]["confusion_matrices"])

            n_classes = confusion_matrix.shape[0]

            # Ensure the confusion matrix is a proper 2D array
            if confusion_matrix.ndim == 1:
                confusion_matrix = np.vstack(confusion_matrix)  # Stack rows into a 2D array

            disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix)
            disp.plot(ax=axes[count],colorbar=False)
            axes[count].set_title(f"Time: {time_breaks[count]}% of Max Time")

        plt.show()

    def plot_all(self):
        """
        Plot all charts: accuracy vs. time and confusion matrices.
        """
        self.plot_accuracy_vs_time()
        self.plot_confusion_matrices()