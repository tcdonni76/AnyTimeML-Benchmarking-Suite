import time
"""

***** Metadata ******
Dataset: Wine
Fold: None of K-Fold cross validaiton
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
    results = [-1, 0] # Initial, bad prediction
    
    # Tree 0
        if time.time() < deadline:
          if x[9] <= 4.7899999619:
            if time.time() < deadline:
              if x[9] <= 3.4900000095:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 727.5000000000:
                    if time.time() < deadline:
                      if x[10] <= 0.9000000060:
                        if time.time() < deadline:
                          if x[5] <= 2.0750000477:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 1.9099999666:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[2] <= 1.8700000048:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 1
        if time.time() < deadline:
          if x[3] <= 17.8000001907:
            if time.time() < deadline:
              if x[12] <= 755.0000000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.8249999285:
                if time.time() < deadline:
                  if x[2] <= 2.5949999094:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 1.9700000286:
                        if time.time() < deadline:
                          if x[0] <= 12.5749998093:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 887.5000000000:
                    if time.time() < deadline:
                      if x[11] <= 2.6200000048:
                        if time.time() < deadline:
                          if x[6] <= 1.4499999881:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[0] <= 12.9800000191:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 2
        if time.time() < deadline:
          if x[12] <= 755.0000000000:
            if time.time() < deadline:
              if x[11] <= 2.1900000572:
                if time.time() < deadline:
                  if x[1] <= 1.1700000167:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 497.5000000000:
                        if time.time() < deadline:
                          if x[11] <= 1.5300000310:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[7] <= 0.6050000191:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[9] <= 6.3500001431:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 0.7450000048:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[10] <= 0.7849999964:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.4349999428:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 3
        if time.time() < deadline:
          if x[3] <= 18.8999996185:
            if time.time() < deadline:
              if x[12] <= 755.0000000000:
                if time.time() < deadline:
                  if x[6] <= 0.8750000298:
                    if time.time() < deadline:
                      if x[0] <= 12.4400000572:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 3.9499999285:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[2] <= 2.1549999714:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[4] <= 112.5000000000:
                                trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.2549999952:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[0] <= 12.5250000954:
                if time.time() < deadline:
                  if x[10] <= 0.6750000119:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[10] <= 0.9649999738:
                    if time.time() < deadline:
                      if x[8] <= 1.5899999738:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[0] <= 13.2649998665:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[7] <= 0.2149999961:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 4
        if time.time() < deadline:
          if x[6] <= 2.3600000143:
            if time.time() < deadline:
              if x[11] <= 2.1149998903:
                if time.time() < deadline:
                  if x[2] <= 2.1050000191:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 0.9699999988:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 4.3350000381:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[3] <= 17.5000000000:
                    if time.time() < deadline:
                      if x[2] <= 2.0600000620:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[0] <= 13.0199999809:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[10] <= 0.7950000167:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 5
        if time.time() < deadline:
          if x[0] <= 12.7800002098:
            if time.time() < deadline:
              if x[9] <= 4.8399999142:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[3] <= 17.1499996185:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[5] <= 2.3000000715:
                if time.time() < deadline:
                  if x[6] <= 1.5800000429:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 755.0000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 6
        if time.time() < deadline:
          if x[10] <= 0.7800000012:
            if time.time() < deadline:
              if x[5] <= 2.4599999189:
                trees.append(2)
    results = vote_logic(trees)
              else:
                trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[4] <= 88.5000000000:
                if time.time() < deadline:
                  if x[8] <= 0.9549999833:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 755.0000000000:
                    if time.time() < deadline:
                      if x[9] <= 4.0600000620:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[10] <= 0.9099999964:
                            if time.time() < deadline:
                              if x[11] <= 2.5750000477:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[0] <= 12.9400000572:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 3.4349999428:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 7
        if time.time() < deadline:
          if x[9] <= 3.8249999285:
            if time.time() < deadline:
              if x[12] <= 978.5000000000:
                if time.time() < deadline:
                  if x[8] <= 1.6549999714:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[8] <= 1.7450000048:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.0049999952:
                if time.time() < deadline:
                  if x[12] <= 460.0000000000:
                    if time.time() < deadline:
                      if x[6] <= 1.3449999690:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.0950000286:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 724.5000000000:
                        if time.time() < deadline:
                          if x[8] <= 1.7149999738:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 8
        if time.time() < deadline:
          if x[6] <= 1.2899999619:
            if time.time() < deadline:
              if x[10] <= 0.8980000019:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[3] <= 18.3999996185:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[7] <= 0.4350000024:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 755.0000000000:
                if time.time() < deadline:
                  if x[0] <= 12.7550001144:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 0.6949999928:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[3] <= 17.2500000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 13.0199999809:
                    if time.time() < deadline:
                      if x[3] <= 19.8000001907:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 9
        if time.time() < deadline:
          if x[12] <= 726.5000000000:
            if time.time() < deadline:
              if x[10] <= 0.9150000215:
                if time.time() < deadline:
                  if x[8] <= 1.3050000072:
                    if time.time() < deadline:
                      if x[9] <= 3.8750000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 1.4499999881:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[3] <= 18.2500000000:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 0.5649999976:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[10] <= 0.8050000072:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.2999999523:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[5] <= 3.2849999666:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 5.0750000477:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 10
        if time.time() < deadline:
          if x[12] <= 755.0000000000:
            if time.time() < deadline:
              if x[11] <= 2.2050000429:
                if time.time() < deadline:
                  if x[9] <= 4.8500001431:
                    if time.time() < deadline:
                      if x[7] <= 0.3200000003:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 465.0000000000:
                        if time.time() < deadline:
                          if x[8] <= 0.6500000060:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[8] <= 0.8499999940:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 2.5699999332:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[0] <= 12.8299999237:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.6400001049:
                if time.time() < deadline:
                  if x[12] <= 862.5000000000:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 12.3699998856:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[11] <= 2.1800000668:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 13.0199999809:
                    if time.time() < deadline:
                      if x[10] <= 1.1999999881:
                        if time.time() < deadline:
                          if x[1] <= 1.3450000286:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 11
        if time.time() < deadline:
          if x[12] <= 755.0000000000:
            if time.time() < deadline:
              if x[1] <= 2.5649999380:
                if time.time() < deadline:
                  if x[2] <= 2.6299999952:
                    if time.time() < deadline:
                      if x[0] <= 12.4700002670:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[6] <= 1.1949999928:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 125.0000000000:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 4.3350000381:
                    if time.time() < deadline:
                      if x[9] <= 4.0600000620:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 2.1000000834:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.6600000858:
                if time.time() < deadline:
                  if x[8] <= 1.3799999952:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[3] <= 27.5000000000:
                    trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 12
        if time.time() < deadline:
          if x[9] <= 4.0699999332:
            if time.time() < deadline:
              if x[12] <= 987.5000000000:
                if time.time() < deadline:
                  if x[2] <= 3.0700000525:
                    if time.time() < deadline:
                      if x[0] <= 13.4949998856:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[2] <= 2.2649999261:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 1.3999999762:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[2] <= 2.0299999714:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[7] <= 0.4299999923:
                        if time.time() < deadline:
                          if x[12] <= 706.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 13
        if time.time() < deadline:
          if x[12] <= 840.0000000000:
            if time.time() < deadline:
              if x[9] <= 3.8249999285:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[2] <= 2.2250000238:
                    if time.time() < deadline:
                      if x[10] <= 0.8550000191:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[8] <= 1.5899999738:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 94.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.5249999762:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 14
        if time.time() < deadline:
          if x[12] <= 755.0000000000:
            if time.time() < deadline:
              if x[9] <= 4.7599999905:
                if time.time() < deadline:
                  if x[11] <= 2.0899999142:
                    if time.time() < deadline:
                      if x[2] <= 2.3149999380:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[2] <= 2.8049999475:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[1] <= 1.1499999762:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 117.5000000000:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[0] <= 13.3750000000:
                if time.time() < deadline:
                  if x[3] <= 18.8000001907:
                    trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[8] <= 1.4050000310:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[11] <= 1.7200000286:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[12] <= 850.0000000000:
                                trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 15
        if time.time() < deadline:
          if x[9] <= 3.8199999332:
            if time.time() < deadline:
              if x[9] <= 3.6499999762:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[7] <= 0.3100000024:
                    if time.time() < deadline:
                      if x[12] <= 746.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 755.0000000000:
                if time.time() < deadline:
                  if x[9] <= 4.7999999523:
                    if time.time() < deadline:
                      if x[8] <= 0.9899999797:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[0] <= 13.1349997520:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[2] <= 2.1050000191:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 115.5000000000:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[5] <= 2.2900000215:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.1650000215:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 16
        if time.time() < deadline:
          if x[9] <= 3.6999999285:
            trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[3] <= 19.7500000000:
                if time.time() < deadline:
                  if x[5] <= 2.2599999905:
                    if time.time() < deadline:
                      if x[5] <= 1.9099999666:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 18.9499998093:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[12] <= 667.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.3250000477:
                    if time.time() < deadline:
                      if x[6] <= 1.4750000238:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 93.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[7] <= 0.5000000149:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 17
        if time.time() < deadline:
          if x[10] <= 0.7849999964:
            if time.time() < deadline:
              if x[12] <= 402.5000000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.0749999881:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[0] <= 13.0599999428:
                if time.time() < deadline:
                  if x[0] <= 12.7850003242:
                    if time.time() < deadline:
                      if x[6] <= 0.9250000119:
                        if time.time() < deadline:
                          if x[6] <= 0.5850000083:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[5] <= 2.0300000310:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[5] <= 3.0099999905:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 89.0000000000:
                    if time.time() < deadline:
                      if x[8] <= 0.9549999833:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[11] <= 2.5750000477:
                        if time.time() < deadline:
                          if x[3] <= 19.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 18
        if time.time() < deadline:
          if x[0] <= 12.7950000763:
            if time.time() < deadline:
              if x[11] <= 2.0299999714:
                if time.time() < deadline:
                  if x[3] <= 17.1499996185:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.1799999475:
                if time.time() < deadline:
                  if x[9] <= 3.8999999762:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 1.8000000119:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 87.5000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 19
        if time.time() < deadline:
          if x[9] <= 3.8199999332:
            if time.time() < deadline:
              if x[11] <= 3.6949999332:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[5] <= 2.3600000143:
                if time.time() < deadline:
                  if x[6] <= 1.3999999762:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[5] <= 1.7099999785:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[2] <= 3.0499999523:
                    if time.time() < deadline:
                      if x[0] <= 12.6100001335:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 20
        if time.time() < deadline:
          if x[0] <= 12.7800002098:
            if time.time() < deadline:
              if x[9] <= 6.5499999523:
                if time.time() < deadline:
                  if x[6] <= 1.2250000238:
                    if time.time() < deadline:
                      if x[6] <= 1.0950000286:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 1.5800000429:
                if time.time() < deadline:
                  if x[10] <= 0.9449999928:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 88.0000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 26.2500000000:
                        if time.time() < deadline:
                          if x[5] <= 2.1499999762:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 21
        if time.time() < deadline:
          if x[12] <= 755.0000000000:
            if time.time() < deadline:
              if x[11] <= 1.9850000143:
                if time.time() < deadline:
                  if x[8] <= 0.5499999970:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 0.7950000167:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 13.1749997139:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[12] <= 603.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.4349999428:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[10] <= 0.7650000155:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 22
        if time.time() < deadline:
          if x[12] <= 882.5000000000:
            if time.time() < deadline:
              if x[8] <= 1.3249999881:
                if time.time() < deadline:
                  if x[10] <= 1.0049999654:
                    if time.time() < deadline:
                      if x[6] <= 1.9200000167:
                        if time.time() < deadline:
                          if x[12] <= 393.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 7.3299999237:
                    if time.time() < deadline:
                      if x[2] <= 2.5049999952:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[12] <= 640.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[3] <= 20.5000000000:
                trees.append(0)
    results = vote_logic(trees)
              else:
                trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 23
        if time.time() < deadline:
          if x[6] <= 1.3000000119:
            if time.time() < deadline:
              if x[7] <= 0.1550000012:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[5] <= 2.2849999666:
                if time.time() < deadline:
                  if x[9] <= 4.9000000954:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 19.3999996185:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.4800000191:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 26.7500000000:
                        if time.time() < deadline:
                          if x[4] <= 88.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 24
        if time.time() < deadline:
          if x[9] <= 3.4900000095:
            trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 1.3849999905:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[5] <= 2.1549999714:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 1.3199999928:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[0] <= 12.2050004005:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 25
        if time.time() < deadline:
          if x[8] <= 1.3550000191:
            if time.time() < deadline:
              if x[9] <= 3.8750000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 1.3299999833:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 2.0950000286:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.3199999332:
                if time.time() < deadline:
                  if x[11] <= 1.7300000191:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 0.6800000072:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[8] <= 3.2699999809:
                    if time.time() < deadline:
                      if x[5] <= 2.2849999666:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[12] <= 591.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[3] <= 26.2500000000:
                                trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 26
        if time.time() < deadline:
          if x[10] <= 0.7849999964:
            if time.time() < deadline:
              if x[0] <= 12.0349998474:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[3] <= 16.7500000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 755.0000000000:
                if time.time() < deadline:
                  if x[11] <= 2.1449999809:
                    if time.time() < deadline:
                      if x[1] <= 2.0550000370:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.4349999428:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 27
        if time.time() < deadline:
          if x[6] <= 1.3999999762:
            if time.time() < deadline:
              if x[0] <= 12.0999999046:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[10] <= 0.9999999702:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.4850000143:
                if time.time() < deadline:
                  if x[6] <= 2.3500000238:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[5] <= 2.3150000572:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.3849999905:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 0.7549999952:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[1] <= 1.2800000310:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 28
        if time.time() < deadline:
          if x[0] <= 12.7800002098:
            if time.time() < deadline:
              if x[10] <= 0.7849999964:
                if time.time() < deadline:
                  if x[11] <= 2.0599999428:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[7] <= 0.6150000095:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 3.3050001264:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.4950000048:
                if time.time() < deadline:
                  if x[10] <= 0.9650000036:
                    if time.time() < deadline:
                      if x[7] <= 0.5949999988:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[6] <= 1.2100000083:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[10] <= 1.2949999571:
                    if time.time() < deadline:
                      if x[1] <= 4.9200000763:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 29
        if time.time() < deadline:
          if x[10] <= 0.7849999964:
            if time.time() < deadline:
              if x[2] <= 2.1400001049:
                if time.time() < deadline:
                  if x[10] <= 0.6399999857:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[0] <= 12.7800002098:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.4950000048:
                    if time.time() < deadline:
                      if x[12] <= 670.0000000000:
                        if time.time() < deadline:
                          if x[1] <= 1.9300000072:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[8] <= 1.3199999928:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 89.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 30
        if time.time() < deadline:
          if x[11] <= 2.1900000572:
            if time.time() < deadline:
              if x[1] <= 1.8899999857:
                if time.time() < deadline:
                  if x[10] <= 0.8330000043:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 393.5000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 85.5000000000:
                        if time.time() < deadline:
                          if x[1] <= 4.4499999285:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 726.5000000000:
                if time.time() < deadline:
                  if x[6] <= 0.7450000048:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 17.7500000000:
                        if time.time() < deadline:
                          if x[2] <= 2.0199999809:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.3500000238:
                    if time.time() < deadline:
                      if x[1] <= 1.6200000048:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 91.5000000000:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[5] <= 3.2849999666:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[2] <= 2.5499999523:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 31
        if time.time() < deadline:
          if x[6] <= 1.3149999976:
            if time.time() < deadline:
              if x[3] <= 17.3999996185:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.5600000620:
                    if time.time() < deadline:
                      if x[10] <= 0.9300000072:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[7] <= 0.3200000003:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 724.5000000000:
                if time.time() < deadline:
                  if x[7] <= 0.2299999967:
                    if time.time() < deadline:
                      if x[6] <= 1.8900000453:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 135.5000000000:
                    if time.time() < deadline:
                      if x[6] <= 2.2350000143:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 32
        if time.time() < deadline:
          if x[12] <= 730.0000000000:
            if time.time() < deadline:
              if x[0] <= 12.5500001907:
                if time.time() < deadline:
                  if x[11] <= 1.9850000739:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 1.9850000143:
                    if time.time() < deadline:
                      if x[10] <= 0.9699999988:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 95.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[1] <= 1.8949999809:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 1000.0000000000:
                if time.time() < deadline:
                  if x[10] <= 0.7949999869:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 3.4649999142:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 33
        if time.time() < deadline:
          if x[9] <= 3.8199999332:
            trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.5199999809:
                if time.time() < deadline:
                  if x[6] <= 1.5800000429:
                    if time.time() < deadline:
                      if x[2] <= 2.0599999428:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 3.0499999523:
                    if time.time() < deadline:
                      if x[12] <= 622.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 1.2400000095:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 89.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[3] <= 24.2500000000:
                                trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 34
        if time.time() < deadline:
          if x[0] <= 12.7900004387:
            if time.time() < deadline:
              if x[6] <= 1.0050000250:
                trees.append(2)
    results = vote_logic(trees)
              else:
                trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.1100000143:
                if time.time() < deadline:
                  if x[10] <= 0.9250000119:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.4349999428:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 35
        if time.time() < deadline:
          if x[10] <= 0.7849999964:
            if time.time() < deadline:
              if x[12] <= 425.0000000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.3199999332:
                if time.time() < deadline:
                  if x[6] <= 0.8950000107:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[2] <= 2.1550000906:
                        if time.time() < deadline:
                          if x[10] <= 1.0299999714:
                            if time.time() < deadline:
                              if x[4] <= 93.0000000000:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 12.7850003242:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 591.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[3] <= 26.2500000000:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 36
        if time.time() < deadline:
          if x[0] <= 12.7950000763:
            if time.time() < deadline:
              if x[6] <= 1.2250000238:
                if time.time() < deadline:
                  if x[2] <= 1.7800000310:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 123.0000000000:
                        if time.time() < deadline:
                          if x[8] <= 1.3550000191:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[10] <= 0.8550000191:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.0799999237:
                    if time.time() < deadline:
                      if x[3] <= 19.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 13.1349997520:
                        if time.time() < deadline:
                          if x[6] <= 2.7850000858:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[1] <= 1.7199999690:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 37
        if time.time() < deadline:
          if x[0] <= 12.7900004387:
            if time.time() < deadline:
              if x[11] <= 1.7750000358:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[10] <= 0.6750000119:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 842.5000000000:
                if time.time() < deadline:
                  if x[10] <= 0.9300000072:
                    if time.time() < deadline:
                      if x[6] <= 1.4900000095:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[3] <= 19.5000000000:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 2.2200000286:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 94.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 38
        if time.time() < deadline:
          if x[11] <= 2.1250000000:
            if time.time() < deadline:
              if x[3] <= 17.5000000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 1.4250000119:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 497.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.3099999428:
                if time.time() < deadline:
                  if x[10] <= 0.7450000048:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 3.8750000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[8] <= 1.1949999928:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 707.5000000000:
                    if time.time() < deadline:
                      if x[0] <= 13.1449999809:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[1] <= 2.7450000048:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 27.5000000000:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 39
        if time.time() < deadline:
          if x[12] <= 755.0000000000:
            if time.time() < deadline:
              if x[8] <= 1.5849999785:
                if time.time() < deadline:
                  if x[9] <= 4.7899999619:
                    if time.time() < deadline:
                      if x[1] <= 4.5099999905:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 1.3999999762:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.9600000381:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 4.4300000668:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 8.5250000954:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 1.4850000143:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 12.7000002861:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 40
        if time.time() < deadline:
          if x[11] <= 2.1149998903:
            if time.time() < deadline:
              if x[9] <= 3.5099999905:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.4600000381:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[2] <= 1.9799999595:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 12.8850002289:
                        if time.time() < deadline:
                          if x[6] <= 0.9250000119:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[3] <= 19.7500000000:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[6] <= 1.5549999475:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 41
        if time.time() < deadline:
          if x[9] <= 3.4600000381:
            trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.4750000238:
                if time.time() < deadline:
                  if x[1] <= 1.3000000119:
                    if time.time() < deadline:
                      if x[5] <= 2.0499999523:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[2] <= 2.0600000024:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 12.6400003433:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 87.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 42
        if time.time() < deadline:
          if x[6] <= 2.3099999428:
            if time.time() < deadline:
              if x[9] <= 3.8249999285:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[3] <= 17.5000000000:
                    if time.time() < deadline:
                      if x[0] <= 13.1649999619:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 85.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.8549998999:
                if time.time() < deadline:
                  if x[4] <= 89.5000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 12.7199997902:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.4500000477:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 724.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 43
        if time.time() < deadline:
          if x[12] <= 842.5000000000:
            if time.time() < deadline:
              if x[9] <= 4.8500001431:
                if time.time() < deadline:
                  if x[1] <= 3.5000000000:
                    if time.time() < deadline:
                      if x[0] <= 13.5050001144:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[7] <= 0.4099999964:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 21.2500000000:
                        if time.time() < deadline:
                          if x[7] <= 0.3750000000:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[1] <= 1.6499999762:
                    if time.time() < deadline:
                      if x[8] <= 1.6749999523:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[5] <= 2.9900000095:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[0] <= 13.0299997330:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 44
        if time.time() < deadline:
          if x[6] <= 0.9550000131:
            trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.3299999237:
                if time.time() < deadline:
                  if x[5] <= 1.5550000072:
                    if time.time() < deadline:
                      if x[0] <= 12.7399997711:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[11] <= 1.4399999976:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[3] <= 24.3000001907:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[6] <= 1.4599999785:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 737.0000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 3.4649999142:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 45
        if time.time() < deadline:
          if x[0] <= 12.7450003624:
            if time.time() < deadline:
              if x[10] <= 0.7700000107:
                if time.time() < deadline:
                  if x[8] <= 2.4149999619:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[7] <= 0.6150000095:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 20.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 842.5000000000:
                if time.time() < deadline:
                  if x[6] <= 1.5800000429:
                    if time.time() < deadline:
                      if x[3] <= 17.7500000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[5] <= 2.2549999952:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 3.8500001431:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 133.0000000000:
                    trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 46
        if time.time() < deadline:
          if x[6] <= 1.2350000143:
            if time.time() < deadline:
              if x[10] <= 0.8980000019:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[1] <= 2.6899999380:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[7] <= 0.3449999988:
                if time.time() < deadline:
                  if x[6] <= 2.3199999332:
                    if time.time() < deadline:
                      if x[10] <= 0.7750000060:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[8] <= 1.8199999928:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[1] <= 2.3799999952:
                            if time.time() < deadline:
                              if x[12] <= 782.5000000000:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 113.5000000000:
                    if time.time() < deadline:
                      if x[5] <= 2.9649999142:
                        if time.time() < deadline:
                          if x[2] <= 2.6299999952:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[1] <= 1.9050000310:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[8] <= 1.8450000286:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[1] <= 1.5199999809:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[12] <= 647.5000000000:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 47
        if time.time() < deadline:
          if x[6] <= 0.9550000131:
            if time.time() < deadline:
              if x[1] <= 1.0900000036:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[3] <= 17.8999996185:
                if time.time() < deadline:
                  if x[5] <= 2.1250000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 1.1800000072:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 87.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[9] <= 3.5499999523:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.3500000238:
                    if time.time() < deadline:
                      if x[9] <= 4.9000000954:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 1.6999999881:
                        if time.time() < deadline:
                          if x[12] <= 1045.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 98.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[9] <= 3.0749999285:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 48
        if time.time() < deadline:
          if x[0] <= 12.7800002098:
            if time.time() < deadline:
              if x[12] <= 687.5000000000:
                if time.time() < deadline:
                  if x[9] <= 6.7000000477:
                    if time.time() < deadline:
                      if x[10] <= 0.7849999964:
                        if time.time() < deadline:
                          if x[10] <= 0.7649999857:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[5] <= 2.0500000119:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[5] <= 2.1499999762:
                if time.time() < deadline:
                  if x[6] <= 1.4900000095:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 89.5000000000:
                    if time.time() < deadline:
                      if x[4] <= 87.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[7] <= 0.4999999851:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[10] <= 0.9549999833:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 49
        if time.time() < deadline:
          if x[5] <= 2.3349999189:
            if time.time() < deadline:
              if x[9] <= 4.1250000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[7] <= 0.6050000191:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[11] <= 1.8500000238:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.4500000477:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.1449999809:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 12.6500000954:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 83.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 50
        if time.time() < deadline:
          if x[11] <= 2.2050000429:
            if time.time() < deadline:
              if x[3] <= 17.2500000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 1.4499999881:
                    if time.time() < deadline:
                      if x[0] <= 12.4000000954:
                        if time.time() < deadline:
                          if x[10] <= 0.8280000091:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[0] <= 12.7750000954:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 682.5000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 51
        if time.time() < deadline:
          if x[6] <= 2.3099999428:
            if time.time() < deadline:
              if x[9] <= 3.8999999762:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[3] <= 17.6499996185:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 1.0399999917:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.2100000381:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 724.5000000000:
                    if time.time() < deadline:
                      if x[4] <= 100.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[1] <= 3.0149999857:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 52
        if time.time() < deadline:
          if x[9] <= 3.6499999762:
            trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.3849999905:
                if time.time() < deadline:
                  if x[9] <= 4.7500000000:
                    if time.time() < deadline:
                      if x[5] <= 1.9800000191:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[8] <= 0.6500000060:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[1] <= 1.3000000119:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 4.5049999952:
                        if time.time() < deadline:
                          if x[4] <= 88.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 53
        if time.time() < deadline:
          if x[10] <= 0.7849999964:
            if time.time() < deadline:
              if x[5] <= 2.8299999237:
                trees.append(2)
    results = vote_logic(trees)
              else:
                trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[4] <= 89.0000000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 12.7750000954:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 3.1349999905:
                        if time.time() < deadline:
                          if x[1] <= 1.3399999738:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[3] <= 26.2500000000:
                                trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[11] <= 2.5549999475:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 54
        if time.time() < deadline:
          if x[11] <= 2.0549999475:
            if time.time() < deadline:
              if x[10] <= 0.8299999833:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 532.5000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 0.9080000222:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 3.3049999475:
                if time.time() < deadline:
                  if x[0] <= 13.1349997520:
                    if time.time() < deadline:
                      if x[12] <= 790.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[2] <= 2.7599999905:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[8] <= 0.9500000179:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 90.0000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 3.4349999428:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 55
        if time.time() < deadline:
          if x[0] <= 12.7800002098:
            if time.time() < deadline:
              if x[9] <= 4.8399999142:
                if time.time() < deadline:
                  if x[1] <= 4.5749998093:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[5] <= 2.0099999905:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 492.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 755.0000000000:
                if time.time() < deadline:
                  if x[9] <= 4.8600001335:
                    if time.time() < deadline:
                      if x[5] <= 2.6299999952:
                        if time.time() < deadline:
                          if x[0] <= 12.9800000191:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 135.5000000000:
                    if time.time() < deadline:
                      if x[11] <= 2.0949999690:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 56
        if time.time() < deadline:
          if x[12] <= 760.0000000000:
            if time.time() < deadline:
              if x[11] <= 2.1149998903:
                if time.time() < deadline:
                  if x[8] <= 0.4849999994:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[11] <= 2.0549999475:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 3.6999999285:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 0.7950000167:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.4349999428:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[8] <= 1.3550000191:
                    if time.time() < deadline:
                      if x[9] <= 5.4199998379:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 57
        if time.time() < deadline:
          if x[12] <= 900.5000000000:
            if time.time() < deadline:
              if x[11] <= 2.1149998903:
                if time.time() < deadline:
                  if x[10] <= 0.9699999988:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[8] <= 0.7899999917:
                    if time.time() < deadline:
                      if x[9] <= 4.1999999285:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 722.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[0] <= 12.6300001144:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
          else:
            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 58
        if time.time() < deadline:
          if x[9] <= 3.4600000381:
            trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.4900000095:
                if time.time() < deadline:
                  if x[6] <= 1.5800000429:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[2] <= 1.9799999595:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 12.7400002480:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[8] <= 1.1399999857:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 59
        if time.time() < deadline:
          if x[0] <= 12.8050003052:
            if time.time() < deadline:
              if x[10] <= 0.8400000036:
                if time.time() < deadline:
                  if x[11] <= 1.9749999642:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[5] <= 2.3349999189:
                if time.time() < deadline:
                  if x[9] <= 3.8999999762:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.3450000286:
                    if time.time() < deadline:
                      if x[9] <= 7.4600000381:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 4.8900001049:
                        if time.time() < deadline:
                          if x[4] <= 135.5000000000:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 60
        if time.time() < deadline:
          if x[9] <= 3.4600000381:
            trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[3] <= 18.9499998093:
                if time.time() < deadline:
                  if x[11] <= 2.4049999714:
                    if time.time() < deadline:
                      if x[5] <= 1.9650000334:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 737.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.4850000143:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 671.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 61
        if time.time() < deadline:
          if x[12] <= 987.5000000000:
            if time.time() < deadline:
              if x[10] <= 0.7250000238:
                if time.time() < deadline:
                  if x[3] <= 17.2500000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 627.5000000000:
                    if time.time() < deadline:
                      if x[8] <= 0.9949999750:
                        if time.time() < deadline:
                          if x[5] <= 1.8149999976:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[5] <= 2.1699999571:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 2.4399999380:
                        if time.time() < deadline:
                          if x[9] <= 3.6250000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[5] <= 3.1999999285:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
          else:
            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 62
        if time.time() < deadline:
          if x[9] <= 3.8199999332:
            if time.time() < deadline:
              if x[9] <= 3.4900000095:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[5] <= 2.2500000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.2849999666:
                if time.time() < deadline:
                  if x[5] <= 2.0099999905:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 505.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[2] <= 3.0499999523:
                    trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 63
        if time.time() < deadline:
          if x[0] <= 12.7800002098:
            if time.time() < deadline:
              if x[9] <= 4.8399999142:
                if time.time() < deadline:
                  if x[1] <= 4.5749998093:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 1.1649999917:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 755.0000000000:
                if time.time() < deadline:
                  if x[10] <= 0.9699999988:
                    if time.time() < deadline:
                      if x[6] <= 2.0100000501:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[6] <= 2.6400001049:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 90.0000000000:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 64
        if time.time() < deadline:
          if x[10] <= 0.7849999964:
            if time.time() < deadline:
              if x[5] <= 2.4099999666:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[2] <= 2.5450000763:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.3099999428:
                if time.time() < deadline:
                  if x[6] <= 0.9550000131:
                    if time.time() < deadline:
                      if x[7] <= 0.3550000042:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 93.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[3] <= 17.5000000000:
                            if time.time() < deadline:
                              if x[6] <= 2.0200000405:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 88.5000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 679.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 65
        if time.time() < deadline:
          if x[5] <= 2.3799999952:
            if time.time() < deadline:
              if x[5] <= 1.8400000334:
                if time.time() < deadline:
                  if x[4] <= 88.5000000000:
                    if time.time() < deadline:
                      if x[0] <= 13.2849998474:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 12.4349999428:
                        if time.time() < deadline:
                          if x[11] <= 1.5450000167:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 4.1500000954:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 515.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[4] <= 88.5000000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 12.7750000954:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 27.5000000000:
                        if time.time() < deadline:
                          if x[7] <= 0.5149999857:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 66
        if time.time() < deadline:
          if x[0] <= 12.7800002098:
            if time.time() < deadline:
              if x[8] <= 1.1800000072:
                if time.time() < deadline:
                  if x[9] <= 4.8399999142:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 1.8750000596:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 1.9099999666:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[10] <= 0.8350000083:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.0849999785:
                    if time.time() < deadline:
                      if x[10] <= 0.9699999988:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[2] <= 1.8700000048:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 3.4500000477:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 67
        if time.time() < deadline:
          if x[9] <= 3.9150000811:
            if time.time() < deadline:
              if x[11] <= 1.4699999690:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 13.4949998856:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 1.1750000119:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[11] <= 2.4900000095:
                if time.time() < deadline:
                  if x[5] <= 2.0099999905:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 0.9350000024:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 83.5000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 68
        if time.time() < deadline:
          if x[10] <= 0.8149999976:
            if time.time() < deadline:
              if x[11] <= 2.4399999380:
                trees.append(2)
    results = vote_logic(trees)
              else:
                trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[3] <= 17.7500000000:
                if time.time() < deadline:
                  if x[2] <= 2.0099999905:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 12.7800002098:
                    if time.time() < deadline:
                      if x[10] <= 0.8400000036:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 2.7749999762:
                        if time.time() < deadline:
                          if x[4] <= 95.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[7] <= 0.3850000054:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[8] <= 1.3199999928:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 69
        if time.time() < deadline:
          if x[0] <= 12.7800002098:
            if time.time() < deadline:
              if x[12] <= 635.0000000000:
                if time.time() < deadline:
                  if x[6] <= 1.2250000238:
                    if time.time() < deadline:
                      if x[12] <= 612.5000000000:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 5.0249998569:
                    if time.time() < deadline:
                      if x[1] <= 3.2649998665:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[5] <= 2.0749999285:
                if time.time() < deadline:
                  if x[6] <= 1.4900000095:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 670.0000000000:
                    if time.time() < deadline:
                      if x[7] <= 0.4199999869:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 1.1450000107:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 70
        if time.time() < deadline:
          if x[6] <= 1.3999999762:
            if time.time() < deadline:
              if x[8] <= 0.4800000042:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 1.2649999857:
                    if time.time() < deadline:
                      if x[4] <= 82.5000000000:
                        if time.time() < deadline:
                          if x[5] <= 1.3050000072:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 6.1249997616:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.3099999428:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 88.5000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[7] <= 0.4249999970:
                        if time.time() < deadline:
                          if x[0] <= 13.0199999809:
                            if time.time() < deadline:
                              if x[3] <= 19.0500001907:
                                if time.time() < deadline:
                                  if x[9] <= 4.5499999523:
                                    trees.append(0)
    results = vote_logic(trees)
                                  else:
                                    trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[7] <= 0.4849999994:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 71
        if time.time() < deadline:
          if x[0] <= 12.7450003624:
            if time.time() < deadline:
              if x[9] <= 4.8399999142:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[3] <= 17.1499996185:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[10] <= 0.8149999976:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 89.5000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[5] <= 2.3600000143:
                        if time.time() < deadline:
                          if x[11] <= 2.3050000668:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[0] <= 13.0199999809:
                            if time.time() < deadline:
                              if x[8] <= 1.7100000381:
                                trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 72
        if time.time() < deadline:
          if x[12] <= 961.0000000000:
            if time.time() < deadline:
              if x[2] <= 2.2250000238:
                if time.time() < deadline:
                  if x[5] <= 1.5450000167:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[5] <= 2.9900000095:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 4.7699999809:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.6150000095:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[5] <= 2.6200000048:
                        if time.time() < deadline:
                          if x[12] <= 760.0000000000:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[9] <= 5.0499999523:
                                trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[7] <= 0.4200000018:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[9] <= 9.5000000000:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
          else:
            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 73
        if time.time() < deadline:
          if x[4] <= 88.5000000000:
            if time.time() < deadline:
              if x[7] <= 0.4999999851:
                if time.time() < deadline:
                  if x[2] <= 2.4700000286:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[11] <= 2.2900000215:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[5] <= 2.2300000191:
                    if time.time() < deadline:
                      if x[2] <= 2.2899999619:
                        if time.time() < deadline:
                          if x[4] <= 82.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[5] <= 2.3799999952:
                if time.time() < deadline:
                  if x[2] <= 2.0599999428:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 1.6600000262:
                        if time.time() < deadline:
                          if x[3] <= 17.2500000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[7] <= 0.1550000012:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 4.3999999762:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.4349999428:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[11] <= 2.4049999714:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 74
        if time.time() < deadline:
          if x[11] <= 2.2050000429:
            if time.time() < deadline:
              if x[9] <= 3.5249999762:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[8] <= 1.5899999738:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[5] <= 1.7249999642:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[0] <= 13.0399999619:
                if time.time() < deadline:
                  if x[1] <= 3.7699999809:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 12.8150000572:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.4500000477:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 0.7599999905:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[2] <= 2.2450000048:
                            if time.time() < deadline:
                              if x[11] <= 2.8149999380:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 75
        if time.time() < deadline:
          if x[10] <= 0.7849999964:
            if time.time() < deadline:
              if x[9] <= 3.9700000286:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[4] <= 99.0000000000:
                if time.time() < deadline:
                  if x[11] <= 3.5149999857:
                    if time.time() < deadline:
                      if x[3] <= 17.2500000000:
                        if time.time() < deadline:
                          if x[10] <= 1.0699999928:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[2] <= 2.0099999905:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[12] <= 874.5000000000:
                            if time.time() < deadline:
                              if x[0] <= 13.2699999809:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                if time.time() < deadline:
                                  if x[9] <= 4.7499998808:
                                    trees.append(1)
    results = vote_logic(trees)
                                  else:
                                    trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.5349999666:
                    if time.time() < deadline:
                      if x[11] <= 2.1900000572:
                        if time.time() < deadline:
                          if x[3] <= 19.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 12.8150000572:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 3.4649999142:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 76
        if time.time() < deadline:
          if x[9] <= 3.8199999332:
            if time.time() < deadline:
              if x[12] <= 1002.5000000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[1] <= 2.1799999475:
                if time.time() < deadline:
                  if x[5] <= 2.3100000620:
                    if time.time() < deadline:
                      if x[2] <= 2.2250000238:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 12.6400003433:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 91.0000000000:
                            if time.time() < deadline:
                              if x[3] <= 18.7500000000:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.7000000477:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 77
        if time.time() < deadline:
          if x[12] <= 760.0000000000:
            if time.time() < deadline:
              if x[9] <= 4.0199999809:
                if time.time() < deadline:
                  if x[5] <= 1.4150000215:
                    if time.time() < deadline:
                      if x[10] <= 0.8149999976:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[8] <= 1.5899999738:
                    if time.time() < deadline:
                      if x[5] <= 2.0099999905:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[5] <= 2.1549999714:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[11] <= 1.9850000143:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[11] <= 2.8999999762:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[10] <= 0.7650000155:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[3] <= 27.5000000000:
                    if time.time() < deadline:
                      if x[1] <= 1.2950000167:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 78
        if time.time() < deadline:
          if x[1] <= 2.4550000429:
            if time.time() < deadline:
              if x[12] <= 765.0000000000:
                if time.time() < deadline:
                  if x[0] <= 12.4650001526:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 24.5000000000:
                        if time.time() < deadline:
                          if x[0] <= 12.5900001526:
                            if time.time() < deadline:
                              if x[3] <= 20.2500000000:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[9] <= 7.8249993324:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[2] <= 2.6850000620:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 13.0199999809:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.3750000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.1000000834:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 79
        if time.time() < deadline:
          if x[9] <= 3.4600000381:
            trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[8] <= 1.2649999857:
                if time.time() < deadline:
                  if x[10] <= 0.9250000119:
                    if time.time() < deadline:
                      if x[12] <= 967.5000000000:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 1.9850000143:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 0.8499999940:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 88.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 80
        if time.time() < deadline:
          if x[6] <= 1.4250000119:
            if time.time() < deadline:
              if x[2] <= 2.0650000572:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.7999999523:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.9450000525:
                if time.time() < deadline:
                  if x[11] <= 3.8200000525:
                    if time.time() < deadline:
                      if x[8] <= 1.3750000000:
                        if time.time() < deadline:
                          if x[2] <= 2.1349999905:
                            if time.time() < deadline:
                              if x[2] <= 2.0099999309:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 710.0000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 81
        if time.time() < deadline:
          if x[9] <= 3.9150000811:
            if time.time() < deadline:
              if x[6] <= 2.6100000143:
                if time.time() < deadline:
                  if x[7] <= 0.5249999762:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 3.6349998713:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[2] <= 2.9450000525:
                    if time.time() < deadline:
                      if x[5] <= 2.5000000000:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 7.0000000000:
                if time.time() < deadline:
                  if x[1] <= 1.2800000310:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 695.0000000000:
                        if time.time() < deadline:
                          if x[4] <= 87.0000000000:
                            if time.time() < deadline:
                              if x[4] <= 82.5000000000:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[12] <= 837.5000000000:
                            if time.time() < deadline:
                              if x[1] <= 3.7799999714:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.3600000739:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 82
        if time.time() < deadline:
          if x[9] <= 3.6499999762:
            trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[10] <= 0.7999999821:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 655.0000000000:
                    if time.time() < deadline:
                      if x[6] <= 1.1049999893:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 83
        if time.time() < deadline:
          if x[12] <= 760.0000000000:
            if time.time() < deadline:
              if x[10] <= 0.9150000215:
                if time.time() < deadline:
                  if x[11] <= 2.4650000334:
                    if time.time() < deadline:
                      if x[2] <= 2.0399999619:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 3.8600000143:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[11] <= 3.0499999523:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 13.1349997520:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 1.2000000179:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[0] <= 13.3649997711:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.2999999523:
                if time.time() < deadline:
                  if x[12] <= 863.0000000000:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[3] <= 27.5000000000:
                    trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 84
        if time.time() < deadline:
          if x[11] <= 2.0899999142:
            if time.time() < deadline:
              if x[4] <= 99.0000000000:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[4] <= 104.0000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[7] <= 0.5399999917:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[3] <= 17.4499998093:
                if time.time() < deadline:
                  if x[2] <= 2.0399999619:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 724.5000000000:
                    if time.time() < deadline:
                      if x[6] <= 0.7950000167:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[1] <= 3.9249999523:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[4] <= 102.5000000000:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 2.3400000334:
                        if time.time() < deadline:
                          if x[0] <= 12.9149999619:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[4] <= 135.5000000000:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 85
        if time.time() < deadline:
          if x[11] <= 2.1149998903:
            if time.time() < deadline:
              if x[4] <= 88.5000000000:
                if time.time() < deadline:
                  if x[5] <= 1.5649999976:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[1] <= 1.1149999797:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.2999999523:
                if time.time() < deadline:
                  if x[6] <= 0.7450000048:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[1] <= 1.4449999928:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 724.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 86
        if time.time() < deadline:
          if x[10] <= 0.7849999964:
            if time.time() < deadline:
              if x[6] <= 2.0749999881:
                if time.time() < deadline:
                  if x[12] <= 393.5000000000:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[5] <= 2.2849999666:
                if time.time() < deadline:
                  if x[8] <= 0.5850000083:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 13.5549998283:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.3199999332:
                    if time.time() < deadline:
                      if x[11] <= 2.7749999762:
                        if time.time() < deadline:
                          if x[2] <= 2.1700000763:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[2] <= 2.2300000191:
                        if time.time() < deadline:
                          if x[10] <= 1.1999999881:
                            if time.time() < deadline:
                              if x[7] <= 0.3299999982:
                                if time.time() < deadline:
                                  if x[4] <= 89.0000000000:
                                    trees.append(1)
    results = vote_logic(trees)
                                  else:
                                    trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[1] <= 2.3799999952:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[1] <= 2.4950000048:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 87
        if time.time() < deadline:
          if x[12] <= 842.5000000000:
            if time.time() < deadline:
              if x[5] <= 1.8499999642:
                if time.time() < deadline:
                  if x[12] <= 618.5000000000:
                    if time.time() < deadline:
                      if x[6] <= 1.4250000119:
                        if time.time() < deadline:
                          if x[1] <= 2.0050000548:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[10] <= 0.6800000072:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[4] <= 122.5000000000:
                        if time.time() < deadline:
                          if x[6] <= 0.9450000226:
                            if time.time() < deadline:
                              if x[6] <= 0.5850000083:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[7] <= 0.2549999952:
                                if time.time() < deadline:
                                  if x[9] <= 4.4749999046:
                                    trees.append(1)
    results = vote_logic(trees)
                                  else:
                                    trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[0] <= 13.1950001717:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.4349999428:
                trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 88
        if time.time() < deadline:
          if x[12] <= 755.0000000000:
            if time.time() < deadline:
              if x[11] <= 2.2050000429:
                if time.time() < deadline:
                  if x[6] <= 1.5800000429:
                    if time.time() < deadline:
                      if x[9] <= 3.5749999285:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 12.8250002861:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[2] <= 2.6850000620:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[9] <= 3.4649999142:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[8] <= 1.1949999928:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[11] <= 2.0949999690:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 89
        if time.time() < deadline:
          if x[0] <= 12.7800002098:
            if time.time() < deadline:
              if x[10] <= 0.7700000107:
                if time.time() < deadline:
                  if x[7] <= 0.4799999893:
                    if time.time() < deadline:
                      if x[11] <= 1.9749999642:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[10] <= 0.7999999821:
                if time.time() < deadline:
                  if x[8] <= 1.9399999976:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 625.0000000000:
                    if time.time() < deadline:
                      if x[12] <= 496.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 90
        if time.time() < deadline:
          if x[10] <= 0.8550000191:
            if time.time() < deadline:
              if x[11] <= 2.0049999952:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[6] <= 2.6050000191:
                    if time.time() < deadline:
                      if x[9] <= 5.2000000477:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[4] <= 88.5000000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 760.0000000000:
                    if time.time() < deadline:
                      if x[9] <= 4.0749999285:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[1] <= 2.5049999952:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[8] <= 3.1200000048:
                        if time.time() < deadline:
                          if x[0] <= 12.4050002098:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 91
        if time.time() < deadline:
          if x[11] <= 2.1149998903:
            if time.time() < deadline:
              if x[10] <= 0.8980000019:
                if time.time() < deadline:
                  if x[4] <= 85.5000000000:
                    if time.time() < deadline:
                      if x[2] <= 2.2749999762:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 13.5149998665:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 953.5000000000:
                if time.time() < deadline:
                  if x[9] <= 4.7999999523:
                    if time.time() < deadline:
                      if x[2] <= 2.6050000191:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[12] <= 725.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[8] <= 1.4199999869:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 5.2000000477:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 92
        if time.time() < deadline:
          if x[9] <= 3.8650000095:
            if time.time() < deadline:
              if x[9] <= 3.4600000381:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[10] <= 1.1750000119:
                    if time.time() < deadline:
                      if x[4] <= 91.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[5] <= 2.3600000143:
                if time.time() < deadline:
                  if x[11] <= 2.4750000238:
                    if time.time() < deadline:
                      if x[6] <= 1.5800000429:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 895.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 670.0000000000:
                    if time.time() < deadline:
                      if x[9] <= 9.5000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 93
        if time.time() < deadline:
          if x[6] <= 0.9749999940:
            trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[1] <= 1.4199999571:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[7] <= 0.3550000042:
                    if time.time() < deadline:
                      if x[1] <= 1.9800000191:
                        if time.time() < deadline:
                          if x[6] <= 2.2999999523:
                            if time.time() < deadline:
                              if x[7] <= 0.2850000113:
                                if time.time() < deadline:
                                  if x[9] <= 3.8450000286:
                                    trees.append(1)
    results = vote_logic(trees)
                                  else:
                                    trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[3] <= 26.2500000000:
                                if time.time() < deadline:
                                  if x[6] <= 2.5699999332:
                                    if time.time() < deadline:
                                      if x[2] <= 2.2050000429:
                                        trees.append(1)
    results = vote_logic(trees)
                                      else:
                                        trees.append(0)
    results = vote_logic(trees)
                                  else:
                                    trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[9] <= 3.8999999762:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[8] <= 1.0449999869:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 4.2200000286:
                        if time.time() < deadline:
                          if x[8] <= 1.9099999666:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[5] <= 2.7300000191:
                                trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[10] <= 1.0900000036:
                            if time.time() < deadline:
                              if x[8] <= 2.2850000262:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 94
        if time.time() < deadline:
          if x[6] <= 1.2350000143:
            if time.time() < deadline:
              if x[2] <= 1.7750000358:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[10] <= 1.0600000024:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 2.2999999523:
                if time.time() < deadline:
                  if x[2] <= 2.5749999285:
                    if time.time() < deadline:
                      if x[4] <= 93.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[12] <= 1111.0000000000:
                            if time.time() < deadline:
                              if x[5] <= 1.5450000167:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[3] <= 26.0000000000:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[0] <= 12.7750000954:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 4.8200000525:
                        if time.time() < deadline:
                          if x[7] <= 0.2149999961:
                            if time.time() < deadline:
                              if x[12] <= 627.5000000000:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[4] <= 84.0000000000:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 95
        if time.time() < deadline:
          if x[11] <= 2.4750000238:
            if time.time() < deadline:
              if x[9] <= 3.8249999285:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[10] <= 0.8299999833:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[6] <= 1.1049999893:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[12] <= 722.5000000000:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.4649999142:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 96
        if time.time() < deadline:
          if x[0] <= 12.7950000763:
            if time.time() < deadline:
              if x[10] <= 0.6750000119:
                trees.append(2)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 1.5500000119:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[11] <= 1.7550000548:
                        if time.time() < deadline:
                          if x[5] <= 1.9049999714:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[7] <= 0.3949999958:
                if time.time() < deadline:
                  if x[5] <= 2.2749999762:
                    if time.time() < deadline:
                      if x[0] <= 13.6250000000:
                        if time.time() < deadline:
                          if x[12] <= 408.5000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[12] <= 631.0000000000:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 790.0000000000:
                    if time.time() < deadline:
                      if x[10] <= 0.9899999797:
                        if time.time() < deadline:
                          if x[11] <= 1.9850000143:
                            trees.append(2)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[1] <= 3.5649999380:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 0.8599999845:
                        trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 97
        if time.time() < deadline:
          if x[3] <= 17.8999996185:
            if time.time() < deadline:
              if x[12] <= 755.0000000000:
                if time.time() < deadline:
                  if x[11] <= 2.9800000191:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 4.8300001621:
                        trees.append(0)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
              else:
                trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[6] <= 1.4250000119:
                if time.time() < deadline:
                  if x[10] <= 0.8980000019:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[9] <= 3.4600000381:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[0] <= 12.8250002861:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[5] <= 2.2549999952:
                            if time.time() < deadline:
                              if x[6] <= 1.6800000072:
                                trees.append(2)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 98
        if time.time() < deadline:
          if x[3] <= 17.8999996185:
            if time.time() < deadline:
              if x[6] <= 2.1800000668:
                trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[1] <= 1.1800000072:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[2] <= 2.3149999380:
                if time.time() < deadline:
                  if x[11] <= 1.7850000262:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[1] <= 3.7899999619:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[5] <= 2.5349999666:
                            trees.append(0)
    results = vote_logic(trees)
                          else:
                            trees.append(1)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[11] <= 2.1899999380:
                    trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[9] <= 3.2100000381:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        if time.time() < deadline:
                          if x[5] <= 1.9750000238:
                            if time.time() < deadline:
                              if x[9] <= 4.0999999046:
                                trees.append(1)
    results = vote_logic(trees)
                              else:
                                trees.append(2)
    results = vote_logic(trees)
                          else:
                            trees.append(0)
    results = vote_logic(trees)
    
    else:
      return vote_logic(results)
    
    # Tree 99
        if time.time() < deadline:
          if x[6] <= 1.2350000143:
            if time.time() < deadline:
              if x[7] <= 0.2849999964:
                if time.time() < deadline:
                  if x[8] <= 0.6249999851:
                    trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(2)
    results = vote_logic(trees)
              else:
                trees.append(2)
    results = vote_logic(trees)
          else:
            if time.time() < deadline:
              if x[5] <= 2.3799999952:
                if time.time() < deadline:
                  if x[6] <= 2.3200000525:
                    if time.time() < deadline:
                      if x[8] <= 1.1449999809:
                        if time.time() < deadline:
                          if x[4] <= 100.0000000000:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            trees.append(2)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
                  else:
                    trees.append(0)
    results = vote_logic(trees)
              else:
                if time.time() < deadline:
                  if x[12] <= 679.0000000000:
                    if time.time() < deadline:
                      if x[8] <= 2.3899999857:
                        trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(2)
    results = vote_logic(trees)
                  else:
                    if time.time() < deadline:
                      if x[10] <= 1.2949999571:
                        if time.time() < deadline:
                          if x[7] <= 0.1499999985:
                            trees.append(1)
    results = vote_logic(trees)
                          else:
                            if time.time() < deadline:
                              if x[8] <= 3.1200000048:
                                if time.time() < deadline:
                                  if x[9] <= 3.1750000715:
                                    trees.append(1)
    results = vote_logic(trees)
                                  else:
                                    trees.append(0)
    results = vote_logic(trees)
                              else:
                                trees.append(1)
    results = vote_logic(trees)
                      else:
                        trees.append(1)
    results = vote_logic(trees)
    
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
