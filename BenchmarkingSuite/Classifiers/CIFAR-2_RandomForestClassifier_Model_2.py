import time
"""

***** Metadata ******
Dataset: CIFAR-2
Fold: 2 of K-Fold cross validaiton
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
        if x[59] <= 0.5529412031:
            if x[2563] <= 0.2450980395:
                if x[1145] <= 0.2627451122:
                    if x[2739] <= 0.1666666716:
                        if x[2699] <= 0.0803921595:
                            results.append(1)
                        else:
                            if x[2419] <= 0.3431372643:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[194] <= 0.4921568632:
                            if x[2458] <= 0.1039215699:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[960] <= 0.5784313977:
                        if x[2335] <= 0.6509804130:
                            if x[1976] <= 0.0882352963:
                                results.append(0)
                            else:
                                if x[519] <= 0.5333333611:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1529] <= 0.4058823586:
                            results.append(0)
                        else:
                            results.append(1)
            else:
                if x[1130] <= 0.5196078718:
                    if x[2328] <= 0.1627451032:
                        if x[399] <= 0.3274509907:
                            if x[1814] <= 0.4039215744:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[720] <= 0.5411764979:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1619] <= 0.6254902184:
                            if x[2922] <= 0.9254902005:
                                if x[2185] <= 0.1039215699:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[1043] <= 0.3470588326:
                                results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[1913] <= 0.4215686321:
                        if x[95] <= 0.2568627521:
                            if x[1480] <= 0.4980392307:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2682] <= 0.3313725591:
                                results.append(1)
                            else:
                                if x[2849] <= 0.5372549295:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[14] <= 0.5274510086:
                            if x[1422] <= 0.3509804010:
                                results.append(0)
                            else:
                                if x[1960] <= 0.8666666746:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[151] <= 0.5235294253:
                                results.append(0)
                            else:
                                results.append(1)
        else:
            if x[317] <= 0.6764706075:
                if x[1289] <= 0.2941176593:
                    if x[2634] <= 0.1470588297:
                        results.append(0)
                    else:
                        if x[1113] <= 0.7000000179:
                            if x[1353] <= 0.2941176593:
                                if x[2347] <= 0.4137254953:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[985] <= 0.2254901975:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2802] <= 0.3588235378:
                        if x[1220] <= 0.3274509907:
                            if x[553] <= 0.5431372821:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[11] <= 0.3372549117:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1954] <= 0.2588235438:
                            if x[625] <= 0.6823529601:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2268] <= 0.7862745225:
                                if x[1536] <= 0.3274509907:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1723] <= 0.5666666925:
                                    results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[1738] <= 0.5745098293:
                    if x[395] <= 0.5862745345:
                        if x[404] <= 0.5274509937:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[745] <= 0.2647058964:
                            results.append(0)
                        else:
                            if x[1106] <= 0.4333333373:
                                if x[1705] <= 0.4862745106:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2334] <= 0.8098039329:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[1388] <= 0.2686274648:
                        if x[2009] <= 0.7450980544:
                            if x[2433] <= 0.3509804010:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2281] <= 0.4549019635:
                            if x[1529] <= 0.1725490242:
                                results.append(1)
                            else:
                                if x[2721] <= 0.8431372643:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[551] <= 0.9392156899:
                                if x[924] <= 0.8156862855:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 1
    if time.time() < deadline or interrupt_flag.is_set():
        if x[161] <= 0.5313725770:
            if x[1754] <= 0.5843137503:
                if x[1268] <= 0.7588235438:
                    if x[2848] <= 0.1509803981:
                        if x[1895] <= 0.2862745225:
                            if x[1664] <= 0.2686274648:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[318] <= 0.2666666731:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2083] <= 0.1901960820:
                            if x[1160] <= 0.3431372643:
                                if x[2471] <= 0.4196078479:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2433] <= 0.4705882370:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[2352] <= 0.0705882385:
                                if x[2473] <= 0.3392156959:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2752] <= 0.1607843190:
                                    results.append(0)
                                else:
                                    results.append(1)
                else:
                    results.append(0)
            else:
                if x[2640] <= 0.2215686291:
                    if x[151] <= 0.5392157137:
                        results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[1331] <= 0.4705882370:
                        if x[1467] <= 0.3764705956:
                            results.append(0)
                        else:
                            if x[2601] <= 0.3882353008:
                                if x[2216] <= 0.3235294223:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2037] <= 0.3823529482:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[1808] <= 0.4313725531:
                            results.append(0)
                        else:
                            if x[1221] <= 0.5313725770:
                                results.append(0)
                            else:
                                if x[1286] <= 0.4764705896:
                                    results.append(1)
                                else:
                                    results.append(1)
        else:
            if x[1475] <= 0.4352941215:
                if x[1007] <= 0.4490196109:
                    if x[2181] <= 0.2843137383:
                        if x[1268] <= 0.5019607991:
                            if x[2867] <= 0.2529411912:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[317] <= 0.7764706016:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1618] <= 0.3627451062:
                            if x[2958] <= 0.6333333552:
                                if x[1199] <= 0.4000000060:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[604] <= 0.4235294163:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[730] <= 0.1352941208:
                                results.append(0)
                            else:
                                if x[1160] <= 0.1901960820:
                                    results.append(1)
                                else:
                                    results.append(1)
                else:
                    if x[2805] <= 0.4176470637:
                        if x[2983] <= 0.5980392396:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2806] <= 0.6509804130:
                            if x[836] <= 0.6411764920:
                                if x[198] <= 0.5607843399:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[1410] <= 0.5588235557:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[1815] <= 0.6784313917:
                                if x[1112] <= 0.6725490391:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[599] <= 0.6901960969:
                                    results.append(1)
                                else:
                                    results.append(0)
            else:
                if x[2148] <= 0.5745098293:
                    if x[170] <= 0.6235294342:
                        if x[566] <= 0.5725490451:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[662] <= 0.1784313768:
                            results.append(1)
                        else:
                            if x[431] <= 0.2803921625:
                                results.append(0)
                            else:
                                if x[2457] <= 0.6764706075:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[2742] <= 0.3823529482:
                        if x[2176] <= 0.3705882430:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2367] <= 0.2803921700:
                            results.append(0)
                        else:
                            if x[1668] <= 0.5549019873:
                                if x[2162] <= 0.3901960850:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2246] <= 0.4882353097:
                                    results.append(1)
                                else:
                                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 2
    if time.time() < deadline or interrupt_flag.is_set():
        if x[248] <= 0.6294117868:
            if x[2427] <= 0.1980392188:
                if x[2891] <= 0.3098039329:
                    if x[1382] <= 0.7686274648:
                        if x[2244] <= 0.0490196086:
                            results.append(0)
                        else:
                            if x[1112] <= 0.6529411972:
                                if x[1775] <= 0.6450980604:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[1763] <= 0.1509803981:
                        results.append(1)
                    else:
                        if x[1012] <= 0.6470588446:
                            if x[344] <= 0.5627451241:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
            else:
                if x[2829] <= 0.0843137279:
                    if x[966] <= 0.3960784376:
                        results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[20] <= 0.4960784316:
                        if x[2342] <= 0.0823529437:
                            if x[2212] <= 0.4215686321:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[380] <= 0.7000000179:
                                if x[2644] <= 0.1392156929:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[2335] <= 0.5176470727:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[390] <= 0.2686274648:
                            if x[643] <= 0.4019607902:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2046] <= 0.2254901975:
                                if x[624] <= 0.4215686321:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2320] <= 0.3470588326:
                                    results.append(0)
                                else:
                                    results.append(1)
        else:
            if x[2331] <= 0.3235294223:
                if x[143] <= 0.6529411972:
                    if x[431] <= 0.6098039448:
                        if x[165] <= 0.6450980604:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        results.append(1)
                else:
                    if x[226] <= 0.9941176474:
                        if x[2332] <= 0.4431372583:
                            if x[3008] <= 0.1431372613:
                                if x[948] <= 0.5607843399:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1094] <= 0.2803921700:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
            else:
                if x[1478] <= 0.2960784435:
                    if x[1888] <= 0.3000000119:
                        if x[255] <= 0.8254902065:
                            if x[379] <= 0.8235294223:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2480] <= 0.3294117749:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[426] <= 0.3823529482:
                            results.append(0)
                        else:
                            if x[3006] <= 0.2450980470:
                                results.append(0)
                            else:
                                if x[2765] <= 0.7725490332:
                                    results.append(1)
                                else:
                                    results.append(1)
                else:
                    if x[287] <= 0.2941176593:
                        results.append(1)
                    else:
                        if x[1406] <= 0.4000000060:
                            if x[907] <= 0.6490196288:
                                if x[1019] <= 0.4019607902:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1675] <= 0.3549019694:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[800] <= 0.6764706075:
                                if x[1740] <= 0.6215686500:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2743] <= 0.7333333492:
                                    results.append(0)
                                else:
                                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 3
    if time.time() < deadline or interrupt_flag.is_set():
        if x[224] <= 0.7000000179:
            if x[2140] <= 0.3431372643:
                if x[2127] <= 0.3294117749:
                    if x[2594] <= 0.2568627596:
                        if x[362] <= 0.2450980395:
                            if x[2049] <= 0.0862745121:
                                results.append(0)
                            else:
                                if x[2850] <= 0.1921568662:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[973] <= 0.5313725621:
                                if x[1077] <= 0.2568627596:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[3061] <= 0.6588235497:
                            if x[1179] <= 0.2803921700:
                                if x[1361] <= 0.2882353067:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2410] <= 0.2352941185:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[70] <= 0.4901960790:
                                if x[1722] <= 0.3176470622:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[2191] <= 0.2294117659:
                        if x[396] <= 0.4098039269:
                            if x[1457] <= 0.3941176534:
                                if x[965] <= 0.1470588297:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[393] <= 0.6764706075:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2839] <= 0.1862745136:
                            results.append(0)
                        else:
                            if x[1869] <= 0.1352941245:
                                results.append(0)
                            else:
                                if x[2655] <= 0.8254902065:
                                    results.append(1)
                                else:
                                    results.append(1)
            else:
                if x[2626] <= 0.1549019665:
                    if x[1022] <= 0.3764705956:
                        results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[1553] <= 0.5039215982:
                        if x[2079] <= 0.1058823541:
                            if x[208] <= 0.3411764801:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1364] <= 0.6039215922:
                                if x[1086] <= 0.2764706016:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[927] <= 0.3568627536:
                            if x[418] <= 0.5254902244:
                                if x[1241] <= 0.2196078449:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1792] <= 0.5196078718:
                                if x[1849] <= 0.4215686321:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[710] <= 0.6490196288:
                                    results.append(1)
                                else:
                                    results.append(0)
        else:
            if x[2334] <= 0.3313725591:
                if x[1289] <= 0.2431372628:
                    if x[2801] <= 0.3450980484:
                        results.append(1)
                    else:
                        if x[1772] <= 0.2549019679:
                            results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[209] <= 0.5470588505:
                        results.append(1)
                    else:
                        if x[707] <= 0.9980392158:
                            if x[2632] <= 0.0509803928:
                                results.append(0)
                            else:
                                if x[1381] <= 0.1627451032:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(0)
            else:
                if x[1289] <= 0.6490196288:
                    if x[2739] <= 0.3470588326:
                        if x[2704] <= 0.3725490272:
                            results.append(0)
                        else:
                            if x[2475] <= 0.3882353008:
                                results.append(0)
                            else:
                                if x[1075] <= 0.5666666925:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[496] <= 0.7078431547:
                            if x[1354] <= 0.2470588312:
                                results.append(0)
                            else:
                                if x[1623] <= 0.4254902005:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1539] <= 0.5294117928:
                                if x[1010] <= 0.3392156959:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[3050] <= 0.8921568692:
                                    results.append(1)
                                else:
                                    results.append(0)
                else:
                    if x[2479] <= 0.6764706075:
                        if x[2636] <= 0.2078431398:
                            results.append(1)
                        else:
                            if x[2786] <= 0.8921568692:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2797] <= 0.7823529541:
                            results.append(1)
                        else:
                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 4
    if time.time() < deadline or interrupt_flag.is_set():
        if x[404] <= 0.6411764920:
            if x[2551] <= 0.2215686291:
                if x[1499] <= 0.4450980425:
                    if x[680] <= 0.2745098174:
                        if x[1471] <= 0.6431372762:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2629] <= 0.2372549027:
                            if x[1252] <= 0.4549019635:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1823] <= 0.5254902095:
                                if x[1954] <= 0.1980392188:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[2349] <= 0.6392157078:
                        if x[944] <= 0.6627451181:
                            if x[1793] <= 0.2333333418:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        results.append(1)
            else:
                if x[2433] <= 0.2529411912:
                    if x[3004] <= 0.5843137503:
                        if x[908] <= 0.4627451003:
                            if x[1999] <= 0.2627451047:
                                results.append(0)
                            else:
                                if x[615] <= 0.2568627596:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[776] <= 0.3098039329:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[975] <= 0.5156863034:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[254] <= 0.4803921580:
                        if x[2658] <= 0.1980392188:
                            if x[904] <= 0.3372549117:
                                if x[2470] <= 0.2098039240:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[133] <= 0.9000000060:
                                if x[828] <= 0.2843137383:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1481] <= 0.4823529422:
                            if x[1878] <= 0.3549019694:
                                if x[1717] <= 0.4901960939:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1674] <= 0.7549019754:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[2499] <= 0.5490196347:
                                if x[903] <= 0.7333333492:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1398] <= 0.4803921580:
                                    results.append(0)
                                else:
                                    results.append(1)
        else:
            if x[2790] <= 0.4960784316:
                if x[2530] <= 0.6117647290:
                    if x[1289] <= 0.3882353008:
                        if x[1871] <= 0.2725490332:
                            if x[1728] <= 0.4098039269:
                                results.append(0)
                            else:
                                if x[1635] <= 0.4137254953:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[851] <= 0.6000000238:
                                if x[637] <= 0.5235294253:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[502] <= 0.6705882549:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[101] <= 0.6431372762:
                            if x[393] <= 0.4941176623:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1584] <= 0.1725490242:
                                results.append(0)
                            else:
                                if x[2944] <= 0.7078431547:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[207] <= 0.7607843280:
                        if x[126] <= 0.5921568871:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
            else:
                if x[377] <= 0.6686274707:
                    if x[2118] <= 0.4078431427:
                        results.append(0)
                    else:
                        if x[721] <= 0.6901960969:
                            if x[773] <= 0.2843137383:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[511] <= 0.5176470876:
                        if x[1430] <= 0.3058823645:
                            results.append(0)
                        else:
                            if x[2834] <= 0.7431372702:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[1364] <= 0.4764705896:
                            if x[2256] <= 0.4862745255:
                                if x[838] <= 0.4254902005:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[51] <= 0.9882352948:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[1207] <= 0.2803921700:
                                results.append(0)
                            else:
                                if x[1455] <= 0.9019607902:
                                    results.append(0)
                                else:
                                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 5
    if time.time() < deadline or interrupt_flag.is_set():
        if x[284] <= 0.5313725770:
            if x[2451] <= 0.2764706016:
                if x[2433] <= 0.3313725591:
                    if x[2681] <= 0.0764705911:
                        results.append(1)
                    else:
                        if x[1685] <= 0.3019607961:
                            if x[327] <= 0.1960784346:
                                results.append(1)
                            else:
                                if x[514] <= 0.5000000149:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[256] <= 0.5705882609:
                                if x[1253] <= 0.1745098084:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[1262] <= 0.5019607991:
                        if x[2331] <= 0.2764706016:
                            results.append(1)
                        else:
                            if x[1751] <= 0.5274510086:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2165] <= 0.2117647082:
                            results.append(0)
                        else:
                            results.append(1)
            else:
                if x[38] <= 0.4764705896:
                    if x[2281] <= 0.1098039225:
                        if x[2405] <= 0.4117647111:
                            if x[1065] <= 0.2823529541:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2656] <= 0.1254901998:
                            results.append(0)
                        else:
                            if x[2073] <= 0.1352941245:
                                results.append(0)
                            else:
                                if x[2279] <= 0.8098039329:
                                    results.append(1)
                                else:
                                    results.append(1)
                else:
                    if x[2823] <= 0.2941176593:
                        if x[1785] <= 0.4176470637:
                            results.append(1)
                        else:
                            if x[2572] <= 0.1901960820:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1866] <= 0.8294117749:
                            if x[2966] <= 0.7666666806:
                                if x[113] <= 0.8823529482:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
        else:
            if x[1379] <= 0.3509804010:
                if x[2368] <= 0.4019607902:
                    if x[2732] <= 0.3980392218:
                        if x[2165] <= 0.0764705911:
                            results.append(0)
                        else:
                            if x[2643] <= 0.1333333403:
                                results.append(0)
                            else:
                                if x[829] <= 0.5058823675:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[2433] <= 0.5058823824:
                            results.append(0)
                        else:
                            if x[1775] <= 0.2215686291:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[2547] <= 0.2960784435:
                        if x[2882] <= 0.5686274767:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2634] <= 0.2647058889:
                            results.append(0)
                        else:
                            if x[842] <= 0.9294117689:
                                if x[642] <= 0.2960784435:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
            else:
                if x[2238] <= 0.4862745106:
                    if x[1920] <= 0.9725490212:
                        if x[1301] <= 0.4960784316:
                            if x[2952] <= 0.3333333433:
                                if x[2701] <= 0.3352941275:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2557] <= 0.7000000179:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[707] <= 0.6039215922:
                                if x[1672] <= 0.5745098293:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[2426] <= 0.3450980484:
                        if x[1286] <= 0.3745098114:
                            results.append(1)
                        else:
                            if x[1141] <= 0.3725490272:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2034] <= 0.4666666687:
                            if x[1478] <= 0.5784313977:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1656] <= 0.3666666746:
                                if x[3042] <= 0.4745098054:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1515] <= 0.4470588267:
                                    results.append(0)
                                else:
                                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 6
    if time.time() < deadline or interrupt_flag.is_set():
        if x[380] <= 0.6058823764:
            if x[2542] <= 0.1784313768:
                if x[2526] <= 0.2803921700:
                    if x[1352] <= 0.0843137279:
                        if x[1904] <= 0.3470588326:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[739] <= 0.6647059023:
                            if x[1551] <= 0.1274509877:
                                results.append(0)
                            else:
                                if x[1003] <= 0.1607843190:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[1046] <= 0.5960784554:
                        if x[976] <= 0.3549019694:
                            if x[1962] <= 0.3960784376:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2853] <= 0.3607843220:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        results.append(0)
            else:
                if x[89] <= 0.5196078718:
                    if x[2634] <= 0.2137254924:
                        if x[2983] <= 0.2568627521:
                            if x[2941] <= 0.1960784346:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[664] <= 0.3411764801:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[1472] <= 0.6705882549:
                            if x[1977] <= 0.1098039225:
                                if x[239] <= 0.3039215803:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[137] <= 0.8529411852:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2449] <= 0.3490196168:
                                if x[2763] <= 0.5392156988:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[59] <= 0.3764705956:
                                    results.append(1)
                                else:
                                    results.append(0)
                else:
                    if x[951] <= 0.5078431666:
                        if x[1315] <= 0.5254902244:
                            if x[2080] <= 0.5117647350:
                                results.append(0)
                            else:
                                if x[541] <= 0.4137254953:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[972] <= 0.2764706016:
                                results.append(0)
                            else:
                                if x[14] <= 0.6588235497:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[1775] <= 0.6627451181:
                            if x[286] <= 0.4431372583:
                                results.append(0)
                            else:
                                if x[178] <= 0.7196078598:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
        else:
            if x[1490] <= 0.4509803951:
                if x[1528] <= 0.4450980425:
                    if x[1351] <= 0.5313725770:
                        if x[296] <= 0.1960784420:
                            results.append(0)
                        else:
                            if x[1277] <= 0.2647058964:
                                if x[3043] <= 0.5058823824:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[2986] <= 0.6333333552:
                            if x[1962] <= 0.3078431487:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1910] <= 0.2941176593:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[1284] <= 0.6392157078:
                        if x[765] <= 0.4313725531:
                            if x[1905] <= 0.4000000060:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[599] <= 0.6549019814:
                                if x[2802] <= 0.2705882490:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[1019] <= 0.5058823675:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[615] <= 0.5725490302:
                            results.append(1)
                        else:
                            if x[1391] <= 0.3274509907:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[500] <= 0.5784313977:
                    if x[1149] <= 0.8843137324:
                        if x[2445] <= 0.4176470637:
                            if x[690] <= 0.2294117659:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2724] <= 0.4470588267:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        results.append(1)
                else:
                    if x[1942] <= 0.8686274588:
                        if x[218] <= 0.9941176474:
                            if x[1917] <= 0.9392156899:
                                if x[744] <= 0.2019607872:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2169] <= 0.4529411793:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2265] <= 0.3607843220:
                            results.append(0)
                        else:
                            results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 7
    if time.time() < deadline or interrupt_flag.is_set():
        if x[275] <= 0.6647059023:
            if x[2841] <= 0.2725490332:
                if x[1472] <= 0.4333333373:
                    if x[3011] <= 0.3352941275:
                        if x[1816] <= 0.3215686381:
                            if x[2204] <= 0.1784313768:
                                if x[2981] <= 0.2627451122:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[2258] <= 0.2039215788:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[2706] <= 0.2058823556:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[1481] <= 0.2470588312:
                            if x[696] <= 0.2980392277:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2037] <= 0.3549019694:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[2118] <= 0.0666666701:
                        results.append(1)
                    else:
                        if x[2640] <= 0.3431372643:
                            if x[792] <= 0.7039215863:
                                if x[1327] <= 0.2176470608:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
            else:
                if x[2464] <= 0.0627450999:
                    if x[2201] <= 0.1764705926:
                        results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[1685] <= 0.8098039329:
                        if x[2332] <= 0.1980392188:
                            if x[2693] <= 0.3941176534:
                                if x[1848] <= 0.7058823705:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1772] <= 0.5392157137:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[386] <= 0.5000000149:
                                if x[1424] <= 0.6117647290:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[585] <= 0.4254902005:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[1055] <= 0.3549019694:
                            if x[1083] <= 0.2235294133:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[571] <= 0.4941176623:
                                results.append(0)
                            else:
                                results.append(0)
        else:
            if x[1208] <= 0.3588235378:
                if x[1807] <= 0.3568627536:
                    if x[2170] <= 0.6254902184:
                        if x[850] <= 0.8431372643:
                            if x[208] <= 0.4901960790:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1295] <= 0.2803921700:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[2422] <= 0.3862745166:
                        if x[321] <= 0.6647059023:
                            if x[1676] <= 0.1882352978:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[1767] <= 0.2294117734:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1502] <= 0.6039215922:
                            if x[746] <= 0.9607843161:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
            else:
                if x[2466] <= 0.5823529661:
                    if x[2424] <= 0.4588235319:
                        if x[917] <= 0.3490196168:
                            results.append(0)
                        else:
                            if x[1185] <= 0.4568627477:
                                if x[1874] <= 0.3333333433:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2320] <= 0.5803921819:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[299] <= 0.7176470757:
                            if x[2867] <= 0.6137255132:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[2333] <= 0.3549019694:
                                results.append(1)
                            else:
                                if x[264] <= 0.5549019873:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[1004] <= 0.6862745285:
                        if x[1539] <= 0.7607843280:
                            if x[2283] <= 0.7000000179:
                                if x[1687] <= 0.3784313798:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1824] <= 0.5333333611:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[1811] <= 0.8117647171:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2042] <= 0.7588235438:
                            results.append(0)
                        else:
                            if x[2082] <= 0.6333333552:
                                results.append(0)
                            else:
                                results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 8
    if time.time() < deadline or interrupt_flag.is_set():
        if x[239] <= 0.6372549236:
            if x[2547] <= 0.1980392188:
                if x[1880] <= 0.3882353008:
                    if x[1457] <= 0.1450980455:
                        results.append(1)
                    else:
                        if x[1382] <= 0.2705882490:
                            if x[178] <= 0.6431372762:
                                if x[2405] <= 0.3450980484:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1420] <= 0.3921568692:
                                if x[420] <= 0.1549019665:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[2779] <= 0.1000000015:
                        results.append(1)
                    else:
                        if x[1535] <= 0.3803921640:
                            results.append(0)
                        else:
                            results.append(0)
            else:
                if x[1966] <= 0.2686274648:
                    if x[185] <= 0.6764706075:
                        if x[2181] <= 0.3470588326:
                            if x[1941] <= 0.4176470637:
                                if x[45] <= 0.2764706016:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[464] <= 0.4176470637:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[652] <= 0.6862745285:
                                if x[2755] <= 0.2156862766:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1747] <= 0.5568627715:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[311] <= 0.4882352948:
                        if x[1784] <= 0.6921568811:
                            if x[2449] <= 0.1137254909:
                                results.append(0)
                            else:
                                if x[942] <= 0.9176470637:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2268] <= 0.5274510086:
                                if x[1619] <= 0.3058823645:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1783] <= 0.8980392218:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[2751] <= 0.1588235348:
                            if x[1995] <= 0.5960784554:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[77] <= 0.4803921580:
                                if x[2040] <= 0.3725490272:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[105] <= 0.5000000149:
                                    results.append(0)
                                else:
                                    results.append(1)
        else:
            if x[2265] <= 0.4647058845:
                if x[908] <= 0.4843137264:
                    if x[557] <= 0.5784313977:
                        if x[1871] <= 0.3862745166:
                            if x[2363] <= 0.1725490242:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[3070] <= 0.4215686321:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1072] <= 0.9372549057:
                            if x[1240] <= 0.6568627656:
                                if x[2248] <= 0.0921568647:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2436] <= 0.3352941275:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[1403] <= 0.2450980470:
                        if x[2122] <= 0.4686274529:
                            if x[1962] <= 0.3862745166:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1096] <= 0.5725490451:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1443] <= 0.9509803951:
                            if x[29] <= 0.6666666865:
                                if x[2827] <= 0.4313725531:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
            else:
                if x[1094] <= 0.4843137264:
                    if x[1714] <= 0.4235294163:
                        if x[275] <= 0.3529411852:
                            results.append(1)
                        else:
                            if x[1350] <= 0.7000000179:
                                if x[965] <= 0.2803921700:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2134] <= 0.1921568662:
                            results.append(0)
                        else:
                            if x[995] <= 0.5745098293:
                                if x[1543] <= 0.3725490272:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[92] <= 0.5960784554:
                        if x[2102] <= 0.4431372583:
                            results.append(0)
                        else:
                            if x[2064] <= 0.6588235497:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[1939] <= 0.5901961029:
                            if x[1931] <= 0.2019607872:
                                results.append(1)
                            else:
                                if x[820] <= 0.5823529661:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[1604] <= 0.3725490272:
                                results.append(1)
                            else:
                                if x[1476] <= 0.5372549295:
                                    results.append(0)
                                else:
                                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 9
    if time.time() < deadline or interrupt_flag.is_set():
        if x[362] <= 0.4921568632:
            if x[2454] <= 0.3627451062:
                if x[2826] <= 0.0607843157:
                    if x[353] <= 0.3803921640:
                        results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[1475] <= 0.4529411793:
                        if x[2987] <= 0.4098039269:
                            if x[2000] <= 0.5588235557:
                                if x[2733] <= 0.2450980395:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1619] <= 0.2235294133:
                                if x[2853] <= 0.5254902244:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[169] <= 0.4882353097:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[1176] <= 0.7431372702:
                            if x[577] <= 0.1901960820:
                                results.append(1)
                            else:
                                if x[2104] <= 0.5901961029:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            results.append(1)
            else:
                if x[2550] <= 0.2588235438:
                    results.append(0)
                else:
                    if x[1287] <= 0.2823529541:
                        if x[80] <= 0.6039215922:
                            if x[1664] <= 0.5156863034:
                                if x[515] <= 0.1019607857:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[1357] <= 0.3039215803:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[1107] <= 0.2039215714:
                            if x[2178] <= 0.3411764801:
                                results.append(0)
                            else:
                                if x[1367] <= 0.3803921640:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[2538] <= 0.1529411823:
                                results.append(1)
                            else:
                                if x[2767] <= 0.1156862751:
                                    results.append(1)
                                else:
                                    results.append(1)
        else:
            if x[710] <= 0.6039215922:
                if x[2454] <= 0.2000000030:
                    if x[2870] <= 0.1313725524:
                        results.append(1)
                    else:
                        if x[329] <= 0.3058823645:
                            results.append(1)
                        else:
                            if x[1175] <= 0.2196078449:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[1342] <= 0.3823529482:
                        if x[1740] <= 0.4039215744:
                            if x[743] <= 0.7058823705:
                                if x[512] <= 0.2431372628:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1380] <= 0.1509803981:
                                results.append(0)
                            else:
                                if x[2158] <= 0.3254902065:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[3022] <= 0.0803921595:
                            results.append(0)
                        else:
                            if x[1095] <= 0.8921568692:
                                if x[2519] <= 0.2294117659:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
            else:
                if x[101] <= 0.5588235557:
                    if x[2154] <= 0.2921568751:
                        if x[2069] <= 0.2019607872:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1057] <= 0.4196078479:
                            results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[1007] <= 0.2647058964:
                        if x[1398] <= 0.5039215833:
                            if x[2355] <= 0.3176470697:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[1100] <= 0.4431372583:
                            if x[1714] <= 0.4078431427:
                                results.append(0)
                            else:
                                if x[1438] <= 0.7235294282:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[884] <= 0.2313725501:
                                results.append(1)
                            else:
                                if x[773] <= 0.5901961029:
                                    results.append(0)
                                else:
                                    results.append(0)
    
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
