# Purpose: Generate Python code from a trained Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
from fogml.generators.base_generator import BaseGenerator
import numpy as np

class RandomForestPythonGeneratorTime(BaseGenerator):
    def __init__(self, clf):
        self.clf = clf
        self.indent_str = '    '
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
                return indent + f'results.append({class_label})\n'
        return recurse(0, 1)

    def generate(self, fname='random_forest_model.py', func_name="classifier"):
        result = 'import time\n'
        result += 'def %s(x, results, deadline, interrupt_flag):\n' % func_name
        # result += self.indent_str + 'results = []\n'


        for idx, estimator in enumerate(self.clf.estimators_):
            result += self.indent_str + f'# Tree {idx}\n'
            self.if_indent_str = self.indent_str
            result += self.indent_str + f'if time.time() < deadline or interrupt_flag.is_set():\n'
            tree_code = self.generate_statements(estimator.tree_)
            # Add extra indentation to tree code
            tree_code = tree_code.replace('\n', '\n' + self.indent_str)
            result += self.indent_str * 2 + tree_code.lstrip()
            result += '\n' + self.if_indent_str + f'else:\n'
            # result += self.if_indent_str + f'  stop_time_recorder["stop_time"] = time.time()\n'
            result += self.if_indent_str + f'  return results\n'


        # Voting logic
        result += self.indent_str + '# Voting logic\n'

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
        result += self.indent_str * 3 + 'result_class = i\n\n'
        result += self.indent_str + 'return result_class, len(results)\n'

        with open(fname, 'w') as py_file:
            py_file.write(result)
        return result