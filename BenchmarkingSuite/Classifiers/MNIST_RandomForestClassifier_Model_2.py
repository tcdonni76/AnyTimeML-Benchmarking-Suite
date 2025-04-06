import time
"""

***** Metadata ******
Dataset: MNIST
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
        if x[457] <= 0.0098039219:
            if x[437] <= 0.0039215689:
                if x[551] <= 0.0078431377:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[351] <= 0.0470588244:
                    results.append(7)
                else:
                    results.append(3)
        else:
            if x[463] <= 0.1529411823:
                if x[434] <= 0.0196078438:
                    results.append(0)
                else:
                    results.append(9)
            else:
                if x[541] <= 0.0431372551:
                    results.append(4)
                else:
                    results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 1
    if time.time() < deadline or interrupt_flag.is_set():
        if x[155] <= 0.0019607844:
            if x[406] <= 0.2333333343:
                if x[486] <= 0.0176470596:
                    results.append(7)
                else:
                    results.append(4)
            else:
                if x[318] <= 0.0058823531:
                    results.append(1)
                else:
                    results.append(9)
        else:
            if x[378] <= 0.0196078438:
                if x[629] <= 0.3137255013:
                    results.append(2)
                else:
                    results.append(0)
            else:
                if x[437] <= 0.0039215689:
                    results.append(1)
                else:
                    results.append(3)
    
    else:
      return vote_logic(results)
    
    # Tree 2
    if time.time() < deadline or interrupt_flag.is_set():
        if x[462] <= 0.0313725499:
            if x[379] <= 0.0274509806:
                if x[181] <= 0.0078431377:
                    results.append(7)
                else:
                    results.append(0)
            else:
                if x[237] <= 0.1843137294:
                    results.append(3)
                else:
                    results.append(5)
        else:
            if x[124] <= 0.0137254908:
                if x[263] <= 0.0019607844:
                    results.append(1)
                else:
                    results.append(9)
            else:
                if x[155] <= 0.0843137279:
                    results.append(6)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 3
    if time.time() < deadline or interrupt_flag.is_set():
        if x[377] <= 0.1745098084:
            if x[154] <= 0.0058823533:
                if x[237] <= 0.0039215689:
                    results.append(4)
                else:
                    results.append(7)
            else:
                if x[386] <= 0.4470588267:
                    results.append(2)
                else:
                    results.append(0)
        else:
            if x[465] <= 0.0019607844:
                if x[373] <= 0.0137254908:
                    results.append(1)
                else:
                    results.append(5)
            else:
                if x[178] <= 0.6627451181:
                    results.append(8)
                else:
                    results.append(3)
    
    else:
      return vote_logic(results)
    
    # Tree 4
    if time.time() < deadline or interrupt_flag.is_set():
        if x[400] <= 0.0117647066:
            if x[465] <= 0.0019607844:
                if x[317] <= 0.0019607844:
                    results.append(1)
                else:
                    results.append(8)
            else:
                if x[350] <= 0.0705882367:
                    results.append(7)
                else:
                    results.append(3)
        else:
            if x[409] <= 0.0254901969:
                if x[455] <= 0.0274509815:
                    results.append(5)
                else:
                    results.append(0)
            else:
                if x[542] <= 0.4588235319:
                    results.append(4)
                else:
                    results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 5
    if time.time() < deadline or interrupt_flag.is_set():
        if x[378] <= 0.0098039219:
            if x[381] <= 0.1078431383:
                if x[568] <= 0.0333333341:
                    results.append(0)
                else:
                    results.append(0)
            else:
                if x[125] <= 0.2745098174:
                    results.append(7)
                else:
                    results.append(2)
        else:
            if x[514] <= 0.0078431377:
                if x[438] <= 0.0019607844:
                    results.append(1)
                else:
                    results.append(3)
            else:
                if x[347] <= 0.0294117657:
                    results.append(2)
                else:
                    results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 6
    if time.time() < deadline or interrupt_flag.is_set():
        if x[413] <= 0.0764705911:
            if x[262] <= 0.0019607844:
                if x[517] <= 0.4039215744:
                    results.append(3)
                else:
                    results.append(1)
            else:
                if x[403] <= 0.0647058841:
                    results.append(7)
                else:
                    results.append(8)
        else:
            if x[188] <= 0.3647058904:
                if x[624] <= 0.0137254903:
                    results.append(6)
                else:
                    results.append(0)
            else:
                if x[439] <= 0.9901960790:
                    results.append(0)
                else:
                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 7
    if time.time() < deadline or interrupt_flag.is_set():
        if x[624] <= 0.0058823533:
            if x[541] <= 0.0235294122:
                if x[458] <= 0.0058823531:
                    results.append(1)
                else:
                    results.append(9)
            else:
                if x[659] <= 0.0117647061:
                    results.append(6)
                else:
                    results.append(8)
        else:
            if x[427] <= 0.1235294156:
                if x[515] <= 0.0215686285:
                    results.append(3)
                else:
                    results.append(8)
            else:
                if x[436] <= 0.5372549146:
                    results.append(0)
                else:
                    results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 8
    if time.time() < deadline or interrupt_flag.is_set():
        if x[401] <= 0.1588235348:
            if x[348] <= 0.0039215689:
                if x[596] <= 0.0058823531:
                    results.append(1)
                else:
                    results.append(2)
            else:
                if x[494] <= 0.1901960820:
                    results.append(8)
                else:
                    results.append(3)
        else:
            if x[490] <= 0.0098039219:
                if x[378] <= 0.0117647063:
                    results.append(0)
                else:
                    results.append(5)
            else:
                if x[570] <= 0.4666666836:
                    results.append(4)
                else:
                    results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 9
    if time.time() < deadline or interrupt_flag.is_set():
        if x[381] <= 0.0019607844:
            if x[330] <= 0.0078431377:
                if x[375] <= 0.0137254908:
                    results.append(1)
                else:
                    results.append(5)
            else:
                if x[551] <= 0.0078431377:
                    results.append(7)
                else:
                    results.append(0)
        else:
            if x[155] <= 0.0156862750:
                if x[269] <= 0.2803921700:
                    results.append(4)
                else:
                    results.append(7)
            else:
                if x[102] <= 0.0156862750:
                    results.append(8)
                else:
                    results.append(6)
    
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
