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
     max_depth: 7
     max_features: sqrt
     max_leaf_nodes: None
     max_samples: None
     min_impurity_decrease: 0.0
     min_samples_leaf: 5
     min_samples_split: 3
     min_weight_fraction_leaf: 0.0
     n_estimators: 10
     n_jobs: None
     oob_score: False
     random_state: None
     verbose: 0
     warm_start: False

"""
def classifier(x, results, deadline, interrupt_flag):
    
    # Tree 0
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                results.append(1)
            else:
                if x[2] <= 5.0499999523:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 1
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    if x[2] <= 5.1499998569:
                        results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 2
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[2] <= 4.6499998569:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 3
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 6.3500001431:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[3] <= 1.7500000000:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 4
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[1] <= 2.5499999523:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[2] <= 5.0499999523:
                        results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 5
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 1.6500000358:
                results.append(0)
            else:
                results.append(0)
        else:
            if x[0] <= 5.9500000477:
                if x[2] <= 3.7500000000:
                    results.append(0)
                else:
                    if x[2] <= 4.1499998569:
                        results.append(1)
                    else:
                        results.append(1)
            else:
                if x[3] <= 1.6999999881:
                    if x[2] <= 4.7500000000:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 6
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 7
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 1.7500000000:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    results.append(1)
        else:
            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 8
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 5.1499998569:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 9
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.6499999762:
                if x[3] <= 1.4499999881:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[0] <= 6.1499998569:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    return vote_logic(results)
    
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
    return result_class, len(results)
