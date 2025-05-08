import json
import os
from sklearn.datasets import fetch_openml
from datetime import datetime
import platform
from sklearn.datasets import load_iris
import numpy as np
import tensorflow as tf
import requests
import tarfile
import random
import pycocotools.coco as COCO
from urllib.request import urlretrieve
from sklearn.datasets import load_breast_cancer, load_wine, load_digits

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
        elif dataset_choice == "Speech Commands":
            return self.load_speech_commands()
        elif dataset_choice == "COCO":
            return self.load_coco()
        elif dataset_choice == "Cancer":
            return self.load_breast_cancer()
        elif dataset_choice == "Wine":
            return self.load_wine()
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

    def load_speech_commands(self, subset_size=2000):
        """
        Load and preprocess a subset of the Speech Commands dataset for keyword spotting.

        Args:
            subset_size (int): The number of files to process. Default is 2000.

        Returns:
            X: Preprocessed audio features (flattened).
            y: Labels for the audio commands.
        """
        print("Loading Speech Commands dataset...")

        dataset_dir = "BenchmarkingSuite/StoredDatasets"
        tar_file = os.path.join(dataset_dir, "speech_commands_v0.02.tar.gz")
        cache_file = os.path.join(dataset_dir, "speech_commands.npz")  # Cache file for processed data

        # Check if cached data exists
        if os.path.exists(cache_file):
            print(f"Loading cached data from {cache_file}...")
            cached_data = np.load(cache_file)
            X = cached_data["X"]
            y = cached_data["y"]
            print(f"Cached data loaded with {len(X)} samples.")
            return X, y

        # Check if the tar file exists in the dataset directory
        if os.path.exists(tar_file):
            # Extract the tar file if the directory is empty or not extracted
            if len(os.listdir(dataset_dir)) == 1 and "speech_commands_v0.02.tar.gz" in os.listdir(dataset_dir):
                print(f"Extracting dataset from {tar_file}...")
                with tarfile.open(tar_file, "r:gz") as tar:
                    tar.extractall(path=dataset_dir)
                print(f"Dataset extracted to: {dataset_dir}")
        else:
            raise FileNotFoundError(f"Dataset not found. Please ensure '{tar_file}' exists in the directory '{dataset_dir}'.")

        # Debug: Check contents of dataset directory after extraction
        print(f"Contents of dataset directory after extraction: {os.listdir(dataset_dir)}")

        # Define the list of target words
        target_words = ["yes", "no", "up", "down", "left", "right", "on", "off", "stop", "go"]
        unknown_label = "_unknown_"
        silence_label = "_silence_"

        # Create a mapping of labels
        label_map = {word: idx for idx, word in enumerate(target_words)}
        label_map[unknown_label] = len(target_words)
        label_map[silence_label] = len(target_words) + 1

        # Collect all `.wav` files and their labels
        all_files = []
        for root, _, files in os.walk(dataset_dir):
            label = os.path.basename(root)  # Infer label from the parent directory name
            label_idx = label_map.get(label, label_map[unknown_label])
            for file in files:
                if file.endswith(".wav"):
                    file_path = os.path.join(root, file)
                    all_files.append((file_path, label_idx))

        # Debug: Check total number of files
        print(f"Total number of `.wav` files found: {len(all_files)}")

        # Randomly sample a subset of files
        if len(all_files) > subset_size:
            all_files = random.sample(all_files, subset_size)
            print(f"Randomly sampled {subset_size} files for processing.")

        # Initialize storage for features and labels
        X = []
        y = []

        # Process the sampled files
        for file_path, label_idx in all_files:
            try:
                features = self.extract_features(file_path)
                if features is not None and features.size > 0:
                    X.append(features)
                    y.append(label_idx)
                else:
                    print(f"Invalid features for {file_path}. Skipping...")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")


        for i, features in enumerate(X):
            print(f"Sample {i}: Feature shape: {features.shape if hasattr(features, 'shape') else 'Not an array'}")

        # Convert to NumPy arrays
        X = np.array(X)
        y = np.array(y)

        # Debug: Check dataset size
        print(f"Number of samples processed: {len(X)}")

        # Cache the processed data
        print(f"Caching processed data to {cache_file}...")
        np.savez(cache_file, X=X, y=y)
        print("Processed data cached successfully.")

        print(f"Speech Commands dataset loaded with {len(X)} samples.")
        return X, y

    def extract_features(self, file_path, fixed_length=16000):
        """
        Extract features (e.g., MFCCs) from an audio file and ensure a fixed length.

        Args:
            file_path: Path to the audio file.
            fixed_length: Desired length of the audio signal in samples (default: 1 second at 16 kHz).

        Returns:
            Flattened feature vector of fixed length.
        """
        audio_binary = tf.io.read_file(file_path)
        audio, sample_rate = tf.audio.decode_wav(audio_binary)
        audio = tf.squeeze(audio, axis=-1)  # Remove the channel dimension

        # Resample to 16 kHz if necessary
        desired_sample_rate = 16000
        if sample_rate != desired_sample_rate:
            audio = tf.audio.resample(audio, sample_rate, desired_sample_rate)

        # Pad or truncate the audio to the fixed length
        if len(audio) < fixed_length:
            audio = tf.pad(audio, [[0, fixed_length - len(audio)]])
        else:
            audio = audio[:fixed_length]

        # Extract MFCCs
        spectrogram = tf.signal.stft(audio, frame_length=256, frame_step=128)
        spectrogram = tf.abs(spectrogram)
        mfccs = tf.signal.mfccs_from_log_mel_spectrograms(tf.math.log(spectrogram + 1e-6))

        # Flatten the MFCCs to create a feature vector
        return tf.reshape(mfccs, [-1]).numpy()

    def load_coco(self, subset_size=2000):
        """
        Load and preprocess a subset of the COCO dataset.

        Args:
            subset_size (int): The number of images to process. Default is 2000.

        Returns:
            X: Preprocessed images (128x128 resolution).
            y: Labels for the selected categories.
        """
        print("Loading COCO dataset...")

        dataset_dir = "BenchmarkingSuite/StoredDatasets/COCO"
        cache_file = os.path.join(dataset_dir, "coco_128x128.npz")  # Cache file for processed data

        # Check if cached data exists
        if os.path.exists(cache_file):
            print(f"Loading cached data from {cache_file}...")
            cached_data = np.load(cache_file)
            X = cached_data["X"]
            y = cached_data["y"]
            print(f"Cached data loaded with {len(X)} samples.")
            return X, y

        # Define the 10 selected categories
        selected_categories = ["person", "car", "dog", "cat", "bicycle", "truck", "motorcycle", "bus", "bird", "horse"]

        # Download COCO dataset if not already downloaded
        if not os.path.exists(dataset_dir):
            os.makedirs(dataset_dir, exist_ok=True)
            print("Downloading COCO dataset...")
            # Use pycocotools to download the dataset

            # Download annotations and images
            annotation_url = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
            image_url = "http://images.cocodataset.org/zips/train2017.zip"
            annotation_zip = os.path.join(dataset_dir, "annotations_trainval2017.zip")
            image_zip = os.path.join(dataset_dir, "train2017.zip")

            urlretrieve(annotation_url, annotation_zip)
            urlretrieve(image_url, image_zip)

            # Extract the downloaded files
            import zipfile
            with zipfile.ZipFile(annotation_zip, "r") as zip_ref:
                zip_ref.extractall(dataset_dir)
            with zipfile.ZipFile(image_zip, "r") as zip_ref:
                zip_ref.extractall(dataset_dir)

        # Load COCO annotations
        annotation_file = os.path.join(dataset_dir, "annotations/instances_train2017.json")
        coco = COCO.COCO(annotation_file)

        # Get category IDs for the selected categories
        category_ids = coco.getCatIds(catNms=selected_categories)
        image_ids = coco.getImgIds(catIds=category_ids)

        # Limit the number of images to the subset size
        image_ids = image_ids[:subset_size]

        # Initialize storage for images and labels
        X = []
        y = []

        # Process each image
        for img_id in image_ids:
            img_info = coco.loadImgs(img_id)[0]
            img_path = os.path.join(dataset_dir, "train2017", img_info["file_name"])

            # Load and preprocess the image
            try:
                img = tf.keras.utils.load_img(img_path, target_size=(128, 128))
                img_array = tf.keras.utils.img_to_array(img) / 255.0  # Normalize to [0, 1]
                X.append(img_array)

                # Get the label for the image
                ann_ids = coco.getAnnIds(imgIds=img_id, catIds=category_ids, iscrowd=None)
                anns = coco.loadAnns(ann_ids)
                label = anns[0]["category_id"]  # Use the first annotation's category ID
                y.append(label)
            except Exception as e:
                print(f"Error processing image {img_path}: {e}")

        # Convert to NumPy arrays
        X = np.array(X)
        y = np.array(y)

        # Cache the processed data
        print(f"Caching processed data to {cache_file}...")
        np.savez(cache_file, X=X, y=y)
        print("Processed data cached successfully.")

        print(f"COCO dataset loaded with {len(X)} samples.")
        return X, y

    def load_breast_cancer(self):
        """Load the Breast Cancer dataset."""
        print("Loading Breast Cancer dataset...")
        data = load_breast_cancer()
        X = data.data
        y = data.target
        print("Breast Cancer dataset loaded.")
        return X, y

    def load_wine(self):
        """Load the Wine dataset."""
        print("Loading Wine dataset...")
        data = load_wine()
        X = data.data
        y = data.target
        print("Wine dataset loaded.")
        return X, y

    def load_digits(self):
        """Load the Digits dataset."""
        print("Loading Digits dataset...")
        data = load_digits()
        X = data.data
        y = data.target
        print("Digits dataset loaded.")
        return X, y

    def load(self, path):
        try:
            with open(path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {path} not found. Initializing an empty file.")
            return {}
        except json.JSONDecodeError:
            print("The JSON has loaded in incorrectly.")
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
            model_details["hyperparameters"] = None
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

    def add_new_model(self, name, model, path):
        """
        Add a new model to the models list. This method is a placeholder and should be implemented as needed.
        """
        model_name = f"{name}_Model_{self.get_number_of_models(name)}"
        model_details = self.get_model_details(model)
        model_data = {
            "model_name": model_name,
            "path": path,
        }
        model_data.update(model_details)
        self.save_data(model_data, self.model_path)
        return model_name
    


