import os
import json
from datetime import datetime
from sklearn.datasets import fetch_openml, load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from RFCPythonGenerator import RandomForestPythonGeneratorTime
from AnytimeWrapper import GeneratedClassifierWrapperTime
from DataHandler import DataHandler
from ResultPlotter import ResultPlotter
import time
from sklearn.metrics import ConfusionMatrixDisplay
import numpy as np

class CLI:
    def __init__(self):
        """Initialize the CLI class."""
        self.data_file = "time_acc.json"
        self.datasets_file = "datasets.json"
        self.data_handler = DataHandler(self.data_file)
        self.plotter = ResultPlotter()

    def save_datasets(self):
        """Save the current dataset mapping to the configuration file."""
        with open(self.datasets_file, "w") as f:
            json.dump(self.dataset_mapping, f, indent=4)


        """Load the Iris dataset."""
        print("Loading Iris dataset...")
        iris = load_iris()
        X = iris["data"]
        y = iris["target"]
        print("Iris dataset loaded.")
        return X, y

    def add_new_dataset(self):
        """Add a new dataset dynamically via the CLI."""
        name = input("Enter the name of the new dataset: ")
        function = input("Enter the Python function to load the dataset (e.g., 'self.load_custom_dataset'): ")

        if name in self.dataset_mapping:
            print(f"Dataset '{name}' already exists.")
            return

        self.dataset_mapping[name] = function
        self.save_datasets()
        print(f"Dataset '{name}' added successfully.")

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
        count = 1
        print("\nAvailable Models:")
        for model in self.data_handler.retrieve_models():
            print(f"{count}. {model}")
            count += 1
        model_choice = int(input("\nEnter the number of the model to use: "))
        try:
            model_details = self.data_handler.retrieve_models()[model_choice - 1]
            if model_details['model_type'] == 'RandomForestClassifier':
                parameters = model_details['parameters']
                model = RandomForestClassifier(**parameters)
            else:
                print("Model type yet not supported.")
        except ValueError or IndexError:
            print("Invalid input. Please enter a number in the range.")
            self.select_model()
        return model

    def load_new_model(self):
        """Allow the user to select either an existing model or train a new one."""
        print("\nOptions:")
        print("1. Train a new model")
        print("2. Use an existing model")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if choice == 1: # If training a new model
            print("Options:")
            print("1. RandomForestClassifier")
            print("2. Neural Network")
        
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
                
            elif model_choice == 2: # If user wants a neural net
                print("NEURAL NETWORKS NOT YET IMPLEMENTED") #TODO: Implement neural networks
                self.main_menu()

        elif choice == 2: # If training an existing model
            model = self.select_model()
            
        # Now give option of dataset selection
        
        print("Please select a dataset to train")
        datasets = self.data_handler.retrieve_datasets()
        for count, dataset in enumerate(datasets):
            print(f"{count + 1}. {dataset}")
        dataset_choice = int(input("\nEnter the number of the dataset to use: "))
        try:
            data_X, data_y = self.data_handler.load_dataset(datasets[dataset_choice - 1])
        except IndexError or ValueError:
            print("Invalid input. Please enter a number displayed.")
            self.load_new_model()

        # Now train the model
        wrapper = GeneratedClassifierWrapperTime()
        results = wrapper.conduct_test(data_X, data_y, model)
        data = self.data_handler.prepare_data(results, model, datasets[dataset_choice - 1])
        self.data_handler.save_data(data)
        print("Model trained successfully.")
        time.sleep(3)
        self.main_menu()

    def display_charts(self):
        """Display charts for a selected model and dataset."""
        # Step 1: Load all models from the JSON file
        if not os.path.exists(self.data_file):
            print("No models found. Please train a new model first.")
            return

        with open(self.data_file, "r") as f:
            try:
                models = json.load(f)
                if not isinstance(models, list):
                    models = [models]
            except json.JSONDecodeError:
                print("Error: time_acc.json is invalid.")
                return

        for r in self.data_handler.data:
            print(r['model_details'])

        # Step 2: List available models
        model = self.select_model()
        print(model.get_params(), '\n\n\n')
        # List out all the runs involving the selected model and with what dataset
        print("\nAvailable Runs:")
        count = 1
        model_runs = [run for run in self.data_handler.data if run['model_details']['parameters'] == model.get_params()]

        for run in self.data_handler.data:
            for key, value in run['model_details']['parameters'].items():
                if value != model.get_params()[key]:
                    print(key, value, model.get_params()[key])

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

        # Step 3: Select a run to display
        selected_run = model_runs[run_choice - 1]
        results = selected_run['results']

        # Step 4: Select the plot
        print("\nOptions:")
        print("1. Quality vs. Time")
        print("2. Confusion Matrices")

        try:
            plot_choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
        if plot_choice == 1:
            self.plotter.plot_quality_map(results, selected_run['dataset'])
        elif plot_choice == 2:
            self.plotter.plot_confusion_matrices(results, selected_run['dataset'])

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
            print("\nOptions:")
            print("1. Train model on a dataset")
            print("2. Display charts for an existing model")
            print("3. List available models")
            print("4. Exit")

            try:
                choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                self.load_new_model()
                time.sleep(1)
            elif choice == 2:
                self.display_charts()
                time.sleep(1)
            elif choice == 3:
                self.data_handler.list_models()
                time.sleep(1)
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    cli = CLI()
    cli.main_menu()