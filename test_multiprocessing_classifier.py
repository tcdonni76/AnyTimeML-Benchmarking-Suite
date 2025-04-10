import time
"""

***** Metadata ******
Dataset: iris
Fold: 1 of K-Fold cross validaiton
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
def classifier(x, result):
    trees = []
  
# Tree 0
    if x[3] <= 0.7000000030:
      trees.append(0)
    else:
      if x[3] <= 1.6999999881:
        if x[1] <= 2.8500000238:
          if x[3] <= 1.3499999642:
            trees.append(1)
          else:
            if x[2] <= 4.9500000477:
              trees.append(1)
            else:
              if x[3] <= 1.5500000119:
                trees.append(2)
              else:
                trees.append(1)
        else:
          trees.append(1)
      else:
        if x[0] <= 5.9500000477:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 1
    if x[2] <= 2.5000000000:
      trees.append(0)
    else:
      if x[2] <= 4.8500001431:
        if x[3] <= 1.6500000358:
          trees.append(1)
        else:
          if x[2] <= 4.6500000954:
            trees.append(2)
          else:
            if x[1] <= 3.1000000238:
              trees.append(2)
            else:
              trees.append(1)
      else:
        if x[3] <= 1.7500000000:
          if x[1] <= 2.3500000238:
            trees.append(2)
          else:
            if x[1] <= 2.7500000000:
              trees.append(1)
            else:
              if x[1] <= 2.8999999762:
                trees.append(2)
              else:
                if x[2] <= 5.4000000954:
                  trees.append(1)
                else:
                  trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 2
    if x[3] <= 0.7000000030:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 5.3499999046:
          if x[1] <= 2.2500000000:
            if x[3] <= 1.2500000000:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      else:
        if x[2] <= 4.8500001431:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 3
    if x[3] <= 1.6500000358:
      if x[2] <= 2.3500000238:
        trees.append(0)
      else:
        if x[3] <= 1.3499999642:
          trees.append(1)
        else:
          if x[2] <= 5.0000000000:
            trees.append(1)
          else:
            if x[0] <= 6.0499999523:
              trees.append(1)
            else:
              trees.append(2)
    else:
      if x[2] <= 5.0499999523:
        if x[0] <= 6.5000000000:
          trees.append(2)
        else:
          trees.append(1)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 4
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[3] <= 1.6500000358:
          trees.append(1)
        else:
          trees.append(2)
      else:
        if x[2] <= 5.0499999523:
          if x[1] <= 2.7500000000:
            trees.append(2)
          else:
            if x[0] <= 6.4499998093:
              trees.append(2)
            else:
              trees.append(1)
        else:
          if x[1] <= 2.7500000000:
            if x[3] <= 1.9499999881:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 5
    if x[3] <= 1.7500000000:
      if x[2] <= 2.4499999881:
        trees.append(0)
      else:
        if x[1] <= 2.5499999523:
          if x[3] <= 1.6000000238:
            if x[2] <= 4.9500000477:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
        else:
          trees.append(1)
    else:
      if x[2] <= 4.8500001431:
        if x[0] <= 5.9500000477:
          trees.append(1)
        else:
          trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 6
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[1] <= 2.5499999523:
          if x[0] <= 4.9500000477:
            if x[2] <= 3.8999999762:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(1)
      else:
        if x[2] <= 5.2000000477:
          if x[3] <= 1.6999999881:
            if x[3] <= 1.5500000119:
              if x[2] <= 4.9500000477:
                trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 7
    if x[2] <= 2.5999999642:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[3] <= 1.6000000238:
          trees.append(1)
        else:
          trees.append(2)
      else:
        if x[2] <= 5.1499998569:
          if x[3] <= 1.7500000000:
            if x[1] <= 2.3500000238:
              trees.append(2)
            else:
              if x[2] <= 5.0499999523:
                trees.append(1)
              else:
                if x[3] <= 1.5500000119:
                  trees.append(2)
                else:
                  trees.append(1)
          else:
            if x[1] <= 3.1499999762:
              trees.append(2)
            else:
              trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 8
    if x[0] <= 5.4500000477:
      if x[2] <= 2.5999999642:
        trees.append(0)
      else:
        if x[2] <= 4.2000000477:
          trees.append(1)
        else:
          if x[3] <= 1.6000000238:
            trees.append(1)
          else:
            trees.append(2)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 2.5000000000:
          trees.append(0)
        else:
          if x[2] <= 5.0499999523:
            trees.append(1)
          else:
            if x[0] <= 6.1500000954:
              trees.append(1)
            else:
              trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 9
    if x[0] <= 5.4500000477:
      if x[2] <= 2.4499999881:
        trees.append(0)
      else:
        trees.append(1)
    else:
      if x[0] <= 7.0499999523:
        if x[3] <= 1.7500000000:
          if x[1] <= 3.7499998808:
            if x[2] <= 5.0499999523:
              if x[1] <= 2.2500000000:
                if x[3] <= 1.2500000000:
                  trees.append(1)
                else:
                  trees.append(2)
              else:
                trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(0)
        else:
          if x[2] <= 4.8500001431:
            if x[0] <= 5.9500000477:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 10
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.8500001431:
        if x[2] <= 4.7500000000:
          trees.append(1)
        else:
          if x[0] <= 6.5000000000:
            if x[0] <= 6.0499999523:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
      else:
        if x[3] <= 1.7500000000:
          if x[0] <= 6.5000000000:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 11
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[2] <= 4.9500000477:
        if x[2] <= 4.8500001431:
          trees.append(1)
        else:
          if x[1] <= 2.7500000000:
            trees.append(1)
          else:
            trees.append(2)
      else:
        if x[3] <= 1.6999999881:
          if x[1] <= 2.7500000000:
            if x[2] <= 5.0499999523:
              trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 12
    if x[2] <= 2.7499999404:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[1] <= 2.2500000000:
          if x[2] <= 4.7500000000:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[2] <= 5.0499999523:
            if x[0] <= 5.2000000477:
              trees.append(2)
            else:
              trees.append(1)
          else:
            if x[1] <= 2.7500000000:
              trees.append(1)
            else:
              trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 13
    if x[0] <= 5.5499999523:
      if x[3] <= 0.8000000119:
        trees.append(0)
      else:
        if x[3] <= 1.6000000238:
          trees.append(1)
        else:
          trees.append(2)
    else:
      if x[2] <= 4.7500000000:
        if x[2] <= 2.6000000238:
          trees.append(0)
        else:
          trees.append(1)
      else:
        if x[1] <= 2.5499999523:
          if x[3] <= 1.6999999881:
            if x[1] <= 2.3500000238:
              trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
        else:
          if x[2] <= 5.0000000000:
            if x[3] <= 1.6499999762:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 14
    if x[3] <= 0.7500000000:
      trees.append(0)
    else:
      if x[0] <= 6.7500000000:
        if x[2] <= 4.7500000000:
          if x[0] <= 4.9500000477:
            if x[2] <= 3.8999999762:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
        else:
          if x[3] <= 1.6999999881:
            if x[3] <= 1.5500000119:
              if x[2] <= 4.9500000477:
                trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(1)
          else:
            if x[1] <= 3.1499999762:
              trees.append(2)
            else:
              if x[3] <= 1.8999999762:
                trees.append(1)
              else:
                trees.append(2)
      else:
        if x[0] <= 6.9500000477:
          if x[2] <= 5.3500001431:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 15
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[3] <= 1.6500000358:
          trees.append(1)
        else:
          trees.append(2)
      else:
        if x[0] <= 6.0499999523:
          if x[1] <= 3.1000000238:
            if x[0] <= 5.9000000954:
              trees.append(2)
            else:
              if x[1] <= 2.8500000238:
                trees.append(1)
              else:
                trees.append(2)
          else:
            trees.append(1)
        else:
          if x[3] <= 1.7500000000:
            if x[0] <= 7.0499999523:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 16
    if x[0] <= 5.4500000477:
      if x[3] <= 0.8000000119:
        trees.append(0)
      else:
        if x[0] <= 4.9500000477:
          trees.append(2)
        else:
          trees.append(1)
    else:
      if x[0] <= 6.2000000477:
        if x[3] <= 1.6999999881:
          if x[3] <= 0.6000000015:
            trees.append(0)
          else:
            if x[0] <= 6.0499999523:
              trees.append(1)
            else:
              if x[2] <= 5.1499998569:
                trees.append(1)
              else:
                trees.append(2)
        else:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
      else:
        if x[2] <= 5.0499999523:
          if x[1] <= 2.7500000000:
            if x[1] <= 2.3999999762:
              trees.append(1)
            else:
              if x[3] <= 1.6499999762:
                trees.append(1)
              else:
                trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 17
    if x[2] <= 2.3500000238:
      trees.append(0)
    else:
      if x[2] <= 4.9500000477:
        if x[2] <= 4.7500000000:
          if x[1] <= 2.5499999523:
            if x[2] <= 4.4500000477:
              trees.append(1)
            else:
              if x[3] <= 1.6000000238:
                trees.append(1)
              else:
                trees.append(2)
          else:
            trees.append(1)
        else:
          if x[3] <= 1.8999999762:
            if x[1] <= 3.0499999523:
              if x[3] <= 1.6499999762:
                trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 18
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[2] <= 4.4500000477:
          trees.append(1)
        else:
          if x[3] <= 1.6500000358:
            trees.append(1)
          else:
            trees.append(2)
      else:
        if x[2] <= 5.1499998569:
          if x[3] <= 1.7500000000:
            if x[3] <= 1.5500000119:
              if x[2] <= 5.0000000000:
                trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 19
    if x[0] <= 5.4500000477:
      if x[3] <= 0.7500000000:
        trees.append(0)
      else:
        if x[3] <= 1.5500000119:
          trees.append(1)
        else:
          trees.append(2)
    else:
      if x[3] <= 1.7500000000:
        if x[3] <= 0.7000000030:
          trees.append(0)
        else:
          if x[3] <= 1.3499999642:
            trees.append(1)
          else:
            if x[2] <= 5.0499999523:
              trees.append(1)
            else:
              if x[3] <= 1.5500000119:
                trees.append(2)
              else:
                trees.append(1)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 20
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[3] <= 1.6500000358:
        if x[1] <= 2.2500000000:
          if x[0] <= 6.0999999046:
            trees.append(2)
          else:
            trees.append(1)
        else:
          if x[2] <= 5.3499999046:
            trees.append(1)
          else:
            trees.append(2)
      else:
        if x[3] <= 1.8499999642:
          if x[1] <= 3.1499999762:
            trees.append(2)
          else:
            if x[0] <= 6.5499999523:
              trees.append(1)
            else:
              trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 21
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[2] <= 4.9500000477:
        if x[0] <= 4.9500000477:
          if x[3] <= 1.3500000238:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[0] <= 5.9000000954:
            trees.append(1)
          else:
            if x[3] <= 1.6999999881:
              trees.append(1)
            else:
              trees.append(2)
      else:
        if x[2] <= 5.1499998569:
          if x[3] <= 1.8000000119:
            if x[3] <= 1.5500000119:
              trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 22
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[3] <= 1.6500000358:
        if x[3] <= 1.5500000119:
          if x[2] <= 5.0000000000:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[0] <= 6.5999999046:
            trees.append(1)
          else:
            trees.append(2)
      else:
        if x[2] <= 4.8500001431:
          if x[3] <= 1.7500000000:
            trees.append(2)
          else:
            if x[1] <= 3.1000000238:
              trees.append(2)
            else:
              trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 23
    if x[3] <= 1.6999999881:
      if x[3] <= 0.7500000000:
        trees.append(0)
      else:
        if x[2] <= 5.3499999046:
          trees.append(1)
        else:
          trees.append(2)
    else:
      trees.append(2)
      result = vote_logic(trees)
  
# Tree 24
    if x[3] <= 0.7500000000:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 4.9500000477:
          if x[0] <= 5.0499999523:
            trees.append(2)
          else:
            trees.append(1)
        else:
          if x[3] <= 1.5500000119:
            trees.append(2)
          else:
            trees.append(1)
      else:
        if x[0] <= 5.9500000477:
          if x[2] <= 4.8500001431:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 25
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[3] <= 1.5500000119:
          if x[2] <= 4.9500000477:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[1] <= 2.7500000000:
            trees.append(2)
          else:
            if x[2] <= 5.4000000954:
              trees.append(1)
            else:
              trees.append(2)
      else:
        if x[0] <= 5.9500000477:
          if x[2] <= 4.8500001431:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 26
    if x[0] <= 5.5499999523:
      if x[2] <= 2.4499999881:
        trees.append(0)
      else:
        if x[3] <= 1.6000000238:
          trees.append(1)
        else:
          trees.append(2)
    else:
      if x[3] <= 1.7500000000:
        if x[3] <= 0.6500000060:
          trees.append(0)
        else:
          if x[2] <= 4.9500000477:
            trees.append(1)
          else:
            if x[1] <= 2.4500000477:
              trees.append(2)
            else:
              if x[1] <= 2.7500000000:
                trees.append(1)
              else:
                if x[3] <= 1.6500000358:
                  trees.append(2)
                else:
                  trees.append(1)
      else:
        if x[2] <= 4.8500001431:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 27
    if x[0] <= 5.7500000000:
      if x[3] <= 0.8000000119:
        trees.append(0)
      else:
        if x[2] <= 4.7000000477:
          trees.append(1)
        else:
          trees.append(2)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 5.0499999523:
          trees.append(1)
        else:
          trees.append(2)
      else:
        if x[2] <= 4.9000000954:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 28
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.9500000477:
        if x[0] <= 6.0499999523:
          trees.append(1)
        else:
          if x[0] <= 6.2500000000:
            if x[2] <= 4.7000000477:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 29
    if x[3] <= 0.7000000030:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 4.9500000477:
          if x[0] <= 4.9500000477:
            if x[3] <= 1.3500000238:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
        else:
          if x[1] <= 2.6499999762:
            trees.append(2)
          else:
            trees.append(1)
      else:
        if x[2] <= 4.8500001431:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 30
    if x[3] <= 0.7500000000:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[3] <= 1.6500000358:
          trees.append(1)
        else:
          trees.append(2)
      else:
        if x[3] <= 1.7500000000:
          if x[1] <= 2.3500000238:
            trees.append(2)
          else:
            if x[0] <= 6.1500000954:
              trees.append(1)
            else:
              if x[2] <= 5.0499999523:
                trees.append(1)
              else:
                trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 31
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[3] <= 1.6500000358:
        if x[2] <= 4.9500000477:
          trees.append(1)
        else:
          if x[1] <= 2.6499999762:
            trees.append(2)
          else:
            if x[2] <= 5.4500000477:
              if x[0] <= 6.1500000954:
                trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 32
    if x[3] <= 0.7500000000:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[3] <= 1.3499999642:
          trees.append(1)
        else:
          if x[2] <= 5.0499999523:
            if x[1] <= 2.6499999762:
              if x[0] <= 5.5499999523:
                trees.append(2)
              else:
                trees.append(1)
            else:
              trees.append(1)
          else:
            trees.append(2)
      else:
        if x[2] <= 4.8500001431:
          if x[1] <= 3.0000000000:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 33
    if x[3] <= 0.7500000000:
      trees.append(0)
    else:
      if x[3] <= 1.6500000358:
        if x[2] <= 4.9500000477:
          trees.append(1)
        else:
          if x[3] <= 1.5500000119:
            trees.append(2)
          else:
            trees.append(1)
      else:
        if x[3] <= 1.7500000000:
          if x[2] <= 4.7500000000:
            trees.append(2)
          else:
            trees.append(1)
        else:
          if x[2] <= 4.8500001431:
            if x[1] <= 3.0000000000:
              trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 34
    if x[0] <= 5.4500000477:
      if x[3] <= 0.8000000119:
        trees.append(0)
      else:
        trees.append(1)
    else:
      if x[2] <= 4.7500000000:
        if x[3] <= 0.6500000060:
          trees.append(0)
        else:
          trees.append(1)
      else:
        if x[2] <= 4.9500000477:
          if x[1] <= 3.0499999523:
            if x[0] <= 6.5000000000:
              trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(1)
        else:
          if x[3] <= 1.6999999881:
            if x[2] <= 5.3499999046:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 35
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[2] <= 5.0499999523:
        if x[2] <= 4.7500000000:
          trees.append(1)
        else:
          if x[3] <= 1.8999999762:
            if x[1] <= 3.0499999523:
              if x[0] <= 6.3499999046:
                trees.append(2)
              else:
                trees.append(1)
            else:
              trees.append(1)
          else:
            trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 36
    if x[2] <= 2.3500000238:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        trees.append(1)
      else:
        if x[2] <= 4.9500000477:
          if x[0] <= 6.5000000000:
            if x[0] <= 5.9500000477:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
        else:
          if x[2] <= 5.1499998569:
            if x[3] <= 1.8000000119:
              if x[3] <= 1.5500000119:
                trees.append(2)
              else:
                trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 37
    if x[0] <= 5.4500000477:
      if x[3] <= 0.8000000119:
        trees.append(0)
      else:
        if x[3] <= 1.5500000119:
          trees.append(1)
        else:
          trees.append(2)
    else:
      if x[2] <= 4.7500000000:
        if x[2] <= 2.6499999762:
          trees.append(0)
        else:
          trees.append(1)
      else:
        if x[2] <= 4.9500000477:
          if x[1] <= 3.0499999523:
            trees.append(2)
          else:
            trees.append(1)
        else:
          if x[3] <= 1.6999999881:
            if x[3] <= 1.5500000119:
              trees.append(2)
            else:
              if x[0] <= 6.5999999046:
                trees.append(1)
              else:
                trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 38
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        trees.append(1)
      else:
        if x[1] <= 2.6000000238:
          if x[3] <= 1.6499999762:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[2] <= 5.1499998569:
            if x[3] <= 1.6999999881:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 39
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 4.9500000477:
          trees.append(1)
        else:
          if x[1] <= 2.8999999762:
            trees.append(2)
          else:
            if x[0] <= 6.9499998093:
              trees.append(1)
            else:
              trees.append(2)
      else:
        if x[2] <= 4.8500001431:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 40
    if x[2] <= 2.5999999642:
      trees.append(0)
    else:
      if x[0] <= 6.1499998569:
        if x[2] <= 4.7500000000:
          if x[0] <= 4.9500000477:
            if x[2] <= 3.8999999762:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      else:
        if x[0] <= 6.7500000000:
          if x[0] <= 6.3500001431:
            if x[3] <= 1.6999999881:
              if x[1] <= 2.6499999762:
                trees.append(1)
              else:
                if x[1] <= 3.0499999523:
                  trees.append(2)
                else:
                  trees.append(1)
            else:
              trees.append(2)
          else:
            if x[2] <= 5.1500000954:
              trees.append(1)
            else:
              trees.append(2)
        else:
          if x[2] <= 4.9500000477:
            trees.append(1)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 41
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[3] <= 1.6999999881:
        if x[1] <= 2.2500000000:
          if x[2] <= 4.5000000000:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[2] <= 5.4500000477:
            if x[2] <= 5.0000000000:
              trees.append(1)
            else:
              if x[0] <= 6.1500000954:
                trees.append(1)
              else:
                trees.append(2)
          else:
            trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 42
    if x[2] <= 2.5999999642:
      trees.append(0)
    else:
      if x[2] <= 4.8500001431:
        if x[2] <= 4.7500000000:
          trees.append(1)
        else:
          if x[0] <= 6.5000000000:
            trees.append(2)
          else:
            trees.append(1)
      else:
        if x[3] <= 1.6999999881:
          if x[3] <= 1.5500000119:
            if x[0] <= 6.6000001431:
              trees.append(2)
            else:
              trees.append(1)
          else:
            if x[2] <= 5.4500000477:
              trees.append(1)
            else:
              trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 43
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 5.2999999523:
          if x[3] <= 1.6500000358:
            trees.append(1)
          else:
            if x[1] <= 2.7500000000:
              trees.append(2)
            else:
              trees.append(1)
        else:
          trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 44
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.9500000477:
        if x[0] <= 6.1499998569:
          if x[1] <= 2.7500000000:
            trees.append(1)
          else:
            if x[3] <= 1.8999999762:
              trees.append(1)
            else:
              trees.append(2)
        else:
          if x[2] <= 4.7500000000:
            trees.append(1)
          else:
            if x[3] <= 1.6499999762:
              trees.append(1)
            else:
              trees.append(2)
      else:
        if x[3] <= 1.6999999881:
          if x[3] <= 1.5500000119:
            trees.append(2)
          else:
            if x[0] <= 6.5999999046:
              trees.append(1)
            else:
              trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 45
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[0] <= 6.6499998569:
        if x[2] <= 4.7500000000:
          if x[3] <= 1.6500000358:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[0] <= 6.0499999523:
            if x[1] <= 3.1000000238:
              if x[0] <= 5.9000000954:
                trees.append(2)
              else:
                if x[3] <= 1.6999999881:
                  trees.append(1)
                else:
                  trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
      else:
        if x[2] <= 5.0499999523:
          trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 46
    if x[3] <= 0.7500000000:
      trees.append(0)
    else:
      if x[2] <= 4.9500000477:
        if x[3] <= 1.6500000358:
          trees.append(1)
        else:
          if x[1] <= 2.9500000477:
            trees.append(2)
          else:
            trees.append(1)
      else:
        if x[0] <= 6.0499999523:
          if x[0] <= 5.9000000954:
            trees.append(2)
          else:
            if x[2] <= 5.0499999523:
              trees.append(2)
            else:
              trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 47
    if x[0] <= 5.4500000477:
      if x[3] <= 0.7500000000:
        trees.append(0)
      else:
        trees.append(1)
    else:
      if x[2] <= 4.9500000477:
        if x[3] <= 0.7000000030:
          trees.append(0)
        else:
          if x[2] <= 4.7500000000:
            trees.append(1)
          else:
            if x[3] <= 1.6499999762:
              trees.append(1)
            else:
              if x[1] <= 3.1000000238:
                trees.append(2)
              else:
                trees.append(1)
      else:
        if x[3] <= 1.7500000000:
          if x[3] <= 1.5500000119:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 48
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[0] <= 6.1499998569:
        if x[3] <= 1.6500000358:
          if x[3] <= 1.3499999642:
            trees.append(1)
          else:
            if x[1] <= 2.6499999762:
              trees.append(2)
            else:
              trees.append(1)
        else:
          if x[2] <= 4.8500001431:
            if x[1] <= 3.1000000238:
              trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
      else:
        if x[3] <= 1.7500000000:
          if x[0] <= 6.3500001431:
            if x[1] <= 2.8500000238:
              trees.append(2)
            else:
              trees.append(1)
          else:
            if x[2] <= 5.4000000954:
              trees.append(1)
            else:
              trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 49
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[3] <= 1.6500000358:
          if x[1] <= 2.2500000000:
            if x[2] <= 4.7500000000:
              trees.append(1)
            else:
              trees.append(2)
          else:
            if x[2] <= 5.0000000000:
              trees.append(1)
            else:
              trees.append(2)
        else:
          if x[1] <= 2.7500000000:
            trees.append(2)
          else:
            trees.append(1)
      else:
        if x[2] <= 4.9000000954:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 50
    if x[2] <= 4.7500000000:
      if x[2] <= 2.5000000000:
        trees.append(0)
      else:
        trees.append(1)
    else:
      if x[2] <= 5.0499999523:
        if x[3] <= 1.7500000000:
          if x[2] <= 4.9500000477:
            trees.append(1)
          else:
            if x[3] <= 1.6000000238:
              trees.append(2)
            else:
              trees.append(1)
        else:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
      else:
        if x[1] <= 2.7500000000:
          if x[3] <= 1.6999999881:
            if x[2] <= 5.3499999046:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 51
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 5.0499999523:
        if x[3] <= 1.7500000000:
          trees.append(1)
        else:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 52
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[0] <= 4.9500000477:
          if x[3] <= 1.3500000238:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(1)
      else:
        if x[1] <= 2.7500000000:
          if x[3] <= 1.7500000000:
            if x[3] <= 1.4499999881:
              trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
        else:
          if x[2] <= 5.0000000000:
            if x[3] <= 1.6499999762:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 53
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[0] <= 6.1499998569:
        if x[2] <= 4.7500000000:
          if x[3] <= 1.6500000358:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[2] <= 5.0499999523:
            trees.append(2)
          else:
            if x[3] <= 1.6999999881:
              trees.append(1)
            else:
              trees.append(2)
      else:
        if x[2] <= 4.9500000477:
          if x[3] <= 1.6499999762:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[3] <= 1.7500000000:
            if x[2] <= 5.4000000954:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 54
    if x[0] <= 5.4500000477:
      if x[2] <= 2.5999999642:
        trees.append(0)
      else:
        trees.append(1)
    else:
      if x[2] <= 4.7500000000:
        if x[2] <= 2.6000000238:
          trees.append(0)
        else:
          trees.append(1)
      else:
        if x[2] <= 5.2500000000:
          if x[1] <= 2.7500000000:
            if x[3] <= 1.6999999881:
              if x[1] <= 2.3500000238:
                trees.append(2)
              else:
                trees.append(1)
            else:
              trees.append(2)
          else:
            if x[3] <= 1.7500000000:
              trees.append(1)
            else:
              if x[1] <= 3.1499999762:
                trees.append(2)
              else:
                if x[0] <= 6.2000000477:
                  trees.append(1)
                else:
                  trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 55
    if x[0] <= 5.4500000477:
      if x[3] <= 0.8000000119:
        trees.append(0)
      else:
        if x[0] <= 4.9500000477:
          trees.append(2)
        else:
          trees.append(1)
    else:
      if x[3] <= 1.6999999881:
        if x[1] <= 3.7999999523:
          if x[2] <= 5.4500000477:
            if x[2] <= 4.9500000477:
              trees.append(1)
            else:
              if x[2] <= 5.0499999523:
                trees.append(2)
              else:
                trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(0)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 56
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[3] <= 1.3499999642:
          trees.append(1)
        else:
          if x[2] <= 5.0499999523:
            if x[0] <= 5.0499999523:
              trees.append(2)
            else:
              if x[2] <= 4.8499999046:
                trees.append(1)
              else:
                if x[0] <= 6.3499999046:
                  trees.append(2)
                else:
                  trees.append(1)
          else:
            trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 57
    if x[0] <= 5.5499999523:
      if x[2] <= 2.4499999881:
        trees.append(0)
      else:
        trees.append(1)
    else:
      if x[0] <= 6.0499999523:
        if x[3] <= 0.7000000030:
          trees.append(0)
        else:
          if x[1] <= 2.6000000238:
            trees.append(2)
          else:
            if x[2] <= 4.6500000954:
              trees.append(1)
            else:
              if x[1] <= 2.7500000000:
                trees.append(1)
              else:
                if x[1] <= 3.1000000238:
                  trees.append(2)
                else:
                  trees.append(1)
      else:
        if x[2] <= 5.0000000000:
          if x[2] <= 4.7500000000:
            trees.append(1)
          else:
            if x[3] <= 1.6499999762:
              trees.append(1)
            else:
              trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 58
    if x[3] <= 0.7500000000:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 4.9500000477:
          trees.append(1)
        else:
          if x[1] <= 2.6499999762:
            trees.append(2)
          else:
            if x[2] <= 5.0499999523:
              trees.append(1)
            else:
              if x[0] <= 6.1500000954:
                trees.append(1)
              else:
                trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 59
    if x[0] <= 5.7500000000:
      if x[2] <= 2.5999999642:
        trees.append(0)
      else:
        if x[0] <= 5.6499998569:
          trees.append(1)
        else:
          if x[2] <= 4.7500000000:
            trees.append(1)
          else:
            trees.append(2)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 5.0499999523:
          trees.append(1)
        else:
          if x[3] <= 1.5500000119:
            trees.append(2)
          else:
            if x[1] <= 2.8500000238:
              trees.append(1)
            else:
              trees.append(2)
      else:
        if x[1] <= 3.1499999762:
          trees.append(2)
        else:
          if x[2] <= 4.9500000477:
            trees.append(1)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 60
    if x[0] <= 5.4500000477:
      if x[2] <= 2.5999999642:
        trees.append(0)
      else:
        if x[2] <= 4.2000000477:
          trees.append(1)
        else:
          trees.append(2)
    else:
      if x[2] <= 4.7500000000:
        if x[1] <= 3.6000000238:
          trees.append(1)
        else:
          trees.append(0)
      else:
        if x[2] <= 5.0499999523:
          if x[1] <= 3.1000000238:
            if x[3] <= 1.7500000000:
              if x[0] <= 6.1500000954:
                trees.append(2)
              else:
                trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 61
    if x[3] <= 0.7000000030:
      trees.append(0)
    else:
      if x[0] <= 6.0499999523:
        if x[3] <= 2.1000000238:
          if x[2] <= 4.6500000954:
            trees.append(1)
          else:
            if x[1] <= 3.1000000238:
              if x[2] <= 5.0499999523:
                trees.append(2)
              else:
                trees.append(1)
            else:
              trees.append(1)
        else:
          trees.append(2)
      else:
        if x[3] <= 1.7500000000:
          if x[2] <= 5.2999999523:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 62
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[0] <= 4.9500000477:
          if x[3] <= 1.3500000238:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(1)
      else:
        if x[3] <= 1.7500000000:
          if x[0] <= 6.5000000000:
            if x[1] <= 2.6499999762:
              trees.append(2)
            else:
              if x[1] <= 2.7500000000:
                trees.append(1)
              else:
                trees.append(2)
          else:
            if x[0] <= 7.0499999523:
              trees.append(1)
            else:
              trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 63
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 5.0499999523:
          trees.append(1)
        else:
          trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 64
    if x[3] <= 1.7500000000:
      if x[3] <= 0.8000000119:
        trees.append(0)
      else:
        if x[1] <= 2.6499999762:
          if x[1] <= 2.5499999523:
            if x[0] <= 4.9500000477:
              if x[1] <= 2.4500000477:
                trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(1)
          else:
            if x[3] <= 1.3000000119:
              trees.append(1)
            else:
              trees.append(2)
        else:
          trees.append(1)
    else:
      trees.append(2)
      result = vote_logic(trees)
  
# Tree 65
    if x[2] <= 2.5999999642:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[3] <= 1.6500000358:
          trees.append(1)
        else:
          trees.append(2)
      else:
        if x[3] <= 1.7500000000:
          if x[2] <= 5.0499999523:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 66
    if x[2] <= 4.8500001431:
      if x[3] <= 0.8000000119:
        trees.append(0)
      else:
        if x[3] <= 1.6999999881:
          trees.append(1)
        else:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
    else:
      if x[2] <= 4.9500000477:
        if x[3] <= 1.6499999762:
          trees.append(1)
        else:
          trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 67
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[3] <= 1.6500000358:
        if x[0] <= 5.9500000477:
          trees.append(1)
        else:
          if x[1] <= 2.6499999762:
            if x[1] <= 2.4499999285:
              if x[2] <= 4.7500000000:
                trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(2)
          else:
            if x[3] <= 1.4499999881:
              trees.append(1)
            else:
              if x[1] <= 2.8500000238:
                if x[1] <= 2.7500000000:
                  trees.append(1)
                else:
                  trees.append(2)
              else:
                trees.append(1)
      else:
        if x[0] <= 5.9500000477:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
        else:
          if x[0] <= 6.5999999046:
            trees.append(2)
          else:
            if x[2] <= 5.0499999523:
              trees.append(1)
            else:
              trees.append(2)
      result = vote_logic(trees)
  
# Tree 68
    if x[3] <= 0.7500000000:
      trees.append(0)
    else:
      if x[2] <= 4.9500000477:
        if x[3] <= 1.6999999881:
          trees.append(1)
        else:
          if x[2] <= 4.8500001431:
            if x[1] <= 3.1000000238:
              trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
      else:
        if x[3] <= 1.6999999881:
          if x[0] <= 6.0499999523:
            if x[2] <= 5.0499999523:
              trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 69
    if x[0] <= 5.4500000477:
      if x[3] <= 0.8000000119:
        trees.append(0)
      else:
        if x[2] <= 4.2000000477:
          trees.append(1)
        else:
          trees.append(2)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 2.5000000000:
          trees.append(0)
        else:
          if x[2] <= 5.0499999523:
            trees.append(1)
          else:
            if x[1] <= 2.7500000000:
              trees.append(1)
            else:
              trees.append(2)
      else:
        if x[0] <= 6.0000000000:
          if x[0] <= 5.8500001431:
            trees.append(2)
          else:
            if x[1] <= 3.1000000238:
              trees.append(2)
            else:
              trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 70
    if x[2] <= 2.5999999642:
      trees.append(0)
    else:
      if x[0] <= 7.0499999523:
        if x[3] <= 1.6500000358:
          if x[2] <= 4.9500000477:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[0] <= 6.5999999046:
            trees.append(2)
          else:
            if x[1] <= 3.0499999523:
              if x[3] <= 2.0000000000:
                trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 71
    if x[0] <= 5.4500000477:
      if x[1] <= 2.8000000715:
        if x[0] <= 4.7000000477:
          trees.append(0)
        else:
          trees.append(1)
      else:
        trees.append(0)
    else:
      if x[0] <= 5.9500000477:
        if x[3] <= 1.6499999762:
          if x[3] <= 0.7000000030:
            trees.append(0)
          else:
            trees.append(1)
        else:
          trees.append(2)
      else:
        if x[2] <= 4.9500000477:
          if x[3] <= 1.6999999881:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[2] <= 5.1499998569:
            if x[2] <= 5.0499999523:
              trees.append(2)
            else:
              if x[0] <= 6.1500000954:
                trees.append(1)
              else:
                trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 72
    if x[0] <= 5.4500000477:
      if x[2] <= 2.3500000238:
        trees.append(0)
      else:
        trees.append(1)
    else:
      if x[3] <= 1.7500000000:
        if x[1] <= 3.3500000238:
          if x[2] <= 5.0499999523:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(0)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 73
    if x[0] <= 5.4500000477:
      if x[2] <= 2.4499999881:
        trees.append(0)
      else:
        trees.append(1)
    else:
      if x[3] <= 1.6999999881:
        if x[3] <= 0.6500000060:
          trees.append(0)
        else:
          if x[0] <= 7.0499999523:
            if x[3] <= 1.3499999642:
              trees.append(1)
            else:
              if x[2] <= 4.9500000477:
                trees.append(1)
              else:
                if x[1] <= 2.6499999762:
                  trees.append(2)
                else:
                  if x[1] <= 2.7500000000:
                    trees.append(1)
                  else:
                    trees.append(2)
          else:
            trees.append(2)
      else:
        if x[0] <= 5.9500000477:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 74
    if x[0] <= 5.5499999523:
      if x[2] <= 2.4499999881:
        trees.append(0)
      else:
        if x[0] <= 4.9500000477:
          trees.append(2)
        else:
          trees.append(1)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 5.4500000477:
          if x[1] <= 3.7000000477:
            if x[2] <= 5.0499999523:
              trees.append(1)
            else:
              if x[1] <= 2.7500000000:
                trees.append(1)
              else:
                trees.append(2)
          else:
            trees.append(0)
        else:
          trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 75
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[3] <= 1.6500000358:
        if x[2] <= 4.9500000477:
          trees.append(1)
        else:
          trees.append(2)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 76
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[0] <= 6.8500001431:
        if x[0] <= 6.0499999523:
          if x[0] <= 4.9500000477:
            trees.append(2)
          else:
            if x[3] <= 1.6999999881:
              trees.append(1)
            else:
              if x[2] <= 4.8500001431:
                trees.append(1)
              else:
                trees.append(2)
        else:
          if x[3] <= 1.6999999881:
            if x[2] <= 5.2500000000:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      else:
        if x[0] <= 7.0499999523:
          if x[0] <= 6.9500000477:
            if x[3] <= 1.8999999762:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 77
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[0] <= 5.7500000000:
        if x[3] <= 1.7500000000:
          trees.append(1)
        else:
          trees.append(2)
      else:
        if x[2] <= 5.0499999523:
          if x[2] <= 4.7500000000:
            trees.append(1)
          else:
            if x[0] <= 6.5000000000:
              if x[2] <= 4.8500001431:
                if x[1] <= 3.1000000238:
                  trees.append(2)
                else:
                  trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(1)
        else:
          if x[0] <= 6.0999999046:
            if x[0] <= 5.9000000954:
              trees.append(2)
            else:
              trees.append(1)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 78
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[3] <= 1.6999999881:
        if x[1] <= 2.6499999762:
          if x[2] <= 5.2500000000:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(1)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 79
    if x[3] <= 1.6500000358:
      if x[2] <= 2.5999999642:
        trees.append(0)
      else:
        if x[2] <= 4.9500000477:
          trees.append(1)
        else:
          trees.append(2)
    else:
      trees.append(2)
      result = vote_logic(trees)
  
# Tree 80
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[0] <= 6.2500000000:
        if x[3] <= 1.6500000358:
          if x[1] <= 2.3000000715:
            if x[3] <= 1.2500000000:
              trees.append(1)
            else:
              if x[2] <= 4.7500000000:
                trees.append(1)
              else:
                trees.append(2)
          else:
            trees.append(1)
        else:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            if x[3] <= 2.0499999523:
              trees.append(1)
            else:
              trees.append(2)
      else:
        if x[2] <= 5.0499999523:
          if x[3] <= 1.7500000000:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 81
    if x[0] <= 5.4500000477:
      if x[3] <= 0.8000000119:
        trees.append(0)
      else:
        if x[3] <= 1.6000000238:
          trees.append(1)
        else:
          trees.append(2)
    else:
      if x[2] <= 4.7500000000:
        if x[3] <= 0.7000000030:
          trees.append(0)
        else:
          trees.append(1)
      else:
        if x[3] <= 1.7500000000:
          if x[1] <= 2.6499999762:
            trees.append(2)
          else:
            if x[1] <= 2.7500000000:
              trees.append(1)
            else:
              if x[2] <= 5.0499999523:
                trees.append(1)
              else:
                trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 82
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        trees.append(1)
      else:
        if x[2] <= 4.9500000477:
          if x[1] <= 2.6000000238:
            trees.append(1)
          else:
            if x[1] <= 3.0499999523:
              if x[3] <= 1.5999999642:
                trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 83
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[2] <= 4.8500001431:
        if x[0] <= 4.9500000477:
          trees.append(2)
        else:
          if x[3] <= 1.6999999881:
            trees.append(1)
          else:
            trees.append(2)
      else:
        if x[3] <= 1.7500000000:
          if x[2] <= 5.3499999046:
            if x[2] <= 5.0499999523:
              trees.append(1)
            else:
              if x[1] <= 2.7500000000:
                trees.append(1)
              else:
                trees.append(2)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 84
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 5.0499999523:
          if x[0] <= 4.9500000477:
            trees.append(2)
          else:
            if x[1] <= 2.2500000000:
              if x[3] <= 1.2500000000:
                trees.append(1)
              else:
                if x[2] <= 4.7500000000:
                  trees.append(1)
                else:
                  trees.append(2)
            else:
              trees.append(1)
        else:
          if x[3] <= 1.5500000119:
            trees.append(2)
          else:
            trees.append(1)
      else:
        if x[0] <= 6.0499999523:
          if x[3] <= 1.8499999642:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 85
    if x[3] <= 0.7500000000:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        trees.append(1)
      else:
        if x[2] <= 4.9500000477:
          if x[3] <= 1.6499999762:
            trees.append(1)
          else:
            if x[0] <= 6.0000000000:
              trees.append(1)
            else:
              trees.append(2)
        else:
          if x[3] <= 1.6999999881:
            if x[0] <= 6.0499999523:
              if x[2] <= 5.0499999523:
                trees.append(2)
              else:
                trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 86
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        trees.append(1)
      else:
        if x[2] <= 5.2000000477:
          if x[0] <= 6.5999999046:
            if x[3] <= 1.6999999881:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 87
    if x[3] <= 0.7000000030:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[3] <= 1.6500000358:
          trees.append(1)
        else:
          trees.append(2)
      else:
        if x[3] <= 1.6999999881:
          if x[2] <= 4.9500000477:
            trees.append(1)
          else:
            if x[3] <= 1.5500000119:
              trees.append(2)
            else:
              trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 88
    if x[0] <= 5.4500000477:
      if x[3] <= 0.7500000000:
        trees.append(0)
      else:
        trees.append(1)
    else:
      if x[3] <= 1.5500000119:
        if x[1] <= 3.5000000000:
          if x[2] <= 5.0000000000:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(0)
      else:
        if x[2] <= 4.7500000000:
          trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 89
    if x[0] <= 5.4500000477:
      if x[1] <= 2.8500000238:
        if x[1] <= 2.3500000238:
          trees.append(0)
        else:
          if x[2] <= 4.2000000477:
            trees.append(1)
          else:
            trees.append(2)
      else:
        trees.append(0)
    else:
      if x[2] <= 4.8500001431:
        if x[3] <= 0.7000000030:
          trees.append(0)
        else:
          if x[2] <= 4.7500000000:
            trees.append(1)
          else:
            if x[3] <= 1.5999999642:
              trees.append(1)
            else:
              if x[1] <= 3.1000000238:
                trees.append(2)
              else:
                trees.append(1)
      else:
        if x[2] <= 5.0499999523:
          if x[0] <= 6.3999998569:
            trees.append(2)
          else:
            trees.append(1)
        else:
          if x[3] <= 1.6999999881:
            if x[3] <= 1.5000000000:
              trees.append(2)
            else:
              if x[2] <= 5.4500000477:
                trees.append(1)
              else:
                trees.append(2)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
# Tree 90
    if x[2] <= 2.5999999642:
      trees.append(0)
    else:
      if x[2] <= 5.0499999523:
        if x[2] <= 4.7500000000:
          if x[2] <= 4.4500000477:
            trees.append(1)
          else:
            if x[1] <= 2.6499999762:
              trees.append(2)
            else:
              trees.append(1)
        else:
          if x[1] <= 3.0499999523:
            if x[3] <= 1.7500000000:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 91
    if x[2] <= 2.5999999642:
      trees.append(0)
    else:
      if x[2] <= 4.8500001431:
        if x[3] <= 1.6500000358:
          trees.append(1)
        else:
          if x[1] <= 3.1000000238:
            trees.append(2)
          else:
            trees.append(1)
      else:
        if x[2] <= 5.1499998569:
          if x[1] <= 2.8999999762:
            if x[0] <= 5.9000000954:
              trees.append(2)
            else:
              if x[2] <= 5.0499999523:
                trees.append(2)
              else:
                if x[3] <= 1.5500000119:
                  trees.append(2)
                else:
                  trees.append(1)
          else:
            if x[2] <= 5.0499999523:
              if x[3] <= 1.7500000000:
                trees.append(1)
              else:
                trees.append(2)
            else:
              trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 92
    if x[3] <= 0.7000000030:
      trees.append(0)
    else:
      if x[3] <= 1.7500000000:
        if x[2] <= 5.3499999046:
          if x[2] <= 4.9000000954:
            trees.append(1)
          else:
            if x[1] <= 2.4500000477:
              trees.append(2)
            else:
              trees.append(1)
        else:
          trees.append(2)
      else:
        if x[2] <= 4.8500001431:
          if x[0] <= 5.9500000477:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 93
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[0] <= 6.6499998569:
        if x[2] <= 4.7999999523:
          if x[2] <= 4.4500000477:
            trees.append(1)
          else:
            if x[0] <= 5.1500000954:
              trees.append(2)
            else:
              trees.append(1)
        else:
          if x[2] <= 5.1499998569:
            if x[0] <= 5.9000000954:
              trees.append(2)
            else:
              if x[1] <= 2.6000000238:
                if x[2] <= 4.9500000477:
                  trees.append(1)
                else:
                  trees.append(2)
              else:
                trees.append(1)
          else:
            trees.append(2)
      else:
        if x[2] <= 5.0999999046:
          trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 94
    if x[2] <= 4.9500000477:
      if x[3] <= 0.7000000030:
        trees.append(0)
      else:
        if x[3] <= 1.6500000358:
          trees.append(1)
        else:
          if x[0] <= 5.7500000000:
            trees.append(2)
          else:
            trees.append(1)
    else:
      if x[0] <= 6.0499999523:
        if x[1] <= 2.6000000238:
          trees.append(2)
        else:
          if x[0] <= 5.9000000954:
            trees.append(2)
          else:
            trees.append(1)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 95
    if x[2] <= 2.7499999404:
      trees.append(0)
    else:
      if x[0] <= 6.2500000000:
        if x[2] <= 4.7500000000:
          if x[3] <= 1.6500000358:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[1] <= 3.1000000238:
            if x[0] <= 5.9500000477:
              trees.append(2)
            else:
              if x[0] <= 6.0499999523:
                if x[3] <= 1.6999999881:
                  trees.append(1)
                else:
                  trees.append(2)
              else:
                trees.append(2)
          else:
            trees.append(1)
      else:
        if x[3] <= 1.7500000000:
          if x[0] <= 7.0499999523:
            if x[2] <= 5.0499999523:
              trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(2)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 96
    if x[2] <= 2.4499999881:
      trees.append(0)
    else:
      if x[2] <= 4.7500000000:
        if x[1] <= 2.5499999523:
          if x[3] <= 1.5000000000:
            trees.append(1)
          else:
            trees.append(2)
        else:
          trees.append(1)
      else:
        if x[2] <= 5.0499999523:
          if x[1] <= 3.0499999523:
            if x[3] <= 1.7500000000:
              if x[1] <= 2.5000000000:
                trees.append(2)
              else:
                trees.append(1)
            else:
              trees.append(2)
          else:
            trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 97
    if x[2] <= 2.5999999642:
      trees.append(0)
    else:
      if x[2] <= 4.9500000477:
        if x[0] <= 4.9500000477:
          if x[2] <= 3.8999999762:
            trees.append(1)
          else:
            trees.append(2)
        else:
          if x[2] <= 4.8500001431:
            trees.append(1)
          else:
            if x[0] <= 6.2000000477:
              trees.append(2)
            else:
              if x[1] <= 2.6000000238:
                trees.append(1)
              else:
                if x[0] <= 6.6000001431:
                  trees.append(2)
                else:
                  trees.append(1)
      else:
        trees.append(2)
      result = vote_logic(trees)
  
# Tree 98
    if x[0] <= 5.4500000477:
      if x[1] <= 2.7000000477:
        if x[3] <= 0.6500000060:
          trees.append(0)
        else:
          trees.append(1)
      else:
        trees.append(0)
    else:
      if x[3] <= 1.5500000119:
        trees.append(1)
      else:
        if x[0] <= 6.0499999523:
          if x[0] <= 5.8500001431:
            trees.append(2)
          else:
            if x[3] <= 1.6999999881:
              trees.append(1)
            else:
              if x[1] <= 3.1000000238:
                trees.append(2)
              else:
                trees.append(1)
        else:
          trees.append(2)
      result = vote_logic(trees)
  
# Tree 99
    if x[3] <= 0.8000000119:
      trees.append(0)
    else:
      if x[3] <= 1.6500000358:
        if x[0] <= 7.0999999046:
          if x[0] <= 6.0499999523:
            trees.append(1)
          else:
            if x[2] <= 5.0000000000:
              trees.append(1)
            else:
              trees.append(2)
        else:
          trees.append(2)
      else:
        if x[1] <= 3.1499999762:
          trees.append(2)
        else:
          if x[0] <= 6.1000001431:
            trees.append(1)
          else:
            trees.append(2)
      result = vote_logic(trees)
  
    return vote_logic(trees)
  
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
