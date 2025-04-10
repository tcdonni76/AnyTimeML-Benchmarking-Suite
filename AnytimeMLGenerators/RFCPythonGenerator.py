# Purpose: Generate Python code from a trained Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
from fogml.generators.base_generator import BaseGenerator
import numpy as np

class RFPyAnytimeGenerator(BaseGenerator):
    def __init__(self, clf, dataset):
        self.clf = clf
        self.indent_str = '  '
        self.dataset = dataset
        self.if_indent_str = self.indent_str # Preserve indent of if statement

    def generate_statements(self, tree, depth=1):
        def recurse(node, depth):
            indent = self.indent_str * depth
            if tree.feature[node] >= 0:
                name = tree.feature[node]
                threshold = tree.threshold[node]
                code = indent + f"if x[{name}] <= {threshold:.10f}:\n"
                code += recurse(tree.children_left[node], depth + 1)
                code += indent + "else:\n"
                code += recurse(tree.children_right[node], depth + 1)
                return code
            else:
                class_label = self.clf.classes_[np.argmax(tree.value[node])]
                return indent + f'trees.append({class_label})\n'
        return recurse(0, 1)

    def generate_metadata(self, fold_number):
        """
        Generate metadata for the generated Python file.

        Args:
            fold_number (int): The fold number from K-Fold cross-validation.

        Returns:
            str: Metadata as a formatted string.
        """
        # Extract hyperparameters from the RandomForestClassifier
        hyperparameters = self.clf.get_params()
        # Format the metadata
        metadata = '"""\n\n***** Metadata ******\n'
        metadata += f"Dataset: {self.dataset}\n"
        metadata += f"Fold: {fold_number} of K-Fold cross validaiton\n"
        metadata += "Hyperparameters:\n"
        for key, value in hyperparameters.items():
            metadata += f"     {key}: {value}\n"
        metadata += '\n"""\n'
        return metadata


    def generate(self, X, y, fold_number, fname='random_forest_model.py', func_name="classifier"):
        self.clf.fit(X, y)  # Fit the model provided to the generator with the relevant data
        result = 'import time\n'
        result += self.generate_metadata(fold_number)
        result += 'def %s(x, result):\n' % func_name
        result += self.indent_str + '  trees = []\n'

        for idx, estimator in enumerate(self.clf.estimators_):
            result += self.indent_str + f'\n# Tree {idx}\n'
            self.if_indent_str = self.indent_str
            tree_code = self.generate_statements(estimator.tree_)

            
            tree_code = tree_code.replace('\n', '\n' + self.indent_str)
            # Add extra indentation to tree code
            result += self.indent_str * 2 + tree_code.lstrip()
            result += self.indent_str + f'  result = vote_logic(trees)\n'

        result += self.indent_str + '\n    return vote_logic(trees)\n'

        # Voting logic
        result += self.indent_str + '\n    # Voting logic\n'

        result += 'def vote_logic(results):\n'
        result += self.indent_str + 'classes_amount = 0\n'
        result += self.indent_str + 'for val in results:\n'
        result += self.indent_str * 2 + 'if val + 1 > classes_amount:\n'
        result += self.indent_str * 3 + 'classes_amount = val + 1\n\n'

        result += self.indent_str + 'result_class = -1\n'
        result += self.indent_str + 'max_apperance = 0\n'
        result += self.indent_str + 'for i in range(classes_amount):\n'
        result += self.indent_str * 2 + 'apperance = 0\n'
        result += self.indent_str * 2 + 'for val in results:\n'
        result += self.indent_str * 3 + 'if val == i:\n'
        result += self.indent_str * 4 + 'apperance += 1\n'
        result += self.indent_str * 2 + 'if apperance > max_apperance:\n'
        result += self.indent_str * 3 + 'max_apperance = apperance\n'
        result += self.indent_str * 3 + 'result_class = i\n'
        result += self.indent_str + '\n    # Return the prediction and number of trees that have been processed\n'
        result += self.indent_str + 'return result_class, len(results)\n'

        with open(fname, 'w') as py_file:
            py_file.write(result)
        return result
    

from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
gen = RFPyAnytimeGenerator(RandomForestClassifier(), 'iris')
gen.generate(X, y, 1, 'test_multiprocessing_classifier.py')