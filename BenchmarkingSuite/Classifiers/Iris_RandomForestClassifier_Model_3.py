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
     n_estimators: 200
     n_jobs: None
     oob_score: False
     random_state: None
     verbose: 0
     warm_start: False

"""
def classifier(x, results, deadline, interrupt_flag):
    
    # Tree 0
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.3499999046:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 1
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.6999999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 2
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 4.8500001431:
            if x[3] <= 0.7500000000:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[0] <= 6.0499999523:
                if x[0] <= 5.9000000954:
                    results.append(2)
                else:
                    if x[1] <= 2.4500000477:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 3
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 6.7500000000:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    if x[3] <= 1.6999999881:
                        if x[1] <= 2.7500000000:
                            if x[2] <= 5.3499999046:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
            else:
                if x[3] <= 1.5999999642:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 4
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 4.7500000000:
            if x[0] <= 5.3499999046:
                if x[2] <= 2.5000000000:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[2] <= 2.6000000238:
                    results.append(0)
                else:
                    results.append(1)
        else:
            if x[0] <= 6.0499999523:
                if x[1] <= 3.1000000238:
                    if x[3] <= 1.6999999881:
                        if x[1] <= 2.4500000477:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 5
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.7500000000:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[2] <= 4.8500001431:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        if x[3] <= 1.5999999642:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 5.0000000000:
                    if x[3] <= 1.6499999762:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 6
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 5.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    if x[3] <= 1.6999999881:
                        if x[0] <= 6.0499999523:
                            if x[1] <= 2.4500000477:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 7
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[2] <= 4.7500000000:
                if x[3] <= 0.7000000030:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.6999999881:
                    if x[3] <= 1.5500000119:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 8
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5000000000:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 6.4000000954:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    if x[0] <= 6.0499999523:
                        if x[3] <= 1.7500000000:
                            if x[1] <= 2.4500000477:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 9
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.3500000238:
            results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[1] <= 2.2500000000:
                    results.append(2)
                else:
                    if x[2] <= 4.6500000954:
                        results.append(1)
                    else:
                        if x[3] <= 1.8499999642:
                            if x[1] <= 3.1000000238:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
            else:
                if x[1] <= 2.3500000238:
                    results.append(1)
                else:
                    if x[3] <= 1.6499999762:
                        if x[0] <= 6.4000000954:
                            if x[2] <= 5.0000000000:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 10
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[3] <= 0.7000000030:
                    results.append(0)
                else:
                    if x[2] <= 5.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[0] <= 5.9500000477:
                    if x[3] <= 1.8499999642:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 11
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.8500000238:
                    if x[1] <= 2.7500000000:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            if x[3] <= 1.5500000119:
                                results.append(2)
                            else:
                                results.append(1)
                    else:
                        if x[0] <= 6.5500001907:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 12
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[1] <= 2.8000000715:
                results.append(1)
            else:
                if x[3] <= 1.0500000119:
                    results.append(0)
                else:
                    results.append(1)
        else:
            if x[0] <= 6.0499999523:
                if x[3] <= 0.7000000030:
                    results.append(0)
                else:
                    if x[1] <= 2.3999999762:
                        results.append(2)
                    else:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            if x[1] <= 2.7500000000:
                                results.append(1)
                            else:
                                results.append(2)
            else:
                if x[3] <= 1.7500000000:
                    if x[2] <= 5.2999999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 13
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 14
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 5.0499999523:
                    if x[0] <= 6.5000000000:
                        if x[3] <= 1.6499999762:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 15
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9000000954:
                    results.append(1)
                else:
                    if x[1] <= 2.4500000477:
                        results.append(2)
                    else:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 16
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    if x[2] <= 4.9500000477:
                        results.append(1)
                    else:
                        if x[0] <= 6.3499999046:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(2)
            else:
                if x[2] <= 4.8500001431:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 17
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[2] <= 5.0499999523:
                if x[1] <= 3.5000000000:
                    if x[3] <= 1.7500000000:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            if x[1] <= 2.6000000238:
                                results.append(2)
                            else:
                                results.append(1)
                    else:
                        if x[3] <= 1.8999999762:
                            if x[0] <= 5.9500000477:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(2)
                else:
                    results.append(0)
            else:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 18
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[0] <= 6.1499998569:
                    results.append(1)
                else:
                    if x[1] <= 2.8500000238:
                        if x[2] <= 4.7000000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 5.1499998569:
                    if x[3] <= 1.6999999881:
                        if x[2] <= 5.0499999523:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 19
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.6999999881:
            results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[2] <= 4.9000000954:
                    results.append(1)
                else:
                    if x[0] <= 5.9000000954:
                        results.append(2)
                    else:
                        if x[1] <= 2.4500000477:
                            results.append(2)
                        else:
                            results.append(1)
            else:
                if x[0] <= 7.0999999046:
                    if x[2] <= 4.8500001431:
                        results.append(1)
                    else:
                        if x[3] <= 1.7500000000:
                            if x[3] <= 1.6000000238:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 20
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 21
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[2] <= 4.6500000954:
                    results.append(1)
                else:
                    if x[2] <= 5.0499999523:
                        if x[2] <= 4.9000000954:
                            if x[1] <= 3.1000000238:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                    else:
                        if x[0] <= 5.9000000954:
                            results.append(2)
                        else:
                            results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[0] <= 6.3500001431:
                        if x[2] <= 5.0000000000:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 22
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[1] <= 3.0000000000:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 23
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[0] <= 6.3500001431:
                if x[3] <= 1.6999999881:
                    if x[2] <= 5.0000000000:
                        results.append(1)
                    else:
                        if x[0] <= 6.1500000954:
                            results.append(1)
                        else:
                            results.append(2)
                else:
                    if x[3] <= 1.8499999642:
                        if x[0] <= 5.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
            else:
                if x[2] <= 5.0999999046:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 24
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[3] <= 1.6499999762:
                        results.append(1)
                    else:
                        if x[0] <= 5.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
            else:
                if x[2] <= 5.2000000477:
                    if x[3] <= 1.8000000119:
                        if x[1] <= 2.4500000477:
                            results.append(2)
                        else:
                            if x[3] <= 1.5500000119:
                                results.append(2)
                            else:
                                results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 25
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    if x[3] <= 1.5500000119:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[1] <= 3.0000000000:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 26
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[3] <= 0.7000000030:
                    results.append(0)
                else:
                    if x[1] <= 2.8500000238:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 27
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    if x[2] <= 5.0499999523:
                        if x[1] <= 2.8999999762:
                            if x[0] <= 6.2500000000:
                                results.append(2)
                            else:
                                if x[1] <= 2.6000000238:
                                    results.append(1)
                                else:
                                    results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 28
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.3000000715:
                    if x[2] <= 4.7500000000:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(1)
            else:
                if x[1] <= 3.1499999762:
                    results.append(2)
                else:
                    if x[3] <= 1.8999999762:
                        if x[0] <= 6.5499999523:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 29
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[1] <= 2.5499999523:
                    if x[2] <= 4.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[2] <= 4.8500001431:
                        if x[0] <= 5.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 30
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.7500000000:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                if x[0] <= 5.6499998569:
                    results.append(1)
                else:
                    if x[1] <= 2.6499999762:
                        results.append(2)
                    else:
                        results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    if x[3] <= 1.6000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[0] <= 5.9500000477:
                    if x[0] <= 5.8500001431:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 31
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.7500000000:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[0] <= 5.7500000000:
                if x[2] <= 4.7500000000:
                    if x[1] <= 3.3999999762:
                        results.append(1)
                    else:
                        results.append(0)
                else:
                    results.append(2)
            else:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[2] <= 4.9500000477:
                        if x[1] <= 2.6000000238:
                            results.append(1)
                        else:
                            if x[1] <= 3.1000000238:
                                results.append(2)
                            else:
                                results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 32
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.2500000000:
                    results.append(2)
                else:
                    results.append(1)
            else:
                if x[0] <= 5.9500000477:
                    if x[2] <= 4.9000000954:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 33
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 5.9500000477:
                if x[0] <= 5.6499998569:
                    results.append(1)
                else:
                    if x[3] <= 1.8499999642:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[3] <= 1.7500000000:
                    if x[0] <= 6.4000000954:
                        if x[1] <= 2.8500000238:
                            if x[2] <= 4.9500000477:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 34
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[3] <= 1.5999999642:
                        results.append(1)
                    else:
                        if x[1] <= 3.1000000238:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    if x[2] <= 5.1499998569:
                        if x[0] <= 5.9000000954:
                            results.append(2)
                        else:
                            if x[3] <= 1.6999999881:
                                if x[2] <= 5.0499999523:
                                    results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 35
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[0] <= 6.5000000000:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 36
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[3] <= 0.6500000060:
                    results.append(0)
                else:
                    if x[1] <= 2.8500000238:
                        if x[0] <= 6.0499999523:
                            results.append(1)
                        else:
                            if x[1] <= 2.5499999523:
                                results.append(1)
                            else:
                                if x[2] <= 4.8499999046:
                                    results.append(1)
                                else:
                                    results.append(2)
                    else:
                        results.append(1)
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
                if x[2] <= 5.0499999523:
                    if x[3] <= 1.7500000000:
                        if x[0] <= 6.1500000954:
                            results.append(2)
                        else:
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
            if x[1] <= 2.6000000238:
                results.append(1)
            else:
                results.append(0)
        else:
            if x[0] <= 6.2500000000:
                if x[0] <= 5.6499998569:
                    results.append(1)
                else:
                    if x[3] <= 1.6999999881:
                        if x[2] <= 2.8500000238:
                            results.append(0)
                        else:
                            if x[1] <= 2.6499999762:
                                if x[1] <= 2.3999999762:
                                    if x[2] <= 4.7500000000:
                                        results.append(1)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(1)
                    else:
                        if x[2] <= 4.8500001431:
                            if x[0] <= 5.9500000477:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(2)
            else:
                if x[3] <= 1.7500000000:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 39
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    if x[1] <= 3.0000000000:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 40
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 1.7500000000:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                if x[2] <= 5.0499999523:
                    if x[3] <= 1.4499999881:
                        results.append(1)
                    else:
                        if x[0] <= 6.0999999046:
                            if x[1] <= 2.5500000715:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
                else:
                    results.append(2)
        else:
            if x[2] <= 4.8500001431:
                if x[0] <= 6.0499999523:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 41
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[0] <= 6.0499999523:
                    if x[3] <= 1.8499999642:
                        if x[1] <= 2.4500000477:
                            results.append(2)
                        else:
                            if x[3] <= 1.6999999881:
                                results.append(1)
                            else:
                                if x[0] <= 5.9500000477:
                                    results.append(1)
                                else:
                                    results.append(2)
                    else:
                        results.append(2)
                else:
                    if x[3] <= 1.7500000000:
                        if x[1] <= 2.8999999762:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 42
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[0] <= 5.9500000477:
                    if x[0] <= 5.8500001431:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 43
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5000000000:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    if x[1] <= 2.4500000477:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 44
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.3500000238:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    if x[1] <= 3.0000000000:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 5.0499999523:
                    if x[3] <= 1.7500000000:
                        if x[1] <= 2.3500000238:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[0] <= 6.0999999046:
                        if x[0] <= 5.9000000954:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 45
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.7000000030:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.6999999881:
                if x[3] <= 0.7000000030:
                    results.append(0)
                else:
                    if x[1] <= 2.8500000238:
                        if x[3] <= 1.3499999642:
                            results.append(1)
                        else:
                            if x[2] <= 4.9500000477:
                                results.append(1)
                            else:
                                if x[0] <= 6.0499999523:
                                    if x[1] <= 2.4500000477:
                                        results.append(2)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(2)
                    else:
                        results.append(1)
            else:
                if x[0] <= 6.0499999523:
                    if x[1] <= 3.0000000000:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 46
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                results.append(1)
            else:
                if x[0] <= 6.7500000000:
                    if x[3] <= 1.7500000000:
                        if x[3] <= 1.5500000119:
                            if x[2] <= 5.0000000000:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 47
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.3000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.2500000000:
                    if x[2] <= 4.7500000000:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[3] <= 1.4499999881:
                        results.append(1)
                    else:
                        if x[2] <= 5.0499999523:
                            results.append(1)
                        else:
                            if x[0] <= 6.1500000954:
                                results.append(1)
                            else:
                                results.append(2)
            else:
                if x[3] <= 1.8499999642:
                    if x[0] <= 6.0000000000:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 48
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[3] <= 1.6499999762:
                    results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[0] <= 6.0499999523:
                    if x[2] <= 5.0499999523:
                        results.append(2)
                    else:
                        if x[0] <= 5.9000000954:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    if x[2] <= 5.0499999523:
                        if x[0] <= 6.5000000000:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 49
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[0] <= 5.9500000477:
                    results.append(1)
                else:
                    if x[3] <= 1.6999999881:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 50
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    if x[3] <= 1.4499999881:
                        results.append(1)
                    else:
                        if x[2] <= 4.8499999046:
                            results.append(1)
                        else:
                            if x[0] <= 6.3499999046:
                                results.append(2)
                            else:
                                results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 51
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[0] <= 6.1499998569:
                if x[3] <= 1.6999999881:
                    if x[2] <= 4.8499999046:
                        results.append(1)
                    else:
                        if x[2] <= 5.0499999523:
                            results.append(2)
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
    
    # Tree 52
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 53
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[0] <= 5.9500000477:
                    if x[2] <= 4.9000000954:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 54
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[1] <= 2.4500000477:
                        results.append(2)
                    else:
                        if x[3] <= 1.5500000119:
                            if x[2] <= 4.9500000477:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 55
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 5.0499999523:
                    if x[3] <= 1.7500000000:
                        if x[0] <= 6.1500000954:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        if x[1] <= 3.1000000238:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 56
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[3] <= 1.6499999762:
                    results.append(1)
                else:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[0] <= 6.0499999523:
                    if x[0] <= 5.9000000954:
                        results.append(2)
                    else:
                        if x[1] <= 2.4500000477:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 57
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    if x[2] <= 5.3499999046:
                        if x[1] <= 2.7500000000:
                            if x[3] <= 1.5500000119:
                                if x[1] <= 2.3500000238:
                                    results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[2] <= 4.8500001431:
                                if x[1] <= 3.0000000000:
                                    results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 58
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 1.6999999881:
            if x[1] <= 2.9500000477:
                if x[0] <= 6.0499999523:
                    results.append(1)
                else:
                    if x[2] <= 4.8999998569:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[3] <= 0.8000000268:
                    results.append(0)
                else:
                    results.append(1)
        else:
            if x[0] <= 5.9500000477:
                if x[3] <= 2.1000000238:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 59
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[3] <= 1.5500000119:
                        if x[1] <= 2.6499999762:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    if x[2] <= 4.8500001431:
                        if x[1] <= 3.1000000238:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 60
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[0] <= 5.9500000477:
                    results.append(1)
                else:
                    if x[2] <= 4.7500000000:
                        results.append(1)
                    else:
                        if x[3] <= 1.6499999762:
                            results.append(1)
                        else:
                            results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 61
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[0] <= 5.7500000000:
                if x[2] <= 2.6000000238:
                    results.append(0)
                else:
                    if x[3] <= 1.7500000000:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[3] <= 1.7500000000:
                    if x[1] <= 2.6999999285:
                        if x[0] <= 6.2000000477:
                            if x[2] <= 4.5000000000:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
                    else:
                        if x[2] <= 5.0499999523:
                            results.append(1)
                        else:
                            results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 62
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[1] <= 2.2500000000:
                    if x[0] <= 6.0999999046:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    if x[2] <= 5.3499999046:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 63
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.3500000238:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 64
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 3.8500000238:
                    if x[0] <= 6.2500000000:
                        results.append(1)
                    else:
                        if x[2] <= 5.0499999523:
                            results.append(1)
                        else:
                            results.append(2)
                else:
                    results.append(0)
            else:
                if x[2] <= 4.8500001431:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 65
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[3] <= 1.5500000119:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 66
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[0] <= 6.2500000000:
                if x[3] <= 0.7000000030:
                    results.append(0)
                else:
                    if x[0] <= 5.7500000000:
                        results.append(1)
                    else:
                        if x[0] <= 6.1499998569:
                            if x[2] <= 4.7500000000:
                                results.append(1)
                            else:
                                if x[2] <= 5.0499999523:
                                    results.append(2)
                                else:
                                    if x[0] <= 5.9000000954:
                                        results.append(2)
                                    else:
                                        if x[2] <= 5.3499999046:
                                            results.append(1)
                                        else:
                                            results.append(2)
                        else:
                            results.append(1)
            else:
                if x[3] <= 1.6499999762:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 67
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[3] <= 1.5999999642:
                        results.append(1)
                    else:
                        if x[0] <= 6.0499999523:
                            results.append(1)
                        else:
                            results.append(2)
            else:
                if x[3] <= 1.7500000000:
                    if x[0] <= 6.2000000477:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        if x[1] <= 2.6499999762:
                            results.append(1)
                        else:
                            if x[3] <= 1.6000000238:
                                results.append(2)
                            else:
                                results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 68
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[1] <= 2.2500000000:
                    if x[1] <= 2.1000000238:
                        results.append(1)
                    else:
                        if x[0] <= 6.0999999046:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    if x[2] <= 5.3499999046:
                        if x[0] <= 6.2000000477:
                            results.append(1)
                        else:
                            if x[1] <= 2.9499999285:
                                if x[0] <= 6.5500001907:
                                    results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                    else:
                        results.append(2)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 6.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 69
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.9000000358:
            results.append(0)
        else:
            if x[2] <= 5.0499999523:
                if x[3] <= 1.7500000000:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 70
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 71
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[0] <= 5.7500000000:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[0] <= 6.7500000000:
                    if x[2] <= 4.7500000000:
                        results.append(1)
                    else:
                        if x[2] <= 5.1499998569:
                            if x[3] <= 1.7500000000:
                                results.append(1)
                            else:
                                if x[1] <= 3.1000000238:
                                    results.append(2)
                                else:
                                    results.append(1)
                        else:
                            results.append(2)
                else:
                    if x[3] <= 1.5999999642:
                        results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 72
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[3] <= 1.3499999642:
                    results.append(1)
                else:
                    if x[2] <= 4.9500000477:
                        results.append(1)
                    else:
                        if x[0] <= 6.3999998569:
                            if x[1] <= 2.6499999762:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 73
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[3] <= 1.6499999762:
                    results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 5.1499998569:
                    if x[1] <= 2.6000000238:
                        results.append(2)
                    else:
                        if x[0] <= 5.9000000954:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 74
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5000000000:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[0] <= 6.0499999523:
                    if x[1] <= 3.1000000238:
                        if x[2] <= 5.0499999523:
                            results.append(2)
                        else:
                            if x[0] <= 5.9000000954:
                                results.append(2)
                            else:
                                results.append(1)
                    else:
                        results.append(1)
                else:
                    if x[1] <= 2.5499999523:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 75
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9000000954:
                    results.append(1)
                else:
                    if x[0] <= 6.3499999046:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 76
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 1.7500000000:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                if x[0] <= 6.2500000000:
                    results.append(1)
                else:
                    if x[2] <= 5.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
        else:
            if x[2] <= 4.8500001431:
                if x[0] <= 6.0499999523:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 77
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[0] <= 6.2500000000:
                if x[1] <= 2.6499999762:
                    if x[2] <= 4.7500000000:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[3] <= 1.6999999881:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[0] <= 6.4500000477:
                    if x[0] <= 6.3500001431:
                        if x[3] <= 1.6499999762:
                            if x[2] <= 5.0000000000:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(2)
                    else:
                        if x[1] <= 2.9500000477:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    if x[3] <= 1.5999999642:
                        results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 78
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[1] <= 2.8999999762:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 79
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                results.append(1)
            else:
                if x[0] <= 6.1500000954:
                    if x[2] <= 5.0499999523:
                        results.append(2)
                    else:
                        if x[0] <= 5.9000000954:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 80
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 5.6499998569:
                results.append(1)
            else:
                if x[3] <= 1.6999999881:
                    if x[2] <= 4.9500000477:
                        results.append(1)
                    else:
                        if x[0] <= 6.0499999523:
                            if x[3] <= 1.5500000119:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 81
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 5.6499998569:
                results.append(1)
            else:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[3] <= 1.7500000000:
                        if x[3] <= 1.6000000238:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 82
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.6999999881:
                if x[3] <= 0.6500000060:
                    results.append(0)
                else:
                    if x[0] <= 6.2500000000:
                        results.append(1)
                    else:
                        if x[2] <= 4.8999998569:
                            results.append(1)
                        else:
                            results.append(2)
            else:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 83
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    if x[0] <= 6.5000000000:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 84
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[1] <= 2.3500000238:
                        results.append(2)
                    else:
                        if x[2] <= 5.0499999523:
                            results.append(1)
                        else:
                            if x[0] <= 6.0499999523:
                                results.append(1)
                            else:
                                results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 85
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 3.6000000238:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[0] <= 5.9500000477:
                    if x[0] <= 5.8500001431:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 86
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.3500000238:
            results.append(0)
        else:
            if x[0] <= 6.2500000000:
                if x[0] <= 5.6499998569:
                    results.append(1)
                else:
                    if x[2] <= 4.7500000000:
                        results.append(1)
                    else:
                        if x[1] <= 2.6499999762:
                            results.append(2)
                        else:
                            if x[3] <= 1.6999999881:
                                results.append(1)
                            else:
                                if x[3] <= 1.8499999642:
                                    if x[0] <= 5.9500000477:
                                        results.append(1)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(2)
            else:
                if x[2] <= 5.0499999523:
                    if x[1] <= 2.6499999762:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 87
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[0] <= 6.2500000000:
                    results.append(1)
                else:
                    if x[2] <= 5.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[0] <= 6.0499999523:
                    if x[3] <= 1.8999999762:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 88
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.6999999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 6.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 89
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.6499999762:
                    if x[2] <= 4.7999999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(1)
            else:
                if x[0] <= 5.9500000477:
                    if x[2] <= 4.9000000954:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 90
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 1.7500000000:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                if x[3] <= 1.4499999881:
                    results.append(1)
                else:
                    if x[1] <= 2.3500000238:
                        if x[2] <= 4.7500000000:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
        else:
            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 91
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    if x[3] <= 1.5500000119:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 92
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9000000954:
                    results.append(1)
                else:
                    if x[1] <= 2.6499999762:
                        results.append(2)
                    else:
                        if x[0] <= 6.5000000000:
                            if x[1] <= 2.7500000000:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 93
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 5.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 94
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    if x[0] <= 6.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 95
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[2] <= 4.9000000954:
                    results.append(1)
                else:
                    if x[0] <= 5.9000000954:
                        results.append(2)
                    else:
                        if x[2] <= 5.0499999523:
                            results.append(2)
                        else:
                            results.append(1)
            else:
                if x[0] <= 7.0999999046:
                    if x[2] <= 4.8500001431:
                        results.append(1)
                    else:
                        if x[2] <= 5.0499999523:
                            if x[3] <= 1.7500000000:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 96
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 5.0499999523:
                if x[3] <= 1.7500000000:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[0] <= 6.0499999523:
                    if x[0] <= 5.9000000954:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 97
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.9500000477:
            if x[1] <= 3.0499999523:
                if x[2] <= 2.1999999881:
                    results.append(0)
                else:
                    if x[2] <= 4.7999999523:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[2] <= 3.3500000834:
                    results.append(0)
                else:
                    results.append(1)
        else:
            if x[1] <= 2.9500000477:
                if x[1] <= 2.7500000000:
                    if x[3] <= 1.6499999762:
                        if x[0] <= 6.2000000477:
                            results.append(2)
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
                if x[2] <= 4.6500000954:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 98
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.2999999523:
            if x[1] <= 2.8500000238:
                results.append(1)
            else:
                results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 2.6000000238:
                    results.append(0)
                else:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            if x[3] <= 1.6000000238:
                                results.append(2)
                            else:
                                results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 99
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[1] <= 2.2500000000:
                    results.append(2)
                else:
                    if x[2] <= 4.9500000477:
                        results.append(1)
                    else:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            results.append(1)
            else:
                if x[1] <= 3.1499999762:
                    results.append(2)
                else:
                    if x[3] <= 2.0000000000:
                        results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 100
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[0] <= 6.1499998569:
                    results.append(1)
                else:
                    if x[3] <= 1.6499999762:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[1] <= 2.5499999523:
                    if x[3] <= 1.6499999762:
                        if x[1] <= 2.3500000238:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[3] <= 1.7500000000:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 101
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[0] <= 6.5000000000:
                        if x[1] <= 3.1000000238:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(1)
            else:
                if x[1] <= 2.6000000238:
                    if x[2] <= 4.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[2] <= 5.0499999523:
                        if x[3] <= 1.7500000000:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 102
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 103
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.9500000477:
                    if x[3] <= 1.6499999762:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 104
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[1] <= 2.8999999762:
                    if x[0] <= 6.7500000000:
                        if x[2] <= 5.2000000477:
                            if x[0] <= 5.8499999046:
                                results.append(2)
                            else:
                                if x[0] <= 6.1500000954:
                                    results.append(1)
                                else:
                                    if x[1] <= 2.6000000238:
                                        results.append(1)
                                    else:
                                        results.append(2)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 105
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 5.0499999523:
                if x[3] <= 1.7500000000:
                    results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[3] <= 1.6999999881:
                    if x[3] <= 1.5500000119:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 106
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    if x[3] <= 1.5500000119:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 6.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 107
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 3.4500000477:
                    results.append(1)
                else:
                    results.append(0)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 108
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.6999999881:
                if x[3] <= 0.7000000030:
                    results.append(0)
                else:
                    if x[2] <= 4.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[2] <= 4.8500001431:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 109
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                results.append(1)
            else:
                if x[0] <= 6.0499999523:
                    if x[0] <= 5.9000000954:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 110
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 6.3500001431:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[2] <= 4.9500000477:
                        if x[0] <= 6.0000000000:
                            results.append(1)
                        else:
                            if x[1] <= 2.6000000238:
                                results.append(1)
                            else:
                                results.append(2)
                    else:
                        if x[2] <= 5.0499999523:
                            results.append(2)
                        else:
                            if x[0] <= 5.9000000954:
                                results.append(2)
                            else:
                                if x[0] <= 6.0499999523:
                                    results.append(1)
                                else:
                                    results.append(2)
            else:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 111
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[1] <= 2.6499999762:
                    if x[1] <= 2.5499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 112
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5000000000:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 113
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.6999999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                results.append(1)
            else:
                if x[0] <= 5.9500000477:
                    if x[2] <= 4.9000000954:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 114
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    if x[3] <= 1.4499999881:
                        results.append(1)
                    else:
                        if x[1] <= 2.3500000238:
                            if x[2] <= 4.7500000000:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 115
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.9500000477:
                    if x[3] <= 1.6499999762:
                        results.append(1)
                    else:
                        if x[1] <= 3.1000000238:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    if x[3] <= 1.6999999881:
                        results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 116
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 5.7500000000:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[1] <= 3.0499999523:
                        if x[0] <= 6.5999999046:
                            results.append(2)
                        else:
                            if x[2] <= 5.0999999046:
                                results.append(1)
                            else:
                                results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 117
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[2] <= 4.8500001431:
                if x[1] <= 3.6000000238:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[2] <= 4.9500000477:
                    if x[3] <= 1.6499999762:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[1] <= 2.7500000000:
                        if x[3] <= 1.6999999881:
                            if x[1] <= 2.4500000477:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 118
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[1] <= 3.0000000000:
                        if x[0] <= 6.2500000000:
                            results.append(2)
                        else:
                            if x[3] <= 1.6499999762:
                                results.append(1)
                            else:
                                results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 5.0499999523:
                    if x[0] <= 6.5000000000:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 119
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[2] <= 4.9000000954:
                    if x[0] <= 6.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 120
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    if x[3] <= 1.5500000119:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 121
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.6499999762:
                    results.append(1)
                else:
                    if x[3] <= 1.8499999642:
                        if x[0] <= 5.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 122
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 6.0499999523:
                if x[2] <= 4.9000000954:
                    if x[2] <= 4.6500000954:
                        results.append(1)
                    else:
                        if x[1] <= 3.1000000238:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    if x[0] <= 5.9000000954:
                        results.append(2)
                    else:
                        if x[2] <= 5.0499999523:
                            results.append(2)
                        else:
                            results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[2] <= 5.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 123
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    if x[1] <= 2.4500000477:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 124
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[2] <= 4.9500000477:
                        results.append(1)
                    else:
                        if x[0] <= 6.5000000000:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    if x[0] <= 5.9500000477:
                        if x[0] <= 5.8500001431:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 125
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.9000000954:
                    if x[3] <= 1.5999999642:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[2] <= 5.1499998569:
                        if x[3] <= 1.7500000000:
                            if x[1] <= 2.4500000477:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 126
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 6.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 127
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[3] <= 1.4499999881:
                        results.append(2)
                    else:
                        if x[1] <= 2.3500000238:
                            results.append(2)
                        else:
                            if x[2] <= 5.0499999523:
                                results.append(1)
                            else:
                                if x[3] <= 1.5500000119:
                                    results.append(2)
                                else:
                                    results.append(1)
                else:
                    if x[0] <= 5.9500000477:
                        if x[0] <= 5.8500001431:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 128
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[1] <= 2.6499999762:
                    if x[2] <= 5.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(1)
            else:
                if x[0] <= 6.0000000000:
                    if x[3] <= 1.8499999642:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 129
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.3500000238:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[1] <= 2.8999999762:
                        if x[0] <= 6.1500000954:
                            if x[1] <= 2.4500000477:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    if x[3] <= 1.8499999642:
                        if x[2] <= 4.8500001431:
                            if x[1] <= 3.1000000238:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 130
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[0] <= 5.9500000477:
                    results.append(1)
                else:
                    if x[1] <= 2.6499999762:
                        if x[0] <= 6.2000000477:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        if x[0] <= 6.3500001431:
                            if x[2] <= 4.8999998569:
                                results.append(1)
                            else:
                                if x[0] <= 6.1500000954:
                                    results.append(1)
                                else:
                                    results.append(2)
                        else:
                            results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 131
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.3499999046:
                    if x[1] <= 2.3000000715:
                        if x[2] <= 4.5000000000:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        if x[0] <= 6.2500000000:
                            results.append(1)
                        else:
                            if x[2] <= 5.0499999523:
                                results.append(1)
                            else:
                                results.append(2)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 132
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[1] <= 2.2500000000:
                    results.append(2)
                else:
                    results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 133
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.2999999523:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 134
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.3499999046:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[0] <= 5.9500000477:
                    if x[3] <= 1.8499999642:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 135
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 2.5999999642:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[0] <= 5.9500000477:
                if x[2] <= 2.6499999762:
                    results.append(0)
                else:
                    if x[3] <= 1.6999999881:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[3] <= 1.6499999762:
                        if x[0] <= 6.2000000477:
                            results.append(2)
                        else:
                            if x[2] <= 5.0000000000:
                                results.append(1)
                            else:
                                results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 136
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.2500000000:
                    if x[1] <= 2.1000000238:
                        results.append(1)
                    else:
                        if x[0] <= 6.0999999046:
                            if x[2] <= 4.5000000000:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 137
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[2] <= 4.7500000000:
                if x[1] <= 3.4500000477:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[2] <= 5.0499999523:
                    if x[1] <= 3.1000000238:
                        if x[3] <= 1.7500000000:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 138
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[2] <= 2.6999999881:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[2] <= 4.8500001431:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        if x[3] <= 1.5999999642:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
            else:
                if x[0] <= 6.1500000954:
                    if x[2] <= 5.0499999523:
                        results.append(2)
                    else:
                        if x[0] <= 5.9000000954:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 139
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 6.1499998569:
                if x[2] <= 4.8499999046:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[3] <= 1.7500000000:
                        results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 140
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[0] <= 6.2500000000:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    if x[3] <= 1.6999999881:
                        if x[1] <= 2.6499999762:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
            else:
                if x[0] <= 6.8500001431:
                    if x[2] <= 5.0999999046:
                        if x[0] <= 6.4000000954:
                            if x[2] <= 4.9500000477:
                                if x[1] <= 2.6000000238:
                                    results.append(1)
                                else:
                                    results.append(2)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 141
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 4.9500000477:
            if x[0] <= 5.4500000477:
                if x[3] <= 0.7000000030:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[2] <= 2.7000000477:
                    results.append(0)
                else:
                    if x[3] <= 1.6999999881:
                        results.append(1)
                    else:
                        if x[1] <= 3.1000000238:
                            results.append(2)
                        else:
                            results.append(1)
        else:
            if x[0] <= 6.5999999046:
                results.append(2)
            else:
                if x[2] <= 5.0999999046:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 142
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    if x[0] <= 6.5000000000:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 143
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.7500000000:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[3] <= 1.4499999881:
                    results.append(1)
                else:
                    if x[1] <= 2.8999999762:
                        if x[1] <= 2.7500000000:
                            if x[0] <= 6.0999999046:
                                if x[3] <= 1.5500000119:
                                    results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[2] <= 4.8499999046:
                                results.append(1)
                            else:
                                results.append(2)
                    else:
                        results.append(1)
            else:
                if x[0] <= 5.9500000477:
                    if x[0] <= 5.8500001431:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 144
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.3499999046:
                    if x[2] <= 5.0499999523:
                        results.append(1)
                    else:
                        if x[0] <= 6.1500000954:
                            results.append(1)
                        else:
                            results.append(2)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 145
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 1.6999999881:
            if x[0] <= 5.4500000477:
                if x[3] <= 0.7500000000:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[3] <= 0.7000000030:
                    results.append(0)
                else:
                    if x[1] <= 2.8500000238:
                        if x[0] <= 5.9000000954:
                            results.append(1)
                        else:
                            if x[0] <= 6.5500001907:
                                if x[2] <= 4.9500000477:
                                    results.append(1)
                                else:
                                    if x[3] <= 1.5500000119:
                                        results.append(2)
                                    else:
                                        results.append(1)
                            else:
                                results.append(1)
                    else:
                        results.append(1)
        else:
            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 146
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    if x[1] <= 2.6000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 147
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.3500000238:
            results.append(0)
        else:
            if x[0] <= 6.3500001431:
                if x[0] <= 5.5999999046:
                    results.append(1)
                else:
                    if x[1] <= 2.7500000000:
                        if x[3] <= 1.6999999881:
                            if x[2] <= 5.3499999046:
                                if x[1] <= 2.3500000238:
                                    if x[2] <= 4.7500000000:
                                        results.append(1)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(2)
                    else:
                        if x[2] <= 4.7500000000:
                            results.append(1)
                        else:
                            if x[3] <= 2.0499999523:
                                if x[1] <= 3.1000000238:
                                    results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
            else:
                if x[0] <= 7.0999999046:
                    if x[3] <= 1.6499999762:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 148
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[0] <= 6.2500000000:
                if x[2] <= 4.6500000954:
                    results.append(1)
                else:
                    if x[0] <= 5.9000000954:
                        results.append(2)
                    else:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            if x[1] <= 2.8500000238:
                                results.append(1)
                            else:
                                results.append(2)
            else:
                if x[3] <= 1.7500000000:
                    if x[1] <= 2.8999999762:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 149
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[2] <= 5.0499999523:
                        if x[1] <= 2.3500000238:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[1] <= 3.1499999762:
                        results.append(2)
                    else:
                        if x[3] <= 2.0000000000:
                            results.append(1)
                        else:
                            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 150
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[0] <= 6.5000000000:
                        if x[3] <= 1.5500000119:
                            if x[2] <= 4.9500000477:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 151
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.6999999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.6999999881:
                    if x[3] <= 1.5500000119:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 152
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.6999999881:
                    if x[3] <= 1.4499999881:
                        results.append(2)
                    else:
                        if x[1] <= 2.7500000000:
                            results.append(1)
                        else:
                            results.append(2)
                else:
                    if x[0] <= 5.9500000477:
                        if x[0] <= 5.8500001431:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 153
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 6.1499998569:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[3] <= 1.6999999881:
                    if x[2] <= 5.0000000000:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 154
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.8499999642:
                if x[2] <= 4.8500001431:
                    if x[0] <= 6.1499998569:
                        results.append(1)
                    else:
                        if x[2] <= 4.7500000000:
                            results.append(1)
                        else:
                            if x[3] <= 1.5999999642:
                                results.append(1)
                            else:
                                results.append(2)
                else:
                    if x[0] <= 6.5000000000:
                        results.append(2)
                    else:
                        if x[3] <= 1.7500000000:
                            results.append(1)
                        else:
                            results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 155
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 5.0499999523:
                    if x[3] <= 1.7500000000:
                        results.append(1)
                    else:
                        if x[0] <= 5.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                else:
                    if x[0] <= 6.0499999523:
                        if x[3] <= 1.7500000000:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 156
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[3] <= 1.6499999762:
                        results.append(1)
                    else:
                        if x[1] <= 3.0000000000:
                            results.append(2)
                        else:
                            results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[3] <= 1.5500000119:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 157
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[1] <= 2.7999999523:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 158
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[0] <= 6.2500000000:
                    results.append(1)
                else:
                    if x[0] <= 6.3500001431:
                        if x[1] <= 2.6499999762:
                            results.append(1)
                        else:
                            if x[3] <= 1.5500000119:
                                results.append(2)
                            else:
                                results.append(1)
                    else:
                        results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 159
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[0] <= 5.6499998569:
                results.append(1)
            else:
                if x[2] <= 4.9500000477:
                    if x[3] <= 1.6499999762:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[1] <= 2.7500000000:
                        if x[1] <= 2.6499999762:
                            results.append(2)
                        else:
                            if x[2] <= 5.2000000477:
                                if x[0] <= 5.9000000954:
                                    results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 160
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 6.2500000000:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[3] <= 1.7500000000:
                    if x[1] <= 2.8999999762:
                        if x[2] <= 5.0000000000:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 161
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 5.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[2] <= 5.0499999523:
                        if x[3] <= 1.7500000000:
                            if x[0] <= 6.3499999046:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 162
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 2.3500000238:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[2] <= 4.7500000000:
                if x[1] <= 3.5000000000:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[3] <= 1.6999999881:
                    if x[3] <= 1.5500000119:
                        if x[1] <= 2.6499999762:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 163
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[3] <= 1.4499999881:
                        results.append(2)
                    else:
                        if x[3] <= 1.6000000238:
                            if x[2] <= 5.0000000000:
                                results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 164
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[2] <= 4.9000000954:
                    results.append(1)
                else:
                    if x[2] <= 5.0499999523:
                        results.append(2)
                    else:
                        if x[1] <= 2.7500000000:
                            results.append(1)
                        else:
                            results.append(2)
            else:
                if x[0] <= 6.0000000000:
                    if x[0] <= 5.8500001431:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 165
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[2] <= 4.9500000477:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 166
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[3] <= 1.5500000119:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 167
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 5.1499998569:
                    if x[0] <= 6.5999999046:
                        if x[3] <= 1.6999999881:
                            if x[3] <= 1.5500000119:
                                if x[2] <= 4.9500000477:
                                    results.append(1)
                                else:
                                    results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                    else:
                        if x[3] <= 2.0000000000:
                            results.append(1)
                        else:
                            results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 168
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.3499999046:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 169
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[0] <= 6.0499999523:
                    results.append(1)
                else:
                    if x[2] <= 5.2999999523:
                        results.append(1)
                    else:
                        results.append(2)
            else:
                if x[3] <= 1.8499999642:
                    if x[1] <= 3.1499999762:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 170
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[2] <= 4.8999998569:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 171
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7500000000:
            results.append(0)
        else:
            if x[0] <= 5.9500000477:
                if x[3] <= 1.8499999642:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[3] <= 1.6999999881:
                    if x[2] <= 4.9000000954:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 172
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[3] <= 1.3499999642:
                    results.append(1)
                else:
                    if x[2] <= 5.3499999046:
                        if x[2] <= 4.9000000954:
                            results.append(1)
                        else:
                            if x[3] <= 1.5500000119:
                                results.append(2)
                            else:
                                results.append(1)
                    else:
                        results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 173
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[0] <= 6.0499999523:
                    if x[1] <= 3.1000000238:
                        if x[3] <= 1.6999999881:
                            if x[2] <= 5.0499999523:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    if x[3] <= 1.7500000000:
                        if x[2] <= 5.2999999523:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 174
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[1] <= 2.3500000238:
                        results.append(2)
                    else:
                        if x[1] <= 2.7500000000:
                            results.append(1)
                        else:
                            if x[0] <= 6.5000000000:
                                results.append(2)
                            else:
                                results.append(1)
                else:
                    if x[2] <= 4.8500001431:
                        if x[0] <= 5.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 175
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.3499999046:
                    if x[1] <= 2.3000000715:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 176
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 177
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[1] <= 2.8000000715:
                results.append(1)
            else:
                results.append(0)
        else:
            if x[0] <= 6.1499998569:
                if x[2] <= 4.8499999046:
                    if x[2] <= 2.6000000238:
                        results.append(0)
                    else:
                        results.append(1)
                else:
                    results.append(2)
            else:
                if x[3] <= 1.7500000000:
                    if x[2] <= 5.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 178
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[0] <= 6.1499998569:
                if x[3] <= 1.6999999881:
                    if x[1] <= 2.2500000000:
                        if x[0] <= 5.5000000000:
                            results.append(1)
                        else:
                            if x[2] <= 4.5000000000:
                                results.append(1)
                            else:
                                results.append(2)
                    else:
                        results.append(1)
                else:
                    if x[0] <= 5.9500000477:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
            else:
                if x[0] <= 6.8500001431:
                    if x[3] <= 1.7500000000:
                        if x[0] <= 6.4500000477:
                            if x[0] <= 6.2500000000:
                                results.append(1)
                            else:
                                if x[2] <= 5.0000000000:
                                    results.append(1)
                                else:
                                    results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 179
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 1.7500000000:
            if x[3] <= 0.7500000000:
                results.append(0)
            else:
                results.append(1)
        else:
            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 180
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.7500000000:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[0] <= 6.0499999523:
                if x[3] <= 1.6999999881:
                    if x[2] <= 2.6000000238:
                        results.append(0)
                    else:
                        if x[0] <= 5.9500000477:
                            results.append(1)
                        else:
                            if x[2] <= 4.7500000000:
                                results.append(1)
                            else:
                                results.append(2)
                else:
                    results.append(2)
            else:
                if x[1] <= 2.5499999523:
                    if x[2] <= 5.3500001431:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[3] <= 1.6999999881:
                        if x[1] <= 2.9499999285:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 181
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.2500000000:
                    if x[2] <= 4.7500000000:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[2] <= 5.0499999523:
                        results.append(1)
                    else:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            results.append(1)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 182
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[0] <= 6.0499999523:
                if x[2] <= 2.6499999762:
                    results.append(0)
                else:
                    if x[2] <= 4.9000000954:
                        results.append(1)
                    else:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            if x[1] <= 2.7500000000:
                                results.append(1)
                            else:
                                results.append(2)
            else:
                if x[2] <= 4.8500001431:
                    results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 183
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[2] <= 5.0499999523:
                        results.append(1)
                    else:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            results.append(1)
                else:
                    if x[0] <= 5.9500000477:
                        if x[0] <= 5.8500001431:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 184
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.2500000000:
                    if x[0] <= 6.0999999046:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    if x[0] <= 6.2000000477:
                        results.append(1)
                    else:
                        if x[2] <= 5.0499999523:
                            results.append(1)
                        else:
                            results.append(2)
            else:
                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 185
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[2] <= 5.0499999523:
                    results.append(1)
                else:
                    if x[3] <= 1.5500000119:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[3] <= 1.8499999642:
                    if x[1] <= 3.1499999762:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 186
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[0] <= 6.1499998569:
                if x[3] <= 1.6999999881:
                    if x[1] <= 2.2500000000:
                        results.append(2)
                    else:
                        if x[0] <= 6.0499999523:
                            results.append(1)
                        else:
                            if x[1] <= 2.6999999285:
                                results.append(2)
                            else:
                                results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[2] <= 5.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 187
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.2500000000:
                    if x[0] <= 6.0999999046:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 188
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5000000000:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                if x[3] <= 1.6999999881:
                    results.append(1)
                else:
                    if x[1] <= 3.1000000238:
                        results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 5.0499999523:
                    if x[3] <= 1.7500000000:
                        if x[1] <= 2.3500000238:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 189
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[3] <= 1.7500000000:
                if x[3] <= 1.3499999642:
                    results.append(1)
                else:
                    if x[1] <= 2.8999999762:
                        if x[1] <= 2.3999999762:
                            results.append(1)
                        else:
                            if x[2] <= 4.9500000477:
                                results.append(1)
                            else:
                                if x[1] <= 2.7500000000:
                                    if x[2] <= 5.3499999046:
                                        results.append(1)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(2)
                    else:
                        results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 190
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.4500000477:
            if x[2] <= 2.4499999881:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[2] <= 4.7500000000:
                if x[2] <= 2.6000000238:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[2] <= 5.1499998569:
                    if x[0] <= 5.8500001431:
                        results.append(2)
                    else:
                        if x[1] <= 2.8999999762:
                            if x[1] <= 2.3500000238:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            if x[0] <= 5.9500000477:
                                results.append(1)
                            else:
                                results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 191
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.9500000477:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[3] <= 1.6499999762:
                        results.append(1)
                    else:
                        if x[1] <= 3.0000000000:
                            results.append(2)
                        else:
                            results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[0] <= 6.5000000000:
                        if x[3] <= 1.5500000119:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 192
    if time.time() < deadline or interrupt_flag.is_set():
        if x[0] <= 5.5499999523:
            if x[3] <= 0.8000000119:
                results.append(0)
            else:
                results.append(1)
        else:
            if x[3] <= 1.7500000000:
                if x[1] <= 2.8500000238:
                    if x[3] <= 1.4499999881:
                        results.append(1)
                    else:
                        if x[0] <= 6.4000000954:
                            if x[2] <= 4.9500000477:
                                results.append(1)
                            else:
                                if x[3] <= 1.5500000119:
                                    results.append(2)
                                else:
                                    results.append(1)
                        else:
                            results.append(1)
                else:
                    results.append(1)
            else:
                if x[0] <= 5.9500000477:
                    if x[1] <= 2.9500000477:
                        results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 193
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 5.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[3] <= 1.6999999881:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            if x[0] <= 6.0499999523:
                                if x[1] <= 2.4500000477:
                                    results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 194
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.7000000030:
            results.append(0)
        else:
            if x[2] <= 4.7500000000:
                results.append(1)
            else:
                if x[3] <= 1.6999999881:
                    if x[2] <= 5.3499999046:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[2] <= 4.8500001431:
                        if x[0] <= 5.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 195
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[3] <= 1.6999999881:
                if x[1] <= 2.6499999762:
                    if x[2] <= 4.9500000477:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(1)
            else:
                if x[2] <= 4.8500001431:
                    if x[0] <= 6.0499999523:
                        results.append(1)
                    else:
                        results.append(2)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 196
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.4499999881:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[0] <= 6.5000000000:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
                        results.append(1)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 197
    if time.time() < deadline or interrupt_flag.is_set():
        if x[3] <= 0.8000000119:
            results.append(0)
        else:
            if x[0] <= 5.9500000477:
                if x[2] <= 4.9000000954:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[2] <= 4.7500000000:
                    results.append(1)
                else:
                    if x[2] <= 5.1499998569:
                        if x[1] <= 2.6000000238:
                            if x[1] <= 2.3500000238:
                                results.append(2)
                            else:
                                results.append(1)
                        else:
                            if x[3] <= 1.7500000000:
                                if x[0] <= 6.5000000000:
                                    if x[1] <= 2.7500000000:
                                        results.append(1)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 198
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                results.append(1)
            else:
                if x[1] <= 2.6000000238:
                    if x[3] <= 1.6499999762:
                        if x[1] <= 2.3500000238:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
                else:
                    if x[3] <= 1.7500000000:
                        if x[1] <= 2.8999999762:
                            results.append(2)
                        else:
                            results.append(1)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 199
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 2.5999999642:
            results.append(0)
        else:
            if x[2] <= 4.8500001431:
                results.append(1)
            else:
                if x[3] <= 1.7500000000:
                    if x[1] <= 2.8999999762:
                        if x[2] <= 4.9500000477:
                            results.append(1)
                        else:
                            results.append(2)
                    else:
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
