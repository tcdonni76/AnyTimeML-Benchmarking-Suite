import json
import os
from sklearn.datasets import fetch_openml
from datetime import datetime
import platform
from sklearn.datasets import load_iris
import numpy as np
import tensorflow as tf

np.set_printoptions(suppress=True)

class DataHandler:
    def __init__(self, results_path='BenchmarkingSuite/results.json', dataset_path='BenchmarkingSuite/datasets.json', model_path='BenchmarkingSuite/models.json'):
        self.file_path = results_path
        self.model_path = model_path
        self.models = [] # Loaded in later
        self.data = [] # Loaded in later
        self.dataset_path = dataset_path
        self.datasets = self.retrieve_datasets()

    def load_dataset(self, dataset_choice):   
        if dataset_choice == "MNIST":
            return self.load_mnist()
        elif dataset_choice == "Iris":
            return self.load_iris()
        elif dataset_choice == "CIFAR-2":
            return self.load_cifar2()
        else:
            return None, None

    def retrieve_datasets(self):
        with open(self.dataset_path, 'r') as file:
            datasets = json.load(file)
        return datasets

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
        (X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()
        print("CIFAR-10 dataset loaded.")

        # Define class mappings
        vehicles = [0, 1, 8, 9]  # airplane, automobile, ship, truck
        animals = [2, 3, 4, 5, 6, 7]  # bird, cat, deer, dog, frog, horse

        # Combine train and test sets for simplicity
        X = np.concatenate([X_train, X_test])
        y = np.concatenate([y_train, y_test]).flatten()

        X, y = self.shuffle_and_subset(X, y, 2000)  # Shuffle and take a subset of 2000 samples for speed

        # Filter for vehicles and animals
        mask = np.isin(y, vehicles + animals)
        X = X[mask]
        y = y[mask]

        # Relabel: 0 for vehicles, 1 for animals
        y = np.where(np.isin(y, vehicles), 0, 1)

        # Normalize pixel values to [0, 1]
        X = X.astype('float32') / 255.0

        # Flatten the images to 2D
        X = X.reshape(X.shape[0], -1)

        print(f"CIFAR-2 dataset created with {len(X)} samples.")
        return X, y

    def load(self, path):
        try:
            with open(path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save_data(self, data, path):
        if os.path.exists(path):
            # Load existing data
            with open(path, "r") as f:
                try:
                    existing_data = json.load(f)
                    # Ensure existing_data is a list
                    if isinstance(existing_data, dict):
                        existing_data = [existing_data]
                except json.JSONDecodeError:
                    # If the file is empty or invalid, initialize as an empty list
                    print(f"Warning: {path} is empty or invalid. Initializing a new file.")
                    existing_data = []
        else:
            # Initialize an empty list if the file doesn't exist
            existing_data = []

        # Append the new data
        existing_data.append(data)

        # Save the updated data back to the JSON file
        with open(path, "w") as f:
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
        model_details = {}

        # Try to get model parameters if the model supports `get_params()`
        try:
            model_details["hyperparameters"] = model.get_params()
        except AttributeError:
            model_details["hyperparameters"] = "Parameters not available"
        return model_details

    def get_model_name(self, model):
        return type(model).__name__

    def prepare_data(self, results, model_name, dataset_name):
        # Include model and device details
        device_details = self.get_device_details()

        # Prepare the data to save
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_to_save = {
            "timestamp": timestamp,
            "dataset": dataset_name,
            "model": model_name,
            "device_details": device_details,
            "results": results
        }
        return data_to_save

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

    def get_number_of_models(self, name):
        count = sum(1 for model in self.models if model["model_name"].startswith(name))
        return count + 1

    def add_new_model(self, model):
        """
        Add a new model to the models list. This method is a placeholder and should be implemented as needed.
        """
        base_name = self.get_model_name(model)
        model_name = f"{base_name}_Model_{self.get_number_of_models(base_name)}"
        model_details = self.get_model_details(model)
        model_data = {
            "model_name": model_name,
        }
        model_data.update(model_details)
        self.save_data(model_data, self.model_path)
        return model_name
    
    def add_custom_model(self, model_name, hyperparameters):
        """
        Add a custom model to the models list.
        """
        model_data = {
            "model_name": f"{model_name}_Model_{self.get_number_of_models(model_name)}",
            "hyperparameters": hyperparameters
        }
        self.save_data(model_data, self.model_path)
        return model_name