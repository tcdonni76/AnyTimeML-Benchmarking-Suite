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
     max_depth: None
     max_features: sqrt
     max_leaf_nodes: None
     max_samples: None
     min_impurity_decrease: 0.0
     min_samples_leaf: 1
     min_samples_split: 2
     min_weight_fraction_leaf: 0.0
     monotonic_cst: None
     n_estimators: 200
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
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[2] <= 5.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 1
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[0] <= 6.2500000000:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.6999999881:
                                    if time.time() < deadline:
                                        if x[2] <= 5.3499999046:
                                            if time.time() < deadline:
                                                if x[1] <= 2.7500000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 2
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
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.3499999046:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 3
    if time.time() < deadline:
        if x[2] <= 2.6999999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.5000000000:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[1] <= 2.5499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 2.6499999762:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 4
    if time.time() < deadline:
        if x[2] <= 2.5000000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.9500000477:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[3] <= 1.8000000119:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 5
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.1499998569:
                    if time.time() < deadline:
                        if x[2] <= 4.8499999046:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9000000954:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[0] <= 6.4000000954:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 6
    if time.time() < deadline:
        if x[0] <= 5.5499999523:
            if time.time() < deadline:
                if x[3] <= 0.8000000119:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.1500000954:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            if time.time() < deadline:
                                if x[3] <= 1.8499999642:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 7
    if time.time() < deadline:
        if x[3] <= 0.7000000030:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.9500000477:
                    if time.time() < deadline:
                        if x[0] <= 6.2500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.7500000000:
                                    if time.time() < deadline:
                                        if x[1] <= 2.6000000238:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[3] <= 1.6000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 8
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.9000000954:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.1499998569:
                            if time.time() < deadline:
                                if x[0] <= 6.5999999046:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.1500000954:
                                                    if time.time() < deadline:
                                                        if x[0] <= 5.9000000954:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 9
    if time.time() < deadline:
        if x[2] <= 2.3500000238:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 10
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.1499998569:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.6999999881:
                                    if time.time() < deadline:
                                        if x[1] <= 2.4500000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
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
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 11
    if time.time() < deadline:
        if x[3] <= 0.7000000030:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5999999642:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 12
    if time.time() < deadline:
        if x[3] <= 0.7000000030:
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
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 13
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[0] <= 6.0499999523:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 5.2500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            if time.time() < deadline:
                                if x[1] <= 2.9500000477:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 14
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 5.0499999523:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 15
    if time.time() < deadline:
        if x[2] <= 2.5000000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 16
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
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
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 17
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
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[1] <= 3.6000000238:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[1] <= 2.5499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 2.8999999762:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 18
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0999999046:
                            if time.time() < deadline:
                                if x[3] <= 1.6999999881:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 19
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
                        if x[1] <= 3.0499999523:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    if time.time() < deadline:
                                        if x[1] <= 2.6499999762:
                                            if time.time() < deadline:
                                                if x[0] <= 6.2000000477:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 20
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.2500000000:
                            if time.time() < deadline:
                                if x[2] <= 4.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.2999999523:
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
                            if time.time() < deadline:
                                if x[3] <= 2.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 21
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.9500000477:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.8999999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[0] <= 6.3499999046:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 22
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
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
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
    
    # Tree 23
    if time.time() < deadline:
        if x[2] <= 2.6999999881:
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
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 24
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.8500001431:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 25
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    if time.time() < deadline:
                                        if x[2] <= 5.3499999046:
                                            if time.time() < deadline:
                                                if x[3] <= 1.5500000119:
                                                    if time.time() < deadline:
                                                        if x[2] <= 5.0000000000:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 26
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 27
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
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[1] <= 2.3500000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 2.6499999762:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0499999523:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 28
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[1] <= 2.3500000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.5000000000:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 29
    if time.time() < deadline:
        if x[3] <= 0.7000000030:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 1.4499999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.8999999762:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            if time.time() < deadline:
                                                if x[1] <= 2.6499999762:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
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
    
    # Tree 30
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.8999999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 31
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6499999762:
                            if time.time() < deadline:
                                if x[0] <= 6.2000000477:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.0000000000:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9000000954:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 32
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
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    if time.time() < deadline:
                                        if x[1] <= 2.3500000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 33
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[2] <= 2.4499999881:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 5.0499999523:
                    if time.time() < deadline:
                        if x[2] <= 2.6499999762:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9500000477:
                                            if time.time() < deadline:
                                                if x[0] <= 5.9500000477:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 34
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 2.7500000000:
                            if time.time() < deadline:
                                if x[0] <= 5.9000000954:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 35
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.8999999762:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0499999523:
                            if time.time() < deadline:
                                if x[0] <= 5.8500001431:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 36
    if time.time() < deadline:
        if x[2] <= 2.3500000238:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            if time.time() < deadline:
                                if x[0] <= 6.2000000477:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.6499999762:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 37
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
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
                            if time.time() < deadline:
                                if x[0] <= 6.1500000954:
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
    
    # Tree 38
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
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
                    if time.time() < deadline:
                        if x[1] <= 3.6000000238:
                            if time.time() < deadline:
                                if x[0] <= 6.2500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.0499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 39
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.0499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[3] <= 1.5500000119:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            if time.time() < deadline:
                                if x[0] <= 5.8500001431:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 40
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
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
                    if time.time() < deadline:
                        if x[1] <= 3.3500000238:
                            if time.time() < deadline:
                                if x[2] <= 4.9000000954:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0000000000:
                            if time.time() < deadline:
                                if x[3] <= 1.8499999642:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 41
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.9500000477:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 42
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
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
                            if time.time() < deadline:
                                if x[0] <= 6.3999998569:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.9000000954:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 43
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[2] <= 2.4499999881:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 5.0499999523:
                    if time.time() < deadline:
                        if x[1] <= 3.4500000477:
                            if time.time() < deadline:
                                if x[2] <= 4.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.2000000477:
                                            if time.time() < deadline:
                                                if x[1] <= 3.1000000238:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[1] <= 2.7500000000:
                                                    if time.time() < deadline:
                                                        if x[2] <= 4.9500000477:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 2.7500000000:
                                    if time.time() < deadline:
                                        if x[3] <= 1.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 44
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0499999523:
                            if time.time() < deadline:
                                if x[3] <= 1.6999999881:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9000000954:
                                            if time.time() < deadline:
                                                if x[0] <= 5.9500000477:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    if time.time() < deadline:
                                        if x[2] <= 4.8500001431:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[3] <= 1.6499999762:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.0499999523:
                                            if time.time() < deadline:
                                                if x[3] <= 1.8000000119:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 45
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[3] <= 0.8000000119:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 2.5000000000:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 46
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.1499998569:
                            if time.time() < deadline:
                                if x[0] <= 6.5000000000:
                                    if time.time() < deadline:
                                        if x[3] <= 1.6999999881:
                                            if time.time() < deadline:
                                                if x[1] <= 2.7500000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 5.9500000477:
                                                    if time.time() < deadline:
                                                        if x[0] <= 5.8500001431:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.8500001431:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 47
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 48
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 2.6499999762:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.8500001431:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 49
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
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[0] <= 6.5000000000:
                                    if time.time() < deadline:
                                        if x[2] <= 4.8500001431:
                                            if time.time() < deadline:
                                                if x[0] <= 6.0499999523:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 50
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
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            if time.time() < deadline:
                                if x[0] <= 5.8500001431:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 51
    if time.time() < deadline:
        if x[2] <= 4.7999999523:
            if time.time() < deadline:
                if x[2] <= 2.3500000238:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[0] <= 6.1500000954:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 52
    if time.time() < deadline:
        if x[2] <= 4.8500001431:
            if time.time() < deadline:
                if x[2] <= 2.5999999642:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0999999046:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.2999999523:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[1] <= 2.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.6499999762:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9000000954:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.1500000954:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 53
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
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
                        if x[0] <= 6.0000000000:
                            if time.time() < deadline:
                                if x[2] <= 4.9000000954:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 54
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 5.9500000477:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    if time.time() < deadline:
                                        if x[0] <= 6.1499998569:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 2.8500000238:
                                            if time.time() < deadline:
                                                if x[2] <= 4.8999998569:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[3] <= 1.5500000119:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 55
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 5.3499999046:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 56
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[0] <= 6.5000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 57
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[3] <= 0.8000000119:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.2500000000:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.8500000238:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0500001907:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.4000000954:
                                                    if time.time() < deadline:
                                                        if x[2] <= 5.0000000000:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 58
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.2500000000:
                            if time.time() < deadline:
                                if x[2] <= 4.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 59
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[2] <= 5.3499999046:
                                    if time.time() < deadline:
                                        if x[1] <= 2.3500000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 60
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.1499998569:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    if time.time() < deadline:
                                        if x[1] <= 2.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 2.8999999762:
                                            if time.time() < deadline:
                                                if x[3] <= 1.7500000000:
                                                    if time.time() < deadline:
                                                        if x[2] <= 5.0499999523:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 61
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.9500000477:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.2500000000:
                                    if time.time() < deadline:
                                        if x[0] <= 5.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 62
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
                    if time.time() < deadline:
                        if x[1] <= 2.6999999285:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 63
    if time.time() < deadline:
        if x[3] <= 1.6999999881:
            if time.time() < deadline:
                if x[3] <= 0.7000000030:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.3499999046:
                            if time.time() < deadline:
                                if x[3] <= 1.4499999881:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[3] <= 1.5500000119:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.9000000954:
                    if time.time() < deadline:
                        if x[1] <= 3.1000000238:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 64
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 1.4499999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 65
    if time.time() < deadline:
        if x[2] <= 2.3500000238:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[0] <= 6.5000000000:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            if time.time() < deadline:
                                                if x[1] <= 2.6499999762:
                                                    if time.time() < deadline:
                                                        if x[2] <= 4.9500000477:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.0499999523:
                                    if time.time() < deadline:
                                        if x[0] <= 5.9000000954:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 66
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.6499999762:
                            if time.time() < deadline:
                                if x[1] <= 2.5499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 4.5499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[1] <= 3.0000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 67
    if time.time() < deadline:
        if x[2] <= 2.6000000238:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.2500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.8500000238:
                            if time.time() < deadline:
                                if x[2] <= 4.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 7.0999999046:
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
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 68
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.2500000000:
                            if time.time() < deadline:
                                if x[2] <= 4.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            if time.time() < deadline:
                                if x[0] <= 6.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 69
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 3.3999999762:
                            if time.time() < deadline:
                                if x[1] <= 2.2500000000:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0999999046:
                                            if time.time() < deadline:
                                                if x[2] <= 4.5000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.2500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0499999523:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 70
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 5.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[2] <= 5.3499999046:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 71
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    if time.time() < deadline:
                                        if x[0] <= 6.4500000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.8499999642:
                                    if time.time() < deadline:
                                        if x[2] <= 4.8500001431:
                                            if time.time() < deadline:
                                                if x[1] <= 3.1000000238:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 72
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 5.0000000000:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0999999046:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 73
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.6499999762:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            if time.time() < deadline:
                                if x[2] <= 4.8500001431:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 74
    if time.time() < deadline:
        if x[2] <= 4.7500000000:
            if time.time() < deadline:
                if x[2] <= 2.3500000238:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[1] <= 3.1000000238:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 75
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.6499999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 76
    if time.time() < deadline:
        if x[3] <= 0.7000000030:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 2.8500000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.3999998569:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 77
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[3] <= 0.8000000119:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 2.7500000000:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            if time.time() < deadline:
                                if x[2] <= 4.8500001431:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 78
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 2.2500000000:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0999999046:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
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
                            if time.time() < deadline:
                                if x[2] <= 5.1000001431:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 79
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[1] <= 2.7000000477:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 3.4500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.2000000477:
                            if time.time() < deadline:
                                if x[3] <= 1.6999999881:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0499999523:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[3] <= 1.5500000119:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1499999762:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.2000000477:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 80
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
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
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 81
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            if time.time() < deadline:
                                if x[0] <= 6.1000001431:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 82
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 83
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[2] <= 2.5999999642:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 0.7000000030:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            if time.time() < deadline:
                                if x[3] <= 1.6499999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 5.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 84
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[3] <= 1.3499999642:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.0499999523:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.0499999523:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 85
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.8499999642:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.3500000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.6999999881:
                                            if time.time() < deadline:
                                                if x[0] <= 6.1500000954:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[3] <= 1.4499999881:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            if time.time() < deadline:
                                                                if x[2] <= 5.0000000000:
                                                                    trees.append(1)
                                                                    results[0], results[1] = vote_logic(trees)
                                                                else:
                                                                    trees.append(2)
                                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 5.9500000477:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 86
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[2] <= 2.5999999642:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 5.3499999046:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 87
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
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
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.5999999046:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 88
    if time.time() < deadline:
        if x[2] <= 2.7499999404:
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
                            if time.time() < deadline:
                                if x[0] <= 6.1500000954:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            if time.time() < deadline:
                                if x[2] <= 4.8500001431:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 89
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
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
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 2.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 90
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
                        if x[2] <= 5.1499998569:
                            if time.time() < deadline:
                                if x[3] <= 1.8499999642:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            if time.time() < deadline:
                                                if x[3] <= 1.7500000000:
                                                    if time.time() < deadline:
                                                        if x[0] <= 6.5000000000:
                                                            if time.time() < deadline:
                                                                if x[3] <= 1.5500000119:
                                                                    if time.time() < deadline:
                                                                        if x[2] <= 4.9500000477:
                                                                            trees.append(1)
                                                                            results[0], results[1] = vote_logic(trees)
                                                                        else:
                                                                            trees.append(2)
                                                                            results[0], results[1] = vote_logic(trees)
                                                                else:
                                                                    trees.append(1)
                                                                    results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 91
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.6999999285:
                                    if time.time() < deadline:
                                        if x[3] <= 1.1999999881:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.1499998569:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            if time.time() < deadline:
                                if x[2] <= 4.9000000954:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 92
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.1500000954:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 93
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.2500000000:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 5.3499999046:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[0] <= 6.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 94
    if time.time() < deadline:
        if x[2] <= 2.9000000358:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.1499998569:
                            if time.time() < deadline:
                                if x[0] <= 6.0499999523:
                                    if time.time() < deadline:
                                        if x[0] <= 5.8500001431:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0499999523:
                                                    if time.time() < deadline:
                                                        if x[1] <= 3.1000000238:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9500000477:
                                            if time.time() < deadline:
                                                if x[0] <= 6.2500000000:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[1] <= 2.6000000238:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            if time.time() < deadline:
                                                                if x[1] <= 2.7500000000:
                                                                    trees.append(2)
                                                                    results[0], results[1] = vote_logic(trees)
                                                                else:
                                                                    trees.append(1)
                                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 95
    if time.time() < deadline:
        if x[2] <= 2.7499999404:
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
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.4499999881:
                                            if time.time() < deadline:
                                                if x[2] <= 5.2000000477:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 96
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[2] <= 2.4499999881:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.1499998569:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            if time.time() < deadline:
                                if x[1] <= 3.6000000238:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
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
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 97
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
                        if x[2] <= 4.9500000477:
                            if time.time() < deadline:
                                if x[3] <= 1.6499999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    if time.time() < deadline:
                                        if x[1] <= 2.7500000000:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 98
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.2500000000:
                    if time.time() < deadline:
                        if x[0] <= 5.6499998569:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.4499999881:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            if time.time() < deadline:
                                                if x[2] <= 4.5000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[2] <= 5.0499999523:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            if time.time() < deadline:
                                                                if x[3] <= 1.7500000000:
                                                                    trees.append(1)
                                                                    results[0], results[1] = vote_logic(trees)
                                                                else:
                                                                    trees.append(2)
                                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 99
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.1499998569:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[3] <= 1.6499999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 2.7500000000:
                                            if time.time() < deadline:
                                                if x[0] <= 5.9000000954:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            if time.time() < deadline:
                                if x[3] <= 1.6499999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 100
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 2.6000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 101
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            if time.time() < deadline:
                                if x[0] <= 6.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 102
    if time.time() < deadline:
        if x[2] <= 2.3500000238:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 5.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.6999999881:
                                    if time.time() < deadline:
                                        if x[2] <= 5.3499999046:
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
                                            if time.time() < deadline:
                                                if x[3] <= 1.8999999762:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 103
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    if time.time() < deadline:
                                        if x[1] <= 2.7500000000:
                                            if time.time() < deadline:
                                                if x[3] <= 1.5500000119:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    if time.time() < deadline:
                                        if x[1] <= 2.6000000238:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 104
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[1] <= 2.3500000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.4499999881:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 105
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.9000000954:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 106
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 2.8500000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 107
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 108
    if time.time() < deadline:
        if x[0] <= 5.7500000000:
            if time.time() < deadline:
                if x[2] <= 2.5999999642:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[1] <= 2.4500000477:
                            if time.time() < deadline:
                                if x[2] <= 4.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 109
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[2] <= 5.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 110
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 2.2500000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.7500000000:
                                    if time.time() < deadline:
                                        if x[1] <= 2.6499999762:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0000000000:
                            if time.time() < deadline:
                                if x[1] <= 3.0000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 111
    if time.time() < deadline:
        if x[2] <= 2.3500000238:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 5.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    if time.time() < deadline:
                                        if x[3] <= 1.6000000238:
                                            if time.time() < deadline:
                                                if x[2] <= 4.9500000477:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 112
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 3.1499999762:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.3500001431:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 113
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 114
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.8500001431:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 115
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
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
                            if time.time() < deadline:
                                if x[0] <= 6.5000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 116
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 5.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            if time.time() < deadline:
                                if x[1] <= 3.0499999523:
                                    if time.time() < deadline:
                                        if x[3] <= 1.6499999762:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 117
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.8999999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 5.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 118
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 5.6499998569:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.2500000000:
                            if time.time() < deadline:
                                if x[2] <= 4.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 5.8500001431:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[1] <= 3.1000000238:
                                                    if time.time() < deadline:
                                                        if x[2] <= 5.0499999523:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[0] <= 6.0499999523:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 119
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
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 2.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 120
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
                        if x[1] <= 2.6499999762:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 121
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
                        if x[2] <= 4.9000000954:
                            if time.time() < deadline:
                                if x[1] <= 3.0000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 122
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.8500000238:
                                    if time.time() < deadline:
                                        if x[2] <= 4.7999999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[1] <= 3.0000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 123
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    if time.time() < deadline:
                                        if x[1] <= 2.5499999523:
                                            if time.time() < deadline:
                                                if x[0] <= 6.1500000954:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 124
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.5999999046:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 5.0999999046:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 125
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.1499998569:
                            if time.time() < deadline:
                                if x[1] <= 3.1499999762:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0999999046:
                                            if time.time() < deadline:
                                                if x[0] <= 5.9000000954:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[3] <= 1.5500000119:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.8999999762:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 126
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[2] <= 2.5999999642:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 0.7000000030:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.6999999881:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 3.0000000000:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6499999762:
                            if time.time() < deadline:
                                if x[0] <= 6.1500000954:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 127
    if time.time() < deadline:
        if x[2] <= 2.6999999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.8499999642:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[3] <= 1.6999999881:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 3.0000000000:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 128
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 5.3499999046:
                            if time.time() < deadline:
                                if x[0] <= 6.2500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.0499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 129
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[1] <= 2.8500000238:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.4000000954:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 130
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 5.0499999523:
                    if time.time() < deadline:
                        if x[1] <= 2.8500000238:
                            if time.time() < deadline:
                                if x[0] <= 5.6499998569:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 4.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 4.9500000477:
                                                    if time.time() < deadline:
                                                        if x[3] <= 1.6499999762:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 2.7500000000:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 131
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[2] <= 2.3500000238:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 0.7000000030:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.5000000000:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 132
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 133
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
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
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            if time.time() < deadline:
                                if x[1] <= 3.7499998808:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.4500000477:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 134
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
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    if time.time() < deadline:
                                        if x[1] <= 2.3500000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.2000000477:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 135
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[2] <= 4.8499999046:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.1500000954:
                                    if time.time() < deadline:
                                        if x[1] <= 2.4500000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 3.0000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 136
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.3500001431:
                    if time.time() < deadline:
                        if x[0] <= 5.6499998569:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.3500000238:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.6999999881:
                                            if time.time() < deadline:
                                                if x[2] <= 5.3499999046:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 137
    if time.time() < deadline:
        if x[0] <= 5.5499999523:
            if time.time() < deadline:
                if x[2] <= 2.5999999642:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 2.6000000238:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.2500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.0499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0000000000:
                            if time.time() < deadline:
                                if x[1] <= 3.0000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 138
    if time.time() < deadline:
        if x[3] <= 0.7000000030:
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
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    if time.time() < deadline:
                                        if x[3] <= 1.6999999881:
                                            if time.time() < deadline:
                                                if x[1] <= 2.6499999762:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[1] <= 2.7500000000:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            if time.time() < deadline:
                                                                if x[0] <= 6.5500001907:
                                                                    trees.append(2)
                                                                    results[0], results[1] = vote_logic(trees)
                                                                else:
                                                                    trees.append(1)
                                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 139
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.2500000000:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0000000000:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 140
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    if time.time() < deadline:
                                        if x[0] <= 6.2000000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 141
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 5.6499998569:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.6499998569:
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
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 142
    if time.time() < deadline:
        if x[3] <= 0.7000000030:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6499999762:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 143
    if time.time() < deadline:
        if x[0] <= 5.5499999523:
            if time.time() < deadline:
                if x[1] <= 2.8000000715:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 0.9500000030:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 3.6000000238:
                            if time.time() < deadline:
                                if x[0] <= 6.2500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.3500001431:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 144
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.1499998569:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.7500000000:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 145
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.1499998569:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[3] <= 1.4499999881:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 4.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0499999523:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            if time.time() < deadline:
                                if x[2] <= 4.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 4.8500001431:
                                            if time.time() < deadline:
                                                if x[3] <= 1.5999999642:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 146
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 5.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    if time.time() < deadline:
                                        if x[1] <= 2.4500000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0499999523:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[1] <= 2.7500000000:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 147
    if time.time() < deadline:
        if x[0] <= 5.7500000000:
            if time.time() < deadline:
                if x[3] <= 0.8000000119:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.1500000954:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 4.9500000477:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 148
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[1] <= 2.8000000715:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 0.7000000030:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.2500000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.2500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0499999523:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            if time.time() < deadline:
                                if x[2] <= 5.4000000954:
                                    if time.time() < deadline:
                                        if x[0] <= 5.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 149
    if time.time() < deadline:
        if x[2] <= 4.7500000000:
            if time.time() < deadline:
                if x[2] <= 2.6999999881:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[1] <= 2.8999999762:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    if time.time() < deadline:
                                        if x[3] <= 1.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 150
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 5.3499999046:
                            if time.time() < deadline:
                                if x[1] <= 2.2500000000:
                                    if time.time() < deadline:
                                        if x[1] <= 2.1000000238:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[3] <= 1.2500000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.0499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.1500000954:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 151
    if time.time() < deadline:
        if x[3] <= 1.6499999762:
            if time.time() < deadline:
                if x[2] <= 2.5000000000:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 2.8500000238:
                            if time.time() < deadline:
                                if x[3] <= 1.3499999642:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.4000000954:
                                            if time.time() < deadline:
                                                if x[0] <= 6.1499998569:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[2] <= 4.7999999523:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            trees.append(2)
            results[0], results[1] = vote_logic(trees)
    
    # Tree 152
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 5.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[0] <= 6.3500001431:
                                    if time.time() < deadline:
                                        if x[3] <= 1.3499999642:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[1] <= 2.6499999762:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            if time.time() < deadline:
                                                                if x[1] <= 2.7500000000:
                                                                    trees.append(1)
                                                                    results[0], results[1] = vote_logic(trees)
                                                                else:
                                                                    trees.append(2)
                                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.0499999523:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 153
    if time.time() < deadline:
        if x[0] <= 5.5499999523:
            if time.time() < deadline:
                if x[3] <= 0.8000000119:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 0.7000000030:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[0] <= 6.3499999046:
                                    if time.time() < deadline:
                                        if x[1] <= 2.4500000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.8500001431:
                                    if time.time() < deadline:
                                        if x[0] <= 5.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 154
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
                        if x[0] <= 6.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 2.8500000238:
                                    if time.time() < deadline:
                                        if x[0] <= 5.9000000954:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.6499999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 155
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.3500001431:
                            if time.time() < deadline:
                                if x[3] <= 1.6999999881:
                                    if time.time() < deadline:
                                        if x[0] <= 6.1500000954:
                                            if time.time() < deadline:
                                                if x[1] <= 2.4500000477:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 156
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 2.7500000000:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 157
    if time.time() < deadline:
        if x[2] <= 2.6999999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 1.4499999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.0999999046:
                                    if time.time() < deadline:
                                        if x[0] <= 5.7000000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.8499999642:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 158
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
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 159
    if time.time() < deadline:
        if x[2] <= 2.6999999881:
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
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 160
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.4500000477:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.1500000954:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.5000000000:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 161
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[3] <= 0.8000000119:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.0499999523:
                    if time.time() < deadline:
                        if x[1] <= 3.4500000477:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[3] <= 1.4499999881:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 4.8999998569:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 162
    if time.time() < deadline:
        if x[2] <= 2.5999999642:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.5000000000:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            if time.time() < deadline:
                                if x[0] <= 5.8500001431:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 163
    if time.time() < deadline:
        if x[2] <= 2.6999999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.9500000477:
                            if time.time() < deadline:
                                if x[3] <= 1.8499999642:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 164
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[2] <= 2.4499999881:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 3.7999999523:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.4499999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    if time.time() < deadline:
                                        if x[3] <= 1.8499999642:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 165
    if time.time() < deadline:
        if x[2] <= 2.3500000238:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.2500000000:
                            if time.time() < deadline:
                                if x[2] <= 4.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.2999999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[1] <= 3.1000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 166
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[1] <= 2.7000000477:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 0.9500000030:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.9500000477:
                    if time.time() < deadline:
                        if x[2] <= 2.7000000477:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.6999999881:
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
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 167
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[1] <= 2.8999999762:
                                    if time.time() < deadline:
                                        if x[0] <= 6.2000000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 168
    if time.time() < deadline:
        if x[2] <= 2.6999999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.5999999642:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 169
    if time.time() < deadline:
        if x[2] <= 4.7500000000:
            if time.time() < deadline:
                if x[3] <= 0.8000000119:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[1] <= 3.0000000000:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 170
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 3.0000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 171
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
                        if x[2] <= 4.9500000477:
                            if time.time() < deadline:
                                if x[3] <= 1.6499999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 172
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 173
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
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
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 174
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
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 175
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
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
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 176
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.6999999881:
                    if time.time() < deadline:
                        if x[1] <= 2.2500000000:
                            if time.time() < deadline:
                                if x[2] <= 4.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.2500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.3500001431:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.9000000954:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 177
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
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 0.7000000030:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[0] <= 6.5000000000:
                                    if time.time() < deadline:
                                        if x[3] <= 1.6499999762:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 178
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[3] <= 0.7500000000:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 0.7000000030:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 5.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.3499999046:
                                            if time.time() < deadline:
                                                if x[3] <= 1.5500000119:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 179
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
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    if time.time() < deadline:
                                        if x[0] <= 6.2000000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 5.0000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 4.8500001431:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1000000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 180
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 5.9500000477:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.5000000000:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 181
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[1] <= 2.7000000477:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 5.2999999523:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 3.4500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 0.6000000015:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    if time.time() < deadline:
                                        if x[3] <= 1.3499999642:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.2000000477:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 182
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
                        if x[3] <= 1.6499999762:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    if time.time() < deadline:
                                        if x[0] <= 5.8500001431:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 183
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
            if time.time() < deadline:
                if x[3] <= 0.8999999911:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[1] <= 3.6000000238:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 6.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 2.6000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.6499999762:
                                    if time.time() < deadline:
                                        if x[0] <= 6.2000000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 184
    if time.time() < deadline:
        if x[2] <= 2.6999999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 6.3500001431:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.5499999523:
                                    if time.time() < deadline:
                                        if x[0] <= 6.1500000954:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0499999523:
                                            if time.time() < deadline:
                                                if x[0] <= 5.8500001431:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[2] <= 4.9500000477:
                                                            if time.time() < deadline:
                                                                if x[0] <= 5.9500000477:
                                                                    trees.append(1)
                                                                    results[0], results[1] = vote_logic(trees)
                                                                else:
                                                                    trees.append(2)
                                                                    results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 185
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6499999762:
                            if time.time() < deadline:
                                if x[1] <= 2.3500000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.4499999881:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 6.0499999523:
                                    if time.time() < deadline:
                                        if x[2] <= 4.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 186
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 2.7500000000:
                            if time.time() < deadline:
                                if x[1] <= 2.6499999762:
                                    if time.time() < deadline:
                                        if x[0] <= 6.2000000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[3] <= 1.6999999881:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.0000000000:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 187
    if time.time() < deadline:
        if x[0] <= 5.4500000477:
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
                        if x[2] <= 2.6000000238:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.2500000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 5.3499999046:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 188
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.5999999642:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 5.9500000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[0] <= 6.0499999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.2000000477:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 189
    if time.time() < deadline:
        if x[3] <= 0.7500000000:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[3] <= 1.3499999642:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.8999999762:
                                    if time.time() < deadline:
                                        if x[2] <= 4.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.0499999523:
                                                    if time.time() < deadline:
                                                        if x[3] <= 1.5500000119:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 4.9000000954:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 190
    if time.time() < deadline:
        if x[2] <= 4.7500000000:
            if time.time() < deadline:
                if x[2] <= 2.3500000238:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 5.1499998569:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 3.1499999762:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.8999999762:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 191
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[0] <= 6.5000000000:
                                    if time.time() < deadline:
                                        if x[1] <= 2.6499999762:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[0] <= 6.1500000954:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 192
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[1] <= 2.2500000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 193
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
                            if time.time() < deadline:
                                if x[0] <= 6.3499999046:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 194
    if time.time() < deadline:
        if x[2] <= 4.8500001431:
            if time.time() < deadline:
                if x[3] <= 0.7000000030:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[1] <= 2.6499999762:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 195
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[2] <= 4.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.5999999642:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 6.0499999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            if time.time() < deadline:
                                if x[2] <= 4.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 196
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    if time.time() < deadline:
                                        if x[1] <= 2.3500000238:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 197
    if time.time() < deadline:
        if x[2] <= 2.6999999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 5.0499999523:
                            if time.time() < deadline:
                                if x[3] <= 1.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.6999999881:
                                    if time.time() < deadline:
                                        if x[3] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 198
    if time.time() < deadline:
        if x[3] <= 0.8000000119:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 4.8500001431:
                    if time.time() < deadline:
                        if x[3] <= 1.6999999881:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 5.9500000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 1.7500000000:
                            if time.time() < deadline:
                                if x[0] <= 6.5000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 199
    if time.time() < deadline:
        if x[2] <= 2.4499999881:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[2] <= 4.9500000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 1.5500000119:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
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
