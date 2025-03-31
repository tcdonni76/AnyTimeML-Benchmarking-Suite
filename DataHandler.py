import json
import os
from sklearn.datasets import fetch_openml
from datetime import datetime
import platform
from sklearn.datasets import load_iris
import numpy as np

np.set_printoptions(suppress=True)

class DataHandler:
    def __init__(self, time_acc_path='time_acc.json'):
        self.file_path = time_acc_path

        self.data = self.load_data()
        datasets = []
        for experiment in self.data:
            if 'dataset' in experiment and experiment['dataset'] not in datasets:
                datasets.append(experiment['dataset'])

    def load_dataset(self, dataset_choice):   
        if dataset_choice == "MNIST":
            return self.load_mnist()
        elif dataset_choice == "Iris":
            return self.load_iris()
        else:
            return None, None

    def retrieve_datasets(self):
        data = self.load_data()

        datasets = []
        for experiment in data:
            if 'dataset' in experiment and experiment['dataset'] not in datasets:
                datasets.append(experiment['dataset'])
        return datasets

    def retrieve_models(self):
        data = self.load_data()

        models = []
        for experiment in data:
            if 'model_details' in experiment and experiment['model_details'] not in models:
                models.append(experiment['model_details'])
        return models

    def load_mnist(self):
        """Load the MNIST dataset."""
        print("Loading MNIST dataset...")
        mnist = fetch_openml('mnist_784', version=1, parser='auto')
        X = np.array(mnist["data"].astype('float32') / 255.0)
        y = np.array(mnist["target"].astype('int'))

        X, y = self.shuffle_and_subset(X, y, 2000)  # Shuffle and take a subset of 2000 samples for speed
        print("MNIST dataset loaded.")
        return X, y

    def load_iris(self):
        """Load the Iris dataset."""
        print("Loading Iris dataset...")
        X = load_iris().data
        y = load_iris().target
        print("Iris dataset loaded.")
        return X, y

    def load_cifar2(self):
        """
        Load and preprocess the CIFAR-2 dataset (vehicles vs. animals).
        
        Returns:
            X: Preprocessed images.
            y: Binary labels (0 for vehicles, 1 for animals).
        """
        # Load CIFAR-10 dataset
        print("Loading CIFAR-10 dataset...")
        (X_train, y_train), (X_test, y_test) = cifar10.load_data()

        # Define class mappings
        vehicles = [0, 1, 8, 9]  # airplane, automobile, ship, truck
        animals = [2, 3, 4, 5, 6, 7]  # bird, cat, deer, dog, frog, horse

        # Combine train and test sets for simplicity
        X = np.concatenate([X_train, X_test])
        y = np.concatenate([y_train, y_test]).flatten()

        # Filter for vehicles and animals
        mask = np.isin(y, vehicles + animals)
        X = X[mask]
        y = y[mask]

        # Relabel: 0 for vehicles, 1 for animals
        y = np.where(np.isin(y, vehicles), 0, 1)

        # Normalize pixel values to [0, 1]
        X = X.astype('float32') / 255.0

        print(f"CIFAR-2 dataset created with {len(X)} samples.")
        return X, y

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save_data(self, data):
        if os.path.exists(self.file_path):
            # Load existing data
            with open(self.file_path, "r") as f:
                try:
                    existing_data = json.load(f)
                    # Ensure existing_data is a list
                    if isinstance(existing_data, dict):
                        existing_data = [existing_data]
                except json.JSONDecodeError:
                    # If the file is empty or invalid, initialize as an empty list
                    print(f"Warning: {self.file_path} is empty or invalid. Initializing a new file.")
                    existing_data = []
        else:
            # Initialize an empty list if the file doesn't exist
            existing_data = []

        # Append the new data
        existing_data.append(data)

        # Save the updated data back to the JSON file
        with open("time_acc.json", "w") as f:
            json.dump(existing_data, f, indent=4)

    def get_device_details(self):
        return {
            "os": platform.system(),
            "os_version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "node": platform.node()  # Hostname of the device
        }

    def get_model_details(self, model):
        model_details = {
            "model_type": type(model).__name__  # Get the class name of the model
        }
        # Try to get model parameters if the model supports `get_params()`
        try:
            model_details["parameters"] = model.get_params()
        except AttributeError:
            model_details["parameters"] = "Parameters not available"
        return model_details

    def prepare_data(self, results, model, dataset_name):
        # Include model and device details
        model_details = self.get_model_details(model)
        device_details = self.get_device_details()

        # Prepare the data to save
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_to_save = {
            "timestamp": timestamp,
            "dataset": dataset_name,
            "model_details": model_details,
            "device_details": device_details,
            "results": results
        }
        return data_to_save

    # Shuffle and take a subset
    def shuffle_and_subset(self, X, y, subset_size):
        """
        Shuffle the dataset and take a subset.

        Args:
            X: Features (e.g., images).
            y: Labels.
            subset_size: Number of samples to take after shuffling.

        Returns:
            X_subset: Shuffled subset of features.
            y_subset: Shuffled subset of labels.
        """
        # Create a random number generator with the given random state
        rng = np.random.default_rng(seed=42)

        # Generate a random permutation of indices
        indices = rng.permutation(len(X))

        # Shuffle X and y using the indices
        X_shuffled = X[indices]
        y_shuffled = y[indices]

        # Take the first `subset_size` samples
        X_subset = X_shuffled[:subset_size]
        y_subset = y_shuffled[:subset_size]

        return X_subset, y_subset

handler = DataHandler()
