import time
"""

***** Metadata ******
Dataset: CIFAR-2
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
        if x[272] <= 0.5823529661:
            if x[2563] <= 0.2254901975:
                if x[2650] <= 0.1000000015:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[2622] <= 0.3352941275:
                    results.append(1)
                else:
                    results.append(1)
        else:
            if x[1103] <= 0.3921568692:
                if x[1068] <= 0.3705882430:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[212] <= 0.6529411972:
                    results.append(1)
                else:
                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 1
    if time.time() < deadline or interrupt_flag.is_set():
        if x[74] <= 0.6137255132:
            if x[2520] <= 0.3509804010:
                if x[1520] <= 0.2431372553:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[2148] <= 0.1784313768:
                    results.append(0)
                else:
                    results.append(1)
        else:
            if x[1109] <= 0.2686274648:
                if x[2640] <= 0.2078431398:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[2361] <= 0.5941176713:
                    results.append(0)
                else:
                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 2
    if time.time() < deadline or interrupt_flag.is_set():
        if x[176] <= 0.6176470816:
            if x[2547] <= 0.2215686291:
                if x[2626] <= 0.1549019665:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[1190] <= 0.5156863034:
                    results.append(1)
                else:
                    results.append(1)
        else:
            if x[2266] <= 0.4254902005:
                if x[2029] <= 0.6764706075:
                    results.append(0)
                else:
                    results.append(0)
            else:
                if x[1478] <= 0.3509804010:
                    results.append(1)
                else:
                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 3
    if time.time() < deadline or interrupt_flag.is_set():
        if x[149] <= 0.6215686500:
            if x[2752] <= 0.1862745136:
                if x[3047] <= 0.1392156929:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[2640] <= 0.2686274648:
                    results.append(1)
                else:
                    results.append(1)
        else:
            if x[2253] <= 0.2294117659:
                if x[176] <= 0.4372549057:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[209] <= 0.4176470637:
                    results.append(1)
                else:
                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 4
    if time.time() < deadline or interrupt_flag.is_set():
        if x[143] <= 0.6529411972:
            if x[2733] <= 0.1549019665:
                if x[1481] <= 0.1313725561:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[1373] <= 0.6372549236:
                    results.append(1)
                else:
                    results.append(1)
        else:
            if x[2469] <= 0.6098039448:
                if x[1186] <= 0.2450980395:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[2358] <= 0.5352941453:
                    results.append(0)
                else:
                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 5
    if time.time() < deadline or interrupt_flag.is_set():
        if x[212] <= 0.6568627656:
            if x[2430] <= 0.3196078539:
                if x[1091] <= 0.3901960850:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[2148] <= 0.1784313768:
                    results.append(0)
                else:
                    results.append(1)
        else:
            if x[3039] <= 0.5235294402:
                if x[2218] <= 0.6215686500:
                    results.append(0)
                else:
                    results.append(0)
            else:
                if x[742] <= 0.6137255132:
                    results.append(1)
                else:
                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 6
    if time.time() < deadline or interrupt_flag.is_set():
        if x[149] <= 0.6313725710:
            if x[2823] <= 0.2019607872:
                if x[2448] <= 0.3882353008:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[2257] <= 0.1000000015:
                    results.append(0)
                else:
                    results.append(1)
        else:
            if x[1193] <= 0.4137254953:
                if x[2725] <= 0.3901960850:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[2430] <= 0.7549019754:
                    results.append(0)
                else:
                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 7
    if time.time() < deadline or interrupt_flag.is_set():
        if x[38] <= 0.5941176713:
            if x[2751] <= 0.1862745136:
                if x[907] <= 0.5392157137:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[2277] <= 0.1313725561:
                    results.append(0)
                else:
                    results.append(1)
        else:
            if x[1007] <= 0.4294117689:
                if x[2250] <= 0.3313725591:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[1635] <= 0.8058823645:
                    results.append(0)
                else:
                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 8
    if time.time() < deadline or interrupt_flag.is_set():
        if x[20] <= 0.6529411972:
            if x[2623] <= 0.1235294156:
                if x[1463] <= 0.2882353067:
                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[1652] <= 0.5352941453:
                    results.append(1)
                else:
                    results.append(1)
        else:
            if x[1010] <= 0.4019607902:
                if x[2349] <= 0.3647058904:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[2421] <= 0.7235294282:
                    results.append(0)
                else:
                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 9
    if time.time() < deadline or interrupt_flag.is_set():
        if x[38] <= 0.6019608080:
            if x[2464] <= 0.1352941245:
                if x[900] <= 0.6372549236:
                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[2835] <= 0.1156862751:
                    results.append(0)
                else:
                    results.append(1)
        else:
            if x[2373] <= 0.5509804189:
                if x[2158] <= 0.3352941275:
                    results.append(0)
                else:
                    results.append(0)
            else:
                if x[1977] <= 0.5705882609:
                    results.append(0)
                else:
                    results.append(1)
    
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
