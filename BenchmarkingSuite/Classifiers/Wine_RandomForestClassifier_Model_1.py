import time
"""

***** Metadata ******
Dataset: Wine
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
     n_estimators: 100
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
        if x[0] <= 12.7900004387:
            if time.time() < deadline:
                if x[6] <= 0.9699999988:
                    if time.time() < deadline:
                        if x[2] <= 1.8199999928:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 4.8399999142:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 19.1499996185:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 1.7500000000:
                    if time.time() < deadline:
                        if x[5] <= 2.4249999523:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 1.5600000173:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 591.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 1
    if time.time() < deadline:
        if x[12] <= 787.5000000000:
            if time.time() < deadline:
                if x[6] <= 1.2350000143:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 1.6050000191:
                    if time.time() < deadline:
                        if x[5] <= 1.2400000095:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 27.5000000000:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 2
    if time.time() < deadline:
        if x[6] <= 1.2250000238:
            if time.time() < deadline:
                if x[9] <= 3.4499999285:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[9] <= 3.6499999762:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 89.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 1.1999999881:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[10] <= 0.7049999833:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 3
    if time.time() < deadline:
        if x[0] <= 12.5250000954:
            if time.time() < deadline:
                if x[10] <= 0.6250000000:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 19.3000001907:
                    if time.time() < deadline:
                        if x[12] <= 797.5000000000:
                            if time.time() < deadline:
                                if x[3] <= 18.2500000000:
                                    if time.time() < deadline:
                                        if x[6] <= 2.2850000858:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[4] <= 90.5000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 2.0599999428:
                            if time.time() < deadline:
                                if x[7] <= 0.5099999905:
                                    if time.time() < deadline:
                                        if x[3] <= 22.0000000000:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 4.9000000954:
                                    if time.time() < deadline:
                                        if x[10] <= 0.8049999774:
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
        if x[6] <= 0.9749999940:
            if time.time() < deadline:
                if x[8] <= 0.5299999863:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 13.1349997520:
                    if time.time() < deadline:
                        if x[4] <= 104.0000000000:
                            if time.time() < deadline:
                                if x[3] <= 15.7500000000:
                                    if time.time() < deadline:
                                        if x[0] <= 13.0899996758:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 2.4150000811:
                                    if time.time() < deadline:
                                        if x[0] <= 12.5599999428:
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
                        if x[12] <= 755.0000000000:
                            if time.time() < deadline:
                                if x[12] <= 742.5000000000:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 5
    if time.time() < deadline:
        if x[11] <= 2.1250000000:
            if time.time() < deadline:
                if x[2] <= 2.2350000143:
                    if time.time() < deadline:
                        if x[9] <= 3.5249999762:
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
                if x[12] <= 830.0000000000:
                    if time.time() < deadline:
                        if x[12] <= 765.0000000000:
                            if time.time() < deadline:
                                if x[11] <= 2.2050000429:
                                    if time.time() < deadline:
                                        if x[2] <= 2.2649999261:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 113.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[1] <= 2.3549998999:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 1.2949999571:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 6
    if time.time() < deadline:
        if x[10] <= 0.8550000191:
            if time.time() < deadline:
                if x[1] <= 5.7250001431:
                    if time.time() < deadline:
                        if x[12] <= 397.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 0.8299999833:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[10] <= 0.8449999988:
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
                if x[0] <= 12.7800002098:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 2.4000000954:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 1.1399999857:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 7
    if time.time() < deadline:
        if x[6] <= 2.5099999905:
            if time.time() < deadline:
                if x[11] <= 2.1449999809:
                    if time.time() < deadline:
                        if x[4] <= 99.0000000000:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.0999999642:
                                    if time.time() < deadline:
                                        if x[8] <= 1.0099999905:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[10] <= 0.7430000007:
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
                        if x[11] <= 3.6000000238:
                            if time.time() < deadline:
                                if x[0] <= 13.1649999619:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 1.6899999976:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 720.0000000000:
                    if time.time() < deadline:
                        if x[0] <= 12.9699997902:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 8
    if time.time() < deadline:
        if x[11] <= 2.4750000238:
            if time.time() < deadline:
                if x[1] <= 1.8899999857:
                    if time.time() < deadline:
                        if x[10] <= 0.8650000095:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 0.8299999833:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[4] <= 93.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 13.0499997139:
                    if time.time() < deadline:
                        if x[11] <= 3.6000000238:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[11] <= 3.6350001097:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 22.5000000000:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 9
    if time.time() < deadline:
        if x[12] <= 1000.0000000000:
            if time.time() < deadline:
                if x[6] <= 1.3149999976:
                    if time.time() < deadline:
                        if x[12] <= 398.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 0.4849999994:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 2.2549999952:
                                            if time.time() < deadline:
                                                if x[1] <= 2.0099999309:
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
                        if x[4] <= 109.0000000000:
                            if time.time() < deadline:
                                if x[11] <= 3.4300000668:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 2.1650000215:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 2.6099998951:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[8] <= 1.3050000072:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
        else:
            trees.append(0)
            results[0], results[1] = vote_logic(trees)
    
    # Tree 10
    if time.time() < deadline:
        if x[11] <= 2.0849999189:
            if time.time() < deadline:
                if x[9] <= 3.5599999428:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 0.9450000226:
                            if time.time() < deadline:
                                if x[4] <= 86.5000000000:
                                    if time.time() < deadline:
                                        if x[6] <= 1.0850000083:
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
                if x[0] <= 12.8100004196:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[6] <= 2.0799999237:
                            if time.time() < deadline:
                                if x[9] <= 4.1999999285:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 21.0000000000:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 22.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 11
    if time.time() < deadline:
        if x[9] <= 3.8199999332:
            if time.time() < deadline:
                if x[9] <= 3.4600000381:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 2.8500000238:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[5] <= 2.3700000048:
                    if time.time() < deadline:
                        if x[11] <= 2.3949999809:
                            if time.time() < deadline:
                                if x[1] <= 1.6299999952:
                                    if time.time() < deadline:
                                        if x[11] <= 1.5500000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[6] <= 1.5800000429:
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
                        if x[12] <= 679.0000000000:
                            if time.time() < deadline:
                                if x[3] <= 22.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 12
    if time.time() < deadline:
        if x[9] <= 3.4600000381:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 2.1799999475:
                    if time.time() < deadline:
                        if x[3] <= 17.1499996185:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[11] <= 2.5449999571:
                                    if time.time() < deadline:
                                        if x[4] <= 86.5000000000:
                                            if time.time() < deadline:
                                                if x[9] <= 4.8500001431:
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
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 13
    if time.time() < deadline:
        if x[0] <= 13.1349997520:
            if time.time() < deadline:
                if x[6] <= 1.2400000095:
                    if time.time() < deadline:
                        if x[9] <= 3.9349999428:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[6] <= 2.6100000143:
                            if time.time() < deadline:
                                if x[11] <= 3.6000000238:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 2.4100000858:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 1.7199999690:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[9] <= 3.4149999619:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 19.3000001907:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[6] <= 2.1300000548:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 14
    if time.time() < deadline:
        if x[6] <= 2.3099999428:
            if time.time() < deadline:
                if x[5] <= 1.8400000334:
                    if time.time() < deadline:
                        if x[10] <= 0.8550000191:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 0.8100000024:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 0.7700000107:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 1111.0000000000:
                                    if time.time() < deadline:
                                        if x[9] <= 4.7999999523:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[9] <= 5.3350000381:
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
                if x[12] <= 724.5000000000:
                    if time.time() < deadline:
                        if x[4] <= 99.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 2.9100000858:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 3.4349999428:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 15
    if time.time() < deadline:
        if x[9] <= 3.9450000525:
            if time.time() < deadline:
                if x[9] <= 3.6499999762:
                    if time.time() < deadline:
                        if x[12] <= 790.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 12.6700000763:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 852.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[8] <= 1.3249999881:
                    if time.time() < deadline:
                        if x[12] <= 460.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 2.5650000572:
                            if time.time() < deadline:
                                if x[3] <= 18.3000001907:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 2.1200000048:
                                    if time.time() < deadline:
                                        if x[9] <= 5.1700000763:
                                            if time.time() < deadline:
                                                if x[6] <= 3.3750000000:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 16
    if time.time() < deadline:
        if x[9] <= 3.4600000381:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.5650000572:
                    if time.time() < deadline:
                        if x[1] <= 1.5149999857:
                            if time.time() < deadline:
                                if x[5] <= 1.7150000334:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 1.5800000429:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 21.2500000000:
                            if time.time() < deadline:
                                if x[12] <= 618.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 2.0750000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 17
    if time.time() < deadline:
        if x[8] <= 1.6449999809:
            if time.time() < deadline:
                if x[6] <= 0.9749999940:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[5] <= 2.5749999285:
                            if time.time() < deadline:
                                if x[12] <= 945.0000000000:
                                    if time.time() < deadline:
                                        if x[3] <= 24.7500000000:
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
                                if x[0] <= 12.8499999046:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[9] <= 4.6499998569:
                    if time.time() < deadline:
                        if x[0] <= 12.9800000191:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 2.6900000572:
                            if time.time() < deadline:
                                if x[12] <= 648.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 1.5899999738:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 18
    if time.time() < deadline:
        if x[6] <= 1.3149999976:
            if time.time() < deadline:
                if x[9] <= 3.6349999905:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 676.0000000000:
                    if time.time() < deadline:
                        if x[11] <= 1.4449999928:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[6] <= 2.9300000668:
                            if time.time() < deadline:
                                if x[9] <= 3.0850000381:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[7] <= 0.2650000006:
                                            if time.time() < deadline:
                                                if x[6] <= 2.4800000191:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 19
    if time.time() < deadline:
        if x[7] <= 0.4599999934:
            if time.time() < deadline:
                if x[6] <= 2.6650000811:
                    if time.time() < deadline:
                        if x[12] <= 976.0000000000:
                            if time.time() < deadline:
                                if x[6] <= 1.5750000477:
                                    if time.time() < deadline:
                                        if x[9] <= 4.2000000477:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[6] <= 2.6050000191:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[4] <= 100.5000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 697.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 26.2500000000:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[10] <= 0.9699999988:
                    if time.time() < deadline:
                        if x[8] <= 1.5899999738:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 7.6600003242:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 957.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 20
    if time.time() < deadline:
        if x[5] <= 2.5749999285:
            if time.time() < deadline:
                if x[4] <= 88.5000000000:
                    if time.time() < deadline:
                        if x[6] <= 0.9499999881:
                            if time.time() < deadline:
                                if x[9] <= 3.4250000715:
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
                        if x[11] <= 2.1599999666:
                            if time.time() < deadline:
                                if x[10] <= 0.8980000019:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[11] <= 1.9899999499:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 2.3799999952:
                                    if time.time() < deadline:
                                        if x[9] <= 4.1999999285:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 133.0000000000:
                                            if time.time() < deadline:
                                                if x[6] <= 2.6450001001:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[7] <= 0.3949999958:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(0)
                                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[9] <= 4.1500000954:
                    if time.time() < deadline:
                        if x[12] <= 1010.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 90.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 21
    if time.time() < deadline:
        if x[12] <= 755.0000000000:
            if time.time() < deadline:
                if x[9] <= 3.8249999285:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 0.9999999702:
                            if time.time() < deadline:
                                if x[6] <= 2.1000000834:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[12] <= 516.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 2.3949999213:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[9] <= 3.4349999428:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 2.4599999189:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 13.7899999619:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 22
    if time.time() < deadline:
        if x[6] <= 1.2350000143:
            if time.time() < deadline:
                if x[10] <= 0.9699999690:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 2.5949999094:
                    if time.time() < deadline:
                        if x[3] <= 24.7500000000:
                            if time.time() < deadline:
                                if x[9] <= 4.9000000954:
                                    if time.time() < deadline:
                                        if x[12] <= 1111.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[6] <= 1.9200000167:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 27.0000000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 88.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 23
    if time.time() < deadline:
        if x[0] <= 12.7900004387:
            if time.time() < deadline:
                if x[9] <= 4.8399999142:
                    if time.time() < deadline:
                        if x[6] <= 0.5199999958:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 1.8750000596:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 755.0000000000:
                    if time.time() < deadline:
                        if x[11] <= 2.3849999905:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 655.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 9.0000000000:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 24
    if time.time() < deadline:
        if x[11] <= 2.1250000000:
            if time.time() < deadline:
                if x[1] <= 1.0900000036:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 13.0399999619:
                    if time.time() < deadline:
                        if x[6] <= 0.7950000167:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 12.7850003242:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[10] <= 1.1400000453:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 83.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 25
    if time.time() < deadline:
        if x[11] <= 2.1900000572:
            if time.time() < deadline:
                if x[9] <= 3.6250000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 5.8150000572:
                            if time.time() < deadline:
                                if x[8] <= 0.6750000119:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[8] <= 1.4599999785:
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
                if x[12] <= 726.5000000000:
                    if time.time() < deadline:
                        if x[8] <= 0.8899999857:
                            if time.time() < deadline:
                                if x[2] <= 2.3100000024:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 2.5950000286:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[5] <= 2.6900000572:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 2.4399999380:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 3.4349999428:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 26
    if time.time() < deadline:
        if x[12] <= 787.5000000000:
            if time.time() < deadline:
                if x[7] <= 0.4500000030:
                    if time.time() < deadline:
                        if x[11] <= 2.0199999213:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 2.7999999523:
                                    if time.time() < deadline:
                                        if x[0] <= 13.1749997139:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[6] <= 2.2100000381:
                                                    if time.time() < deadline:
                                                        if x[0] <= 13.5149998665:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 460.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 3.8249999285:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[12] <= 517.5000000000:
                                            if time.time() < deadline:
                                                if x[11] <= 1.8199999928:
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
                if x[5] <= 1.9249999523:
                    if time.time() < deadline:
                        if x[12] <= 862.5000000000:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 27
    if time.time() < deadline:
        if x[2] <= 2.0599999428:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[10] <= 0.8750000000:
                    if time.time() < deadline:
                        if x[5] <= 2.6099998951:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 1.7149999738:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 13.6950001717:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 1.4350000024:
                            if time.time() < deadline:
                                if x[11] <= 3.4049999714:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 21.5000000000:
                                    if time.time() < deadline:
                                        if x[5] <= 2.1000000238:
                                            if time.time() < deadline:
                                                if x[4] <= 97.5000000000:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[6] <= 2.3500000238:
                                                    if time.time() < deadline:
                                                        if x[1] <= 2.0750000477:
                                                            trees.append(0)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 2.5149999857:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[9] <= 3.6749999523:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 28
    if time.time() < deadline:
        if x[12] <= 755.0000000000:
            if time.time() < deadline:
                if x[9] <= 4.7899999619:
                    if time.time() < deadline:
                        if x[5] <= 1.4150000215:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 3.9249999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 89.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[10] <= 0.8650000095:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[8] <= 0.6500000060:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 1.1250000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.3450000286:
                    if time.time() < deadline:
                        if x[12] <= 862.5000000000:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 29
    if time.time() < deadline:
        if x[0] <= 12.5500001907:
            if time.time() < deadline:
                if x[7] <= 0.4749999940:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[8] <= 1.0449999571:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.5650000572:
                    if time.time() < deadline:
                        if x[10] <= 0.9899999797:
                            if time.time() < deadline:
                                if x[11] <= 1.9649999738:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[12] <= 532.5000000000:
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
                        if x[3] <= 23.2500000000:
                            if time.time() < deadline:
                                if x[0] <= 12.7850003242:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 30
    if time.time() < deadline:
        if x[6] <= 2.3600000143:
            if time.time() < deadline:
                if x[9] <= 3.8249999285:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 2.1450001001:
                            if time.time() < deadline:
                                if x[0] <= 13.1649999619:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[9] <= 3.3849999905:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 15.0999999046:
                            if time.time() < deadline:
                                if x[3] <= 14.8000001907:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 12.7100000381:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 31
    if time.time() < deadline:
        if x[6] <= 1.2350000143:
            if time.time() < deadline:
                if x[9] <= 3.5599999428:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 13.1349997520:
                    if time.time() < deadline:
                        if x[11] <= 1.6700000167:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 790.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[9] <= 3.4649999142:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[8] <= 1.1399999857:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 23.7500000000:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 32
    if time.time() < deadline:
        if x[9] <= 3.4600000381:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 842.5000000000:
                    if time.time() < deadline:
                        if x[6] <= 1.4399999976:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 12.8049998283:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 17.7500000000:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 33
    if time.time() < deadline:
        if x[1] <= 2.7200000286:
            if time.time() < deadline:
                if x[6] <= 2.3199999332:
                    if time.time() < deadline:
                        if x[9] <= 4.6249998808:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 17.1499996185:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[5] <= 2.2749999762:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 3.4349999428:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[10] <= 1.1150000095:
                                            if time.time() < deadline:
                                                if x[0] <= 12.6100001335:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[12] <= 761.5000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[5] <= 2.3750000000:
                    if time.time() < deadline:
                        if x[0] <= 12.0199999809:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 1.5800000429:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[8] <= 1.8050000072:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 3.2150000334:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 34
    if time.time() < deadline:
        if x[1] <= 2.4300000668:
            if time.time() < deadline:
                if x[9] <= 4.6899998188:
                    if time.time() < deadline:
                        if x[5] <= 2.2749999762:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 2.6049998999:
                                    if time.time() < deadline:
                                        if x[12] <= 987.5000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 2.7350000143:
                            if time.time() < deadline:
                                if x[6] <= 1.8699999452:
                                    if time.time() < deadline:
                                        if x[7] <= 0.5249999762:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[3] <= 17.1499996185:
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
        else:
            if time.time() < deadline:
                if x[8] <= 1.6099999547:
                    if time.time() < deadline:
                        if x[9] <= 3.8249999285:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 2.1100000739:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 677.5000000000:
                            if time.time() < deadline:
                                if x[7] <= 0.5200000107:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 35
    if time.time() < deadline:
        if x[9] <= 3.4600000381:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 755.0000000000:
                    if time.time() < deadline:
                        if x[0] <= 12.7450003624:
                            if time.time() < deadline:
                                if x[8] <= 0.9249999821:
                                    if time.time() < deadline:
                                        if x[1] <= 3.0399999022:
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
                                if x[2] <= 2.0749999881:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[8] <= 1.5899999738:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[9] <= 7.6600003242:
                                                    if time.time() < deadline:
                                                        if x[11] <= 2.4700000286:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(0)
                                                            results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[5] <= 1.8500000238:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 36
    if time.time() < deadline:
        if x[6] <= 1.2350000143:
            if time.time() < deadline:
                if x[2] <= 1.7299999595:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[7] <= 0.6200000048:
                            if time.time() < deadline:
                                if x[10] <= 0.8980000019:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[7] <= 0.4200000018:
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
                if x[0] <= 13.3650002480:
                    if time.time() < deadline:
                        if x[12] <= 790.0000000000:
                            if time.time() < deadline:
                                if x[0] <= 13.1749997139:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[10] <= 1.0299999714:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 3.1499999762:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 3.8199999332:
                            if time.time() < deadline:
                                if x[8] <= 1.3449999690:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 37
    if time.time() < deadline:
        if x[5] <= 2.3799999952:
            if time.time() < deadline:
                if x[11] <= 2.2050000429:
                    if time.time() < deadline:
                        if x[1] <= 1.7549999952:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 4.8500001431:
                                    if time.time() < deadline:
                                        if x[6] <= 1.1950000226:
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
                        if x[10] <= 0.8149999976:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 772.5000000000:
                    if time.time() < deadline:
                        if x[9] <= 8.5250000954:
                            if time.time() < deadline:
                                if x[9] <= 3.7450001240:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[8] <= 1.8850000501:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 38
    if time.time() < deadline:
        if x[0] <= 12.7450003624:
            if time.time() < deadline:
                if x[10] <= 0.7400000095:
                    if time.time() < deadline:
                        if x[4] <= 87.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[5] <= 1.4150000215:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[10] <= 0.8350000083:
                    if time.time() < deadline:
                        if x[2] <= 2.1600000858:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 707.5000000000:
                            if time.time() < deadline:
                                if x[10] <= 0.9699999988:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[4] <= 131.5000000000:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 39
    if time.time() < deadline:
        if x[10] <= 0.7849999964:
            if time.time() < deadline:
                if x[12] <= 397.5000000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 11.8550000191:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[5] <= 2.2899999619:
                    if time.time() < deadline:
                        if x[3] <= 22.8999996185:
                            if time.time() < deadline:
                                if x[10] <= 0.9300000072:
                                    if time.time() < deadline:
                                        if x[6] <= 0.9099999964:
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
                                if x[9] <= 3.6749999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 670.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 2.2999999523:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[9] <= 3.4349999428:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 40
    if time.time() < deadline:
        if x[9] <= 3.6499999762:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 1.4050000310:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 4.8500001431:
                            if time.time() < deadline:
                                if x[12] <= 724.5000000000:
                                    if time.time() < deadline:
                                        if x[11] <= 2.9199999571:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[4] <= 94.5000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 41
    if time.time() < deadline:
        if x[0] <= 12.7900004387:
            if time.time() < deadline:
                if x[6] <= 0.8849999905:
                    if time.time() < deadline:
                        if x[7] <= 0.2849999964:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 3.4900000095:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 490.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[10] <= 0.8149999976:
                    if time.time() < deadline:
                        if x[6] <= 2.1100000739:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[6] <= 2.1100000143:
                            if time.time() < deadline:
                                if x[10] <= 0.9450000226:
                                    if time.time() < deadline:
                                        if x[7] <= 0.5699999928:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 42
    if time.time() < deadline:
        if x[9] <= 3.4600000381:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 1.3599999547:
                    if time.time() < deadline:
                        if x[11] <= 2.5600000620:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 724.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 43
    if time.time() < deadline:
        if x[9] <= 3.9150000811:
            if time.time() < deadline:
                if x[12] <= 772.0000000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 1.7399999499:
                            if time.time() < deadline:
                                if x[8] <= 1.4150000215:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[10] <= 0.8099999726:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 2.5249999762:
                            if time.time() < deadline:
                                if x[8] <= 1.2400000095:
                                    if time.time() < deadline:
                                        if x[10] <= 0.9699999988:
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
                                if x[12] <= 697.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 44
    if time.time() < deadline:
        if x[6] <= 1.3149999976:
            if time.time() < deadline:
                if x[10] <= 0.8980000019:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 3.2799999118:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[4] <= 90.5000000000:
                    if time.time() < deadline:
                        if x[1] <= 3.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 13.2300000191:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 12.7750000954:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 1.9900000095:
                                    if time.time() < deadline:
                                        if x[12] <= 565.0000000000:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[9] <= 3.4349999428:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 45
    if time.time() < deadline:
        if x[8] <= 1.1999999881:
            if time.time() < deadline:
                if x[6] <= 1.2350000143:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 2.5949999094:
                    if time.time() < deadline:
                        if x[10] <= 0.6800000072:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 986.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 19.6999998093:
                            if time.time() < deadline:
                                if x[0] <= 13.1749997139:
                                    if time.time() < deadline:
                                        if x[12] <= 849.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 0.9999999702:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 13.0199999809:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 46
    if time.time() < deadline:
        if x[0] <= 12.5199999809:
            if time.time() < deadline:
                if x[9] <= 5.0649998188:
                    if time.time() < deadline:
                        if x[1] <= 4.5149998665:
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
                if x[11] <= 2.4399999380:
                    if time.time() < deadline:
                        if x[5] <= 2.4249999523:
                            if time.time() < deadline:
                                if x[6] <= 1.5800000429:
                                    if time.time() < deadline:
                                        if x[3] <= 17.2500000000:
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
                        if x[0] <= 13.0199999809:
                            if time.time() < deadline:
                                if x[9] <= 3.9150000811:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[4] <= 87.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 47
    if time.time() < deadline:
        if x[0] <= 13.3650002480:
            if time.time() < deadline:
                if x[10] <= 0.8400000036:
                    if time.time() < deadline:
                        if x[4] <= 87.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 2.6000000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 12.7699999809:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 2.2299998999:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 108.0000000000:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 755.0000000000:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 48
    if time.time() < deadline:
        if x[9] <= 3.9150000811:
            if time.time() < deadline:
                if x[3] <= 15.7500000000:
                    if time.time() < deadline:
                        if x[11] <= 2.2550000548:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.4750000238:
                    if time.time() < deadline:
                        if x[6] <= 1.4350000024:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 89.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 49
    if time.time() < deadline:
        if x[4] <= 92.5000000000:
            if time.time() < deadline:
                if x[10] <= 0.8249999881:
                    if time.time() < deadline:
                        if x[3] <= 16.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 874.5000000000:
                            if time.time() < deadline:
                                if x[8] <= 1.0249999762:
                                    if time.time() < deadline:
                                        if x[10] <= 0.9799999893:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[5] <= 2.3349999189:
                    if time.time() < deadline:
                        if x[1] <= 2.1949999332:
                            if time.time() < deadline:
                                if x[9] <= 4.1499999762:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[8] <= 1.4850000143:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 1.2700000405:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 117.5000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 2.6600000858:
                            if time.time() < deadline:
                                if x[3] <= 22.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 512.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 50
    if time.time() < deadline:
        if x[0] <= 12.5250000954:
            if time.time() < deadline:
                if x[1] <= 4.0749999285:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[8] <= 1.3249999881:
                    if time.time() < deadline:
                        if x[3] <= 18.5500001907:
                            if time.time() < deadline:
                                if x[11] <= 2.8499999046:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 0.9699999988:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 3.8499999046:
                            if time.time() < deadline:
                                if x[9] <= 3.4349999428:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[9] <= 10.3249998093:
                                            if time.time() < deadline:
                                                if x[10] <= 0.7450000048:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 0.7150000036:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 51
    if time.time() < deadline:
        if x[0] <= 13.0399999619:
            if time.time() < deadline:
                if x[8] <= 1.3000000119:
                    if time.time() < deadline:
                        if x[6] <= 1.2700000405:
                            if time.time() < deadline:
                                if x[6] <= 0.5749999881:
                                    if time.time() < deadline:
                                        if x[6] <= 0.5300000012:
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
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[1] <= 2.3600000143:
                    if time.time() < deadline:
                        if x[12] <= 772.5000000000:
                            if time.time() < deadline:
                                if x[9] <= 6.2000000477:
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
                        if x[10] <= 0.7999999821:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 2.2250000238:
                                    if time.time() < deadline:
                                        if x[5] <= 1.8249999881:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 52
    if time.time() < deadline:
        if x[0] <= 12.7900004387:
            if time.time() < deadline:
                if x[11] <= 2.0599999428:
                    if time.time() < deadline:
                        if x[1] <= 1.1149999797:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 862.5000000000:
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
                if x[5] <= 2.2749999762:
                    if time.time() < deadline:
                        if x[1] <= 1.7799999714:
                            if time.time() < deadline:
                                if x[8] <= 1.5150000453:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 1.2900000215:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 21.2500000000:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 105.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 53
    if time.time() < deadline:
        if x[0] <= 12.7900004387:
            if time.time() < deadline:
                if x[9] <= 4.8399999142:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 17.8999996185:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 21.2500000000:
                    if time.time() < deadline:
                        if x[11] <= 2.5249999762:
                            if time.time() < deadline:
                                if x[6] <= 1.6250000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[4] <= 83.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 5.1900000572:
                            if time.time() < deadline:
                                if x[5] <= 1.5999999642:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 1.0300000310:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 54
    if time.time() < deadline:
        if x[9] <= 3.4600000381:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 1.5800000429:
                    if time.time() < deadline:
                        if x[2] <= 2.0550000072:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 88.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 12.3050003052:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 55
    if time.time() < deadline:
        if x[6] <= 0.9099999964:
            if time.time() < deadline:
                if x[9] <= 2.8999999762:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 755.0000000000:
                    if time.time() < deadline:
                        if x[1] <= 2.4950000048:
                            if time.time() < deadline:
                                if x[2] <= 2.7450000048:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 581.0000000000:
                                    if time.time() < deadline:
                                        if x[11] <= 1.7699999213:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[5] <= 2.1700000763:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[6] <= 1.6050000191:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 56
    if time.time() < deadline:
        if x[9] <= 3.4600000381:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 17.4499998093:
                    if time.time() < deadline:
                        if x[2] <= 2.0099999309:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 2.4850000143:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 12.9800000191:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 57
    if time.time() < deadline:
        if x[10] <= 0.8299999833:
            if time.time() < deadline:
                if x[12] <= 402.5000000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 12.0199999809:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 18.2500000000:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 772.5000000000:
                    if time.time() < deadline:
                        if x[6] <= 0.9450000226:
                            if time.time() < deadline:
                                if x[4] <= 90.0000000000:
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
                        if x[10] <= 1.2949999571:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 58
    if time.time() < deadline:
        if x[9] <= 3.8199999332:
            if time.time() < deadline:
                if x[4] <= 97.5000000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 3.1800000668:
                            if time.time() < deadline:
                                if x[12] <= 978.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 3.4649999142:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 1.5800000429:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 1.2599999905:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 1.9250000119:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 59
    if time.time() < deadline:
        if x[2] <= 2.2849999666:
            if time.time() < deadline:
                if x[7] <= 0.4549999982:
                    if time.time() < deadline:
                        if x[0] <= 13.0599999428:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 1.1899999976:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[8] <= 2.1799999475:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[7] <= 0.6450000107:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 755.0000000000:
                    if time.time() < deadline:
                        if x[1] <= 1.6399999857:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[2] <= 2.7300000191:
                                    if time.time() < deadline:
                                        if x[3] <= 18.5000000000:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[5] <= 2.1650000811:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 0.7400000095:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 3.4649999142:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 60
    if time.time() < deadline:
        if x[12] <= 892.5000000000:
            if time.time() < deadline:
                if x[6] <= 1.2350000143:
                    if time.time() < deadline:
                        if x[2] <= 2.2200000286:
                            if time.time() < deadline:
                                if x[1] <= 2.5999999642:
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
                        if x[4] <= 114.0000000000:
                            if time.time() < deadline:
                                if x[0] <= 13.8400001526:
                                    if time.time() < deadline:
                                        if x[3] <= 17.7500000000:
                                            if time.time() < deadline:
                                                if x[6] <= 2.3300000429:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[4] <= 90.5000000000:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(0)
                                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 726.5000000000:
                                    if time.time() < deadline:
                                        if x[0] <= 12.6599998474:
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
                if x[6] <= 2.2999999523:
                    if time.time() < deadline:
                        if x[11] <= 2.7000000477:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 61
    if time.time() < deadline:
        if x[11] <= 2.1250000000:
            if time.time() < deadline:
                if x[10] <= 0.9899999797:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 726.5000000000:
                    if time.time() < deadline:
                        if x[1] <= 2.6050000191:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 1.2600000203:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 0.7800000012:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 2.3949999809:
                                    if time.time() < deadline:
                                        if x[4] <= 115.0000000000:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[5] <= 3.2849999666:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[12] <= 1232.5000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 62
    if time.time() < deadline:
        if x[9] <= 3.9450000525:
            if time.time() < deadline:
                if x[9] <= 3.4600000381:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 2.3249999285:
                            if time.time() < deadline:
                                if x[9] <= 3.7200000286:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[7] <= 0.4849999994:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 3.1149998903:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.4399999380:
                    if time.time() < deadline:
                        if x[6] <= 1.5800000429:
                            if time.time() < deadline:
                                if x[8] <= 0.6299999952:
                                    if time.time() < deadline:
                                        if x[5] <= 1.7849999666:
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
                        if x[0] <= 12.7649998665:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 63
    if time.time() < deadline:
        if x[12] <= 837.5000000000:
            if time.time() < deadline:
                if x[1] <= 2.4450000525:
                    if time.time() < deadline:
                        if x[9] <= 5.0649998188:
                            if time.time() < deadline:
                                if x[2] <= 3.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 17.1499996185:
                                    if time.time() < deadline:
                                        if x[8] <= 1.4799999595:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 13.1050000191:
                            if time.time() < deadline:
                                if x[5] <= 1.6250000000:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[12] <= 616.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 2.3200000525:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 12.5700001717:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 64
    if time.time() < deadline:
        if x[0] <= 13.0599999428:
            if time.time() < deadline:
                if x[10] <= 0.7849999964:
                    if time.time() < deadline:
                        if x[9] <= 4.2699999809:
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
                if x[0] <= 13.5400004387:
                    if time.time() < deadline:
                        if x[9] <= 5.6899998188:
                            if time.time() < deadline:
                                if x[7] <= 0.4099999964:
                                    if time.time() < deadline:
                                        if x[8] <= 1.1899999976:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[12] <= 618.5000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[10] <= 0.9549999833:
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
                        if x[6] <= 1.5799999535:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 65
    if time.time() < deadline:
        if x[6] <= 0.9749999940:
            trees.append(2)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 772.5000000000:
                    if time.time() < deadline:
                        if x[11] <= 1.5049999952:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 679.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[11] <= 2.6549999714:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[1] <= 2.8949999809:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[8] <= 2.8300000429:
                            if time.time() < deadline:
                                if x[6] <= 1.6050000191:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 27.5000000000:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 66
    if time.time() < deadline:
        if x[11] <= 2.1900000572:
            if time.time() < deadline:
                if x[11] <= 1.8000000119:
                    if time.time() < deadline:
                        if x[2] <= 2.0850000381:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 2.4200000167:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 532.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[4] <= 94.5000000000:
                    if time.time() < deadline:
                        if x[0] <= 13.2049999237:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 705.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[6] <= 1.3450000286:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 2.5449999571:
                            if time.time() < deadline:
                                if x[10] <= 0.8649999797:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 3.4099999666:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 67
    if time.time() < deadline:
        if x[6] <= 1.2350000143:
            trees.append(2)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 2.5149999857:
                    if time.time() < deadline:
                        if x[10] <= 0.6449999809:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 3.8650000095:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[9] <= 4.2649999857:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 0.8050000072:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 1.2799999714:
                                    if time.time() < deadline:
                                        if x[3] <= 22.0000000000:
                                            if time.time() < deadline:
                                                if x[4] <= 99.0000000000:
                                                    if time.time() < deadline:
                                                        if x[7] <= 0.3299999982:
                                                            trees.append(0)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            if time.time() < deadline:
                                                                if x[3] <= 14.7500000000:
                                                                    trees.append(0)
                                                                    results[0], results[1] = vote_logic(trees)
                                                                else:
                                                                    trees.append(1)
                                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[12] <= 646.5000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 68
    if time.time() < deadline:
        if x[12] <= 805.0000000000:
            if time.time() < deadline:
                if x[10] <= 0.8949999809:
                    if time.time() < deadline:
                        if x[8] <= 1.8849999905:
                            if time.time() < deadline:
                                if x[6] <= 1.2250000238:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 13.0799999237:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[7] <= 0.2899999917:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[3] <= 24.7500000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 0.9650000036:
                            if time.time() < deadline:
                                if x[6] <= 0.8950000107:
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
                if x[11] <= 2.6400001049:
                    if time.time() < deadline:
                        if x[12] <= 862.5000000000:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 1.2949999571:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 69
    if time.time() < deadline:
        if x[9] <= 3.9450000525:
            if time.time() < deadline:
                if x[11] <= 3.8200000525:
                    if time.time() < deadline:
                        if x[12] <= 790.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.4750000238:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 88.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 70
    if time.time() < deadline:
        if x[12] <= 875.0000000000:
            if time.time() < deadline:
                if x[10] <= 0.8550000191:
                    if time.time() < deadline:
                        if x[7] <= 0.4099999964:
                            if time.time() < deadline:
                                if x[11] <= 2.6399999857:
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
                        if x[8] <= 2.3099999428:
                            if time.time() < deadline:
                                if x[6] <= 0.9099999964:
                                    if time.time() < deadline:
                                        if x[12] <= 535.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 118.0000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[0] <= 12.7600002289:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 71
    if time.time() < deadline:
        if x[9] <= 3.4099999666:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.3949999809:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[2] <= 2.1099998951:
                            if time.time() < deadline:
                                if x[7] <= 0.2699999958:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[5] <= 1.8250000477:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 21.2500000000:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[9] <= 4.8199999332:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 72
    if time.time() < deadline:
        if x[10] <= 0.7899999917:
            if time.time() < deadline:
                if x[2] <= 2.0399999619:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[5] <= 2.8299999237:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 772.5000000000:
                    if time.time() < deadline:
                        if x[1] <= 2.9250000715:
                            if time.time() < deadline:
                                if x[1] <= 2.5699999332:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 12.7649998665:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[11] <= 2.5750000477:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 12.9699997902:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[3] <= 20.1999998093:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 3.4649999142:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 73
    if time.time() < deadline:
        if x[12] <= 772.5000000000:
            if time.time() < deadline:
                if x[5] <= 1.8400000334:
                    if time.time() < deadline:
                        if x[0] <= 12.1799998283:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 1.2350000143:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[5] <= 1.4250000119:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 5.3750000000:
                            if time.time() < deadline:
                                if x[4] <= 114.0000000000:
                                    if time.time() < deadline:
                                        if x[7] <= 0.4599999934:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[7] <= 0.4949999899:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[6] <= 0.8450000286:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(1)
                                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 134.5000000000:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 0.8650000095:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[5] <= 1.8649999499:
                    if time.time() < deadline:
                        if x[12] <= 862.5000000000:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 74
    if time.time() < deadline:
        if x[5] <= 2.3349999189:
            if time.time() < deadline:
                if x[5] <= 1.5749999881:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 2.9250000715:
                            if time.time() < deadline:
                                if x[9] <= 4.8399999142:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 97.5000000000:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 572.0000000000:
                                    if time.time() < deadline:
                                        if x[6] <= 1.0850000083:
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
                if x[6] <= 2.3099999428:
                    if time.time() < deadline:
                        if x[10] <= 0.7150000036:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 3.2100000381:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[4] <= 87.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[12] <= 736.5000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 75
    if time.time() < deadline:
        if x[9] <= 4.6899998188:
            if time.time() < deadline:
                if x[11] <= 3.6000000238:
                    if time.time() < deadline:
                        if x[9] <= 3.9250000715:
                            if time.time() < deadline:
                                if x[9] <= 3.4900000095:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 24.5000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 679.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 13.1999998093:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 1.9499999881:
                    if time.time() < deadline:
                        if x[3] <= 17.1499996185:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 76
    if time.time() < deadline:
        if x[9] <= 3.8199999332:
            if time.time() < deadline:
                if x[12] <= 797.5000000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 129.0000000000:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 19.4499998093:
                    if time.time() < deadline:
                        if x[0] <= 12.8450002670:
                            if time.time() < deadline:
                                if x[11] <= 2.0649999976:
                                    if time.time() < deadline:
                                        if x[6] <= 1.0349999964:
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
                                if x[11] <= 2.1200000048:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 2.5600000620:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 12.9549999237:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 77
    if time.time() < deadline:
        if x[6] <= 1.2250000238:
            if time.time() < deadline:
                if x[3] <= 16.7500000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 2.2050000429:
                    if time.time() < deadline:
                        if x[9] <= 3.9250000715:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 1.0299999714:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 679.0000000000:
                            if time.time() < deadline:
                                if x[3] <= 24.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[12] <= 563.0000000000:
                                            if time.time() < deadline:
                                                if x[4] <= 109.0000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 78
    if time.time() < deadline:
        if x[9] <= 3.8199999332:
            if time.time() < deadline:
                if x[12] <= 790.0000000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 1.0080000162:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[5] <= 2.0000000000:
                    if time.time() < deadline:
                        if x[1] <= 1.0949999690:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 1.5800000429:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 0.7549999952:
                            if time.time() < deadline:
                                if x[5] <= 2.5199999809:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 679.0000000000:
                                    if time.time() < deadline:
                                        if x[3] <= 21.0500001907:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 79
    if time.time() < deadline:
        if x[3] <= 17.8999996185:
            if time.time() < deadline:
                if x[2] <= 2.0399999619:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 1.3000000119:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[8] <= 1.1850000024:
                    if time.time() < deadline:
                        if x[6] <= 1.4750000238:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 13.1399998665:
                            if time.time() < deadline:
                                if x[11] <= 1.7799999714:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[3] <= 24.7500000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 3.0000000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 6.7750000954:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 80
    if time.time() < deadline:
        if x[11] <= 2.1900000572:
            if time.time() < deadline:
                if x[7] <= 0.3850000054:
                    if time.time() < deadline:
                        if x[1] <= 1.8899999857:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[5] <= 2.4249999523:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 1.3049999774:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 724.5000000000:
                    if time.time() < deadline:
                        if x[2] <= 2.6299999952:
                            if time.time() < deadline:
                                if x[12] <= 679.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 2.2450000048:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[1] <= 2.7450000048:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 134.0000000000:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 81
    if time.time() < deadline:
        if x[6] <= 2.3199999332:
            if time.time() < deadline:
                if x[10] <= 0.7849999964:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 4.8600001335:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 520.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 2.1500000954:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 13.0749998093:
                            if time.time() < deadline:
                                if x[3] <= 17.9499998093:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 82
    if time.time() < deadline:
        if x[0] <= 13.0799999237:
            if time.time() < deadline:
                if x[9] <= 4.8600001335:
                    if time.time() < deadline:
                        if x[2] <= 2.5149999857:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 3.8249999285:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 12.5500001907:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[8] <= 1.7149999738:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 730.0000000000:
                    if time.time() < deadline:
                        if x[5] <= 2.4200000763:
                            if time.time() < deadline:
                                if x[10] <= 0.9699999988:
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
                        if x[9] <= 3.3450000286:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 83
    if time.time() < deadline:
        if x[0] <= 13.4949998856:
            if time.time() < deadline:
                if x[1] <= 2.3750000000:
                    if time.time() < deadline:
                        if x[10] <= 0.7700000107:
                            if time.time() < deadline:
                                if x[5] <= 2.6699999571:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 815.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[7] <= 0.2349999920:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 3.8999999762:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[5] <= 2.1000000238:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 84
    if time.time() < deadline:
        if x[6] <= 1.3349999785:
            if time.time() < deadline:
                if x[11] <= 2.5600000620:
                    if time.time() < deadline:
                        if x[1] <= 1.1949999928:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 398.5000000000:
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
                if x[0] <= 13.1050000191:
                    if time.time() < deadline:
                        if x[3] <= 24.7500000000:
                            if time.time() < deadline:
                                if x[0] <= 12.7250003815:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 12.9400000572:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 1.8149999976:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[7] <= 0.3399999961:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[11] <= 2.5550000668:
                            if time.time() < deadline:
                                if x[11] <= 1.8799999952:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[4] <= 88.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 85
    if time.time() < deadline:
        if x[6] <= 2.6700000763:
            if time.time() < deadline:
                if x[10] <= 0.8949999809:
                    if time.time() < deadline:
                        if x[12] <= 393.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[9] <= 3.3750000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[12] <= 517.5000000000:
                                            if time.time() < deadline:
                                                if x[7] <= 0.5450000018:
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
                        if x[12] <= 1108.5000000000:
                            if time.time() < deadline:
                                if x[6] <= 0.5649999976:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 13.4949998856:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[2] <= 2.1349999309:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    if time.time() < deadline:
                                                        if x[4] <= 94.0000000000:
                                                            trees.append(2)
                                                            results[0], results[1] = vote_logic(trees)
                                                        else:
                                                            trees.append(0)
                                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[2] <= 1.9850000143:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 86
    if time.time() < deadline:
        if x[12] <= 875.0000000000:
            if time.time() < deadline:
                if x[10] <= 0.8299999833:
                    if time.time() < deadline:
                        if x[6] <= 2.0749999881:
                            if time.time() < deadline:
                                if x[9] <= 3.6250000000:
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
                        if x[4] <= 113.0000000000:
                            if time.time() < deadline:
                                if x[1] <= 3.0449999571:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 13.3699998856:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[11] <= 3.1349999905:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[6] <= 2.2999999523:
                    if time.time() < deadline:
                        if x[6] <= 2.2300000191:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 87
    if time.time() < deadline:
        if x[9] <= 3.8199999332:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.4750000238:
                    if time.time() < deadline:
                        if x[12] <= 465.0000000000:
                            if time.time() < deadline:
                                if x[3] <= 18.3999996185:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 0.8249999881:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[7] <= 0.6050000191:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 4.7400000095:
                            if time.time() < deadline:
                                if x[12] <= 697.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 13.2500000000:
                                    if time.time() < deadline:
                                        if x[7] <= 0.2699999958:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 88
    if time.time() < deadline:
        if x[0] <= 12.7950000763:
            if time.time() < deadline:
                if x[6] <= 1.2250000238:
                    if time.time() < deadline:
                        if x[9] <= 2.8999999762:
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
                if x[10] <= 0.9150000215:
                    if time.time() < deadline:
                        if x[11] <= 2.7350000143:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[8] <= 1.0250000060:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 1.2949999571:
                                    if time.time() < deadline:
                                        if x[1] <= 1.1250000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 89
    if time.time() < deadline:
        if x[6] <= 0.9749999940:
            if time.time() < deadline:
                if x[9] <= 2.8999999762:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[12] <= 755.0000000000:
                    if time.time() < deadline:
                        if x[0] <= 13.4949998856:
                            if time.time() < deadline:
                                if x[10] <= 0.6349999905:
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
                        if x[8] <= 3.0449999571:
                            if time.time() < deadline:
                                if x[3] <= 20.1999998093:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[11] <= 2.2650000453:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 90
    if time.time() < deadline:
        if x[0] <= 13.0399999619:
            if time.time() < deadline:
                if x[1] <= 2.2350000143:
                    if time.time() < deadline:
                        if x[9] <= 5.0649998188:
                            if time.time() < deadline:
                                if x[12] <= 976.0000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[6] <= 0.9949999750:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[9] <= 4.3999999762:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[3] <= 19.7500000000:
                    if time.time() < deadline:
                        if x[8] <= 0.8349999934:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[7] <= 0.5550000072:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 837.5000000000:
                            if time.time() < deadline:
                                if x[9] <= 3.8700000048:
                                    if time.time() < deadline:
                                        if x[4] <= 105.5000000000:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 91
    if time.time() < deadline:
        if x[12] <= 755.0000000000:
            if time.time() < deadline:
                if x[7] <= 0.3949999958:
                    if time.time() < deadline:
                        if x[11] <= 2.0300000310:
                            if time.time() < deadline:
                                if x[10] <= 0.9149999619:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[0] <= 13.1749997139:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[9] <= 4.0300000906:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 505.0000000000:
                            if time.time() < deadline:
                                if x[0] <= 12.7350001335:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[2] <= 2.1050000191:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 0.4849999994:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[10] <= 1.0150000155:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[5] <= 1.6500000358:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 135.5000000000:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 92
    if time.time() < deadline:
        if x[9] <= 3.8199999332:
            trees.append(1)
            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.5249999762:
                    if time.time() < deadline:
                        if x[10] <= 0.9699999988:
                            if time.time() < deadline:
                                if x[6] <= 1.5800000429:
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
                        if x[4] <= 88.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 93
    if time.time() < deadline:
        if x[10] <= 0.7849999964:
            if time.time() < deadline:
                if x[11] <= 2.3849999905:
                    trees.append(2)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[5] <= 2.3349999189:
                    if time.time() < deadline:
                        if x[6] <= 0.9099999964:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[1] <= 1.1800000072:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 611.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 135.5000000000:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 94
    if time.time() < deadline:
        if x[6] <= 1.2350000143:
            if time.time() < deadline:
                if x[1] <= 1.1149999797:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[12] <= 855.0000000000:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.5349999666:
                    if time.time() < deadline:
                        if x[9] <= 6.4249999523:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[5] <= 2.3150000572:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[4] <= 89.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[4] <= 135.5000000000:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
    
    # Tree 95
    if time.time() < deadline:
        if x[9] <= 3.8199999332:
            if time.time() < deadline:
                if x[12] <= 1002.5000000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[11] <= 2.5199999809:
                    if time.time() < deadline:
                        if x[0] <= 12.6700000763:
                            if time.time() < deadline:
                                if x[0] <= 12.6200003624:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[7] <= 0.6050000191:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[0] <= 13.1399998665:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 12.6100001335:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 96
    if time.time() < deadline:
        if x[11] <= 2.1149998903:
            if time.time() < deadline:
                if x[6] <= 1.2899999619:
                    if time.time() < deadline:
                        if x[9] <= 3.6349999905:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[10] <= 0.7049999833:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[4] <= 95.0000000000:
                    if time.time() < deadline:
                        if x[9] <= 5.3500001431:
                            if time.time() < deadline:
                                if x[12] <= 874.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 13.0199999809:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
    
    # Tree 97
    if time.time() < deadline:
        if x[9] <= 3.8199999332:
            if time.time() < deadline:
                if x[0] <= 12.8750000000:
                    trees.append(1)
                    results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 95.0000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[8] <= 0.8949999958:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[5] <= 2.0549999475:
                    if time.time() < deadline:
                        if x[3] <= 16.7500000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 0.8249999881:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[6] <= 1.2550000250:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[0] <= 13.1349997520:
                            if time.time() < deadline:
                                if x[5] <= 2.9900000095:
                                    if time.time() < deadline:
                                        if x[6] <= 1.4600000083:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[1] <= 1.4200000167:
                                            trees.append(1)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[10] <= 0.6949999928:
                                    trees.append(2)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    trees.append(0)
                                    results[0], results[1] = vote_logic(trees)
    
    # Tree 98
    if time.time() < deadline:
        if x[0] <= 12.4900002480:
            if time.time() < deadline:
                if x[11] <= 2.0700000525:
                    if time.time() < deadline:
                        if x[9] <= 3.4499999285:
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
                if x[12] <= 842.5000000000:
                    if time.time() < deadline:
                        if x[11] <= 1.8949999809:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            if time.time() < deadline:
                                if x[12] <= 517.5000000000:
                                    trees.append(1)
                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[9] <= 4.0600000620:
                                            if time.time() < deadline:
                                                if x[3] <= 21.7500000000:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[12] <= 670.0000000000:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                else:
                    trees.append(0)
                    results[0], results[1] = vote_logic(trees)
    
    # Tree 99
    if time.time() < deadline:
        if x[1] <= 2.4950000048:
            if time.time() < deadline:
                if x[12] <= 877.5000000000:
                    if time.time() < deadline:
                        if x[7] <= 0.5750000179:
                            if time.time() < deadline:
                                if x[3] <= 24.7500000000:
                                    if time.time() < deadline:
                                        if x[11] <= 1.7250000238:
                                            if time.time() < deadline:
                                                if x[1] <= 1.8349999785:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(2)
                                                    results[0], results[1] = vote_logic(trees)
                                        else:
                                            if time.time() < deadline:
                                                if x[6] <= 3.2350000143:
                                                    trees.append(1)
                                                    results[0], results[1] = vote_logic(trees)
                                                else:
                                                    trees.append(0)
                                                    results[0], results[1] = vote_logic(trees)
                                else:
                                    if time.time() < deadline:
                                        if x[6] <= 1.9950000048:
                                            trees.append(2)
                                            results[0], results[1] = vote_logic(trees)
                                        else:
                                            trees.append(0)
                                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(2)
                            results[0], results[1] = vote_logic(trees)
                else:
                    if time.time() < deadline:
                        if x[4] <= 135.5000000000:
                            trees.append(0)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
        else:
            if time.time() < deadline:
                if x[8] <= 1.6099999547:
                    if time.time() < deadline:
                        if x[5] <= 2.3849999905:
                            if time.time() < deadline:
                                if x[10] <= 1.0949999988:
                                    if time.time() < deadline:
                                        if x[2] <= 2.0850000381:
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
                        if x[4] <= 102.5000000000:
                            trees.append(1)
                            results[0], results[1] = vote_logic(trees)
                        else:
                            trees.append(0)
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
