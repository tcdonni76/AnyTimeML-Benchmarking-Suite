import os
import json
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from AnytimeWrapper import AnytimeBenchmarkTester
from DataHandler import DataHandler
from ResultPlotter import ResultPlotter
import time


class CLI:
    def __init__(self):
        """Initialize the CLI class."""
        self.data_file = "BenchmarkingSuite/results.json"
        self.model_file = "BenchmarkingSuite/models.json"
        self.datasets_file = "datasets.json"
        self.data_handler = DataHandler(self.data_file)
        self.plotter = ResultPlotter()

    def select_dataset(self):
        """Allow the user to select a dataset."""
        print("\nAvailable Datasets:")
        for i, dataset_name in enumerate(self.dataset_mapping.keys(), start=1):
            print(f"{i}. {dataset_name}")

        try:
            choice = int(input("\nEnter the number of the dataset to load: ")) - 1
            if choice < 0 or choice >= len(self.dataset_mapping):
                print("Invalid choice.")
                return None, None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None, None

        dataset_name = list(self.dataset_mapping.keys())[choice]
        load_function = eval(self.dataset_mapping[dataset_name])  # Dynamically call the function
        return load_function()

    def select_model(self):
        """
        Allows the user to select a machine learning model from a list of available models.

        The method displays a list of models, prompts the user to select one by entering its
        corresponding number, and initializes the selected model with its hyperparameters.
        Handles both RandomForestClassifier and custom classifiers.

        Returns:
            tuple: A tuple containing:
                - model_name (str): The name of the selected model.
                - model (object): The initialized model object or None for custom models.
                - classifier_path (str): The path to the custom classifier file (if applicable).
        """
        self.print_models()
        model_choice = int(input("\nEnter the number of the model to use: "))
        if model_choice < 1 or model_choice > len(self.data_handler.models):
            print("Invalid input. Please enter a number in the range.")
            return self.select_model()

        try:
            model = self.data_handler.models[model_choice - 1]
            model_name = model['model_name']
            classifier_path = model.get('path', None)

            if model_name.startswith('RandomForestClassifier'):
                # Initialize RFC with hyperparameters
                parameters = model['hyperparameters']
                model = RandomForestClassifier(**parameters)
            else:
                # Custom model: Return the path for dynamic loading
                model = None
                if not classifier_path:
                    print("Error: Custom model path not found.")
                    return self.select_model()

            return model_name, model, classifier_path

        except (ValueError, IndexError):
            print("Invalid input. Please enter a number in the range.")
            return self.select_model()

    def load_new_model(self):
        print("Options:")
        print("1. RandomForestClassifier")
        print("2. Enter a custom model")
        
        try:
            model_choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
        if model_choice == 1: # If user wants a RandomForest
            # Train a new RandomForestClassifier model
            print("Enter hyperparameters seperated by commas: (n_estimators, max_depth, min_samples_split, min_samples_leaf)")
            hyperparameters = input()
            hyperparameters = hyperparameters.split(',')
            hyperparameters = [int(x) for x in hyperparameters]
            n_estimators, max_depth, min_samples_split, min_samples_leaf = hyperparameters

            model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)
            model_name = model.__class__.__name__
            classifier_path = None
            print("New Model added successfully.")


        elif model_choice == 2: # If user wants to enter a new model
            print("The naming convention for models is: <model_type>_Model_<model_number>")
            print("For example, the second RandomForestClassifier would be named RandomForestClassifier_Model_2")
            print("Enter the model type (eg. RandomForestClassifier):")
            model_name = input()

            classifier_path = os.path.join(os.getcwd(), input("Enter the relative path to the classifier file: "))
            model = None
            if not os.path.exists(classifier_path):
                print("Error: The specified file does not exist. Please check the path and try again.")
                return

        self.data_handler.add_new_model(model_name, model, classifier_path)
        print("New Model added successfully.")

    def evaluate_model(self):
        """
        Evaluate a selected model on a selected dataset.
        Handles both RandomForestClassifier and custom classifiers.
        """
        # Step 1: Select the model
        model_name, model, classifier_path = self.select_model()

        # Step 2: Select the dataset
        print("Please select a dataset to train:")
        for count, dataset in enumerate(self.data_handler.datasets):
            print(f"{count + 1}. {dataset['dataset']}")
        dataset_choice = int(input("\nEnter the number of the dataset to use: "))
        try:
            data_X, data_y = self.data_handler.load_dataset(self.data_handler.datasets[dataset_choice - 1]['dataset'])
        except (IndexError, ValueError):
            print("Invalid input. Please enter a number displayed.")
            return self.evaluate_model()

        # Step 3: Train and evaluate the model
        wrapper = AnytimeBenchmarkTester()
        results = wrapper.conduct_test(
            X=data_X,
            y=data_y,
            model=model,
            model_name=model_name,
            dataset_name=self.data_handler.datasets[dataset_choice - 1]['dataset'],
            classifier_name=classifier_path  # Pass the path for custom models
        )

        # Step 4: Save the results
        data = self.data_handler.prepare_data(results, model_name, self.data_handler.datasets[dataset_choice - 1]['dataset'])
        self.data_handler.save_data(data, self.data_handler.file_path)
        print("Model trained and evaluated successfully.")

    def print_models(self):
        """Print all models in the JSON file in presentafble way."""

        print("\nAvailable Models:")
        for i, model in enumerate(self.data_handler.models, start=1):
            print(f"{i}. Name: {model['model_name']}")
            # Group hyperparameters into chunks of 2 for better readability
            try:
                hyperparameters = list(model['hyperparameters'].items())
            except KeyError:
                print("Error: Hyperparameters not found for this model.")
                hyperparameters = []
            except AttributeError:
                pass

            # Calculate the maximum key length for alignment
            max_key_length = max_key_length = max((len(key) + len(str(val)) for key, val in hyperparameters), default=0)

            for j in range(0, len(hyperparameters), 2):
                chunk = hyperparameters[j:j + 2]
                formatted_chunk = "   ".join(
                    [f"{key}:  {value}".ljust(max_key_length + 5) for key, value in chunk]
                )
                print(f"       {formatted_chunk}")
            print("Model path: ", model['path'])

    def display_charts(self):
        """Display charts for a selected model and dataset."""

        model_name, model, path = self.select_model()
        # List out all the runs involving the selected model and with what dataset
        print("\nAvailable Runs:")
        count = 1
        model_runs = [run for run in self.data_handler.data if run['model'] == model_name]

        for run in model_runs:
            print(f"{count}. {run['dataset']} (Timestamp: {run['timestamp']})")
            count += 1

        try:
            run_choice = int(input("\nEnter the number of the run to display: "))
            if run_choice < 1 or run_choice > len(model_runs):
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        selected_run = model_runs[run_choice - 1]
        results = selected_run['results']

        # Step 4: Select the plot
        while True:
            print("\nOptions:")
            print("1. Quality vs. Time")
            print("2. Confusion Matrices")
            print("3. ROC AUC vs. Time")
            print("4. Back to Main Menu")

            try:
                plot_choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                return
            
            if plot_choice == 1:
                self.plotter.func(results, model_name, selected_run['dataset'])
            elif plot_choice == 2:
                self.plotter.plot_confusion_matrices(results, selected_run['dataset'])
            elif plot_choice == 3:
                print("ROC AUC vs. Time not yet implemented") #TODO: Implement ROC AUC vs. Time
            elif plot_choice == 4:
                break

    def display_dataset_charts(self):
        """Display charts for a selected dataset."""
        print("Available Datasets:")
        count = 1
        for dataset in self.data_handler.datasets:
            print(f"{count}. {dataset['dataset']}")
            count += 1

        try:
            dataset_choice = int(input("\nEnter the number of the dataset to display: "))
            if dataset_choice < 1 or dataset_choice > len(self.data_handler.datasets):
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        dataset = self.data_handler.datasets[dataset_choice - 1]['dataset']

        res = []
        for run in self.data_handler.data:
            if run['dataset'] == dataset:
                res.append(run)
        
        print("\nOptions:")
        print("1. Comparative Line Plot")
        print("2. Table Showing AUC Values")
        print("3. Back to Main Menu")

        try:
            plot_choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if plot_choice == 1:
            self.plotter.plot_models(res, dataset)
        elif plot_choice == 2:
            self.plotter.plot_auc_table(res, dataset)
        elif plot_choice == 3:
            return
        else:
            print("Invalid choice. Please try again.")
        
        if not res:
            print("No runs found for the selected dataset.")
            return

    def plot_quality_map(self, time_acc, model):
        """Plot the quality map (accuracy vs. time)."""
        # Extract data for plotting
        times = list(map(float, time_acc.keys()))
        times.sort()

        accuracies = [time_acc[str(t)]["accuracy"] for t in times]
        upper_bounds = [time_acc[str(t)]["upper_bound"] for t in times]
        lower_bounds = [time_acc[str(t)]["lower_bound"] for t in times]

        # Plot Quality vs. Time with Confidence Intervals
        plt.figure(figsize=(10, 6))
        plt.plot(times, accuracies, label="Accuracy")
        plt.fill_between(times, lower_bounds, upper_bounds, color='grey', alpha=0.3, label="Confidence Interval")
        plt.xlabel("Time (s)")
        plt.ylabel("Accuracy")
        plt.title(f"Quality vs. Time for {model['model_details']['model_type']} (Dataset: {model['dataset']})")
        plt.legend()
        plt.grid()
        plt.show()

    def main_menu(self):
        """Main CLI menu."""
        while True:

            # Update the results data
            self.data_handler.data = self.data_handler.load(self.data_handler.file_path)
            self.data_handler.models = self.data_handler.load(self.model_file) # Load in latest models
            

            print("\nOptions:")
            print("1. Add a new model")
            print("2. Train model on a dataset")
            print("3. Display charts for an existing model")
            print("4. Display charts for a dataset")
            print("5. Exit")

            try:
                choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                self.load_new_model()
            elif choice == 2:
                self.evaluate_model()
            elif choice == 3:
                self.display_charts()
            elif choice == 4:
                self.display_dataset_charts()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    cli = CLI()
    cli.main_menu()