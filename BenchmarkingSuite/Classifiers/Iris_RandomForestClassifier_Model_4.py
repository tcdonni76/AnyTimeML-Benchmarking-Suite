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
     max_depth: 10
     max_features: sqrt
     max_leaf_nodes: None
     max_samples: None
     min_impurity_decrease: 0.0
     min_samples_leaf: 5
     min_samples_split: 10
     min_weight_fraction_leaf: 0.0
     n_estimators: 50
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
            if x[3] <= 1.7500000000:
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
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 5.7500000000:
                if x[0] <= 5.5499999523:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[2] <= 4.7999999523:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    if x[3] <= 1.8499999642:
                        results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 2
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[2] <= 2.8499999642:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[2] <= 4.8500001431:
                if x[1] <= 3.1499999762:
                    if x[2] <= 4.4500000477:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(1)
            else:
                if x[1] <= 2.5499999523:
                    results.append(2)
                else:
                    if x[1] <= 3.0499999523:
                        if x[0] <= 6.5999999046:
                            results.append(2)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 3
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[3] <= 1.4499999881:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.6999999881:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 4
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 5.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.9500000477:
                    if x[0] <= 6.3500001431:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 5
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[0] <= 6.0999999046:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 6
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[0] <= 6.0499999523:
                    results.append(1)
                else:
                    if x[1] <= 2.8500000238:
                        results.append(1)
                    else:
                        results.append(1)
            else:
                if x[1] <= 3.1499999762:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 7
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 5.0499999523:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 8
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 1.7500000000:
            if x[2] <= 2.5999999642:
                results.append(0)
            else:
                if x[3] <= 1.4499999881:
                    results.append(1)
                else:
                    if x[0] <= 6.0999999046:
                        results.append(1)
                    else:
                        results.append(1)
        else:
            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 9
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[1] <= 2.8000000715:
                results.append(1)
            else:
                results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.7999999523:
                    if x[1] <= 3.1000000238:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 10
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[0] <= 5.9500000477:
                    results.append(1)
                else:
                    if x[0] <= 6.3500001431:
                        results.append(1)
                    else:
                        results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 11
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 1.7500000000:
            if x[2] <= 2.5999999642:
                results.append(0)
            else:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    results.append(1)
        else:
            if x[2] <= 4.9500000477:
                results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 12
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9000000954:
                    results.append(1)
                else:
                    results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 13
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[2] <= 4.5999999046:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[2] <= 4.9500000477:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 14
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[0] <= 5.9500000477:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[1] <= 3.1499999762:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 15
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[1] <= 3.0499999523:
                results.append(0)
            else:
                results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.0499999523:
                    results.append(1)
                else:
                    if x[1] <= 2.7500000000:
                        results.append(1)
                    else:
                        results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 16
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 6.1499998569:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[0] <= 6.7500000000:
                    if x[3] <= 1.7500000000:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 17
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 18
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[3] <= 1.4499999881:
                    results.append(1)
                else:
                    if x[1] <= 2.8500000238:
                        results.append(1)
                    else:
                        results.append(1)
            else:
                if x[1] <= 3.1499999762:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 19
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.8000000119:
            results.append(0)
        else:
            if x[0] <= 6.2500000000:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 20
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[2] <= 4.6499998569:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 21
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[1] <= 2.7500000000:
                results.append(1)
            else:
                results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[3] <= 1.1500000358:
                    results.append(1)
                else:
                    if x[0] <= 6.1499998569:
                        results.append(1)
                    else:
                        results.append(1)
            else:
                if x[3] <= 1.9499999881:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 22
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[3] <= 0.7500000000:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.8500001431:
                    if x[3] <= 1.2500000000:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(1)
            else:
                if x[2] <= 5.0499999523:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 23
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 1.8000000119:
                results.append(0)
            else:
                results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[2] <= 3.9500000477:
                    results.append(1)
                else:
                    if x[2] <= 4.6499998569:
                        results.append(1)
                    else:
                        results.append(1)
            else:
                if x[3] <= 1.9499999881:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 24
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[0] <= 5.9500000477:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[1] <= 2.9500000477:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 25
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.3500000089:
                results.append(0)
            else:
                results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[2] <= 4.6500000954:
                    if x[2] <= 3.9500000477:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(2)
            else:
                if x[2] <= 5.0499999523:
                    if x[2] <= 4.7500000000:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 26
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[2] <= 4.6499998569:
                    results.append(1)
                else:
                    results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 27
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 3.2500000000:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[0] <= 6.2500000000:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 28
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[2] <= 1.6500000358:
                results.append(0)
            else:
                results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[2] <= 4.0499999523:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 29
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[0] <= 5.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[1] <= 2.9500000477:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    if x[3] <= 1.8499999642:
                        results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 30
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 31
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 5.7500000000:
                results.append(1)
            else:
                if x[1] <= 2.9500000477:
                    if x[3] <= 1.6999999881:
                        if x[2] <= 4.6499998569:
                            results.append(1)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[3] <= 1.8999999762:
                        results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 32
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[3] <= 1.4499999881:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 33
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.3500000089:
                results.append(0)
            else:
                results.append(0)
        else:
            if x[2] <= 4.7500000000:
                if x[1] <= 3.1499999762:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    if x[0] <= 6.1499998569:
                        results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 34
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[3] <= 1.5500000119:
                    if x[3] <= 1.3499999642:
                        results.append(1)
                    else:
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
    
    # Tree 35
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.4500000477:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[0] <= 6.2500000000:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 36
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[3] <= 1.4499999881:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[0] <= 6.2500000000:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 37
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 5.2000000477:
                    if x[1] <= 2.7500000000:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 38
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.3500000089:
                results.append(0)
            else:
                results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[3] <= 1.1500000358:
                    results.append(1)
                else:
                    if x[2] <= 4.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[2] <= 5.1499998569:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 39
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.3500000238:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 40
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 41
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                results.append(1)
            else:
                if x[2] <= 5.1499998569:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 42
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[0] <= 5.7500000000:
                    results.append(1)
                else:
                    results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    if x[2] <= 5.1499998569:
                        results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 43
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 44
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.5999999046:
                    results.append(1)
                else:
                    results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 45
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[1] <= 2.9500000477:
                results.append(1)
            else:
                results.append(0)
        else:
            if x[1] <= 2.9500000477:
                if x[3] <= 1.6499999762:
                    if x[2] <= 4.5999999046:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(2)
            else:
                if x[0] <= 5.9500000477:
                    results.append(0)
                else:
                    if x[3] <= 1.7500000000:
                        results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 46
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[2] <= 4.6500000954:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 6.4500000477:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    if x[2] <= 5.1499998569:
                        results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 47
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 48
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 49
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                results.append(1)
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
