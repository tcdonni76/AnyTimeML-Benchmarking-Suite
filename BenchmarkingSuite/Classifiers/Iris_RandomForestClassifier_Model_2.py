import time
"""

***** Metadata ******
Dataset: Iris
Fold: 5 of K-Fold cross validaiton
Hyperparameters:
     bootstrap: True
     ccp_alpha: 0.0
     class_weight: None
     criterion: gini
     max_depth: 3
     max_features: sqrt
     max_leaf_nodes: None
     max_samples: None
     min_impurity_decrease: 0.0
     min_samples_leaf: 2
     min_samples_split: 5
     min_weight_fraction_leaf: 0.0
     monotonic_cst: None
     n_estimators: 10
     n_jobs: None
     oob_score: False
     random_state: None
     verbose: 0
     warm_start: False

"""
def classifier(x, results, deadline, interrupt_flag):
    trees = []
    
    # Tree 0
    if time.time() < deadline:
        if x[2] <= 4.7500000000:
            if time.time() < deadline:
                if x[2] <= 2.4499999881:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 1
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 2
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.2500000000:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 3
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 3.1499999762:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 4
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.9000000954:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 5
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 6
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 7
    if time.time() < deadline:
        if x[2] <= 4.8500001431:
            if time.time() < deadline:
                if x[3] <= 0.8000000119:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[1] <= 2.5499999523:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 8
    if time.time() < deadline:
        if x[0] <= 5.5499999523:
            if time.time() < deadline:
                if x[2] <= 2.4499999881:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[3] <= 1.0500000119:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 9
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[1] <= 2.8500000238:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Voting logic
def vote_logic(results):
    classes_amount = 0
    for val in results:
        if val + 1 > classes_amount:
            classes_amount = val + 1

    result_class = -1
    max_apperance = 0
    for i in range(classes_amount):
        apperance = 0
        for val in results:
            if val == i:
                apperance += 1
        if apperance > max_apperance:
            max_apperance = apperance
            result_class = i
    
    # Return the prediction and number of trees that have been processed
    return [result_class, len(results)]
