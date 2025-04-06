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
        if x[119] <= 0.6882353127:
            if x[2646] <= 0.1784313768:
                if x[921] <= 0.4764705896:
                    if x[2402] <= 0.1470588297:
                        results.append(1)
                    else:
                        if x[2470] <= 0.3313725591:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[2426] <= 0.2725490332:
                        if x[640] <= 0.4470588267:
                            if x[1503] <= 0.7078431547:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1472] <= 0.4392156899:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        results.append(1)
            else:
                if x[131] <= 0.5039215982:
                    if x[2347] <= 0.1156862751:
                        if x[886] <= 0.1823529452:
                            results.append(1)
                        else:
                            if x[1840] <= 0.3098039329:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2139] <= 0.4098039269:
                            if x[1265] <= 0.3980392218:
                                if x[472] <= 0.6588235497:
                                    if x[1784] <= 0.0607843157:
                                        results.append(0)
                                    else:
                                        if x[2693] <= 0.5333333611:
                                            if x[1814] <= 0.5235294402:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1173] <= 0.2274509817:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                else:
                                    if x[1318] <= 0.3470588326:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[603] <= 0.3745098114:
                                    if x[2278] <= 0.4235294163:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1613] <= 0.4980392307:
                                        results.append(1)
                                    else:
                                        results.append(0)
                        else:
                            if x[2741] <= 0.1000000015:
                                results.append(1)
                            else:
                                if x[474] <= 0.8254902065:
                                    if x[1839] <= 0.1372549050:
                                        results.append(1)
                                    else:
                                        if x[1289] <= 0.8568627536:
                                            if x[1312] <= 0.9156862795:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(1)
                else:
                    if x[249] <= 0.4843137264:
                        if x[794] <= 0.3960784376:
                            if x[175] <= 0.5372549295:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2009] <= 0.2352941260:
                                if x[395] <= 0.5607843399:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1909] <= 0.6784313917:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[1858] <= 0.8490196168:
                            if x[2171] <= 0.1176470630:
                                results.append(0)
                            else:
                                if x[1178] <= 0.6568627656:
                                    if x[521] <= 0.6176470816:
                                        if x[565] <= 0.4176470637:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[782] <= 0.2823529541:
                                            results.append(0)
                                        else:
                                            if x[2658] <= 0.5274510086:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    if x[727] <= 0.6529411972:
                                        results.append(0)
                                    else:
                                        results.append(1)
                        else:
                            results.append(0)
        else:
            if x[1106] <= 0.3509804010:
                if x[2741] <= 0.1254901998:
                    results.append(0)
                else:
                    if x[2044] <= 0.4843137264:
                        if x[1281] <= 0.4980392307:
                            if x[1496] <= 0.2529411912:
                                results.append(1)
                            else:
                                if x[156] <= 0.8137255013:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[875] <= 0.3274509907:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2329] <= 0.3411764801:
                            results.append(0)
                        else:
                            if x[1402] <= 0.6666666865:
                                results.append(1)
                            else:
                                results.append(1)
            else:
                if x[2473] <= 0.7549019754:
                    if x[746] <= 0.6078431606:
                        if x[2292] <= 0.5901961029:
                            if x[2117] <= 0.2980392277:
                                if x[527] <= 0.4627451003:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1944] <= 0.6215686500:
                                    if x[542] <= 0.6509804130:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[762] <= 0.4450980425:
                                results.append(0)
                            else:
                                if x[2742] <= 0.8039215803:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[197] <= 0.5411764830:
                            results.append(1)
                        else:
                            if x[2448] <= 0.7803921700:
                                if x[1757] <= 0.7686274648:
                                    if x[2068] <= 0.1078431383:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1932] <= 0.5254902244:
                                        results.append(0)
                                    else:
                                        if x[2503] <= 0.6117647290:
                                            results.append(0)
                                        else:
                                            results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[1257] <= 0.6882353127:
                        if x[648] <= 0.6078431606:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[696] <= 0.8607843220:
                            if x[210] <= 0.7372549176:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 1
    if time.time() < deadline or interrupt_flag.is_set():
        if x[62] <= 0.6176470816:
            if x[2334] <= 0.3411764801:
                if x[299] <= 0.3705882430:
                    if x[1553] <= 0.5215686560:
                        if x[2638] <= 0.1431372613:
                            if x[2252] <= 0.1078431383:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2597] <= 0.4686274529:
                                if x[1999] <= 0.7411764860:
                                    if x[2758] <= 0.7666666806:
                                        if x[2459] <= 0.1588235348:
                                            if x[1764] <= 0.5901961029:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1671] <= 0.1490196139:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2223] <= 0.3843137324:
                            if x[2225] <= 0.0705882367:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[699] <= 0.3137255013:
                        if x[323] <= 0.5901961029:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1649] <= 0.5588235557:
                            if x[2681] <= 0.2156862766:
                                if x[1327] <= 0.3862745166:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1451] <= 0.4333333373:
                                    if x[1167] <= 0.5431372672:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[511] <= 0.6000000238:
                                        results.append(1)
                                    else:
                                        results.append(0)
                        else:
                            if x[1586] <= 0.3235294223:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[2820] <= 0.1196078472:
                    if x[1674] <= 0.6647059023:
                        results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[1358] <= 0.4843137264:
                        if x[2188] <= 0.0647058841:
                            results.append(0)
                        else:
                            if x[1581] <= 0.9098039269:
                                if x[2551] <= 0.1470588297:
                                    if x[15] <= 0.4666666836:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[2159] <= 0.0647058859:
                                        results.append(0)
                                    else:
                                        if x[1978] <= 0.1372549087:
                                            results.append(1)
                                        else:
                                            if x[2645] <= 0.0862745121:
                                                results.append(1)
                                            else:
                                                results.append(1)
                            else:
                                if x[2869] <= 0.3784313798:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[1666] <= 0.2960784435:
                            if x[682] <= 0.4725490361:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2892] <= 0.5588235557:
                                if x[1996] <= 0.4705882370:
                                    if x[1947] <= 0.3549019694:
                                        results.append(0)
                                    else:
                                        if x[2] <= 0.5294117928:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[1210] <= 0.6294117868:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[1742] <= 0.4254902005:
                                    results.append(1)
                                else:
                                    results.append(1)
        else:
            if x[2292] <= 0.6529411972:
                if x[929] <= 0.5313725770:
                    if x[1735] <= 0.2882353067:
                        if x[181] <= 0.3470588326:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1085] <= 0.4745098054:
                            if x[2617] <= 0.2215686291:
                                if x[2896] <= 0.3823529556:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1481] <= 0.5333333462:
                                    if x[1274] <= 0.3058823645:
                                        if x[519] <= 0.4058823586:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[1735] <= 0.4490196109:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2287] <= 0.5058823675:
                                        results.append(0)
                                    else:
                                        results.append(1)
                        else:
                            if x[1897] <= 0.3882353008:
                                if x[98] <= 0.6215686500:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1172] <= 0.5921568871:
                                    if x[2269] <= 0.6490196288:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2664] <= 0.3470588326:
                                        results.append(0)
                                    else:
                                        results.append(1)
                else:
                    if x[920] <= 0.5352941453:
                        if x[2134] <= 0.5215686560:
                            if x[1818] <= 0.7862745225:
                                if x[2440] <= 0.2039215714:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
                    else:
                        if x[1730] <= 0.2764706016:
                            if x[751] <= 0.6803921759:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1817] <= 0.1764705926:
                                results.append(0)
                            else:
                                if x[2779] <= 0.7509804070:
                                    if x[485] <= 0.2843137309:
                                        results.append(0)
                                    else:
                                        if x[2141] <= 0.7470588386:
                                            results.append(0)
                                        else:
                                            if x[323] <= 0.8117647171:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                else:
                                    if x[2463] <= 0.4705882370:
                                        results.append(0)
                                    else:
                                        results.append(0)
            else:
                if x[1936] <= 0.2490196154:
                    if x[1978] <= 0.3960784376:
                        results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[2811] <= 0.2568627521:
                        results.append(0)
                    else:
                        if x[1261] <= 0.9019607902:
                            if x[649] <= 0.7313725650:
                                if x[365] <= 0.8294117749:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1239] <= 0.6666666865:
                                    results.append(0)
                                else:
                                    if x[1878] <= 0.4901960939:
                                        results.append(0)
                                    else:
                                        if x[2833] <= 0.8137255013:
                                            results.append(1)
                                        else:
                                            results.append(1)
                        else:
                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 2
    if time.time() < deadline or interrupt_flag.is_set():
        if x[116] <= 0.5980392396:
            if x[2541] <= 0.2294117659:
                if x[1288] <= 0.3333333433:
                    if x[1560] <= 0.6254902184:
                        if x[2567] <= 0.0705882367:
                            results.append(0)
                        else:
                            if x[556] <= 0.1686274558:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2512] <= 0.2019607872:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2424] <= 0.4725490212:
                        if x[943] <= 0.7117647231:
                            if x[1472] <= 0.3921568692:
                                if x[889] <= 0.2960784435:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2539] <= 0.1764705926:
                            results.append(0)
                        else:
                            results.append(1)
            else:
                if x[2074] <= 0.1862745136:
                    if x[2849] <= 0.2000000030:
                        results.append(1)
                    else:
                        if x[2437] <= 0.5156863034:
                            if x[2404] <= 0.5000000149:
                                if x[251] <= 0.4058823586:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1608] <= 0.2980392277:
                                results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[1483] <= 0.7862745225:
                        if x[2235] <= 0.3509804010:
                            if x[2603] <= 0.3549019694:
                                if x[1230] <= 0.1666666716:
                                    results.append(1)
                                else:
                                    if x[1956] <= 0.6882353127:
                                        if x[1987] <= 0.1784313768:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[2964] <= 0.6980392337:
                                    if x[89] <= 0.4294117689:
                                        if x[2260] <= 0.7039215863:
                                            if x[2361] <= 0.3705882430:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[311] <= 0.2588235363:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[1574] <= 0.3117647171:
                                        results.append(1)
                                    else:
                                        results.append(0)
                        else:
                            if x[2755] <= 0.2039215714:
                                if x[1853] <= 0.3686274588:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2041] <= 0.1196078435:
                                    results.append(0)
                                else:
                                    if x[2192] <= 0.6117647290:
                                        if x[2716] <= 0.3313725591:
                                            if x[789] <= 0.3392156959:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[2179] <= 0.2039215714:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[1860] <= 0.3803921640:
                                            if x[2563] <= 0.7196078598:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                    else:
                        if x[2176] <= 0.6196078658:
                            if x[786] <= 0.3313725591:
                                results.append(1)
                            else:
                                if x[2631] <= 0.4196078479:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
        else:
            if x[2365] <= 0.3823529482:
                if x[1032] <= 0.1627451032:
                    results.append(1)
                else:
                    if x[2605] <= 0.6686274707:
                        if x[931] <= 0.3078431487:
                            if x[745] <= 0.4960784465:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1516] <= 0.8647058904:
                                if x[2338] <= 0.5509804189:
                                    if x[397] <= 0.3215686381:
                                        results.append(0)
                                    else:
                                        if x[1559] <= 0.0882352963:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[1096] <= 0.5509804189:
                                        if x[2761] <= 0.3803921640:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2730] <= 0.6176470816:
                            if x[788] <= 0.8490196168:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[897] <= 0.7176470757:
                                results.append(0)
                            else:
                                results.append(1)
            else:
                if x[1094] <= 0.3666666746:
                    if x[3015] <= 0.3156862855:
                        if x[1425] <= 0.5235294253:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1214] <= 0.6117647290:
                            if x[811] <= 0.3039215803:
                                if x[2245] <= 0.3352941275:
                                    results.append(0)
                                else:
                                    if x[1058] <= 0.3254902065:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[404] <= 0.7196078598:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[110] <= 0.7117647231:
                        if x[2472] <= 0.5411764979:
                            if x[3050] <= 0.4215686321:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1876] <= 0.4901960939:
                                results.append(1)
                            else:
                                if x[1256] <= 0.5647059083:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[2427] <= 0.6372549236:
                            if x[2056] <= 0.4627451003:
                                if x[1548] <= 0.7431372702:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2050] <= 0.4803921580:
                                    results.append(1)
                                else:
                                    if x[2616] <= 0.5333333611:
                                        if x[188] <= 0.9764705896:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2093] <= 0.5980392396:
                                            results.append(1)
                                        else:
                                            results.append(0)
                        else:
                            if x[2391] <= 0.8666666746:
                                if x[2294] <= 0.5254902244:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[2256] <= 0.7588235438:
                                    results.append(0)
                                else:
                                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 3
    if time.time() < deadline or interrupt_flag.is_set():
        if x[200] <= 0.6058823764:
            if x[2841] <= 0.1352941245:
                if x[1530] <= 0.1352941245:
                    results.append(1)
                else:
                    if x[1083] <= 0.5529412031:
                        if x[2667] <= 0.4627451152:
                            if x[2903] <= 0.3901960850:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        results.append(1)
            else:
                if x[1421] <= 0.5392157137:
                    if x[2432] <= 0.1431372613:
                        if x[2939] <= 0.1921568662:
                            if x[2469] <= 0.4039215744:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[2446] <= 0.3882353008:
                                if x[1246] <= 0.1352941208:
                                    results.append(1)
                                else:
                                    if x[1328] <= 0.4549019635:
                                        if x[1697] <= 0.1156862751:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                if x[1853] <= 0.4529411793:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[1504] <= 0.1627451032:
                            if x[301] <= 0.4745098054:
                                if x[2650] <= 0.6215686500:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[2799] <= 0.4843137264:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[1491] <= 0.7647058964:
                                if x[1973] <= 0.0686274543:
                                    if x[1889] <= 0.2509803995:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2097] <= 0.8921568692:
                                        if x[1427] <= 0.4450980425:
                                            if x[1895] <= 0.6411764920:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[2131] <= 0.2686274648:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[2506] <= 0.4176470637:
                                    if x[1130] <= 0.2529411837:
                                        results.append(1)
                                    else:
                                        if x[1734] <= 0.2862745225:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2816] <= 0.6372549236:
                                        results.append(1)
                                    else:
                                        results.append(1)
                else:
                    if x[2661] <= 0.3431372643:
                        if x[2326] <= 0.5274510086:
                            if x[1886] <= 0.4274509847:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2353] <= 0.1235294156:
                            results.append(0)
                        else:
                            if x[1899] <= 0.2176470608:
                                results.append(0)
                            else:
                                if x[1682] <= 0.7784313858:
                                    if x[2628] <= 0.1862745136:
                                        results.append(0)
                                    else:
                                        if x[1515] <= 0.4568627477:
                                            if x[1364] <= 0.4000000060:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1277] <= 0.6843137443:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    results.append(0)
        else:
            if x[1307] <= 0.3509804010:
                if x[2313] <= 0.4470588267:
                    if x[2217] <= 0.4254902005:
                        if x[1273] <= 0.3117647171:
                            if x[654] <= 0.6901960969:
                                if x[1036] <= 0.3000000119:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[106] <= 0.9470588267:
                                if x[2408] <= 0.2019607872:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[242] <= 0.7235294282:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[1942] <= 0.2647058964:
                        if x[24] <= 0.9647058845:
                            if x[1260] <= 0.4509803951:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1009] <= 0.6235294342:
                            if x[630] <= 0.9647058845:
                                if x[1471] <= 0.5882353187:
                                    results.append(1)
                                else:
                                    if x[191] <= 0.7529411912:
                                        results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1960] <= 0.5274509937:
                                results.append(0)
                            else:
                                results.append(1)
            else:
                if x[347] <= 0.4686274529:
                    if x[890] <= 0.4627451003:
                        results.append(0)
                    else:
                        if x[1788] <= 0.4705882519:
                            results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[1183] <= 0.3392156959:
                        if x[1072] <= 0.5705882609:
                            if x[1454] <= 0.4960784465:
                                if x[2292] <= 0.2803921700:
                                    results.append(0)
                                else:
                                    if x[1093] <= 0.3294117749:
                                        results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[578] <= 0.8254902065:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1412] <= 0.2196078449:
                            if x[1657] <= 0.6117647290:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1899] <= 0.5470588505:
                                if x[1384] <= 0.2862745225:
                                    results.append(0)
                                else:
                                    if x[1916] <= 0.1862745136:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[476] <= 0.5921568871:
                                    results.append(1)
                                else:
                                    if x[968] <= 0.8058823645:
                                        if x[1295] <= 0.4411764741:
                                            results.append(0)
                                        else:
                                            if x[2534] <= 0.7745098174:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                    else:
                                        if x[1963] <= 0.5784313977:
                                            if x[2978] <= 0.6450980604:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1966] <= 0.7313725650:
                                                results.append(1)
                                            else:
                                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 4
    if time.time() < deadline or interrupt_flag.is_set():
        if x[80] <= 0.6098039448:
            if x[2649] <= 0.3352941275:
                if x[1292] <= 0.3470588326:
                    if x[2232] <= 0.1745098084:
                        if x[3050] <= 0.3627451062:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2721] <= 0.1274509877:
                            results.append(0)
                        else:
                            if x[1987] <= 0.5078431517:
                                if x[1493] <= 0.4294117689:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                else:
                    if x[593] <= 0.2137254924:
                        if x[2646] <= 0.0705882385:
                            results.append(0)
                        else:
                            if x[1582] <= 0.7117647231:
                                if x[794] <= 0.3000000119:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[804] <= 0.3607843220:
                            if x[989] <= 0.1843137294:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[374] <= 0.3803921640:
                                if x[980] <= 0.3686274588:
                                    results.append(0)
                                else:
                                    if x[1502] <= 0.3568627536:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[2663] <= 0.0686274543:
                                    results.append(0)
                                else:
                                    results.append(0)
            else:
                if x[2287] <= 0.0745098069:
                    if x[1003] <= 0.6313725710:
                        results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[1380] <= 0.9509803951:
                        if x[2151] <= 0.2313725501:
                            if x[1798] <= 0.1666666716:
                                results.append(0)
                            else:
                                if x[749] <= 0.0921568647:
                                    results.append(0)
                                else:
                                    if x[2565] <= 0.7607843280:
                                        results.append(1)
                                    else:
                                        results.append(0)
                        else:
                            if x[2473] <= 0.1215686314:
                                if x[1418] <= 0.2627451122:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2740] <= 0.1666666716:
                                    if x[1662] <= 0.5156862885:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1181] <= 0.7431372702:
                                        if x[321] <= 0.0803921595:
                                            if x[2846] <= 0.4862745255:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1884] <= 0.1313725524:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[2441] <= 0.2333333418:
                                            results.append(0)
                                        else:
                                            if x[1034] <= 0.6176470816:
                                                results.append(1)
                                            else:
                                                results.append(1)
                    else:
                        results.append(0)
        else:
            if x[2364] <= 0.5509804189:
                if x[2608] <= 0.7392157018:
                    if x[917] <= 0.5196078718:
                        if x[2253] <= 0.3078431487:
                            if x[3065] <= 0.7039215863:
                                if x[1445] <= 0.7607843280:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2539] <= 0.1666666716:
                                results.append(0)
                            else:
                                if x[928] <= 0.6921568811:
                                    if x[2424] <= 0.3705882430:
                                        if x[60] <= 0.7784313858:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[2976] <= 0.7901960909:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[2326] <= 0.6823529601:
                            if x[1288] <= 0.3509804010:
                                if x[2283] <= 0.4196078479:
                                    if x[422] <= 0.8392156959:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1053] <= 0.9725490212:
                                    if x[1303] <= 0.3529411852:
                                        results.append(0)
                                    else:
                                        if x[470] <= 0.4058823586:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[1379] <= 0.4098039269:
                        if x[2262] <= 0.3549019694:
                            results.append(1)
                        else:
                            results.append(1)
                    else:
                        if x[3020] <= 0.6470588446:
                            results.append(1)
                        else:
                            if x[2768] <= 0.8607843220:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[611] <= 0.6058823764:
                    if x[642] <= 0.2862745225:
                        results.append(0)
                    else:
                        if x[2174] <= 0.2313725501:
                            results.append(0)
                        else:
                            if x[1246] <= 0.2960784435:
                                results.append(1)
                            else:
                                if x[415] <= 0.8078431487:
                                    results.append(1)
                                else:
                                    results.append(1)
                else:
                    if x[1975] <= 0.6196078658:
                        if x[553] <= 0.4450980425:
                            if x[1789] <= 0.3803921640:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[1585] <= 0.2960784435:
                                results.append(1)
                            else:
                                if x[1959] <= 0.6196078658:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[338] <= 0.7235294282:
                            results.append(0)
                        else:
                            if x[630] <= 0.6294117868:
                                results.append(1)
                            else:
                                results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 5
    if time.time() < deadline or interrupt_flag.is_set():
        if x[149] <= 0.6215686500:
            if x[2430] <= 0.2490196154:
                if x[2659] <= 0.3019607961:
                    if x[1910] <= 0.0901960805:
                        results.append(1)
                    else:
                        if x[797] <= 0.1137254909:
                            results.append(0)
                        else:
                            if x[2328] <= 0.0921568647:
                                if x[480] <= 0.2529411837:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[2016] <= 0.6254902184:
                        if x[2262] <= 0.1352941245:
                            if x[381] <= 0.3156862855:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1673] <= 0.4078431427:
                                if x[290] <= 0.6039215922:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[2338] <= 0.2313725501:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        results.append(0)
            else:
                if x[2235] <= 0.2176470608:
                    if x[1847] <= 0.1313725561:
                        if x[2645] <= 0.4490196109:
                            results.append(1)
                        else:
                            results.append(1)
                    else:
                        if x[1638] <= 0.5039215833:
                            results.append(0)
                        else:
                            if x[1644] <= 0.5274510086:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[479] <= 0.5666666925:
                        if x[921] <= 0.1352941245:
                            if x[2167] <= 0.5098039508:
                                results.append(0)
                            else:
                                if x[2671] <= 0.4313725531:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2184] <= 0.2960784435:
                                if x[1473] <= 0.7372549176:
                                    if x[1947] <= 0.1666666716:
                                        results.append(0)
                                    else:
                                        if x[2384] <= 0.2450980395:
                                            results.append(1)
                                        else:
                                            if x[1002] <= 0.3568627536:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1316] <= 0.4294117689:
                                    if x[359] <= 0.6352941394:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2166] <= 0.3627451062:
                                        if x[1909] <= 0.3705882430:
                                            results.append(0)
                                        else:
                                            if x[742] <= 0.4392156899:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[633] <= 0.2098039240:
                                            if x[2515] <= 0.5627451241:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1002] <= 0.8627451062:
                                                results.append(1)
                                            else:
                                                results.append(1)
                    else:
                        if x[1692] <= 0.7274509966:
                            if x[2842] <= 0.1392156929:
                                results.append(0)
                            else:
                                if x[382] <= 0.5882353187:
                                    if x[2765] <= 0.6137255132:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[2244] <= 0.3803921640:
                                        results.append(1)
                                    else:
                                        if x[1689] <= 0.2901960909:
                                            results.append(1)
                                        else:
                                            results.append(1)
                        else:
                            if x[2623] <= 0.4215686321:
                                results.append(0)
                            else:
                                results.append(0)
        else:
            if x[899] <= 0.4764705896:
                if x[2253] <= 0.3078431487:
                    if x[64] <= 0.5823529661:
                        results.append(1)
                    else:
                        if x[1633] <= 0.8745098114:
                            if x[1249] <= 0.2294117659:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[990] <= 0.2372549027:
                        if x[1873] <= 0.4686274529:
                            if x[1085] <= 0.3862745166:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[3006] <= 0.5078431666:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[2046] <= 0.2490196154:
                            if x[168] <= 0.8176470697:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1481] <= 0.6333333552:
                                if x[1165] <= 0.4235294163:
                                    if x[1934] <= 0.4235294163:
                                        if x[1873] <= 0.2254901975:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
            else:
                if x[2661] <= 0.6705882549:
                    if x[1184] <= 0.2254901975:
                        results.append(1)
                    else:
                        if x[2221] <= 0.6254902184:
                            if x[197] <= 0.5745098293:
                                if x[693] <= 0.6000000238:
                                    if x[1984] <= 0.5686274767:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2209] <= 0.7666666806:
                                    if x[2750] <= 0.1862745136:
                                        if x[746] <= 0.9137254953:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[95] <= 0.5862745345:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[844] <= 0.6078431606:
                                        results.append(1)
                                    else:
                                        results.append(0)
                        else:
                            if x[382] <= 0.7784313858:
                                if x[552] <= 0.6294117868:
                                    if x[1750] <= 0.6882353127:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[494] <= 0.7411764860:
                                        results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                if x[2650] <= 0.4313725531:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[2846] <= 0.6039215922:
                        if x[1655] <= 0.3862745166:
                            results.append(0)
                        else:
                            if x[1527] <= 0.5509804189:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[1968] <= 0.3313725591:
                            if x[1474] <= 0.2529411837:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[723] <= 0.8176470697:
                                if x[908] <= 0.6607843339:
                                    results.append(1)
                                else:
                                    if x[2130] <= 0.6058823764:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[2723] <= 0.8333333433:
                                    results.append(1)
                                else:
                                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 6
    if time.time() < deadline or interrupt_flag.is_set():
        if x[83] <= 0.4843137264:
            if x[2730] <= 0.2098039240:
                if x[1868] <= 0.6568627656:
                    if x[1121] <= 0.5647059083:
                        if x[947] <= 0.1039215699:
                            results.append(0)
                        else:
                            if x[1621] <= 0.3294117749:
                                if x[1963] <= 0.2745098174:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2645] <= 0.1235294156:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[2675] <= 0.2588235363:
                        results.append(0)
                    else:
                        results.append(0)
            else:
                if x[233] <= 0.8803921640:
                    if x[2329] <= 0.1450980455:
                        if x[960] <= 0.1588235348:
                            if x[1392] <= 0.4176470637:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[2966] <= 0.2941176593:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[506] <= 0.7843137383:
                            if x[1995] <= 0.0411764719:
                                results.append(0)
                            else:
                                if x[2845] <= 0.0901960805:
                                    results.append(0)
                                else:
                                    if x[2929] <= 0.1039215699:
                                        results.append(0)
                                    else:
                                        if x[2077] <= 0.1529411823:
                                            if x[2667] <= 0.4235294163:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[2653] <= 0.1764705926:
                                                results.append(1)
                                            else:
                                                results.append(1)
                        else:
                            results.append(0)
                else:
                    results.append(0)
        else:
            if x[2359] <= 0.3078431487:
                if x[629] <= 0.5078431666:
                    if x[1385] <= 0.4627451003:
                        if x[1098] <= 0.3254902065:
                            if x[1802] <= 0.2882353067:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2582] <= 0.4568627477:
                                if x[2788] <= 0.5392157137:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[744] <= 0.4803921580:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[2368] <= 0.4843137264:
                        if x[1711] <= 0.8921568692:
                            if x[1831] <= 0.8784313798:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2786] <= 0.4764705896:
                            results.append(1)
                        else:
                            results.append(0)
            else:
                if x[1208] <= 0.4921568632:
                    if x[2373] <= 0.6490196288:
                        if x[2733] <= 0.2098039240:
                            if x[1963] <= 0.2058823556:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2468] <= 0.6156862974:
                                if x[2221] <= 0.2156862766:
                                    results.append(0)
                                else:
                                    if x[1384] <= 0.5980392396:
                                        if x[650] <= 0.8705882430:
                                            if x[90] <= 0.5274510086:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[495] <= 0.7764706016:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                    else:
                                        if x[2413] <= 0.4784313887:
                                            results.append(0)
                                        else:
                                            results.append(1)
                            else:
                                if x[2712] <= 0.6450980604:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[1666] <= 0.6196078658:
                            if x[1844] <= 0.1196078435:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[1169] <= 0.5411764979:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[1638] <= 0.5470588505:
                        if x[197] <= 0.6215686500:
                            if x[804] <= 0.6509804130:
                                if x[1349] <= 0.4745098054:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[968] <= 0.3156862855:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[503] <= 0.6509804130:
                            if x[161] <= 0.5745098293:
                                if x[1605] <= 0.6156862974:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1425] <= 0.6352941394:
                                if x[2358] <= 0.7372549176:
                                    if x[1757] <= 0.3176470697:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2433] <= 0.5274510086:
                                    results.append(0)
                                else:
                                    if x[770] <= 0.7196078598:
                                        if x[512] <= 0.6941176653:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[906] <= 0.6392157078:
                                            results.append(1)
                                        else:
                                            if x[1267] <= 0.8078431487:
                                                results.append(0)
                                            else:
                                                results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 7
    if time.time() < deadline or interrupt_flag.is_set():
        if x[176] <= 0.6411764920:
            if x[1379] <= 0.4686274529:
                if x[2644] <= 0.0392156877:
                    results.append(0)
                else:
                    if x[2328] <= 0.1588235348:
                        if x[2401] <= 0.2000000030:
                            results.append(1)
                        else:
                            if x[1595] <= 0.2764706016:
                                results.append(0)
                            else:
                                if x[355] <= 0.4235294163:
                                    if x[2138] <= 0.2000000030:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[2935] <= 0.0901960805:
                            if x[2876] <= 0.1529411823:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2648] <= 0.8058823645:
                                if x[1648] <= 0.8941176534:
                                    if x[1576] <= 0.7549019754:
                                        if x[2242] <= 0.0568627454:
                                            results.append(1)
                                        else:
                                            if x[1296] <= 0.8509804010:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[2830] <= 0.4705882370:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[643] <= 0.3705882430:
                                    results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[2517] <= 0.4058823586:
                    if x[2557] <= 0.2176470608:
                        if x[1226] <= 0.3313725591:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1817] <= 0.6725490391:
                            if x[620] <= 0.4666666687:
                                if x[1495] <= 0.6470588446:
                                    if x[1799] <= 0.5372549295:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1884] <= 0.6686274707:
                                        results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                if x[62] <= 0.5000000149:
                                    if x[2491] <= 0.4176470637:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1104] <= 0.6254902184:
                                        results.append(0)
                                    else:
                                        results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2551] <= 0.1549019665:
                        results.append(0)
                    else:
                        if x[2204] <= 0.6392157078:
                            if x[3048] <= 0.3333333433:
                                if x[1944] <= 0.4568627477:
                                    results.append(0)
                                else:
                                    if x[1690] <= 0.4235294163:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[248] <= 0.7901960909:
                                    if x[1296] <= 0.1823529452:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[867] <= 0.3960784376:
                                results.append(0)
                            else:
                                if x[305] <= 0.5058823675:
                                    results.append(1)
                                else:
                                    results.append(1)
        else:
            if x[704] <= 0.5078431666:
                if x[2452] <= 0.4117647111:
                    if x[702] <= 0.5392157137:
                        if x[1945] <= 0.3294117749:
                            if x[1758] <= 0.1725490242:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[21] <= 0.6588235497:
                                results.append(1)
                            else:
                                if x[1590] <= 0.4549019635:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[565] <= 0.6156862974:
                        if x[2604] <= 0.5431372821:
                            if x[1517] <= 0.2450980470:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[421] <= 0.4019607902:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[2028] <= 0.2411764786:
                            results.append(0)
                        else:
                            if x[385] <= 0.8509804010:
                                results.append(1)
                            else:
                                if x[1437] <= 0.9784313738:
                                    results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[1100] <= 0.2000000030:
                    if x[797] <= 0.7352941334:
                        if x[966] <= 0.5450980663:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[711] <= 0.7039215863:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[722] <= 0.3450980484:
                        if x[2313] <= 0.7274509966:
                            if x[1771] <= 0.4000000060:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2556] <= 0.6647059023:
                            if x[1595] <= 0.1529411823:
                                if x[1922] <= 0.4666666687:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[629] <= 0.6627451181:
                                    if x[2547] <= 0.3137255013:
                                        if x[1891] <= 0.5000000149:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[661] <= 0.4666666687:
                                            results.append(0)
                                        else:
                                            if x[2774] <= 0.4490196258:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                else:
                                    if x[1372] <= 0.1745098084:
                                        results.append(0)
                                    else:
                                        if x[2491] <= 0.1019607857:
                                            results.append(0)
                                        else:
                                            if x[2365] <= 0.6490196288:
                                                results.append(0)
                                            else:
                                                results.append(0)
                        else:
                            if x[518] <= 0.7666666806:
                                if x[26] <= 0.7607843280:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1424] <= 0.8960784376:
                                    if x[1514] <= 0.3196078539:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 8
    if time.time() < deadline or interrupt_flag.is_set():
        if x[308] <= 0.6411764920:
            if x[2638] <= 0.2725490332:
                if x[1646] <= 0.4882352948:
                    if x[2427] <= 0.3392156959:
                        if x[2441] <= 0.2156862766:
                            if x[2731] <= 0.1392156929:
                                if x[898] <= 0.4254902005:
                                    if x[2526] <= 0.1372549050:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[1090] <= 0.1921568662:
                                    results.append(0)
                                else:
                                    if x[1271] <= 0.2784313858:
                                        results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            if x[48] <= 0.2745098174:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2822] <= 0.5490196347:
                            if x[1765] <= 0.1352941245:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2695] <= 0.5333333611:
                        if x[750] <= 0.6647059023:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(0)
            else:
                if x[2073] <= 0.1705882400:
                    if x[1114] <= 0.3490196168:
                        if x[1254] <= 0.3764705956:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2668] <= 0.6372549236:
                            if x[2350] <= 0.2215686291:
                                results.append(0)
                            else:
                                if x[1279] <= 0.2215686366:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2253] <= 0.4176470637:
                        if x[2255] <= 0.3509804010:
                            if x[2269] <= 0.2235294133:
                                if x[2648] <= 0.3019607961:
                                    results.append(1)
                                else:
                                    if x[1772] <= 0.4039215744:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[2181] <= 0.2333333343:
                                    results.append(0)
                                else:
                                    if x[1770] <= 0.5803921819:
                                        if x[2975] <= 0.8117647171:
                                            if x[215] <= 0.6039215922:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[2029] <= 0.4372549057:
                                            if x[1298] <= 0.4215686321:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1985] <= 0.2588235438:
                                                results.append(1)
                                            else:
                                                results.append(1)
                        else:
                            if x[908] <= 0.2529411837:
                                results.append(1)
                            else:
                                if x[2608] <= 0.4647058845:
                                    if x[1323] <= 0.4450980425:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[1193] <= 0.5745098293:
                            if x[2370] <= 0.1705882400:
                                results.append(0)
                            else:
                                if x[2184] <= 0.9686274529:
                                    if x[2143] <= 0.1274509840:
                                        results.append(1)
                                    else:
                                        if x[1573] <= 0.7333333492:
                                            if x[667] <= 0.9431372583:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[496] <= 0.4568627477:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[1185] <= 0.4784313738:
                                if x[1373] <= 0.4352941215:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2802] <= 0.3470588326:
                                    results.append(0)
                                else:
                                    if x[2136] <= 0.4313725531:
                                        if x[2259] <= 0.5450980663:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[1654] <= 0.3235294223:
                                            results.append(1)
                                        else:
                                            if x[1434] <= 0.7960784435:
                                                results.append(1)
                                            else:
                                                results.append(1)
        else:
            if x[2631] <= 0.5431372821:
                if x[1106] <= 0.3549019694:
                    if x[2233] <= 0.2823529541:
                        if x[1757] <= 0.1647058874:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2833] <= 0.3529411852:
                            results.append(0)
                        else:
                            if x[1611] <= 0.6352941394:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[188] <= 0.1725490242:
                        results.append(1)
                    else:
                        if x[2410] <= 0.5235294402:
                            if x[1594] <= 0.1647058874:
                                results.append(0)
                            else:
                                if x[11] <= 0.6137255132:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[626] <= 0.6333333552:
                                if x[93] <= 0.4882352948:
                                    results.append(0)
                                else:
                                    if x[1459] <= 0.4372549057:
                                        results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                if x[2447] <= 0.2098039314:
                                    results.append(0)
                                else:
                                    if x[2496] <= 0.4568627477:
                                        results.append(0)
                                    else:
                                        results.append(0)
            else:
                if x[2097] <= 0.3294117749:
                    if x[875] <= 0.5176470727:
                        results.append(1)
                    else:
                        if x[852] <= 0.5745098293:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[2470] <= 0.1705882400:
                        results.append(0)
                    else:
                        if x[659] <= 0.6921568811:
                            if x[106] <= 0.7333333492:
                                if x[197] <= 0.6196078658:
                                    if x[1102] <= 0.6941176653:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[883] <= 0.7823529541:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1740] <= 0.6254902184:
                                if x[2895] <= 0.7725490332:
                                    if x[107] <= 0.7411764860:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2055] <= 0.5607843399:
                                    if x[814] <= 0.7941176593:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1659] <= 0.6098039448:
                                        results.append(0)
                                    else:
                                        if x[2396] <= 0.4568627626:
                                            results.append(1)
                                        else:
                                            results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 9
    if time.time() < deadline or interrupt_flag.is_set():
        if x[356] <= 0.6450980604:
            if x[2454] <= 0.2411764711:
                if x[1292] <= 0.3156862855:
                    if x[3032] <= 0.6098039448:
                        if x[1578] <= 0.5784313977:
                            if x[1661] <= 0.3725490272:
                                if x[2992] <= 0.5607843399:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[5] <= 0.2176470608:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[2719] <= 0.3725490272:
                        if x[2868] <= 0.2274509817:
                            if x[1707] <= 0.3941176534:
                                if x[1193] <= 0.5039215833:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1618] <= 0.4686274529:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[2509] <= 0.0941176489:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1658] <= 0.5098039359:
                            if x[1373] <= 0.4568627626:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
            else:
                if x[2640] <= 0.2490196154:
                    if x[968] <= 0.6372549236:
                        if x[2447] <= 0.2490196154:
                            if x[1091] <= 0.4941176623:
                                if x[998] <= 0.1882352978:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2421] <= 0.4980392307:
                                if x[3061] <= 0.1941176504:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[746] <= 0.3607843220:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[2742] <= 0.1392156929:
                        results.append(0)
                    else:
                        if x[2257] <= 0.1156862751:
                            if x[2805] <= 0.3392156959:
                                results.append(1)
                            else:
                                if x[1451] <= 0.3745098114:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[2735] <= 0.8607843220:
                                if x[1118] <= 0.6117647290:
                                    if x[1502] <= 0.7039215863:
                                        if x[1703] <= 0.8098039329:
                                            if x[1698] <= 0.9019607902:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1141] <= 0.5019607991:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[1106] <= 0.4313725531:
                                            if x[2356] <= 0.4098039269:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2669] <= 0.5137255192:
                                        if x[476] <= 0.5803921819:
                                            if x[3012] <= 0.2705882415:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2370] <= 0.6725490391:
                                            if x[1972] <= 0.4764705896:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                            else:
                                if x[2773] <= 0.4156862795:
                                    results.append(0)
                                else:
                                    if x[779] <= 0.5862745345:
                                        results.append(1)
                                    else:
                                        results.append(0)
        else:
            if x[1118] <= 0.3588235378:
                if x[2062] <= 0.2686274648:
                    if x[304] <= 0.4470588267:
                        results.append(1)
                    else:
                        if x[3036] <= 0.4078431427:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2238] <= 0.1823529452:
                        results.append(0)
                    else:
                        if x[990] <= 0.1235294156:
                            results.append(0)
                        else:
                            if x[2169] <= 0.2588235438:
                                results.append(0)
                            else:
                                if x[924] <= 0.6196078658:
                                    if x[2494] <= 0.3058823645:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2511] <= 0.6274510026:
                                        results.append(0)
                                    else:
                                        results.append(1)
            else:
                if x[2229] <= 0.7627451122:
                    if x[2136] <= 0.4568627477:
                        if x[98] <= 0.3666666746:
                            if x[2522] <= 0.2294117734:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[751] <= 0.5627451241:
                                if x[1910] <= 0.4450980425:
                                    if x[2634] <= 0.4098039269:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1238] <= 0.9686274529:
                                    if x[1225] <= 0.3137255013:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[920] <= 0.3647058904:
                            if x[2512] <= 0.5862745345:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[707] <= 0.5686274767:
                                if x[762] <= 0.4980392307:
                                    results.append(0)
                                else:
                                    if x[2489] <= 0.4725490361:
                                        results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[305] <= 0.7784313858:
                                    if x[2687] <= 0.6058823764:
                                        if x[2765] <= 0.2666666731:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2534] <= 0.5823529512:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[2466] <= 0.7098039389:
                                        results.append(0)
                                    else:
                                        results.append(0)
                else:
                    if x[1705] <= 0.7588235438:
                        if x[640] <= 0.7019608021:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1803] <= 0.8392156959:
                            results.append(1)
                        else:
                            results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 10
    if time.time() < deadline or interrupt_flag.is_set():
        if x[68] <= 0.6137255132:
            if x[2239] <= 0.1098039225:
                if x[1847] <= 0.0862745121:
                    if x[2392] <= 0.3725490272:
                        results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[718] <= 0.2764706016:
                        results.append(0)
                    else:
                        results.append(0)
            else:
                if x[2730] <= 0.2176470608:
                    if x[1874] <= 0.3078431487:
                        if x[1492] <= 0.2392156944:
                            results.append(0)
                        else:
                            if x[1452] <= 0.5941176713:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1577] <= 0.3490196168:
                            results.append(1)
                        else:
                            if x[846] <= 0.5549019873:
                                if x[994] <= 0.6470588446:
                                    if x[830] <= 0.5568627715:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[2845] <= 0.1470588297:
                        if x[2863] <= 0.0549019612:
                            results.append(1)
                        else:
                            if x[2636] <= 0.3960784376:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2831] <= 0.9274509847:
                            if x[1598] <= 0.8862745166:
                                if x[2179] <= 0.1823529452:
                                    if x[2465] <= 0.3431372643:
                                        if x[2957] <= 0.2823529541:
                                            results.append(1)
                                        else:
                                            if x[1835] <= 0.3470588326:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[111] <= 0.2588235438:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    if x[470] <= 0.4647058845:
                                        if x[1463] <= 0.7843137383:
                                            if x[75] <= 0.7843137383:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[1891] <= 0.1803921610:
                                            results.append(0)
                                        else:
                                            if x[2439] <= 0.2803921700:
                                                results.append(0)
                                            else:
                                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
        else:
            if x[1539] <= 0.7843137383:
                if x[1586] <= 0.3901960850:
                    if x[1621] <= 0.5078431666:
                        if x[2975] <= 0.2039215714:
                            results.append(1)
                        else:
                            if x[206] <= 0.3921568692:
                                results.append(1)
                            else:
                                if x[1055] <= 0.2725490332:
                                    results.append(0)
                                else:
                                    if x[1022] <= 0.1764705926:
                                        results.append(0)
                                    else:
                                        results.append(0)
                    else:
                        if x[1026] <= 0.4490196109:
                            if x[379] <= 0.5901961029:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[48] <= 0.5431372821:
                                results.append(0)
                            else:
                                if x[1582] <= 0.2392156944:
                                    if x[1855] <= 0.3941176534:
                                        results.append(0)
                                    else:
                                        if x[2633] <= 0.4607843161:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2114] <= 0.6137255132:
                                        if x[1454] <= 0.2117647082:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                else:
                    if x[2359] <= 0.8411764801:
                        if x[425] <= 0.2490196154:
                            results.append(1)
                        else:
                            if x[1718] <= 0.1705882400:
                                if x[2214] <= 0.2764705941:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2222] <= 0.0921568647:
                                    results.append(0)
                                else:
                                    if x[3009] <= 0.3764705956:
                                        results.append(0)
                                    else:
                                        if x[1779] <= 0.5686274767:
                                            if x[719] <= 0.4196078479:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1924] <= 0.2294117659:
                                                results.append(1)
                                            else:
                                                results.append(0)
                    else:
                        results.append(1)
            else:
                if x[2362] <= 0.3509804010:
                    if x[138] <= 0.6372549236:
                        results.append(1)
                    else:
                        if x[2606] <= 0.9098039269:
                            if x[2058] <= 0.6352941394:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[1088] <= 0.7490196228:
                        if x[2553] <= 0.3411764801:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1835] <= 0.8627451062:
                            if x[1963] <= 0.4098039269:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 11
    if time.time() < deadline or interrupt_flag.is_set():
        if x[140] <= 0.6019608080:
            if x[2743] <= 0.2254901975:
                if x[2637] <= 0.3784313798:
                    if x[282] <= 0.1882352978:
                        if x[1482] <= 0.6980392337:
                            if x[709] <= 0.1490196101:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2878] <= 0.4666666687:
                            if x[1099] <= 0.6392157078:
                                if x[1532] <= 0.2039215714:
                                    results.append(0)
                                else:
                                    if x[2793] <= 0.4745098054:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[784] <= 0.5568627566:
                                results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[2593] <= 0.3137255013:
                        results.append(1)
                    else:
                        results.append(1)
            else:
                if x[2377] <= 0.0607843157:
                    if x[981] <= 0.2196078524:
                        results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[2637] <= 0.2372549027:
                        if x[2168] <= 0.1882352978:
                            results.append(1)
                        else:
                            if x[2475] <= 0.4392156899:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[1791] <= 0.1137254909:
                            if x[1310] <= 0.1980392188:
                                results.append(1)
                            else:
                                if x[1393] <= 0.4411764741:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2075] <= 0.0980392173:
                                if x[1299] <= 0.6235294342:
                                    if x[1861] <= 0.2725490332:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1472] <= 0.4098039269:
                                    if x[435] <= 0.0627450999:
                                        results.append(0)
                                    else:
                                        if x[2459] <= 0.0450980403:
                                            results.append(0)
                                        else:
                                            if x[720] <= 0.0686274543:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    if x[1470] <= 0.4294117689:
                                        results.append(0)
                                    else:
                                        if x[103] <= 0.4960784316:
                                            if x[813] <= 0.1568627506:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1709] <= 0.5176470876:
                                                results.append(1)
                                            else:
                                                results.append(0)
        else:
            if x[2808] <= 0.4568627477:
                if x[721] <= 0.2568627596:
                    if x[1302] <= 0.3549019694:
                        results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[542] <= 0.2117647082:
                        results.append(1)
                    else:
                        if x[296] <= 0.5980392396:
                            if x[2163] <= 0.3156862855:
                                results.append(0)
                            else:
                                if x[2443] <= 0.3098039329:
                                    results.append(0)
                                else:
                                    if x[1542] <= 0.2980392277:
                                        results.append(0)
                                    else:
                                        results.append(1)
                        else:
                            if x[1706] <= 0.1294117719:
                                results.append(0)
                            else:
                                if x[1019] <= 0.2607843280:
                                    if x[1134] <= 0.4431372583:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2135] <= 0.7450980544:
                                        if x[1610] <= 0.2176470608:
                                            if x[2376] <= 0.3529411852:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2473] <= 0.4784313887:
                                            results.append(0)
                                        else:
                                            results.append(1)
            else:
                if x[2344] <= 0.2882353067:
                    if x[1493] <= 0.1450980455:
                        results.append(1)
                    else:
                        if x[2814] <= 0.4960784465:
                            if x[2833] <= 0.4215686321:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1536] <= 0.2352941185:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[896] <= 0.3725490272:
                        if x[2073] <= 0.1509803981:
                            results.append(0)
                        else:
                            if x[1070] <= 0.1823529452:
                                results.append(1)
                            else:
                                if x[1284] <= 0.1588235348:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[2091] <= 0.8411764801:
                            if x[2826] <= 0.4078431427:
                                results.append(1)
                            else:
                                if x[749] <= 0.4431372583:
                                    if x[1216] <= 0.2549019679:
                                        results.append(0)
                                    else:
                                        if x[2657] <= 0.5392156988:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[1496] <= 0.1333333366:
                                        results.append(1)
                                    else:
                                        if x[198] <= 0.3078431487:
                                            results.append(1)
                                        else:
                                            if x[2633] <= 0.4294117689:
                                                results.append(0)
                                            else:
                                                results.append(0)
                        else:
                            if x[1246] <= 0.7352941334:
                                results.append(1)
                            else:
                                if x[772] <= 0.8803921640:
                                    results.append(1)
                                else:
                                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 12
    if time.time() < deadline or interrupt_flag.is_set():
        if x[59] <= 0.6490196288:
            if x[2562] <= 0.2372549027:
                if x[2876] <= 0.1607843190:
                    if x[834] <= 0.1431372575:
                        results.append(0)
                    else:
                        if x[1088] <= 0.5764706135:
                            results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[273] <= 0.6333333552:
                        if x[1434] <= 0.1196078435:
                            results.append(1)
                        else:
                            if x[2625] <= 0.3960784376:
                                if x[1240] <= 0.5980392396:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2079] <= 0.5196078718:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[784] <= 0.4470588416:
                            results.append(0)
                        else:
                            results.append(1)
            else:
                if x[1980] <= 0.1019607857:
                    if x[2635] <= 0.6450980604:
                        results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[2244] <= 0.2078431398:
                        if x[2216] <= 0.2823529541:
                            if x[2260] <= 0.1392156929:
                                results.append(0)
                            else:
                                if x[2418] <= 0.1137254909:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[792] <= 0.3470588326:
                                if x[2450] <= 0.2372549102:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1416] <= 0.4058823586:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[419] <= 0.5078431666:
                            if x[2173] <= 0.2568627596:
                                if x[734] <= 0.4627451003:
                                    if x[1665] <= 0.5823529661:
                                        results.append(1)
                                    else:
                                        if x[1230] <= 0.5607843399:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2783] <= 0.4058823586:
                                        results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[2760] <= 0.1117647104:
                                    results.append(1)
                                else:
                                    if x[2049] <= 0.2450980395:
                                        if x[1956] <= 0.1450980455:
                                            if x[1958] <= 0.1039215699:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[1523] <= 0.7549019754:
                                            if x[2214] <= 0.9117647111:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                        else:
                            if x[74] <= 0.4549019635:
                                if x[1679] <= 0.7176470757:
                                    if x[2159] <= 0.1803921610:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[989] <= 0.6039215922:
                                    if x[148] <= 0.5588235557:
                                        if x[725] <= 0.5745098293:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[2554] <= 0.3372549117:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[1474] <= 0.6921568811:
                                        results.append(0)
                                    else:
                                        results.append(1)
        else:
            if x[1298] <= 0.4098039269:
                if x[2518] <= 0.4843137264:
                    if x[2236] <= 0.3490196168:
                        if x[926] <= 0.1941176504:
                            results.append(1)
                        else:
                            if x[2368] <= 0.5196078718:
                                if x[1761] <= 0.2274509817:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[1300] <= 0.2490196154:
                            if x[2628] <= 0.6313725710:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1014] <= 0.7098039389:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[2439] <= 0.2666666806:
                        results.append(0)
                    else:
                        if x[478] <= 0.6705882549:
                            if x[922] <= 0.4196078479:
                                results.append(1)
                            else:
                                if x[2644] <= 0.5921568871:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2282] <= 0.8333333433:
                                if x[1045] <= 0.9764705896:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
            else:
                if x[2316] <= 0.7705882490:
                    if x[2457] <= 0.8627451062:
                        if x[194] <= 0.6568627656:
                            if x[2511] <= 0.4058823586:
                                if x[13] <= 0.5470588505:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[293] <= 0.5313725770:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[1622] <= 0.1098039225:
                                results.append(0)
                            else:
                                if x[1657] <= 0.7078431547:
                                    if x[2117] <= 0.1784313768:
                                        if x[1868] <= 0.3098039255:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[952] <= 0.4156862795:
                                            if x[1774] <= 0.4686274529:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[1732] <= 0.6921568811:
                                        if x[2766] <= 0.5568627715:
                                            if x[2501] <= 0.3627451062:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[2951] <= 0.5980392396:
                        results.append(1)
                    else:
                        if x[2621] <= 0.8450980484:
                            results.append(0)
                        else:
                            results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 13
    if time.time() < deadline or interrupt_flag.is_set():
        if x[176] <= 0.5980392396:
            if x[2631] <= 0.2372549027:
                if x[1457] <= 0.6745098233:
                    if x[1508] <= 0.5372549295:
                        if x[1793] <= 0.4666666687:
                            if x[1984] <= 0.5568627715:
                                if x[659] <= 0.4117647111:
                                    if x[1659] <= 0.6058823764:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[282] <= 0.6333333552:
                                        results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2364] <= 0.6627451181:
                            if x[286] <= 0.4745098054:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[1382] <= 0.6117647290:
                        results.append(0)
                    else:
                        results.append(0)
            else:
                if x[785] <= 0.5627451241:
                    if x[1593] <= 0.8901960850:
                        if x[2278] <= 0.0960784331:
                            if x[2702] <= 0.2960784435:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2238] <= 0.2137254924:
                                if x[2416] <= 0.2960784435:
                                    results.append(1)
                                else:
                                    if x[2513] <= 0.4549019635:
                                        if x[2205] <= 0.4568627477:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[917] <= 0.2058823556:
                                            results.append(0)
                                        else:
                                            results.append(0)
                            else:
                                if x[2445] <= 0.1647058874:
                                    results.append(0)
                                else:
                                    if x[1424] <= 0.4843137264:
                                        if x[1454] <= 0.6450980604:
                                            if x[1020] <= 0.1941176504:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[348] <= 0.2843137383:
                                            if x[959] <= 0.2019607872:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[3039] <= 0.2960784435:
                                                results.append(0)
                                            else:
                                                results.append(1)
                    else:
                        if x[425] <= 0.4235294163:
                            results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2124] <= 0.4411764741:
                        if x[2250] <= 0.3568627536:
                            results.append(0)
                        else:
                            if x[1071] <= 0.6490196288:
                                if x[1629] <= 0.4862745106:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[946] <= 0.4176470637:
                            results.append(1)
                        else:
                            if x[1097] <= 0.5666666925:
                                if x[2185] <= 0.4274509847:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
        else:
            if x[1295] <= 0.3588235378:
                if x[2853] <= 0.3705882430:
                    if x[2371] <= 0.4607843161:
                        if x[240] <= 0.7490196228:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2196] <= 0.7156862915:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[1987] <= 0.3862745166:
                        if x[2512] <= 0.5549019873:
                            if x[2894] <= 0.2745098174:
                                results.append(1)
                            else:
                                if x[1626] <= 0.5843137503:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[2814] <= 0.6000000238:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[1009] <= 0.6274510026:
                            if x[2275] <= 0.3764705956:
                                results.append(0)
                            else:
                                if x[45] <= 0.5235294402:
                                    if x[2126] <= 0.6156862974:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
            else:
                if x[2365] <= 0.8098039329:
                    if x[2346] <= 0.7196078598:
                        if x[1523] <= 0.2215686291:
                            if x[2795] <= 0.1313725561:
                                results.append(1)
                            else:
                                if x[1833] <= 0.4803921580:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[2433] <= 0.6705882549:
                                if x[200] <= 0.6058823764:
                                    if x[519] <= 0.7333333492:
                                        if x[2422] <= 0.3764705956:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1737] <= 0.0588235315:
                                        results.append(0)
                                    else:
                                        if x[1481] <= 0.2803921700:
                                            if x[69] <= 0.7450980544:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1229] <= 0.2843137383:
                                                results.append(0)
                                            else:
                                                results.append(0)
                            else:
                                if x[1589] <= 0.2431372553:
                                    results.append(1)
                                else:
                                    if x[2473] <= 0.5137255043:
                                        results.append(0)
                                    else:
                                        results.append(0)
                    else:
                        if x[1202] <= 0.4411764741:
                            results.append(1)
                        else:
                            if x[220] <= 0.7078431547:
                                results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[1680] <= 0.5529412031:
                        if x[2733] <= 0.8705882430:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 14
    if time.time() < deadline or interrupt_flag.is_set():
        if x[329] <= 0.6137255132:
            if x[89] <= 0.4803921580:
                if x[2613] <= 0.2294117659:
                    if x[1658] <= 0.2745098174:
                        if x[2216] <= 0.3156862855:
                            if x[2823] <= 0.1196078435:
                                results.append(0)
                            else:
                                if x[809] <= 0.5019607991:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2622] <= 0.2686274648:
                            if x[665] <= 0.1411764771:
                                if x[1953] <= 0.3627451062:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2168] <= 0.1333333403:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2136] <= 0.1470588297:
                        if x[1843] <= 0.1313725561:
                            if x[16] <= 0.4274509847:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[1188] <= 0.2176470608:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[2740] <= 0.1196078435:
                            if x[3006] <= 0.2372549102:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1261] <= 0.8490196168:
                                if x[2142] <= 0.3862745166:
                                    if x[2427] <= 0.4411764741:
                                        if x[864] <= 0.0549019631:
                                            results.append(1)
                                        else:
                                            if x[1676] <= 0.5764706135:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[1731] <= 0.2666666731:
                                            results.append(0)
                                        else:
                                            if x[2789] <= 0.6411764920:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                else:
                                    if x[915] <= 0.1196078435:
                                        results.append(1)
                                    else:
                                        if x[2242] <= 0.2274509817:
                                            results.append(1)
                                        else:
                                            if x[1124] <= 0.8490196168:
                                                results.append(1)
                                            else:
                                                results.append(1)
                            else:
                                if x[1929] <= 0.8058823645:
                                    results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[2136] <= 0.2647058964:
                    if x[1316] <= 0.2960784435:
                        if x[635] <= 0.2490196154:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[1755] <= 0.2666666806:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[630] <= 0.5117647350:
                        if x[2251] <= 0.3078431487:
                            if x[1155] <= 0.5372549295:
                                if x[503] <= 0.2274509892:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2034] <= 0.4196078479:
                                if x[719] <= 0.3745098114:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1695] <= 0.6823529601:
                                    if x[2948] <= 0.5529412031:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[2605] <= 0.1843137294:
                            results.append(0)
                        else:
                            if x[73] <= 0.3784313798:
                                results.append(1)
                            else:
                                if x[2542] <= 0.2529411837:
                                    results.append(1)
                                else:
                                    results.append(1)
        else:
            if x[143] <= 0.5980392396:
                if x[1802] <= 0.2117647082:
                    results.append(0)
                else:
                    if x[2583] <= 0.3352941275:
                        results.append(1)
                    else:
                        results.append(1)
            else:
                if x[2382] <= 0.4568627477:
                    if x[1388] <= 0.3725490272:
                        if x[306] <= 0.5000000149:
                            if x[1859] <= 0.3294117749:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2125] <= 0.6196078658:
                                if x[926] <= 0.1862745136:
                                    results.append(1)
                                else:
                                    if x[788] <= 0.3254902065:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[218] <= 0.5411764979:
                            results.append(0)
                        else:
                            if x[1982] <= 0.1039215699:
                                results.append(0)
                            else:
                                if x[1264] <= 0.8450980484:
                                    results.append(0)
                                else:
                                    if x[1564] <= 0.6000000238:
                                        results.append(0)
                                    else:
                                        results.append(0)
                else:
                    if x[554] <= 0.8313725591:
                        if x[2245] <= 0.2333333343:
                            if x[2244] <= 0.1764705926:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1226] <= 0.5235294402:
                                if x[2192] <= 0.9019607902:
                                    if x[722] <= 0.6901960969:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1355] <= 0.7313725650:
                                    if x[1296] <= 0.7039215863:
                                        if x[1671] <= 0.5784313977:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1618] <= 0.7058823705:
                                        results.append(0)
                                    else:
                                        results.append(1)
                    else:
                        if x[1196] <= 0.2921568751:
                            if x[2185] <= 0.4431372583:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2774] <= 0.4039215744:
                                if x[2030] <= 0.4411764741:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2126] <= 0.8588235378:
                                    results.append(0)
                                else:
                                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 15
    if time.time() < deadline or interrupt_flag.is_set():
        if x[284] <= 0.5705882609:
            if x[2542] <= 0.2568627596:
                if x[242] <= 0.2823529541:
                    if x[1263] <= 0.7254902124:
                        if x[713] <= 0.4215686321:
                            if x[1682] <= 0.4058823586:
                                results.append(1)
                            else:
                                if x[2928] <= 0.2450980470:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2108] <= 0.1960784346:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[376] <= 0.4588235319:
                        if x[522] <= 0.5117647350:
                            if x[1645] <= 0.6196078658:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2123] <= 0.2372549027:
                                results.append(1)
                            else:
                                if x[179] <= 0.3666666746:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[2337] <= 0.1529411823:
                            results.append(0)
                        else:
                            if x[2196] <= 0.5254902244:
                                if x[1927] <= 0.3960784376:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
            else:
                if x[1580] <= 0.5941176713:
                    if x[2558] <= 0.8960784376:
                        if x[209] <= 0.8019607961:
                            if x[2831] <= 0.0529411770:
                                results.append(0)
                            else:
                                if x[1973] <= 0.1156862751:
                                    if x[2238] <= 0.2960784435:
                                        if x[1073] <= 0.2627451047:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[1883] <= 0.1313725561:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[2303] <= 0.6058823764:
                                        if x[1793] <= 0.8294117749:
                                            if x[62] <= 0.6843137443:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[374] <= 0.2705882490:
                                            if x[38] <= 0.1431372613:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1656] <= 0.7039215863:
                                                results.append(1)
                                            else:
                                                results.append(1)
                        else:
                            if x[1109] <= 0.4411764741:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[549] <= 0.2450980470:
                        if x[272] <= 0.2431372553:
                            if x[2474] <= 0.4509803951:
                                results.append(0)
                            else:
                                if x[1501] <= 0.4156862795:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2265] <= 0.3352941275:
                            if x[131] <= 0.2921568751:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[341] <= 0.7372549176:
                                if x[788] <= 0.6254902184:
                                    if x[1486] <= 0.8803921640:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
        else:
            if x[398] <= 0.6176470816:
                if x[2328] <= 0.3901960850:
                    if x[2323] <= 0.4156862795:
                        if x[1496] <= 0.3019607961:
                            if x[136] <= 0.7803921700:
                                if x[2028] <= 0.2843137383:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2956] <= 0.2607843280:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[2184] <= 0.2117647082:
                        results.append(0)
                    else:
                        if x[2713] <= 0.2627451122:
                            results.append(0)
                        else:
                            if x[2714] <= 0.7000000179:
                                if x[258] <= 0.4509803951:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[984] <= 0.6450980604:
                                    results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[1202] <= 0.3137255013:
                    if x[2137] <= 0.4960784465:
                        if x[731] <= 0.2784313858:
                            if x[279] <= 0.9019607902:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[1423] <= 0.4941176623:
                                if x[1555] <= 0.4745098054:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1396] <= 0.2490196154:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[2113] <= 0.4352941215:
                            results.append(0)
                        else:
                            if x[941] <= 0.5156862885:
                                results.append(1)
                            else:
                                results.append(1)
                else:
                    if x[26] <= 0.4803921580:
                        results.append(1)
                    else:
                        if x[1268] <= 0.5470588505:
                            if x[2372] <= 0.6431372762:
                                if x[1483] <= 0.1313725524:
                                    results.append(1)
                                else:
                                    if x[650] <= 0.4941176623:
                                        if x[273] <= 0.7274509966:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[1106] <= 0.3725490272:
                                            results.append(1)
                                        else:
                                            if x[132] <= 0.9000000060:
                                                results.append(0)
                                            else:
                                                results.append(0)
                            else:
                                if x[320] <= 0.7372549176:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2138] <= 0.5529412031:
                                results.append(0)
                            else:
                                if x[1761] <= 0.5470588505:
                                    if x[732] <= 0.3705882430:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[807] <= 0.9196078479:
                                        if x[334] <= 0.6137255132:
                                            results.append(0)
                                        else:
                                            if x[2816] <= 0.7686274648:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                    else:
                                        results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 16
    if time.time() < deadline or interrupt_flag.is_set():
        if x[266] <= 0.6215686500:
            if x[2133] <= 0.3000000119:
                if x[137] <= 0.6568627656:
                    if x[2643] <= 0.1823529452:
                        if x[933] <= 0.7529411912:
                            if x[1985] <= 0.1509803981:
                                if x[82] <= 0.2078431398:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1998] <= 0.3588235378:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2495] <= 0.2588235438:
                            if x[2322] <= 0.5352941453:
                                if x[2745] <= 0.1823529452:
                                    results.append(1)
                                else:
                                    if x[2722] <= 0.5313725770:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[996] <= 0.6960784495:
                                if x[3058] <= 0.4490196109:
                                    if x[2612] <= 0.4058823586:
                                        if x[2968] <= 0.3686274588:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[360] <= 0.1666666716:
                                        results.append(0)
                                    else:
                                        if x[482] <= 0.2274509817:
                                            results.append(0)
                                        else:
                                            if x[2773] <= 0.4607843161:
                                                results.append(1)
                                            else:
                                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[2654] <= 0.5705882609:
                        results.append(0)
                    else:
                        results.append(0)
            else:
                if x[2733] <= 0.2921568751:
                    if x[1652] <= 0.5235294402:
                        if x[2104] <= 0.1921568662:
                            results.append(0)
                        else:
                            if x[2743] <= 0.0941176489:
                                results.append(0)
                            else:
                                if x[517] <= 0.3372549117:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[1626] <= 0.3176470697:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[1488] <= 0.7823529541:
                        if x[2927] <= 0.7254902124:
                            if x[2529] <= 0.1901960820:
                                if x[725] <= 0.4352941364:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2279] <= 0.8117647171:
                                    if x[1743] <= 0.3156862855:
                                        if x[1094] <= 0.6019608080:
                                            if x[1037] <= 0.4901960790:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2145] <= 0.2137254924:
                                            results.append(1)
                                        else:
                                            if x[1785] <= 0.8196078539:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2266] <= 0.4941176623:
                                if x[1523] <= 0.4254902005:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[465] <= 0.2098039240:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[1622] <= 0.5392157137:
                            if x[1282] <= 0.2882353067:
                                results.append(0)
                            else:
                                if x[757] <= 0.4333333373:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1548] <= 0.6078431606:
                                results.append(1)
                            else:
                                if x[1779] <= 0.7098039389:
                                    results.append(0)
                                else:
                                    results.append(0)
        else:
            if x[1190] <= 0.4725490212:
                if x[2706] <= 0.1862745136:
                    if x[314] <= 0.4921568781:
                        results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[2269] <= 0.3843137324:
                        if x[1333] <= 0.5529412031:
                            if x[973] <= 0.5098039508:
                                results.append(0)
                            else:
                                if x[1739] <= 0.3843137324:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[206] <= 0.8156862855:
                                if x[1556] <= 0.3588235304:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[1835] <= 0.7627451122:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[2739] <= 0.1764705926:
                            results.append(0)
                        else:
                            if x[701] <= 0.5647059083:
                                if x[862] <= 0.3686274588:
                                    results.append(1)
                                else:
                                    if x[2718] <= 0.8392156959:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[1025] <= 0.5627451241:
                                    if x[1448] <= 0.5411764979:
                                        if x[725] <= 0.7509804070:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2056] <= 0.5686274767:
                                        if x[2694] <= 0.4313725531:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
            else:
                if x[2125] <= 0.5784313977:
                    if x[2433] <= 0.4803921580:
                        if x[1277] <= 0.2058823556:
                            results.append(0)
                        else:
                            if x[1102] <= 0.2627451122:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1508] <= 0.5411764979:
                            if x[2611] <= 0.7156862915:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2732] <= 0.7392157018:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[2129] <= 0.5647059083:
                        if x[2128] <= 0.5941176713:
                            results.append(1)
                        else:
                            results.append(1)
                    else:
                        if x[1378] <= 0.9352941215:
                            if x[2845] <= 0.8196078539:
                                if x[1202] <= 0.5117647201:
                                    results.append(0)
                                else:
                                    if x[2909] <= 0.3098039329:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[2344] <= 0.7921568751:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 17
    if time.time() < deadline or interrupt_flag.is_set():
        if x[656] <= 0.5941176713:
            if x[2338] <= 0.2137254924:
                if x[3053] <= 0.5431372821:
                    if x[2845] <= 0.1392156929:
                        if x[1224] <= 0.2725490257:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1290] <= 0.8431372643:
                            if x[2164] <= 0.0647058859:
                                results.append(0)
                            else:
                                if x[1675] <= 0.8274509907:
                                    if x[489] <= 0.7235294282:
                                        if x[2577] <= 0.2529411912:
                                            if x[575] <= 0.1823529452:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[1026] <= 0.7000000179:
                        if x[282] <= 0.2647058964:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
            else:
                if x[2650] <= 0.1823529452:
                    if x[2151] <= 0.3901960850:
                        if x[1226] <= 0.5117647201:
                            if x[726] <= 0.2549019679:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2542] <= 0.4294117689:
                            if x[2621] <= 0.1470588297:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2154] <= 0.2529411912:
                        if x[20] <= 0.3470588326:
                            if x[2178] <= 0.2313725501:
                                results.append(0)
                            else:
                                if x[1040] <= 0.1215686314:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1576] <= 0.2529411837:
                                results.append(1)
                            else:
                                if x[563] <= 0.4941176474:
                                    if x[1870] <= 0.2352941185:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[1271] <= 0.6725490391:
                            if x[2620] <= 0.1078431383:
                                if x[340] <= 0.4509803951:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[3009] <= 0.1607843190:
                                    if x[1349] <= 0.3843137324:
                                        if x[1604] <= 0.5784313977:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1622] <= 0.5705882609:
                                        if x[2445] <= 0.1843137294:
                                            results.append(1)
                                        else:
                                            if x[2143] <= 0.1039215699:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[2906] <= 0.2450980395:
                                            results.append(0)
                                        else:
                                            if x[2431] <= 0.3117647171:
                                                results.append(1)
                                            else:
                                                results.append(1)
                        else:
                            if x[979] <= 0.5098039359:
                                if x[346] <= 0.2019607872:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1253] <= 0.7509804070:
                                    if x[1115] <= 0.7000000179:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
        else:
            if x[914] <= 0.4549019635:
                if x[2355] <= 0.4098039269:
                    if x[2861] <= 0.1745098084:
                        if x[2684] <= 0.1764705926:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2101] <= 0.6254902184:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[2640] <= 0.3156862855:
                        results.append(0)
                    else:
                        if x[1689] <= 0.1882352978:
                            results.append(0)
                        else:
                            if x[1464] <= 0.4254902005:
                                if x[3064] <= 0.5549019873:
                                    results.append(0)
                                else:
                                    if x[110] <= 0.6411764920:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(1)
            else:
                if x[404] <= 0.7509804070:
                    if x[918] <= 0.6490196288:
                        if x[583] <= 0.7470588386:
                            if x[2745] <= 0.7137255073:
                                if x[499] <= 0.3607843220:
                                    results.append(0)
                                else:
                                    if x[1868] <= 0.1156862751:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[2962] <= 0.6450980604:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2083] <= 0.2000000030:
                            results.append(0)
                        else:
                            if x[886] <= 0.6235294342:
                                if x[2237] <= 0.3509804010:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[2628] <= 0.6294117868:
                                    if x[1295] <= 0.6039215922:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[167] <= 0.6725490391:
                                        results.append(0)
                                    else:
                                        results.append(1)
                else:
                    if x[758] <= 0.6823529601:
                        if x[1005] <= 0.6529411972:
                            if x[1395] <= 0.5392156988:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2028] <= 0.3254902065:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[1298] <= 0.3352941275:
                            if x[1226] <= 0.7686274648:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1169] <= 0.1627451032:
                                results.append(0)
                            else:
                                if x[170] <= 0.6901960969:
                                    results.append(0)
                                else:
                                    if x[491] <= 0.7666666806:
                                        results.append(0)
                                    else:
                                        results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 18
    if time.time() < deadline or interrupt_flag.is_set():
        if x[158] <= 0.6058823764:
            if x[2739] <= 0.1588235348:
                if x[954] <= 0.4764705896:
                    if x[2881] <= 0.2372549027:
                        if x[1687] <= 0.3392156959:
                            results.append(1)
                        else:
                            if x[793] <= 0.2372549102:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[942] <= 0.3862745166:
                            results.append(0)
                        else:
                            if x[1138] <= 0.5078431517:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[1364] <= 0.3117647171:
                        results.append(1)
                    else:
                        results.append(0)
            else:
                if x[2256] <= 0.0960784331:
                    if x[2339] <= 0.1529411785:
                        results.append(0)
                    else:
                        if x[740] <= 0.3137255013:
                            results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2419] <= 0.3784313798:
                        if x[1361] <= 0.3490196168:
                            if x[2032] <= 0.4803921580:
                                if x[787] <= 0.6607843339:
                                    if x[793] <= 0.6529411972:
                                        if x[2631] <= 0.1725490242:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1330] <= 0.2450980470:
                                    results.append(0)
                                else:
                                    if x[576] <= 0.4117647111:
                                        results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            if x[234] <= 0.4470588267:
                                if x[2527] <= 0.4490196109:
                                    if x[1757] <= 0.1921568662:
                                        results.append(1)
                                    else:
                                        if x[2728] <= 0.3450980484:
                                            if x[1377] <= 0.3686274588:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2064] <= 0.4274509847:
                                    if x[677] <= 0.4980392307:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1632] <= 0.5470588505:
                                        results.append(1)
                                    else:
                                        results.append(1)
                    else:
                        if x[2226] <= 0.3549019694:
                            if x[2139] <= 0.3431372643:
                                if x[813] <= 0.4352941215:
                                    if x[534] <= 0.2137254924:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[155] <= 0.3274509907:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1748] <= 0.8294117749:
                                if x[612] <= 0.0803921595:
                                    results.append(1)
                                else:
                                    if x[296] <= 0.9039215744:
                                        if x[2172] <= 0.1313725561:
                                            results.append(1)
                                        else:
                                            if x[1664] <= 0.5549019873:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[1554] <= 0.8431372643:
                                    results.append(0)
                                else:
                                    results.append(1)
        else:
            if x[923] <= 0.5705882609:
                if x[2274] <= 0.4392156899:
                    if x[917] <= 0.3549019694:
                        if x[2167] <= 0.2176470608:
                            if x[2282] <= 0.1392156929:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1799] <= 0.2686274648:
                                results.append(1)
                            else:
                                if x[304] <= 0.7098039389:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[1196] <= 0.2901960909:
                            results.append(1)
                        else:
                            if x[274] <= 0.8529411852:
                                if x[1440] <= 0.6215686500:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[359] <= 0.9098039269:
                                    results.append(1)
                                else:
                                    results.append(0)
                else:
                    if x[2618] <= 0.1333333366:
                        if x[2121] <= 0.3039215803:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1960] <= 0.5000000149:
                            if x[1484] <= 0.4921568632:
                                if x[2755] <= 0.3294117749:
                                    results.append(0)
                                else:
                                    if x[848] <= 0.3607843220:
                                        if x[11] <= 0.8352941275:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[830] <= 0.5901961029:
                                            results.append(1)
                                        else:
                                            results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2250] <= 0.4725490212:
                                results.append(0)
                            else:
                                if x[1668] <= 0.2196078524:
                                    results.append(1)
                                else:
                                    results.append(1)
            else:
                if x[2121] <= 0.7509804070:
                    if x[2367] <= 0.4529411793:
                        if x[197] <= 0.5705882609:
                            if x[1545] <= 0.3117647171:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2600] <= 0.1039215699:
                                results.append(0)
                            else:
                                if x[1715] <= 0.1588235348:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[2643] <= 0.6372549236:
                            if x[949] <= 0.4078431427:
                                results.append(1)
                            else:
                                if x[1022] <= 0.6176470816:
                                    results.append(0)
                                else:
                                    if x[1791] <= 0.5607843399:
                                        results.append(0)
                                    else:
                                        if x[1665] <= 0.6176470816:
                                            if x[771] <= 0.5627451241:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(0)
                        else:
                            if x[1933] <= 0.5078431517:
                                results.append(0)
                            else:
                                if x[102] <= 0.6372549236:
                                    results.append(1)
                                else:
                                    results.append(1)
                else:
                    if x[2466] <= 0.8352941275:
                        if x[611] <= 0.7882353067:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2609] <= 0.7411764860:
                            results.append(0)
                        else:
                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 19
    if time.time() < deadline or interrupt_flag.is_set():
        if x[5] <= 0.5784313977:
            if x[2923] <= 0.1549019665:
                if x[92] <= 0.0666666701:
                    if x[24] <= 0.1803921610:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    if x[330] <= 0.5411764979:
                        if x[69] <= 0.1470588297:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2342] <= 0.2627451047:
                            results.append(1)
                        else:
                            results.append(0)
            else:
                if x[2050] <= 0.0725490227:
                    if x[1219] <= 0.2509803995:
                        results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[2127] <= 0.3352941275:
                        if x[1922] <= 0.3294117749:
                            if x[1454] <= 0.4156862795:
                                if x[2027] <= 0.2450980395:
                                    if x[2339] <= 0.0568627454:
                                        results.append(1)
                                    else:
                                        if x[1195] <= 0.0960784331:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[43] <= 0.3843137324:
                                        results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[1460] <= 0.5882353187:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[602] <= 0.6745098233:
                                if x[2658] <= 0.4058823586:
                                    if x[943] <= 0.5568627715:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1081] <= 0.3823529482:
                                        results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2238] <= 0.2725490332:
                            if x[2031] <= 0.4764705896:
                                if x[2565] <= 0.4450980425:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[1959] <= 0.2784313858:
                                    if x[2229] <= 0.4705882370:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[642] <= 0.5294117928:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            if x[2532] <= 0.1235294156:
                                results.append(0)
                            else:
                                if x[2224] <= 0.2529411837:
                                    if x[2768] <= 0.2666666806:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1214] <= 0.6411764920:
                                        if x[1002] <= 0.0803921595:
                                            results.append(1)
                                        else:
                                            if x[246] <= 0.1039215699:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[1213] <= 0.6607843339:
                                            results.append(0)
                                        else:
                                            if x[1325] <= 0.8549019694:
                                                results.append(1)
                                            else:
                                                results.append(0)
        else:
            if x[2022] <= 0.8117647171:
                if x[206] <= 0.6254902184:
                    if x[2076] <= 0.1960784346:
                        results.append(0)
                    else:
                        if x[1739] <= 0.7352941334:
                            if x[2140] <= 0.1882352978:
                                results.append(0)
                            else:
                                if x[98] <= 0.5098039508:
                                    results.append(1)
                                else:
                                    if x[2853] <= 0.7274509966:
                                        results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            if x[1828] <= 0.7529411912:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[1181] <= 0.4137254953:
                        if x[2757] <= 0.3431372643:
                            if x[85] <= 0.6725490391:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2495] <= 0.4254902005:
                                if x[2678] <= 0.1764705926:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[1232] <= 0.1333333366:
                                    results.append(1)
                                else:
                                    if x[688] <= 0.5294117928:
                                        if x[2575] <= 0.5764706135:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[77] <= 0.8431372643:
                                            if x[148] <= 0.7627451122:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1980] <= 0.3823529482:
                                                results.append(0)
                                            else:
                                                results.append(0)
                    else:
                        if x[2557] <= 0.5058823824:
                            if x[1031] <= 0.2039215714:
                                results.append(0)
                            else:
                                if x[1118] <= 0.3647058904:
                                    if x[1570] <= 0.5764706135:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[2493] <= 0.9666666687:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            if x[1651] <= 0.6333333552:
                                if x[2585] <= 0.4117647111:
                                    results.append(0)
                                else:
                                    if x[1870] <= 0.1764705926:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[86] <= 0.8274509907:
                                    if x[1312] <= 0.6450980604:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[803] <= 0.6921568811:
                                        results.append(1)
                                    else:
                                        if x[1808] <= 0.8372549117:
                                            results.append(0)
                                        else:
                                            results.append(0)
            else:
                if x[1103] <= 0.5196078718:
                    if x[2748] <= 0.2568627596:
                        results.append(0)
                    else:
                        if x[2732] <= 0.8862745166:
                            results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[2409] <= 0.9509803951:
                        if x[1182] <= 0.4431372583:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 20
    if time.time() < deadline or interrupt_flag.is_set():
        if x[203] <= 0.5941176713:
            if x[2172] <= 0.2117647082:
                if x[2806] <= 0.2176470608:
                    if x[35] <= 0.1411764771:
                        results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[2977] <= 0.5215686560:
                        if x[1463] <= 0.3901960850:
                            if x[1601] <= 0.1352941208:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2002] <= 0.1921568662:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2849] <= 0.5098039359:
                            results.append(1)
                        else:
                            if x[2001] <= 0.1196078472:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[2658] <= 0.2490196154:
                    if x[1895] <= 0.3235294223:
                        if x[2489] <= 0.2078431398:
                            if x[1121] <= 0.1431372613:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[33] <= 0.2235294133:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[473] <= 0.0705882385:
                            results.append(1)
                        else:
                            if x[2425] <= 0.3705882430:
                                results.append(0)
                            else:
                                if x[1003] <= 0.4921568632:
                                    results.append(0)
                                else:
                                    results.append(1)
                else:
                    if x[2117] <= 0.6490196288:
                        if x[1661] <= 0.7607843280:
                            if x[638] <= 0.6176470816:
                                if x[558] <= 0.0803921595:
                                    if x[190] <= 0.0941176489:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1007] <= 0.6254902184:
                                        if x[2] <= 0.7666666806:
                                            if x[1560] <= 0.8470588326:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[1102] <= 0.5941176713:
                                            results.append(0)
                                        else:
                                            if x[2792] <= 0.4568627477:
                                                results.append(1)
                                            else:
                                                results.append(1)
                            else:
                                if x[2775] <= 0.5392157137:
                                    if x[329] <= 0.5784313977:
                                        results.append(1)
                                    else:
                                        if x[524] <= 0.6411764920:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                else:
                                    if x[1723] <= 0.4254902005:
                                        results.append(0)
                                    else:
                                        results.append(1)
                        else:
                            if x[2902] <= 0.5019607991:
                                if x[1676] <= 0.7431372702:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2424] <= 0.4784313738:
                            if x[1811] <= 0.6941176653:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1578] <= 0.8843137324:
                                if x[2002] <= 0.1823529452:
                                    results.append(0)
                                else:
                                    if x[2720] <= 0.7686274648:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(0)
        else:
            if x[1112] <= 0.3392156959:
                if x[2374] <= 0.3960784376:
                    if x[862] <= 0.8607843220:
                        if x[3003] <= 0.7274509966:
                            if x[1249] <= 0.7549019754:
                                if x[2455] <= 0.4039215744:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1486] <= 0.5156862885:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2615] <= 0.2098039240:
                        if x[2455] <= 0.4529411793:
                            results.append(1)
                        else:
                            if x[1711] <= 0.4333333373:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1977] <= 0.1901960820:
                            results.append(0)
                        else:
                            if x[1892] <= 0.4941176623:
                                results.append(1)
                            else:
                                if x[20] <= 0.9431372583:
                                    results.append(1)
                                else:
                                    results.append(0)
            else:
                if x[50] <= 0.5901961029:
                    if x[753] <= 0.4098039269:
                        if x[999] <= 0.5549019873:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[247] <= 0.7078431547:
                            results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[743] <= 0.5647059083:
                        if x[1983] <= 0.3980392218:
                            if x[901] <= 0.7000000179:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1408] <= 0.3666666746:
                                results.append(0)
                            else:
                                if x[2358] <= 0.4411764741:
                                    if x[2263] <= 0.3647058904:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[33] <= 0.8000000119:
                                        results.append(1)
                                    else:
                                        results.append(1)
                    else:
                        if x[497] <= 0.7117647231:
                            if x[1328] <= 0.3607843220:
                                results.append(1)
                            else:
                                if x[944] <= 0.9117647111:
                                    if x[2076] <= 0.5098039508:
                                        if x[2797] <= 0.5705882609:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[911] <= 0.6725490391:
                                            results.append(1)
                                        else:
                                            if x[2947] <= 0.5411764979:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[1649] <= 0.9549019635:
                                if x[2221] <= 0.6254902184:
                                    if x[1882] <= 0.0921568647:
                                        results.append(0)
                                    else:
                                        if x[1205] <= 0.2470588312:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2894] <= 0.5137255043:
                                        results.append(1)
                                    else:
                                        if x[562] <= 0.7078431547:
                                            results.append(0)
                                        else:
                                            if x[2884] <= 0.9392156899:
                                                results.append(0)
                                            else:
                                                results.append(0)
                            else:
                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 21
    if time.time() < deadline or interrupt_flag.is_set():
        if x[131] <= 0.6529411972:
            if x[2538] <= 0.3176470697:
                if x[2430] <= 0.2803921700:
                    if x[1061] <= 0.1137254909:
                        if x[1784] <= 0.4313725680:
                            results.append(1)
                        else:
                            if x[1484] <= 0.5686274767:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[2554] <= 0.4137254953:
                            if x[1679] <= 0.3784313798:
                                if x[925] <= 0.4588235319:
                                    if x[1352] <= 0.3039215803:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1623] <= 0.4176470637:
                                        results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[107] <= 0.6431372762:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[2318] <= 0.1313725524:
                                results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[2057] <= 0.5607843399:
                        if x[3029] <= 0.0803921595:
                            results.append(0)
                        else:
                            if x[68] <= 0.6450980604:
                                if x[2639] <= 0.3176470697:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1085] <= 0.4098039269:
                            results.append(1)
                        else:
                            results.append(0)
            else:
                if x[1550] <= 0.6019608080:
                    if x[2328] <= 0.2235294133:
                        if x[1417] <= 0.4509803951:
                            results.append(0)
                        else:
                            if x[1875] <= 0.6862745285:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2943] <= 0.1549019665:
                            if x[1700] <= 0.4137254953:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[464] <= 0.5784313977:
                                if x[2152] <= 0.0960784331:
                                    results.append(0)
                                else:
                                    if x[1576] <= 0.9078431427:
                                        if x[1067] <= 0.6980392337:
                                            if x[1699] <= 0.8313725591:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[1770] <= 0.4058823586:
                                    if x[1201] <= 0.4352941215:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[948] <= 0.3960784376:
                                        results.append(0)
                                    else:
                                        if x[1222] <= 0.2490196154:
                                            results.append(1)
                                        else:
                                            results.append(1)
                else:
                    if x[1740] <= 0.5666666925:
                        if x[707] <= 0.6333333552:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2102] <= 0.8627451062:
                            if x[739] <= 0.3058823645:
                                if x[1479] <= 0.4294117689:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[523] <= 0.2823529541:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
        else:
            if x[830] <= 0.5745098293:
                if x[2355] <= 0.3980392218:
                    if x[1996] <= 0.5784313977:
                        if x[2867] <= 0.2176470608:
                            if x[2736] <= 0.2529411837:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[610] <= 0.3235294223:
                                results.append(0)
                            else:
                                if x[2436] <= 0.4176470637:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[1668] <= 0.4333333373:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[627] <= 0.4215686321:
                        if x[2936] <= 0.7843137383:
                            if x[2403] <= 0.5411764979:
                                if x[1529] <= 0.3803921640:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2484] <= 0.2156862766:
                            results.append(0)
                        else:
                            if x[2219] <= 0.9078431427:
                                if x[1332] <= 0.3745098114:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[267] <= 0.9058823586:
                                    results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[1694] <= 0.2117647082:
                    if x[244] <= 0.6294117868:
                        results.append(0)
                    else:
                        if x[994] <= 0.7274509966:
                            if x[1320] <= 0.5941176713:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2550] <= 0.7843137383:
                        if x[1894] <= 0.6529411972:
                            if x[1517] <= 0.1647058874:
                                results.append(1)
                            else:
                                if x[1106] <= 0.2882353067:
                                    if x[2059] <= 0.4784313887:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1976] <= 0.1235294156:
                                        results.append(0)
                                    else:
                                        if x[2596] <= 0.9333333373:
                                            if x[188] <= 0.5568627715:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(0)
                        else:
                            if x[2315] <= 0.6588235497:
                                if x[2624] <= 0.3509804010:
                                    results.append(0)
                                else:
                                    if x[1059] <= 0.6215686500:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[688] <= 0.7392157018:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[877] <= 0.8568627536:
                            results.append(1)
                        else:
                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 22
    if time.time() < deadline or interrupt_flag.is_set():
        if x[110] <= 0.6960784495:
            if x[2559] <= 0.2450980395:
                if x[3068] <= 0.1980392188:
                    if x[2832] <= 0.2529411912:
                        if x[1465] <= 0.4039215744:
                            if x[1350] <= 0.2196078524:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[2088] <= 0.2568627596:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[1067] <= 0.6098039448:
                        if x[2521] <= 0.5588235557:
                            if x[2594] <= 0.1862745136:
                                if x[2166] <= 0.2823529541:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2466] <= 0.2764706016:
                                    if x[2450] <= 0.4450980425:
                                        if x[1069] <= 0.1745098084:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[553] <= 0.4274509847:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        results.append(0)
            else:
                if x[362] <= 0.6176470816:
                    if x[2421] <= 0.4921568632:
                        if x[2164] <= 0.0764705911:
                            if x[3029] <= 0.4000000060:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2567] <= 0.3862745166:
                                if x[1121] <= 0.4764705896:
                                    if x[1904] <= 0.5313725770:
                                        if x[2272] <= 0.1333333366:
                                            results.append(1)
                                        else:
                                            if x[13] <= 0.6450980604:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1820] <= 0.2509803995:
                                        if x[2864] <= 0.4196078479:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[2810] <= 0.3725490272:
                                            if x[2563] <= 0.3549019694:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                            else:
                                if x[117] <= 0.5235294402:
                                    if x[2390] <= 0.5431372821:
                                        if x[2183] <= 0.3941176534:
                                            if x[1515] <= 0.3882353008:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[2327] <= 0.4568627477:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                    else:
                                        if x[3038] <= 0.5823529661:
                                            if x[1041] <= 0.3411764801:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(1)
                                else:
                                    if x[1082] <= 0.5627451241:
                                        results.append(1)
                                    else:
                                        results.append(1)
                    else:
                        if x[2345] <= 0.8490196168:
                            if x[2151] <= 0.1666666716:
                                if x[2606] <= 0.6352941394:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2224] <= 0.3823529482:
                                    if x[1361] <= 0.4568627477:
                                        if x[1092] <= 0.7392157018:
                                            if x[2297] <= 0.1215686314:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[137] <= 0.7882353067:
                                        if x[2465] <= 0.8294117749:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            if x[283] <= 0.3823529482:
                                results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[447] <= 0.5313725770:
                        if x[2089] <= 0.7392157018:
                            if x[508] <= 0.5450980663:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2269] <= 0.6039215922:
                            if x[2265] <= 0.5000000149:
                                if x[2867] <= 0.4960784465:
                                    if x[2533] <= 0.3372549117:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2444] <= 0.4137254953:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[2475] <= 0.6450980604:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(1)
        else:
            if x[2739] <= 0.4450980425:
                if x[1691] <= 0.2725490332:
                    if x[1859] <= 0.3764705956:
                        if x[3044] <= 0.2333333418:
                            results.append(1)
                        else:
                            if x[830] <= 0.2647058889:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[2596] <= 0.5823529661:
                        if x[1424] <= 0.2607843280:
                            if x[2248] <= 0.3117647171:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2795] <= 0.6058823764:
                            if x[818] <= 0.4450980425:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2720] <= 0.1980392188:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[269] <= 0.5411764979:
                    if x[2568] <= 0.2470588312:
                        results.append(0)
                    else:
                        if x[3013] <= 0.6607843339:
                            results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[2625] <= 0.7784313858:
                        if x[1171] <= 0.5568627715:
                            if x[1062] <= 0.7039215863:
                                if x[1574] <= 0.6450980604:
                                    if x[2108] <= 0.3470588326:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1798] <= 0.5333333611:
                                    if x[367] <= 0.9117647111:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[777] <= 0.4745098203:
                                results.append(0)
                            else:
                                if x[1879] <= 0.1313725561:
                                    results.append(0)
                                else:
                                    if x[968] <= 0.9823529422:
                                        results.append(0)
                                    else:
                                        results.append(0)
                    else:
                        if x[2775] <= 0.9490196109:
                            if x[2463] <= 0.5274510086:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[1823] <= 0.9431372583:
                                results.append(0)
                            else:
                                results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 23
    if time.time() < deadline or interrupt_flag.is_set():
        if x[2] <= 0.6215686500:
            if x[2829] <= 0.1039215699:
                if x[1956] <= 0.1313725561:
                    results.append(1)
                else:
                    if x[1784] <= 0.1294117682:
                        results.append(0)
                    else:
                        if x[2427] <= 0.5078431517:
                            if x[1465] <= 0.2823529541:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
            else:
                if x[2557] <= 0.0392156877:
                    results.append(0)
                else:
                    if x[2448] <= 0.1588235348:
                        if x[1286] <= 0.4607843161:
                            if x[1039] <= 0.1901960820:
                                results.append(0)
                            else:
                                if x[2448] <= 0.1431372613:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[274] <= 0.3039215803:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[534] <= 0.2490196154:
                            if x[1112] <= 0.5823529661:
                                if x[2108] <= 0.5235294402:
                                    if x[1014] <= 0.1490196139:
                                        if x[2477] <= 0.2274509817:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[83] <= 0.0235294122:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[998] <= 0.3470588326:
                                        if x[1669] <= 0.4607843161:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                if x[1518] <= 0.3039215803:
                                    results.append(1)
                                else:
                                    if x[1515] <= 0.5176470876:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            if x[2233] <= 0.1372549087:
                                if x[2047] <= 0.0960784331:
                                    results.append(1)
                                else:
                                    if x[2528] <= 0.1607843153:
                                        results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[410] <= 0.4803921580:
                                    if x[1023] <= 0.9352941215:
                                        if x[2468] <= 0.5235294402:
                                            if x[2932] <= 0.1176470593:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1670] <= 0.7000000179:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2220] <= 0.5607843399:
                                        if x[1457] <= 0.6843137443:
                                            if x[2524] <= 0.1509803981:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[123] <= 0.6313725710:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(1)
        else:
            if x[719] <= 0.3862745166:
                if x[2625] <= 0.1784313768:
                    if x[2323] <= 0.1686274558:
                        results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[1500] <= 0.8098039329:
                        if x[1156] <= 0.3862745166:
                            if x[2017] <= 0.5313725770:
                                if x[2863] <= 0.5352941453:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2265] <= 0.1137254909:
                                results.append(0)
                            else:
                                if x[1109] <= 0.5921568871:
                                    if x[2080] <= 0.2156862766:
                                        results.append(1)
                                    else:
                                        if x[1098] <= 0.1803921610:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
                    else:
                        results.append(0)
            else:
                if x[2553] <= 0.7313725650:
                    if x[2216] <= 0.9509803951:
                        if x[2053] <= 0.5215686560:
                            if x[545] <= 0.3352941275:
                                results.append(1)
                            else:
                                if x[2879] <= 0.2215686291:
                                    if x[1097] <= 0.4686274529:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1033] <= 0.4568627477:
                                        if x[2894] <= 0.2901960909:
                                            results.append(0)
                                        else:
                                            if x[2976] <= 0.7372549176:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                    else:
                                        if x[3031] <= 0.1000000015:
                                            results.append(0)
                                        else:
                                            results.append(0)
                        else:
                            if x[437] <= 0.4647058845:
                                results.append(1)
                            else:
                                if x[1214] <= 0.2176470608:
                                    if x[1341] <= 0.5490196198:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2560] <= 0.7490196228:
                                        if x[629] <= 0.5862745345:
                                            results.append(1)
                                        else:
                                            if x[827] <= 0.8627451062:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                    else:
                                        results.append(1)
                    else:
                        if x[2384] <= 0.6960784495:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2377] <= 0.4705882370:
                        if x[2318] <= 0.5313725621:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1425] <= 0.4470588267:
                            results.append(0)
                        else:
                            if x[1589] <= 0.2078431398:
                                results.append(1)
                            else:
                                results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 24
    if time.time() < deadline or interrupt_flag.is_set():
        if x[308] <= 0.6568627656:
            if x[2643] <= 0.1823529452:
                if x[1755] <= 0.3627451062:
                    if x[1448] <= 0.3352941275:
                        if x[1873] <= 0.5274509937:
                            if x[1786] <= 0.1803921610:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[2230] <= 0.5098039508:
                        if x[1427] <= 0.3294117749:
                            if x[2146] <= 0.4000000060:
                                if x[1703] <= 0.2823529541:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[868] <= 0.4117647111:
                            results.append(0)
                        else:
                            results.append(1)
            else:
                if x[653] <= 0.5901961029:
                    if x[1598] <= 0.7921568751:
                        if x[2140] <= 0.4725490212:
                            if x[1764] <= 0.7862745225:
                                if x[2678] <= 0.3823529482:
                                    if x[1127] <= 0.4686274529:
                                        if x[1858] <= 0.1490196139:
                                            if x[1453] <= 0.1627451032:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[740] <= 0.4313725531:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[2495] <= 0.1745098084:
                                            results.append(1)
                                        else:
                                            if x[2245] <= 0.4039215744:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                else:
                                    if x[2178] <= 0.3294117749:
                                        if x[2640] <= 0.3941176534:
                                            results.append(1)
                                        else:
                                            if x[2097] <= 0.3686274588:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                    else:
                                        if x[1586] <= 0.5294117928:
                                            if x[1113] <= 0.7607843280:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1875] <= 0.6333333552:
                                                results.append(0)
                                            else:
                                                results.append(1)
                            else:
                                if x[2894] <= 0.2627451122:
                                    results.append(1)
                                else:
                                    if x[2320] <= 0.3333333433:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            if x[2070] <= 0.1470588297:
                                results.append(1)
                            else:
                                if x[2270] <= 0.8411764801:
                                    if x[2145] <= 0.2274509892:
                                        results.append(1)
                                    else:
                                        if x[286] <= 0.9117647111:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[2466] <= 0.8862745166:
                                        results.append(1)
                                    else:
                                        results.append(0)
                    else:
                        if x[720] <= 0.3215686381:
                            results.append(0)
                        else:
                            if x[382] <= 0.3666666746:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[2326] <= 0.4196078479:
                        if x[2370] <= 0.6176470816:
                            if x[2410] <= 0.4235294163:
                                if x[1671] <= 0.2490196154:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1834] <= 0.4235294163:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[235] <= 0.4509803951:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[1785] <= 0.2019607872:
                            results.append(0)
                        else:
                            if x[2672] <= 0.8019607961:
                                if x[2270] <= 0.2411764786:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
        else:
            if x[2127] <= 0.5392157137:
                if x[845] <= 0.5627451241:
                    if x[2467] <= 0.2607843280:
                        if x[946] <= 0.7039215863:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[795] <= 0.3980392218:
                            if x[1843] <= 0.3882353008:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1557] <= 0.6803921759:
                                if x[1971] <= 0.2490196154:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[2710] <= 0.7745098174:
                        if x[2625] <= 0.7372549176:
                            if x[338] <= 0.6568627656:
                                if x[2559] <= 0.3607843220:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1844] <= 0.7803921700:
                                    if x[1380] <= 0.8882353008:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1390] <= 0.4882352948:
                            results.append(1)
                        else:
                            results.append(0)
            else:
                if x[719] <= 0.6607843339:
                    if x[1888] <= 0.4176470637:
                        if x[1771] <= 0.2058823556:
                            results.append(1)
                        else:
                            if x[2245] <= 0.5431372821:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[869] <= 0.3000000119:
                            results.append(1)
                        else:
                            if x[867] <= 0.5980392396:
                                results.append(1)
                            else:
                                results.append(1)
                else:
                    if x[129] <= 0.9901960790:
                        if x[1592] <= 0.2137254924:
                            if x[1331] <= 0.8549019694:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[17] <= 0.6392157078:
                                results.append(1)
                            else:
                                if x[2597] <= 0.7921568751:
                                    results.append(0)
                                else:
                                    if x[167] <= 0.8705882430:
                                        results.append(0)
                                    else:
                                        results.append(0)
                    else:
                        results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 25
    if time.time() < deadline or interrupt_flag.is_set():
        if x[50] <= 0.5941176713:
            if x[2140] <= 0.2058823556:
                if x[2454] <= 0.1588235348:
                    if x[1679] <= 0.2784313858:
                        results.append(1)
                    else:
                        if x[2512] <= 0.4450980425:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[2807] <= 0.4235294163:
                        if x[113] <= 0.4823529422:
                            if x[3040] <= 0.2039215714:
                                results.append(0)
                            else:
                                if x[2748] <= 0.1764705926:
                                    results.append(0)
                                else:
                                    if x[3018] <= 0.6313725710:
                                        if x[2486] <= 0.1098039225:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[873] <= 0.2117647082:
                            results.append(1)
                        else:
                            if x[331] <= 0.4196078479:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[1463] <= 0.6431372762:
                    if x[2658] <= 0.3156862855:
                        if x[3050] <= 0.3117647171:
                            if x[1210] <= 0.6098039448:
                                results.append(1)
                            else:
                                if x[293] <= 0.2862745225:
                                    if x[1084] <= 0.2647058889:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[1992] <= 0.3745098114:
                                if x[2353] <= 0.3568627536:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[463] <= 0.8058823645:
                            if x[1960] <= 0.2215686291:
                                if x[1004] <= 0.5627451241:
                                    if x[2293] <= 0.6137255132:
                                        if x[294] <= 0.5705882609:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1370] <= 0.6098039448:
                                    if x[2524] <= 0.0647058859:
                                        results.append(1)
                                    else:
                                        if x[1315] <= 0.2215686291:
                                            if x[109] <= 0.2019607872:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1548] <= 0.2254901975:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    if x[2025] <= 0.5078431517:
                                        results.append(1)
                                    else:
                                        results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[1270] <= 0.6352941394:
                        if x[2874] <= 0.5196078569:
                            if x[655] <= 0.1901960820:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2346] <= 0.3411764801:
                            results.append(0)
                        else:
                            if x[2056] <= 0.3215686381:
                                results.append(0)
                            else:
                                if x[1386] <= 0.8529411852:
                                    results.append(1)
                                else:
                                    results.append(0)
        else:
            if x[2568] <= 0.5470588505:
                if x[536] <= 0.2372549027:
                    results.append(1)
                else:
                    if x[1022] <= 0.4960784316:
                        if x[2473] <= 0.2294117659:
                            if x[222] <= 0.6490196288:
                                results.append(0)
                            else:
                                if x[2532] <= 0.5156862885:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[1292] <= 0.3078431487:
                                if x[1231] <= 0.2529411837:
                                    results.append(0)
                                else:
                                    if x[276] <= 0.8960784376:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[3071] <= 0.2960784435:
                                    if x[132] <= 0.8313725591:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1779] <= 0.2647058889:
                                        results.append(0)
                                    else:
                                        if x[626] <= 0.4254902005:
                                            results.append(0)
                                        else:
                                            results.append(0)
                    else:
                        if x[2462] <= 0.7666666806:
                            if x[1429] <= 0.1549019665:
                                results.append(1)
                            else:
                                if x[396] <= 0.2215686291:
                                    results.append(0)
                                else:
                                    if x[842] <= 0.6156862974:
                                        if x[2127] <= 0.4941176623:
                                            if x[965] <= 0.8235294223:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[2831] <= 0.4784313738:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                    else:
                                        if x[1136] <= 0.9803921580:
                                            if x[1143] <= 0.9568627477:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(0)
                        else:
                            results.append(0)
            else:
                if x[2268] <= 0.4980392307:
                    if x[2355] <= 0.3176470697:
                        if x[2214] <= 0.7764706016:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1500] <= 0.4823529422:
                            if x[1959] <= 0.2549019754:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1719] <= 0.7588235438:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[1205] <= 0.8019607961:
                        if x[2832] <= 0.3666666746:
                            results.append(0)
                        else:
                            if x[989] <= 0.8470588326:
                                if x[2305] <= 0.3607843220:
                                    results.append(0)
                                else:
                                    if x[1824] <= 0.5588235557:
                                        if x[1736] <= 0.5803921819:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[209] <= 0.9470588267:
                                            if x[689] <= 0.8019607961:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                            else:
                                if x[2664] <= 0.8980392218:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[1152] <= 0.6490196288:
                            results.append(0)
                        else:
                            results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 26
    if time.time() < deadline or interrupt_flag.is_set():
        if x[161] <= 0.6411764920:
            if x[2727] <= 0.1392156929:
                if x[664] <= 0.0607843157:
                    results.append(1)
                else:
                    if x[2437] <= 0.2764706016:
                        if x[96] <= 0.6039215922:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1506] <= 0.5784313977:
                            results.append(1)
                        else:
                            results.append(0)
            else:
                if x[2266] <= 0.1509803981:
                    if x[2069] <= 0.1235294156:
                        if x[2783] <= 0.1803921573:
                            results.append(1)
                        else:
                            if x[2927] <= 0.5215686411:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2681] <= 0.2666666731:
                            if x[2327] <= 0.2686274573:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[52] <= 0.5647059083:
                                if x[982] <= 0.4627451152:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[1268] <= 0.7392157018:
                        if x[2161] <= 0.2019607872:
                            if x[2233] <= 0.2352941185:
                                if x[1543] <= 0.3039215803:
                                    results.append(1)
                                else:
                                    if x[2144] <= 0.1098039225:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[2077] <= 0.1823529452:
                                    results.append(0)
                                else:
                                    if x[1796] <= 0.6372549236:
                                        results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            if x[2546] <= 0.1431372613:
                                if x[1660] <= 0.7235294282:
                                    if x[650] <= 0.2000000030:
                                        results.append(1)
                                    else:
                                        if x[3042] <= 0.5078431517:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1487] <= 0.3980392218:
                                    if x[2751] <= 0.1921568662:
                                        results.append(1)
                                    else:
                                        if x[167] <= 0.6137255132:
                                            if x[2645] <= 0.7235294282:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[364] <= 0.6274510026:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    if x[1485] <= 0.4490196109:
                                        if x[1673] <= 0.5509804189:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2847] <= 0.2156862766:
                                            if x[1908] <= 0.5431372821:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[277] <= 0.6509804130:
                                                results.append(1)
                                            else:
                                                results.append(1)
                    else:
                        if x[2413] <= 0.7235294282:
                            if x[994] <= 0.8078431487:
                                if x[1683] <= 0.4607843161:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
        else:
            if x[1406] <= 0.4058823586:
                if x[2259] <= 0.3078431487:
                    if x[1443] <= 0.8058823645:
                        if x[1295] <= 0.2392156869:
                            results.append(1)
                        else:
                            if x[1151] <= 0.2921568751:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[1969] <= 0.2725490332:
                        if x[296] <= 0.6294117868:
                            if x[2464] <= 0.4980392307:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[150] <= 0.8254902065:
                                if x[1890] <= 0.5333333611:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2916] <= 0.2156862766:
                            results.append(0)
                        else:
                            if x[1102] <= 0.4882352948:
                                if x[769] <= 0.4568627477:
                                    results.append(0)
                                else:
                                    if x[1249] <= 0.4196078479:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[1860] <= 0.3333333433:
                                    results.append(0)
                                else:
                                    if x[2644] <= 0.7705882490:
                                        if x[48] <= 0.6019608080:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
            else:
                if x[1828] <= 0.9784313738:
                    if x[371] <= 0.3254902065:
                        if x[2252] <= 0.4470588416:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2277] <= 0.5784313977:
                            if x[2221] <= 0.6176470816:
                                if x[545] <= 0.4647058845:
                                    if x[1157] <= 0.2490196154:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[388] <= 0.1509803981:
                                        results.append(0)
                                    else:
                                        if x[1510] <= 0.2098039240:
                                            results.append(0)
                                        else:
                                            results.append(0)
                            else:
                                if x[3008] <= 0.6156862974:
                                    results.append(1)
                                else:
                                    if x[2623] <= 0.8294117749:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            if x[484] <= 0.6450980604:
                                if x[1868] <= 0.6921568811:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2748] <= 0.7156862915:
                                    if x[83] <= 0.9862745106:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                else:
                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 27
    if time.time() < deadline or interrupt_flag.is_set():
        if x[212] <= 0.6529411972:
            if x[2634] <= 0.2843137383:
                if x[734] <= 0.3078431487:
                    if x[1738] <= 0.5647059083:
                        if x[1688] <= 0.7392157018:
                            if x[12] <= 0.0352941193:
                                results.append(0)
                            else:
                                if x[632] <= 0.3568627536:
                                    if x[1587] <= 0.1372549087:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2386] <= 0.3294117749:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[1681] <= 0.3901960850:
                        if x[1126] <= 0.6549019814:
                            if x[2861] <= 0.3745098114:
                                if x[1206] <= 0.4725490361:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2618] <= 0.2745098174:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[662] <= 0.2960784435:
                            if x[1984] <= 0.3607843220:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2991] <= 0.6254902184:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[1550] <= 0.6117647290:
                    if x[2139] <= 0.2274509817:
                        if x[2659] <= 0.5156863034:
                            if x[729] <= 0.1490196139:
                                if x[677] <= 0.3254901990:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[572] <= 0.6215686500:
                                    if x[1427] <= 0.1039215699:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1582] <= 0.4235294163:
                                if x[1674] <= 0.2058823556:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[646] <= 0.4549019635:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[230] <= 0.7392157018:
                            if x[2944] <= 0.0784313753:
                                results.append(0)
                            else:
                                if x[2648] <= 0.8470588326:
                                    if x[119] <= 0.5882353187:
                                        if x[1891] <= 0.0568627473:
                                            results.append(0)
                                        else:
                                            if x[1014] <= 0.1019607857:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[1984] <= 0.2960784435:
                                            results.append(0)
                                        else:
                                            if x[1832] <= 0.5235294402:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                else:
                                    if x[3050] <= 0.7117647231:
                                        results.append(0)
                                    else:
                                        results.append(1)
                        else:
                            if x[1459] <= 0.4352941215:
                                if x[2363] <= 0.5490196347:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                else:
                    if x[2230] <= 0.5921568871:
                        if x[2223] <= 0.5588235557:
                            if x[1593] <= 0.1980392225:
                                results.append(0)
                            else:
                                if x[2590] <= 0.2862745225:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[1300] <= 0.3529411852:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[3003] <= 0.4411764741:
                            results.append(0)
                        else:
                            if x[261] <= 0.1529411823:
                                results.append(1)
                            else:
                                results.append(1)
        else:
            if x[2458] <= 0.5078431666:
                if x[2526] <= 0.4176470637:
                    if x[938] <= 0.2647058964:
                        if x[1229] <= 0.3686274588:
                            if x[3014] <= 0.2980392277:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2611] <= 0.6019608080:
                            if x[2643] <= 0.4450980425:
                                if x[1982] <= 0.0882352963:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2644] <= 0.5411764979:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[1745] <= 0.5352941304:
                                results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[2143] <= 0.3372549117:
                        if x[554] <= 0.4058823586:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1322] <= 0.3921568692:
                            if x[1521] <= 0.2882353067:
                                results.append(0)
                            else:
                                if x[413] <= 0.9509803951:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[448] <= 0.6000000238:
                                if x[649] <= 0.3254902065:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[765] <= 0.9509803951:
                                    if x[1962] <= 0.5156862885:
                                        results.append(0)
                                    else:
                                        if x[2055] <= 0.6764706075:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[800] <= 0.5921568871:
                    if x[921] <= 0.1627451032:
                        results.append(0)
                    else:
                        if x[1984] <= 0.3450980484:
                            if x[2415] <= 0.3588235378:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[709] <= 0.6686274707:
                                results.append(1)
                            else:
                                results.append(1)
                else:
                    if x[528] <= 0.8156862855:
                        if x[278] <= 0.5156862885:
                            results.append(1)
                        else:
                            if x[2985] <= 0.6019608080:
                                results.append(0)
                            else:
                                if x[2991] <= 0.6196078658:
                                    results.append(1)
                                else:
                                    if x[358] <= 0.6941176653:
                                        results.append(1)
                                    else:
                                        results.append(0)
                    else:
                        if x[1623] <= 0.6294117868:
                            results.append(0)
                        else:
                            if x[1471] <= 0.8215686381:
                                if x[1519] <= 0.6843137443:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 28
    if time.time() < deadline or interrupt_flag.is_set():
        if x[131] <= 0.5901961029:
            if x[2442] <= 0.2960784435:
                if x[1400] <= 0.6098039448:
                    if x[2338] <= 0.1333333403:
                        if x[2402] <= 0.1235294156:
                            results.append(1)
                        else:
                            if x[2475] <= 0.4137254953:
                                if x[697] <= 0.3725490272:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[1484] <= 0.4568627477:
                            if x[1185] <= 0.7921568751:
                                if x[2691] <= 0.5568627715:
                                    if x[2727] <= 0.1117647067:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1653] <= 0.5078431517:
                                        results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1622] <= 0.3784313798:
                                if x[1247] <= 0.2803921700:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[987] <= 0.4666666836:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[2829] <= 0.5156863034:
                        if x[2188] <= 0.4274509847:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
            else:
                if x[2541] <= 0.1862745136:
                    if x[3006] <= 0.5941176713:
                        if x[1176] <= 0.3529411852:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[805] <= 0.0607843157:
                        results.append(0)
                    else:
                        if x[1175] <= 0.4019607902:
                            if x[2628] <= 0.1490196139:
                                results.append(0)
                            else:
                                if x[1675] <= 0.8372549117:
                                    if x[1703] <= 0.1098039225:
                                        if x[1377] <= 0.4058823586:
                                            if x[809] <= 0.1490196139:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[702] <= 0.1196078435:
                                            if x[2702] <= 0.3921568692:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(1)
                                else:
                                    if x[1702] <= 0.5196078569:
                                        results.append(1)
                                    else:
                                        results.append(0)
                        else:
                            if x[2236] <= 0.1784313768:
                                if x[920] <= 0.6176470816:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1500] <= 0.8843137324:
                                    if x[1174] <= 0.4254902005:
                                        if x[1229] <= 0.4294117689:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2101] <= 0.8450980484:
                                            if x[1564] <= 0.7490196228:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    results.append(0)
        else:
            if x[998] <= 0.3588235378:
                if x[2442] <= 0.3235294223:
                    if x[1468] <= 0.3137255013:
                        if x[1455] <= 0.4529411793:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1573] <= 0.3490196168:
                            if x[251] <= 0.7686274648:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[708] <= 0.2647058964:
                        if x[239] <= 0.7058823705:
                            if x[2415] <= 0.4215686321:
                                results.append(0)
                            else:
                                if x[731] <= 0.3686274588:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[1394] <= 0.5294117928:
                            if x[1368] <= 0.2529411912:
                                if x[90] <= 0.6980392337:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2736] <= 0.3196078539:
                                    results.append(1)
                                else:
                                    if x[1435] <= 0.2725490332:
                                        results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            results.append(0)
            else:
                if x[2448] <= 0.5431372821:
                    if x[158] <= 0.5568627715:
                        if x[2469] <= 0.4352941215:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[1086] <= 0.9705882370:
                            if x[1490] <= 0.1980392188:
                                if x[1933] <= 0.4568627477:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[719] <= 0.6098039448:
                                    if x[1336] <= 0.6980392337:
                                        if x[2128] <= 0.4352941215:
                                            if x[1098] <= 0.7000000179:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2718] <= 0.2509803995:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                else:
                                    if x[63] <= 0.9686274529:
                                        results.append(0)
                                    else:
                                        if x[103] <= 0.9568627477:
                                            results.append(0)
                                        else:
                                            results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2088] <= 0.3647058904:
                        if x[2140] <= 0.6509804130:
                            if x[2151] <= 0.6431372762:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2551] <= 0.3372549117:
                            results.append(0)
                        else:
                            if x[1953] <= 0.3588235378:
                                if x[824] <= 0.6745098233:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1016] <= 0.8490196168:
                                    if x[1658] <= 0.5509804189:
                                        results.append(1)
                                    else:
                                        if x[126] <= 0.7078431547:
                                            results.append(0)
                                        else:
                                            if x[457] <= 0.7745098174:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 29
    if time.time() < deadline or interrupt_flag.is_set():
        if x[65] <= 0.6254902184:
            if x[2346] <= 0.2019607872:
                if x[1649] <= 0.4215686321:
                    if x[1469] <= 0.3941176534:
                        if x[2987] <= 0.4137254953:
                            if x[908] <= 0.0764705911:
                                results.append(0)
                            else:
                                if x[532] <= 0.6058823764:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1633] <= 0.3647058904:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[675] <= 0.4882352948:
                        if x[2082] <= 0.1529411823:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
            else:
                if x[2667] <= 0.1156862751:
                    if x[401] <= 0.2039215714:
                        if x[1703] <= 0.4215686321:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[1526] <= 0.1529411823:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[2046] <= 0.1392156929:
                        if x[1682] <= 0.2235294133:
                            results.append(1)
                        else:
                            if x[1656] <= 0.3313725516:
                                results.append(1)
                            else:
                                if x[2744] <= 0.2411764786:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[1268] <= 0.6058823764:
                            if x[2245] <= 0.9470588267:
                                if x[911] <= 0.5901961029:
                                    if x[1780] <= 0.8901960850:
                                        if x[1299] <= 0.8215686381:
                                            if x[2076] <= 0.1392156929:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[977] <= 0.1960784346:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[2634] <= 0.2882353067:
                                        results.append(0)
                                    else:
                                        if x[1026] <= 0.5568627715:
                                            if x[1468] <= 0.3352941275:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1858] <= 0.8058823645:
                                                results.append(1)
                                            else:
                                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2145] <= 0.4843137264:
                                if x[1022] <= 0.3921568692:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1110] <= 0.4000000060:
                                    results.append(0)
                                else:
                                    if x[1511] <= 0.6470588446:
                                        results.append(1)
                                    else:
                                        results.append(1)
        else:
            if x[1286] <= 0.3568627536:
                if x[2170] <= 0.1823529452:
                    if x[2433] <= 0.3686274588:
                        results.append(0)
                    else:
                        results.append(0)
                else:
                    if x[2332] <= 0.2490196154:
                        if x[1383] <= 0.3568627536:
                            if x[2140] <= 0.2745098174:
                                if x[2156] <= 0.4862745106:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[932] <= 0.4019607902:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1459] <= 0.1235294156:
                            results.append(0)
                        else:
                            if x[1112] <= 0.6607843339:
                                if x[1185] <= 0.2607843280:
                                    if x[248] <= 0.7745098174:
                                        results.append(0)
                                    else:
                                        if x[912] <= 0.2490196154:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                else:
                                    if x[3036] <= 0.5215686560:
                                        if x[721] <= 0.6176470816:
                                            if x[2443] <= 0.5980392396:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                if x[2684] <= 0.4019607902:
                                    results.append(1)
                                else:
                                    results.append(0)
            else:
                if x[2331] <= 0.5392157137:
                    if x[1705] <= 0.1823529452:
                        if x[918] <= 0.3019607961:
                            results.append(1)
                        else:
                            if x[2125] <= 0.2058823556:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2984] <= 0.1058823541:
                            results.append(0)
                        else:
                            if x[2422] <= 0.6294117868:
                                if x[1761] <= 0.8784313798:
                                    if x[2253] <= 0.6647059023:
                                        if x[1196] <= 0.4078431427:
                                            if x[194] <= 0.8568627536:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[3012] <= 0.8019607961:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2186] <= 0.7000000179:
                                    results.append(0)
                                else:
                                    results.append(1)
                else:
                    if x[2685] <= 0.5549019873:
                        if x[35] <= 0.5294117928:
                            results.append(1)
                        else:
                            if x[1505] <= 0.3372549117:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1963] <= 0.4529411793:
                            if x[774] <= 0.5509804189:
                                results.append(1)
                            else:
                                if x[1391] <= 0.4901960939:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[701] <= 0.9215686321:
                                if x[1567] <= 0.4725490212:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 30
    if time.time() < deadline or interrupt_flag.is_set():
        if x[11] <= 0.5078431666:
            if x[2652] <= 0.2921568751:
                if x[1610] <= 0.3392156959:
                    if x[2749] <= 0.1450980455:
                        if x[86] <= 0.1470588297:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[219] <= 0.0725490227:
                            results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[1553] <= 0.4215686321:
                        if x[2535] <= 0.2352941185:
                            if x[2061] <= 0.2117647082:
                                results.append(1)
                            else:
                                if x[1058] <= 0.4313725531:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[1573] <= 0.7470588386:
                                if x[1906] <= 0.6117647290:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[3007] <= 0.5823529661:
                            if x[2134] <= 0.5372549295:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
            else:
                if x[2073] <= 0.1509803981:
                    if x[1281] <= 0.5411764979:
                        results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[2266] <= 0.2647058964:
                        if x[695] <= 0.4372549057:
                            if x[2278] <= 0.1588235348:
                                results.append(0)
                            else:
                                if x[1897] <= 0.1666666716:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[275] <= 0.4666666687:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1190] <= 0.7313725650:
                            if x[3047] <= 0.0333333351:
                                results.append(0)
                            else:
                                if x[1305] <= 0.0862745121:
                                    results.append(1)
                                else:
                                    if x[723] <= 0.0803921595:
                                        results.append(1)
                                    else:
                                        if x[2600] <= 0.3980392218:
                                            results.append(1)
                                        else:
                                            if x[1028] <= 0.1372549087:
                                                results.append(1)
                                            else:
                                                results.append(1)
                        else:
                            if x[2834] <= 0.4784313738:
                                results.append(1)
                            else:
                                results.append(0)
        else:
            if x[2343] <= 0.3627451062:
                if x[1529] <= 0.9941176474:
                    if x[380] <= 0.7235294282:
                        if x[65] <= 0.8666666746:
                            if x[2595] <= 0.6764706075:
                                if x[2128] <= 0.4470588267:
                                    if x[763] <= 0.2196078449:
                                        results.append(0)
                                    else:
                                        if x[1303] <= 0.6372549236:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2415] <= 0.4549019635:
                                        results.append(0)
                                    else:
                                        if x[1790] <= 0.3568627536:
                                            results.append(1)
                                        else:
                                            results.append(0)
                            else:
                                if x[1132] <= 0.4372549057:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[1358] <= 0.4333333373:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2431] <= 0.4568627477:
                            if x[2501] <= 0.1000000015:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[965] <= 0.4372549057:
                                results.append(1)
                            else:
                                if x[1330] <= 0.7274509966:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    results.append(1)
            else:
                if x[89] <= 0.5176470876:
                    if x[2232] <= 0.1784313768:
                        results.append(0)
                    else:
                        if x[2540] <= 0.7431372702:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[1295] <= 0.4058823586:
                        if x[2931] <= 0.2490196154:
                            if x[1387] <= 0.3509804010:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[3070] <= 0.6823529601:
                                if x[293] <= 0.6039215922:
                                    if x[3058] <= 0.4019607902:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1304] <= 0.2901960909:
                                        if x[1358] <= 0.4843137264:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[497] <= 0.6705882549:
                                            results.append(1)
                                        else:
                                            if x[3068] <= 0.3843137324:
                                                results.append(0)
                                            else:
                                                results.append(0)
                            else:
                                if x[1310] <= 0.6529411972:
                                    if x[948] <= 0.4627451003:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[1031] <= 0.4039215744:
                            if x[681] <= 0.8215686381:
                                if x[667] <= 0.4098039269:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2382] <= 0.6156862974:
                                if x[1775] <= 0.3117647171:
                                    if x[977] <= 0.5254902095:
                                        results.append(0)
                                    else:
                                        if x[2076] <= 0.5000000149:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2903] <= 0.8529411852:
                                        if x[1646] <= 0.8313725591:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[713] <= 0.3588235378:
                                    results.append(1)
                                else:
                                    if x[1743] <= 0.6509804130:
                                        if x[1878] <= 0.7352941334:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[1747] <= 0.8352941275:
                                            results.append(1)
                                        else:
                                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 31
    if time.time() < deadline or interrupt_flag.is_set():
        if x[113] <= 0.6254902184:
            if x[2653] <= 0.1470588297:
                if x[529] <= 0.1509803981:
                    results.append(1)
                else:
                    if x[966] <= 0.7196078598:
                        if x[1980] <= 0.3980392218:
                            if x[623] <= 0.3549019694:
                                results.append(1)
                            else:
                                if x[2142] <= 0.1392156929:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
            else:
                if x[1181] <= 0.5784313977:
                    if x[1463] <= 0.7647058964:
                        if x[2247] <= 0.1823529452:
                            if x[2088] <= 0.4666666687:
                                if x[179] <= 0.2098039240:
                                    results.append(1)
                                else:
                                    if x[1828] <= 0.3117647171:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2736] <= 0.1196078435:
                                results.append(0)
                            else:
                                if x[2158] <= 0.1000000015:
                                    if x[1690] <= 0.4705882370:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[815] <= 0.6176470816:
                                        if x[1476] <= 0.9137254953:
                                            if x[320] <= 0.4686274529:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[1954] <= 0.3647058904:
                                            results.append(0)
                                        else:
                                            if x[2737] <= 0.2941176593:
                                                results.append(0)
                                            else:
                                                results.append(1)
                    else:
                        if x[789] <= 0.4117647111:
                            if x[1387] <= 0.4745098054:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[984] <= 0.7784313858:
                        if x[2256] <= 0.5901961029:
                            if x[543] <= 0.3254902065:
                                if x[1422] <= 0.8352941275:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[438] <= 0.4705882370:
                                    results.append(1)
                                else:
                                    if x[68] <= 0.5215686560:
                                        if x[928] <= 0.5196078718:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                        else:
                            if x[627] <= 0.3980392218:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[629] <= 0.6196078658:
                            if x[25] <= 0.2333333343:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
        else:
            if x[557] <= 0.5196078718:
                if x[2530] <= 0.3372549117:
                    if x[2218] <= 0.7196078598:
                        if x[658] <= 0.3196078539:
                            if x[1685] <= 0.3627451062:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[2855] <= 0.1607843190:
                        results.append(0)
                    else:
                        if x[2545] <= 0.3078431487:
                            results.append(0)
                        else:
                            if x[1595] <= 0.5666666925:
                                if x[828] <= 0.7372549176:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
            else:
                if x[311] <= 0.6607843339:
                    if x[1316] <= 0.3823529482:
                        if x[711] <= 0.3941176534:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2389] <= 0.6411764920:
                            if x[7] <= 0.8607843220:
                                if x[173] <= 0.6549019814:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[1193] <= 0.1137254946:
                        results.append(1)
                    else:
                        if x[440] <= 0.3372549117:
                            results.append(1)
                        else:
                            if x[1799] <= 0.9725490212:
                                if x[2355] <= 0.4705882370:
                                    if x[1317] <= 0.2019607872:
                                        results.append(0)
                                    else:
                                        if x[1871] <= 0.2627451122:
                                            if x[750] <= 0.4627451003:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[1650] <= 0.4450980425:
                                        if x[2360] <= 0.3941176534:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[1013] <= 0.4901960790:
                                            if x[447] <= 0.6627451181:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[296] <= 0.6784313917:
                                                results.append(1)
                                            else:
                                                results.append(0)
                            else:
                                results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 32
    if time.time() < deadline or interrupt_flag.is_set():
        if x[221] <= 0.6490196288:
            if x[2454] <= 0.2490196154:
                if x[1370] <= 0.4176470637:
                    if x[1779] <= 0.6509804130:
                        if x[2858] <= 0.5549019873:
                            if x[1676] <= 0.5117647350:
                                if x[1835] <= 0.0529411770:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[805] <= 0.4784313738:
                            if x[1734] <= 0.3745098114:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2809] <= 0.5117647350:
                        if x[1912] <= 0.1490196139:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2990] <= 0.5039215833:
                            results.append(1)
                        else:
                            results.append(0)
            else:
                if x[128] <= 0.4882352948:
                    if x[1208] <= 0.5745098293:
                        if x[2808] <= 0.1450980455:
                            if x[2713] <= 0.0882352963:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2012] <= 0.4647058845:
                                if x[910] <= 0.0686274543:
                                    results.append(1)
                                else:
                                    if x[1557] <= 0.9450980425:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[2491] <= 0.3098039329:
                                    results.append(0)
                                else:
                                    if x[2039] <= 0.1254901998:
                                        results.append(0)
                                    else:
                                        if x[154] <= 0.1941176504:
                                            results.append(1)
                                        else:
                                            if x[1802] <= 0.6372549236:
                                                results.append(1)
                                            else:
                                                results.append(1)
                    else:
                        if x[1694] <= 0.8882353008:
                            if x[2879] <= 0.4000000060:
                                if x[1017] <= 0.3274509907:
                                    results.append(0)
                                else:
                                    if x[828] <= 0.8882353008:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[2223] <= 0.4901960939:
                                    if x[229] <= 0.3745098114:
                                        if x[1163] <= 0.3588235378:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[402] <= 0.2921568751:
                        if x[1538] <= 0.2607843205:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1842] <= 0.3372549117:
                            if x[1458] <= 0.2333333343:
                                results.append(1)
                            else:
                                if x[1923] <= 0.3392156959:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[344] <= 0.2313725501:
                                results.append(0)
                            else:
                                if x[1695] <= 0.5568627715:
                                    if x[1727] <= 0.2196078449:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2086] <= 0.5549019873:
                                        if x[1093] <= 0.6137255132:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[1699] <= 0.6000000238:
                                            results.append(1)
                                        else:
                                            if x[1958] <= 0.7000000179:
                                                results.append(1)
                                            else:
                                                results.append(1)
        else:
            if x[638] <= 0.6490196288:
                if x[2524] <= 0.3313725591:
                    if x[2823] <= 0.4705882370:
                        if x[2510] <= 0.3784313798:
                            if x[2879] <= 0.1490196139:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2911] <= 0.5352941453:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[1592] <= 0.4215686321:
                        if x[3023] <= 0.3607843220:
                            if x[931] <= 0.2941176593:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[51] <= 0.5254902244:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[930] <= 0.5117647201:
                            if x[3019] <= 0.4549019635:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1817] <= 0.5117647350:
                                results.append(0)
                            else:
                                if x[2837] <= 0.5921568871:
                                    results.append(1)
                                else:
                                    results.append(1)
            else:
                if x[2545] <= 0.7941176593:
                    if x[1279] <= 0.1725490242:
                        if x[1441] <= 0.4490196109:
                            results.append(0)
                        else:
                            if x[1817] <= 0.5490196347:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1684] <= 0.0901960805:
                            results.append(1)
                        else:
                            if x[1097] <= 0.5039215982:
                                if x[2421] <= 0.6117647290:
                                    if x[1347] <= 0.9156862795:
                                        if x[317] <= 0.6725490391:
                                            results.append(0)
                                        else:
                                            if x[2993] <= 0.7411764860:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[239] <= 0.6235294342:
                                    results.append(0)
                                else:
                                    if x[613] <= 0.4686274529:
                                        results.append(0)
                                    else:
                                        if x[552] <= 0.4254902005:
                                            results.append(0)
                                        else:
                                            if x[852] <= 0.9725490212:
                                                results.append(0)
                                            else:
                                                results.append(0)
                else:
                    if x[1081] <= 0.7901960909:
                        results.append(1)
                    else:
                        results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 33
    if time.time() < deadline or interrupt_flag.is_set():
        if x[557] <= 0.6529411972:
            if x[2835] <= 0.2333333343:
                if x[1799] <= 0.4078431427:
                    if x[1655] <= 0.4588235319:
                        if x[152] <= 0.4470588267:
                            if x[606] <= 0.1352941208:
                                results.append(0)
                            else:
                                if x[1750] <= 0.1862745136:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[1916] <= 0.3549019694:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[1580] <= 0.2843137383:
                        results.append(1)
                    else:
                        if x[2641] <= 0.3313725591:
                            results.append(0)
                        else:
                            results.append(0)
            else:
                if x[56] <= 0.6058823764:
                    if x[2160] <= 0.2000000030:
                        if x[1787] <= 0.5098039359:
                            if x[2943] <= 0.4352941215:
                                if x[1976] <= 0.2901960909:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[2073] <= 0.1156862788:
                                    results.append(0)
                                else:
                                    if x[2348] <= 0.3647058904:
                                        if x[230] <= 0.3372549117:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2236] <= 0.1274509877:
                            if x[2308] <= 0.2333333418:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1616] <= 0.7039215863:
                                if x[822] <= 0.1392156929:
                                    if x[1218] <= 0.3980392218:
                                        if x[1078] <= 0.2098039240:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1954] <= 0.2725490332:
                                        if x[1518] <= 0.7372549176:
                                            if x[77] <= 0.1392156929:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2527] <= 0.1156862751:
                                            results.append(1)
                                        else:
                                            if x[2725] <= 0.3980392218:
                                                results.append(1)
                                            else:
                                                results.append(1)
                            else:
                                if x[2976] <= 0.3450980484:
                                    results.append(0)
                                else:
                                    if x[1276] <= 0.5411764979:
                                        results.append(1)
                                    else:
                                        results.append(0)
                else:
                    if x[723] <= 0.3647058904:
                        if x[2291] <= 0.6176470816:
                            if x[2393] <= 0.2803921700:
                                if x[1889] <= 0.2784313858:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2704] <= 0.8039215803:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1001] <= 0.3980392218:
                            if x[2290] <= 0.3235294223:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[762] <= 0.5450980663:
                                if x[950] <= 0.2392156944:
                                    results.append(1)
                                else:
                                    if x[1596] <= 0.6333333552:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[2720] <= 0.5431372821:
                                    if x[1698] <= 0.2529411837:
                                        results.append(0)
                                    else:
                                        if x[1083] <= 0.4588235319:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
        else:
            if x[107] <= 0.5254902244:
                if x[2713] <= 0.4215686321:
                    if x[76] <= 0.6921568811:
                        if x[863] <= 0.3784313798:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[2350] <= 0.3705882430:
                        results.append(1)
                    else:
                        if x[994] <= 0.7352941334:
                            results.append(1)
                        else:
                            results.append(1)
            else:
                if x[2365] <= 0.4254902005:
                    if x[728] <= 0.3666666746:
                        if x[2072] <= 0.3823529482:
                            if x[940] <= 0.5176470727:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1035] <= 0.9784313738:
                            if x[660] <= 0.4098039269:
                                results.append(0)
                            else:
                                if x[107] <= 0.5862745345:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[1012] <= 0.5156863034:
                        if x[1440] <= 0.6784313917:
                            if x[1798] <= 0.3490196168:
                                if x[426] <= 0.7803921700:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[120] <= 0.8078431487:
                                    if x[1181] <= 0.2431372628:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2107] <= 0.9627451003:
                                if x[1783] <= 0.7568627596:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[1458] <= 0.5137255192:
                            if x[2144] <= 0.7352941334:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2779] <= 0.3333333433:
                                results.append(1)
                            else:
                                if x[596] <= 0.7215686440:
                                    results.append(1)
                                else:
                                    if x[1959] <= 0.5568627715:
                                        if x[2561] <= 0.3764705956:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[1459] <= 0.7019608021:
                                            results.append(0)
                                        else:
                                            results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 34
    if time.time() < deadline or interrupt_flag.is_set():
        if x[14] <= 0.5941176713:
            if x[2523] <= 0.2843137383:
                if x[1661] <= 0.4058823586:
                    if x[2038] <= 0.0764705911:
                        if x[1016] <= 0.4196078479:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2129] <= 0.4058823586:
                            if x[2065] <= 0.1725490242:
                                if x[548] <= 0.3274509907:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[38] <= 0.5784313977:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[202] <= 0.2529411837:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[232] <= 0.7196078598:
                        if x[2737] <= 0.3431372643:
                            if x[2445] <= 0.3450980484:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2059] <= 0.2941176593:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        results.append(1)
            else:
                if x[2468] <= 0.0607843157:
                    if x[2345] <= 0.1098039262:
                        results.append(0)
                    else:
                        if x[1241] <= 0.2803921625:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[1268] <= 0.6215686500:
                        if x[2166] <= 0.1294117719:
                            if x[2852] <= 0.3941176534:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[317] <= 0.4686274529:
                                if x[2650] <= 0.1372549087:
                                    results.append(1)
                                else:
                                    if x[1877] <= 0.8921568692:
                                        if x[1989] <= 0.1352941245:
                                            if x[1950] <= 0.3098039329:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[2368] <= 0.8764705956:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[1143] <= 0.5450980663:
                                    if x[2531] <= 0.1647058874:
                                        results.append(0)
                                    else:
                                        if x[64] <= 0.5196078718:
                                            if x[2445] <= 0.2607843205:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[5] <= 0.4901960790:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                else:
                                    if x[923] <= 0.3019607961:
                                        results.append(1)
                                    else:
                                        results.append(1)
                    else:
                        if x[1304] <= 0.5764706135:
                            if x[1552] <= 0.4666666687:
                                results.append(0)
                            else:
                                if x[1669] <= 0.2450980470:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1134] <= 0.6470588446:
                                if x[2139] <= 0.6862745285:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
        else:
            if x[2724] <= 0.3235294223:
                if x[2407] <= 0.5470588505:
                    if x[1376] <= 0.2333333343:
                        if x[1634] <= 0.3117647171:
                            results.append(1)
                        else:
                            if x[344] <= 0.7549019754:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2500] <= 0.2039215714:
                            if x[2357] <= 0.3352941275:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2066] <= 0.1235294156:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[2237] <= 0.4431372583:
                        if x[692] <= 0.6176470816:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
            else:
                if x[1115] <= 0.4411764741:
                    if x[2415] <= 0.4372549057:
                        if x[1754] <= 0.4078431427:
                            if x[1023] <= 0.4705882370:
                                if x[1473] <= 0.2960784435:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[2996] <= 0.4450980425:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2173] <= 0.1098039225:
                            results.append(0)
                        else:
                            if x[822] <= 0.1921568662:
                                if x[2658] <= 0.6235294342:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2230] <= 0.2176470608:
                                    results.append(0)
                                else:
                                    if x[2349] <= 0.3215686381:
                                        if x[1775] <= 0.4176470637:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2444] <= 0.9352941215:
                                            if x[2102] <= 0.8039215803:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                else:
                    if x[2367] <= 0.5078431666:
                        if x[287] <= 0.4431372732:
                            results.append(1)
                        else:
                            if x[785] <= 0.3960784376:
                                if x[2145] <= 0.4156862795:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2584] <= 0.8705882430:
                                    if x[2501] <= 0.8294117749:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[640] <= 0.7117647231:
                            if x[798] <= 0.3274509907:
                                results.append(0)
                            else:
                                if x[1856] <= 0.3941176534:
                                    results.append(0)
                                else:
                                    if x[1952] <= 0.8784313798:
                                        results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            if x[80] <= 0.6313725710:
                                results.append(1)
                            else:
                                if x[929] <= 0.9117647111:
                                    results.append(0)
                                else:
                                    results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 35
    if time.time() < deadline or interrupt_flag.is_set():
        if x[47] <= 0.6450980604:
            if x[2536] <= 0.2803921700:
                if x[1367] <= 0.6764706075:
                    if x[548] <= 0.2764706016:
                        if x[2919] <= 0.1921568662:
                            if x[1542] <= 0.0862745140:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2277] <= 0.0941176489:
                                results.append(0)
                            else:
                                if x[2024] <= 0.5588235557:
                                    if x[1614] <= 0.0980392173:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[1477] <= 0.1960784346:
                            if x[619] <= 0.5196078569:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1898] <= 0.3058823645:
                                if x[351] <= 0.2882353067:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1272] <= 0.3333333433:
                                    if x[2131] <= 0.2156862766:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[2669] <= 0.1823529452:
                                        if x[2876] <= 0.3392156959:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[1933] <= 0.3450980484:
                                            results.append(1)
                                        else:
                                            results.append(1)
                else:
                    if x[2364] <= 0.4274509847:
                        results.append(0)
                    else:
                        results.append(1)
            else:
                if x[2641] <= 0.1058823541:
                    if x[2471] <= 0.2882353067:
                        results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[1346] <= 0.5705882609:
                        if x[2133] <= 0.3627451062:
                            if x[1831] <= 0.5470588505:
                                if x[173] <= 0.6294117868:
                                    if x[1847] <= 0.3215686381:
                                        if x[2565] <= 0.7843137383:
                                            if x[1884] <= 0.6117647290:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[675] <= 0.4450980425:
                                            if x[835] <= 0.5000000149:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[2202] <= 0.6000000238:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[1703] <= 0.5784313977:
                                if x[2832] <= 0.9117647111:
                                    if x[2822] <= 0.8000000119:
                                        if x[1196] <= 0.8725490272:
                                            if x[2037] <= 0.3078431487:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2195] <= 0.2588235438:
                                    if x[856] <= 0.3784313798:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[129] <= 0.1862745136:
                                        results.append(0)
                                    else:
                                        if x[1686] <= 0.8901960850:
                                            results.append(1)
                                        else:
                                            results.append(1)
                    else:
                        if x[1344] <= 0.7431372702:
                            if x[1680] <= 0.3156862855:
                                results.append(1)
                            else:
                                if x[1555] <= 0.4333333373:
                                    if x[1220] <= 0.4235294163:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[266] <= 0.3392156959:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            if x[1886] <= 0.5196078569:
                                results.append(1)
                            else:
                                results.append(0)
        else:
            if x[2949] <= 0.5156863034:
                if x[941] <= 0.3039215803:
                    if x[924] <= 0.1490196139:
                        results.append(0)
                    else:
                        if x[1979] <= 0.4803921729:
                            if x[2851] <= 0.4078431427:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[1022] <= 0.3352941275:
                        if x[889] <= 0.5921568871:
                            if x[2629] <= 0.2647058964:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[104] <= 0.4588235319:
                            results.append(1)
                        else:
                            if x[2679] <= 0.0450980403:
                                results.append(0)
                            else:
                                if x[1687] <= 0.8450980484:
                                    if x[1851] <= 0.6882353127:
                                        results.append(0)
                                    else:
                                        if x[1726] <= 0.5686274767:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    results.append(0)
            else:
                if x[644] <= 0.9588235319:
                    if x[2277] <= 0.5470588505:
                        if x[1196] <= 0.4156862795:
                            if x[1311] <= 0.7117647231:
                                if x[1754] <= 0.4470588267:
                                    if x[2170] <= 0.2705882490:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2677] <= 0.4803921580:
                                if x[2822] <= 0.3647058904:
                                    if x[2795] <= 0.3058823645:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1492] <= 0.3137255013:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[2948] <= 0.6176470816:
                            if x[1726] <= 0.4215686321:
                                results.append(1)
                            else:
                                if x[3003] <= 0.5039215982:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1156] <= 0.8235294223:
                                if x[310] <= 0.6627451181:
                                    if x[1206] <= 0.5176470727:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2282] <= 0.5745098293:
                                        results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[2318] <= 0.5078431517:
                                    results.append(1)
                                else:
                                    results.append(1)
                else:
                    if x[1222] <= 0.9784313738:
                        results.append(0)
                    else:
                        results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 36
    if time.time() < deadline or interrupt_flag.is_set():
        if x[176] <= 0.6647059023:
            if x[2724] <= 0.1666666716:
                if x[2376] <= 0.5117647350:
                    if x[1568] <= 0.2901960909:
                        if x[2057] <= 0.0509803928:
                            results.append(0)
                        else:
                            if x[2299] <= 0.2000000030:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[133] <= 0.3843137324:
                            results.append(0)
                        else:
                            if x[1508] <= 0.5509804189:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[2281] <= 0.6294117868:
                        results.append(1)
                    else:
                        results.append(0)
            else:
                if x[2137] <= 0.1784313768:
                    if x[2597] <= 0.3862745166:
                        if x[2419] <= 0.1411764771:
                            results.append(0)
                        else:
                            if x[2664] <= 0.2392156869:
                                results.append(0)
                            else:
                                if x[2455] <= 0.2058823556:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[2484] <= 0.5137255192:
                            if x[1461] <= 0.4764705896:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2283] <= 0.3529411852:
                                results.append(1)
                            else:
                                if x[1410] <= 0.3627451062:
                                    results.append(1)
                                else:
                                    results.append(0)
                else:
                    if x[1139] <= 0.6176470816:
                        if x[252] <= 0.8960784376:
                            if x[2143] <= 0.2176470608:
                                if x[2976] <= 0.4725490212:
                                    if x[2027] <= 0.3294117749:
                                        if x[1082] <= 0.1823529452:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1317] <= 0.5333333611:
                                        if x[1812] <= 0.3764705956:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                if x[1694] <= 0.7549019754:
                                    if x[2184] <= 0.1156862751:
                                        if x[3053] <= 0.3078431487:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[1860] <= 0.2921568751:
                                            if x[2534] <= 0.5078431666:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[2553] <= 0.1549019665:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    if x[2349] <= 0.4039215744:
                                        results.append(0)
                                    else:
                                        if x[1648] <= 0.6490196288:
                                            results.append(1)
                                        else:
                                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[946] <= 0.6098039448:
                            if x[839] <= 0.3117647171:
                                results.append(1)
                            else:
                                if x[2816] <= 0.3588235378:
                                    results.append(1)
                                else:
                                    if x[995] <= 0.5490196347:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            if x[2368] <= 0.4784313738:
                                if x[2932] <= 0.6137255132:
                                    if x[623] <= 0.5549019873:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
        else:
            if x[1289] <= 0.2470588312:
                if x[2362] <= 0.1039215699:
                    results.append(0)
                else:
                    if x[2251] <= 0.2960784435:
                        if x[1654] <= 0.5725490451:
                            if x[1128] <= 0.4333333373:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1463] <= 0.1215686314:
                            results.append(0)
                        else:
                            if x[1468] <= 0.1686274558:
                                results.append(1)
                            else:
                                results.append(1)
            else:
                if x[788] <= 0.6411764920:
                    if x[2931] <= 0.5960784554:
                        if x[906] <= 0.4725490212:
                            if x[2784] <= 0.5803921819:
                                if x[1760] <= 0.1666666716:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2197] <= 0.3019607887:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[1315] <= 0.5705882609:
                                if x[1102] <= 0.6901960969:
                                    if x[2705] <= 0.3686274588:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1166] <= 0.4019607902:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[2229] <= 0.3764705956:
                            results.append(0)
                        else:
                            if x[1701] <= 0.3725490272:
                                results.append(1)
                            else:
                                if x[1306] <= 0.8039215803:
                                    results.append(1)
                                else:
                                    results.append(1)
                else:
                    if x[2808] <= 0.5294117928:
                        if x[1220] <= 0.1490196139:
                            results.append(0)
                        else:
                            if x[2556] <= 0.6686274707:
                                if x[2348] <= 0.7098039389:
                                    if x[1026] <= 0.2019607872:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2921] <= 0.4372549057:
                            results.append(1)
                        else:
                            if x[2448] <= 0.5196078718:
                                results.append(0)
                            else:
                                if x[2362] <= 0.5666666925:
                                    if x[1301] <= 0.4627451003:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[2110] <= 0.8235294223:
                                        results.append(0)
                                    else:
                                        results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 37
    if time.time() < deadline or interrupt_flag.is_set():
        if x[56] <= 0.6019608080:
            if x[2245] <= 0.1470588297:
                if x[1565] <= 0.1588235348:
                    if x[476] <= 0.0568627454:
                        results.append(1)
                    else:
                        results.append(1)
                else:
                    if x[1438] <= 0.4313725531:
                        if x[1315] <= 0.6647059023:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2148] <= 0.2509803995:
                            if x[1331] <= 0.4647058845:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
            else:
                if x[2640] <= 0.2647058964:
                    if x[1154] <= 0.4274509847:
                        if x[2297] <= 0.3254902065:
                            if x[2512] <= 0.1117647067:
                                results.append(0)
                            else:
                                if x[817] <= 0.2705882490:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[2394] <= 0.7019608021:
                                if x[2520] <= 0.3313725591:
                                    results.append(0)
                                else:
                                    if x[1055] <= 0.2176470608:
                                        results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2390] <= 0.1117647067:
                            results.append(1)
                        else:
                            if x[1942] <= 0.6019608080:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[870] <= 0.4215686321:
                        if x[2064] <= 0.1274509877:
                            results.append(0)
                        else:
                            if x[1451] <= 0.5588235557:
                                if x[2824] <= 0.1764705926:
                                    results.append(0)
                                else:
                                    if x[2236] <= 0.1196078435:
                                        results.append(1)
                                    else:
                                        if x[250] <= 0.0882352963:
                                            if x[2891] <= 0.2843137383:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[965] <= 0.4450980425:
                                                results.append(1)
                                            else:
                                                results.append(1)
                            else:
                                if x[142] <= 0.2960784435:
                                    if x[1450] <= 0.6333333552:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2030] <= 0.6294117868:
                                        results.append(0)
                                    else:
                                        results.append(0)
                    else:
                        if x[2184] <= 0.3137255013:
                            if x[320] <= 0.6000000238:
                                if x[2085] <= 0.1803921610:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1295] <= 0.0294117657:
                                results.append(1)
                            else:
                                if x[274] <= 0.7666666806:
                                    if x[907] <= 0.7803921700:
                                        results.append(1)
                                    else:
                                        if x[333] <= 0.5431372821:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[263] <= 0.6215686500:
                                        results.append(0)
                                    else:
                                        results.append(1)
        else:
            if x[2463] <= 0.4372549057:
                if x[842] <= 0.1529411823:
                    if x[345] <= 0.5313725770:
                        results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[815] <= 0.3941176534:
                        if x[2377] <= 0.2333333343:
                            if x[2383] <= 0.1823529452:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1292] <= 0.2705882490:
                                if x[498] <= 0.7823529541:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[107] <= 0.7686274648:
                                    if x[35] <= 0.7196078598:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[62] <= 0.6156862974:
                            if x[1963] <= 0.1862745136:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[739] <= 0.9980392158:
                                if x[1203] <= 0.4117647111:
                                    if x[2284] <= 0.5019607991:
                                        if x[1007] <= 0.3352941275:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1667] <= 0.8215686381:
                                        results.append(0)
                                    else:
                                        if x[2241] <= 0.3117647171:
                                            results.append(0)
                                        else:
                                            results.append(0)
                            else:
                                results.append(0)
            else:
                if x[1389] <= 0.4431372583:
                    if x[647] <= 0.7117647231:
                        if x[2172] <= 0.3529411852:
                            if x[201] <= 0.7215686440:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2571] <= 0.4019607902:
                                results.append(0)
                            else:
                                if x[2760] <= 0.5294117928:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[1356] <= 0.5392157137:
                            if x[2513] <= 0.4098039269:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2049] <= 0.4764705896:
                                if x[931] <= 0.5137255043:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[2073] <= 0.3470588326:
                        if x[1503] <= 0.4647058845:
                            if x[2957] <= 0.5196078718:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1591] <= 0.4294117689:
                            if x[515] <= 0.4431372583:
                                results.append(1)
                            else:
                                if x[108] <= 0.4803921580:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[2008] <= 0.4803921580:
                                if x[2577] <= 0.3705882430:
                                    results.append(1)
                                else:
                                    if x[1040] <= 0.6000000238:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[295] <= 0.6333333552:
                                    if x[1234] <= 0.6039215922:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1314] <= 0.5039215833:
                                        results.append(1)
                                    else:
                                        if x[2574] <= 0.5941176713:
                                            if x[1075] <= 0.8196078539:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1758] <= 0.6117647290:
                                                results.append(0)
                                            else:
                                                results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 38
    if time.time() < deadline or interrupt_flag.is_set():
        if x[389] <= 0.6137255132:
            if x[2832] <= 0.2490196154:
                if x[1460] <= 0.4254902005:
                    if x[314] <= 0.3725490272:
                        if x[1583] <= 0.5019607991:
                            if x[2230] <= 0.1098039225:
                                results.append(1)
                            else:
                                if x[2257] <= 0.5843137503:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[877] <= 0.3627451062:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2635] <= 0.3843137324:
                            if x[4] <= 0.2921568751:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2473] <= 0.4294117689:
                        results.append(0)
                    else:
                        results.append(1)
            else:
                if x[2173] <= 0.1784313768:
                    if x[3053] <= 0.2745098174:
                        results.append(1)
                    else:
                        if x[2779] <= 0.2647058889:
                            results.append(1)
                        else:
                            if x[2160] <= 0.3784313798:
                                results.append(0)
                            else:
                                if x[2209] <= 0.4764705896:
                                    results.append(0)
                                else:
                                    results.append(1)
                else:
                    if x[2545] <= 0.0529411770:
                        results.append(0)
                    else:
                        if x[83] <= 0.5745098293:
                            if x[1553] <= 0.5901961029:
                                if x[1020] <= 0.8137255013:
                                    if x[1988] <= 0.8470588326:
                                        if x[721] <= 0.0431372561:
                                            results.append(1)
                                        else:
                                            if x[1191] <= 0.8823529482:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[2112] <= 0.2568627596:
                                        results.append(0)
                                    else:
                                        if x[2316] <= 0.4725490361:
                                            results.append(1)
                                        else:
                                            results.append(1)
                            else:
                                if x[829] <= 0.5647059083:
                                    if x[2419] <= 0.6764706075:
                                        if x[437] <= 0.5372549295:
                                            if x[2250] <= 0.4960784465:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2487] <= 0.6901960969:
                                        results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            if x[2257] <= 0.2568627596:
                                if x[763] <= 0.4196078479:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1388] <= 0.7549019754:
                                    if x[90] <= 0.5196078718:
                                        if x[1320] <= 0.3705882430:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[2471] <= 0.4450980425:
                                            results.append(1)
                                        else:
                                            if x[2850] <= 0.5274510086:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                else:
                                    results.append(0)
        else:
            if x[2400] <= 0.8058823645:
                if x[815] <= 0.6372549236:
                    if x[317] <= 0.6843137443:
                        if x[2467] <= 0.4058823586:
                            if x[2330] <= 0.2607843280:
                                results.append(0)
                            else:
                                if x[1467] <= 0.4196078479:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[1511] <= 0.5862745345:
                                if x[160] <= 0.8058823645:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2358] <= 0.3156862855:
                            if x[1013] <= 0.1803921610:
                                results.append(1)
                            else:
                                if x[2015] <= 0.6254902184:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[2850] <= 0.3411764801:
                                results.append(0)
                            else:
                                if x[865] <= 0.7921568751:
                                    if x[2864] <= 0.3784313798:
                                        results.append(1)
                                    else:
                                        if x[723] <= 0.2686274648:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    if x[1527] <= 0.6176470816:
                                        results.append(1)
                                    else:
                                        results.append(1)
                else:
                    if x[1604] <= 0.3392156959:
                        if x[2473] <= 0.4745098054:
                            if x[1437] <= 0.6274510026:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2474] <= 0.6960784495:
                                if x[1479] <= 0.2882353067:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[134] <= 0.4352941215:
                            results.append(1)
                        else:
                            if x[2114] <= 0.7627451122:
                                if x[2557] <= 0.7745098174:
                                    if x[1382] <= 0.1803921610:
                                        results.append(0)
                                    else:
                                        if x[2472] <= 0.6568627656:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[971] <= 0.8156862855:
                                    results.append(1)
                                else:
                                    if x[1483] <= 0.6196078658:
                                        results.append(0)
                                    else:
                                        results.append(0)
            else:
                if x[2266] <= 0.4156862795:
                    if x[282] <= 0.9627451003:
                        if x[146] <= 0.8196078539:
                            results.append(1)
                        else:
                            if x[247] <= 0.8607843220:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[213] <= 0.7529411912:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[917] <= 0.6666666865:
                        if x[2738] <= 0.1941176504:
                            results.append(0)
                        else:
                            if x[1208] <= 0.4294117689:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[821] <= 0.7156862915:
                            results.append(0)
                        else:
                            if x[1017] <= 0.8686274588:
                                results.append(1)
                            else:
                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 39
    if time.time() < deadline or interrupt_flag.is_set():
        if x[92] <= 0.5156863034:
            if x[2728] <= 0.0960784331:
                if x[423] <= 0.7470588386:
                    if x[507] <= 0.5450980663:
                        results.append(0)
                    else:
                        results.append(0)
                else:
                    results.append(1)
            else:
                if x[1578] <= 0.7823529541:
                    if x[220] <= 0.8901960850:
                        if x[1975] <= 0.1078431383:
                            if x[706] <= 0.2235294133:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1442] <= 0.5470588505:
                                if x[633] <= 0.1117647067:
                                    if x[1129] <= 0.4352941215:
                                        if x[2155] <= 0.1960784346:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[314] <= 0.0588235315:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                else:
                                    if x[266] <= 0.6901960969:
                                        if x[206] <= 0.6549019814:
                                            if x[746] <= 0.7607843280:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[1440] <= 0.6294117868:
                                    if x[283] <= 0.3431372643:
                                        if x[2208] <= 0.3196078464:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[236] <= 0.3803921640:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[1506] <= 0.7745098174:
                                        if x[1547] <= 0.8098039329:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[2749] <= 0.2980392277:
                        if x[1622] <= 0.2019607872:
                            results.append(1)
                        else:
                            if x[481] <= 0.1725490242:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1493] <= 0.8647058904:
                            if x[1744] <= 0.7000000179:
                                if x[1030] <= 0.1823529452:
                                    results.append(1)
                                else:
                                    if x[1889] <= 0.1411764771:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
        else:
            if x[1004] <= 0.4078431427:
                if x[2665] <= 0.2627451122:
                    if x[1521] <= 0.1921568662:
                        results.append(1)
                    else:
                        if x[3058] <= 0.7294117808:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[1097] <= 0.3803921640:
                        if x[2285] <= 0.1274509877:
                            if x[2882] <= 0.6098039448:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2322] <= 0.1980392188:
                                if x[1814] <= 0.4568627626:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1546] <= 0.1352941245:
                                    results.append(0)
                                else:
                                    if x[1297] <= 0.6098039448:
                                        if x[1005] <= 0.1352941245:
                                            results.append(1)
                                        else:
                                            if x[2951] <= 0.1313725524:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(1)
                    else:
                        if x[1003] <= 0.3372549117:
                            if x[1234] <= 0.4784313738:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[642] <= 0.5039215833:
                                results.append(0)
                            else:
                                if x[1815] <= 0.5705882609:
                                    results.append(1)
                                else:
                                    results.append(1)
            else:
                if x[2163] <= 0.4901960790:
                    if x[245] <= 0.4411764741:
                        if x[2046] <= 0.3705882430:
                            if x[2723] <= 0.1980392188:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1748] <= 0.5882353187:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[2310] <= 0.9490196109:
                            if x[490] <= 0.3392156959:
                                results.append(0)
                            else:
                                if x[2514] <= 0.3627451062:
                                    if x[443] <= 0.4274509847:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[389] <= 0.6117647290:
                                        if x[2282] <= 0.4705882519:
                                            if x[79] <= 0.7921568751:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[1235] <= 0.9392156899:
                                            if x[1320] <= 0.2196078449:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(1)
                        else:
                            if x[2778] <= 0.9647058845:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[257] <= 0.5784313977:
                        if x[2235] <= 0.4392156899:
                            if x[933] <= 0.7431372702:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1878] <= 0.7607843280:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[60] <= 0.5980392396:
                            if x[1706] <= 0.4843137264:
                                results.append(0)
                            else:
                                if x[1391] <= 0.5843137503:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[1199] <= 0.6117647290:
                                if x[2146] <= 0.3313725591:
                                    results.append(0)
                                else:
                                    if x[497] <= 0.8529411852:
                                        if x[2951] <= 0.2980392277:
                                            results.append(0)
                                        else:
                                            if x[2923] <= 0.8450980484:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[1177] <= 0.6294117868:
                                    if x[298] <= 0.7823529541:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[2399] <= 0.9078431427:
                                        results.append(0)
                                    else:
                                        results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 40
    if time.time() < deadline or interrupt_flag.is_set():
        if x[653] <= 0.6647059023:
            if x[2244] <= 0.2450980395:
                if x[2894] <= 0.3078431487:
                    if x[2336] <= 0.0431372561:
                        results.append(0)
                    else:
                        if x[1853] <= 0.4294117689:
                            if x[3039] <= 0.0705882385:
                                results.append(0)
                            else:
                                if x[1817] <= 0.5411764979:
                                    if x[811] <= 0.5941176713:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2227] <= 0.4254902005:
                        if x[973] <= 0.2549019679:
                            results.append(0)
                        else:
                            if x[1840] <= 0.0784313753:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[1021] <= 0.5078431666:
                            if x[1868] <= 0.2274509892:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1392] <= 0.5803921819:
                                results.append(1)
                            else:
                                results.append(1)
            else:
                if x[2170] <= 0.2686274648:
                    if x[713] <= 0.4137254953:
                        if x[1880] <= 0.4803921580:
                            if x[1257] <= 0.6450980604:
                                if x[440] <= 0.5098039508:
                                    if x[1976] <= 0.0921568647:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[1854] <= 0.6176470816:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2801] <= 0.2960784435:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[2158] <= 0.3705882430:
                            if x[616] <= 0.7549019754:
                                if x[2500] <= 0.4450980425:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1819] <= 0.4313725531:
                                results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[2838] <= 0.1352941245:
                        if x[1409] <= 0.4313725531:
                            results.append(1)
                        else:
                            if x[2600] <= 0.3725490272:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[443] <= 0.4411764741:
                            if x[2653] <= 0.1176470630:
                                results.append(0)
                            else:
                                if x[1385] <= 0.9196078479:
                                    if x[2072] <= 0.8372549117:
                                        if x[1790] <= 0.1274509877:
                                            if x[1103] <= 0.1333333366:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1274] <= 0.8078431487:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2049] <= 0.2921568751:
                                if x[2880] <= 0.4666666687:
                                    results.append(0)
                                else:
                                    if x[2636] <= 0.5215686411:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[2236] <= 0.2098039240:
                                    results.append(0)
                                else:
                                    if x[107] <= 0.5117647350:
                                        if x[558] <= 0.7941176593:
                                            if x[1679] <= 0.8078431487:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[2671] <= 0.1921568662:
                                            results.append(0)
                                        else:
                                            if x[1223] <= 0.6490196288:
                                                results.append(1)
                                            else:
                                                results.append(0)
        else:
            if x[197] <= 0.5823529661:
                if x[1809] <= 0.4039215744:
                    if x[1861] <= 0.3274509907:
                        results.append(0)
                    else:
                        if x[1947] <= 0.4549019784:
                            results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[846] <= 0.7137255073:
                        if x[2609] <= 0.4156862795:
                            if x[2207] <= 0.3921568692:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1681] <= 0.2352941185:
                            results.append(1)
                        else:
                            results.append(1)
            else:
                if x[2427] <= 0.7960784435:
                    if x[1010] <= 0.3882353008:
                        if x[2346] <= 0.4196078479:
                            if x[731] <= 0.3333333358:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1762] <= 0.2725490332:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2056] <= 0.0392156877:
                            results.append(0)
                        else:
                            if x[1322] <= 0.1803921610:
                                results.append(0)
                            else:
                                if x[1478] <= 0.1019607857:
                                    results.append(0)
                                else:
                                    if x[3029] <= 0.2294117659:
                                        if x[1925] <= 0.7470588386:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                else:
                    if x[1230] <= 0.7411764860:
                        if x[1497] <= 0.4980392307:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[1642] <= 0.5313725621:
                            results.append(0)
                        else:
                            if x[1513] <= 0.5647058934:
                                results.append(1)
                            else:
                                results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 41
    if time.time() < deadline or interrupt_flag.is_set():
        if x[71] <= 0.5352941453:
            if x[2541] <= 0.2333333343:
                if x[1171] <= 0.1333333366:
                    results.append(1)
                else:
                    if x[1676] <= 0.4078431427:
                        if x[2211] <= 0.4764705896:
                            if x[1116] <= 0.6313725710:
                                if x[524] <= 0.3156862855:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2326] <= 0.3784313798:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2037] <= 0.7254902124:
                            if x[470] <= 0.5372549295:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
            else:
                if x[2140] <= 0.2117647082:
                    if x[2909] <= 0.4352941215:
                        if x[2832] <= 0.2901960909:
                            results.append(0)
                        else:
                            if x[490] <= 0.4705882370:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2353] <= 0.3529411852:
                            if x[1526] <= 0.4156862795:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2687] <= 0.4862745255:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[2922] <= 0.1313725561:
                        if x[1104] <= 0.7196078598:
                            if x[16] <= 0.3274509832:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[2940] <= 0.1254901998:
                            results.append(0)
                        else:
                            if x[1978] <= 0.1137254909:
                                if x[1272] <= 0.5254902095:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1706] <= 0.7000000179:
                                    if x[141] <= 0.0450980403:
                                        results.append(0)
                                    else:
                                        if x[1524] <= 0.8098039329:
                                            if x[1517] <= 0.7156862915:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1672] <= 0.4176470637:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                else:
                                    if x[1327] <= 0.5549019873:
                                        if x[2145] <= 0.4392156899:
                                            results.append(0)
                                        else:
                                            if x[2471] <= 0.6058823764:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                    else:
                                        if x[2938] <= 0.7862745225:
                                            results.append(1)
                                        else:
                                            results.append(1)
        else:
            if x[308] <= 0.6215686500:
                if x[2617] <= 0.3411764801:
                    if x[2348] <= 0.4549019635:
                        if x[341] <= 0.7784313858:
                            if x[2443] <= 0.3509804010:
                                if x[2799] <= 0.5941176713:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2529] <= 0.1862745136:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[1215] <= 0.3745098114:
                            results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[726] <= 0.3392156959:
                        if x[2888] <= 0.3568627536:
                            results.append(1)
                        else:
                            if x[1187] <= 0.3764705956:
                                if x[1113] <= 0.4176470637:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[2550] <= 0.3098039329:
                            if x[1443] <= 0.3450980484:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1787] <= 0.5156862885:
                                if x[1458] <= 0.2549019679:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[60] <= 0.5784313977:
                                    results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[2604] <= 0.4921568632:
                    if x[539] <= 0.6019608080:
                        if x[2751] <= 0.5509804189:
                            if x[3041] <= 0.2313725501:
                                if x[2745] <= 0.2588235363:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1214] <= 0.2647058964:
                            if x[341] <= 0.8745098114:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[2540] <= 0.5901961029:
                                if x[2320] <= 0.5686274767:
                                    if x[1676] <= 0.2058823556:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2804] <= 0.5450980663:
                                    results.append(1)
                                else:
                                    results.append(0)
                else:
                    if x[1403] <= 0.5588235557:
                        if x[2170] <= 0.1980392188:
                            if x[1789] <= 0.2901960909:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2335] <= 0.1764705926:
                                results.append(0)
                            else:
                                if x[821] <= 0.7352941334:
                                    if x[966] <= 0.3745098114:
                                        results.append(0)
                                    else:
                                        if x[521] <= 0.9705882370:
                                            if x[1056] <= 0.5509804189:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[587] <= 0.9372549057:
                                        if x[2877] <= 0.5372549295:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(1)
                    else:
                        if x[1894] <= 0.9117647111:
                            if x[758] <= 0.5921568871:
                                results.append(1)
                            else:
                                if x[2930] <= 0.4078431427:
                                    results.append(0)
                                else:
                                    if x[2081] <= 0.1764705926:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            results.append(1)
    
    else:
      return vote_logic(results)
    
    # Tree 42
    if time.time() < deadline or interrupt_flag.is_set():
        if x[197] <= 0.6137255132:
            if x[2520] <= 0.3509804010:
                if x[1652] <= 0.3274509907:
                    if x[353] <= 0.7274509966:
                        if x[2542] <= 0.0725490227:
                            if x[1874] <= 0.2039215714:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[587] <= 0.2960784435:
                                if x[2867] <= 0.4921568632:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[1809] <= 0.5019607991:
                                    if x[2300] <= 0.3352941275:
                                        if x[1834] <= 0.2411764711:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[746] <= 0.1078431383:
                        if x[2173] <= 0.2823529541:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1580] <= 0.4215686321:
                            if x[328] <= 0.3960784376:
                                if x[1506] <= 0.7098039389:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2174] <= 0.3490196168:
                                    if x[230] <= 0.3803921640:
                                        results.append(1)
                                    else:
                                        if x[1807] <= 0.3470588326:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[2077] <= 0.5843137503:
                                if x[207] <= 0.5098039359:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[894] <= 0.3529411852:
                                    if x[225] <= 0.3352941275:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[2239] <= 0.1078431383:
                    if x[2864] <= 0.2137254998:
                        results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[2052] <= 0.2372549027:
                        if x[2969] <= 0.5862745345:
                            if x[1953] <= 0.3843137324:
                                if x[2268] <= 0.1431372575:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[906] <= 0.0803921595:
                            results.append(0)
                        else:
                            if x[1217] <= 0.7745098174:
                                if x[2136] <= 0.1235294156:
                                    results.append(0)
                                else:
                                    if x[2329] <= 0.2294117659:
                                        if x[260] <= 0.1921568662:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[2536] <= 0.1509803981:
                                            results.append(1)
                                        else:
                                            if x[1709] <= 0.7196078598:
                                                results.append(1)
                                            else:
                                                results.append(1)
                            else:
                                if x[1986] <= 0.6411764920:
                                    if x[1603] <= 0.6647059023:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
        else:
            if x[1190] <= 0.3235294223:
                if x[2350] <= 0.2137254924:
                    if x[164] <= 0.7313725650:
                        results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[1564] <= 0.5960784554:
                        if x[2037] <= 0.2549019754:
                            if x[1914] <= 0.4784313738:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1942] <= 0.1372549087:
                                results.append(0)
                            else:
                                if x[2335] <= 0.8725490272:
                                    if x[2359] <= 0.2627451122:
                                        results.append(1)
                                    else:
                                        if x[865] <= 0.4568627477:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[778] <= 0.7039215863:
                            results.append(1)
                        else:
                            results.append(0)
            else:
                if x[2250] <= 0.5039215982:
                    if x[596] <= 0.5313725770:
                        if x[606] <= 0.4862745106:
                            if x[2270] <= 0.4019607902:
                                if x[2517] <= 0.2294117659:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1378] <= 0.5784313977:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[455] <= 0.3117647171:
                            results.append(1)
                        else:
                            if x[2358] <= 0.5882353187:
                                if x[2655] <= 0.7274509966:
                                    if x[705] <= 0.9431372583:
                                        results.append(0)
                                    else:
                                        if x[239] <= 0.9666666687:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1188] <= 0.6529411972:
                                    if x[1741] <= 0.6117647290:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                else:
                    if x[2542] <= 0.5862745345:
                        if x[1923] <= 0.7843137383:
                            if x[1882] <= 0.6470588446:
                                if x[443] <= 0.6176470816:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2150] <= 0.7058823705:
                                    results.append(1)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[617] <= 0.6333333552:
                            if x[199] <= 0.6450980604:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[2639] <= 0.9294117689:
                                if x[1193] <= 0.8450980484:
                                    if x[1917] <= 0.4058823586:
                                        results.append(0)
                                    else:
                                        if x[998] <= 0.7862745225:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 43
    if time.time() < deadline or interrupt_flag.is_set():
        if x[98] <= 0.6137255132:
            if x[2839] <= 0.1490196139:
                if x[711] <= 0.7254902124:
                    if x[1618] <= 0.1176470630:
                        results.append(1)
                    else:
                        if x[391] <= 0.5254902244:
                            if x[238] <= 0.1431372613:
                                results.append(0)
                            else:
                                if x[580] <= 0.4745098054:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(0)
                else:
                    results.append(1)
            else:
                if x[2427] <= 0.2686274648:
                    if x[551] <= 0.2764706016:
                        if x[1577] <= 0.3901960850:
                            if x[1167] <= 0.6352941394:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[2233] <= 0.2509803995:
                                results.append(0)
                            else:
                                if x[583] <= 0.3686274588:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[2498] <= 0.1666666716:
                            if x[1222] <= 0.3529411852:
                                results.append(0)
                            else:
                                if x[110] <= 0.3980392218:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1954] <= 0.3862745166:
                                if x[2179] <= 0.4176470637:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[909] <= 0.6000000238:
                                    if x[1148] <= 0.3274509907:
                                        results.append(1)
                                    else:
                                        if x[2291] <= 0.4725490361:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    results.append(1)
                else:
                    if x[2140] <= 0.2490196154:
                        if x[1264] <= 0.4176470637:
                            if x[1549] <= 0.3529411852:
                                if x[1403] <= 0.7627451122:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[1831] <= 0.2647058964:
                                    results.append(0)
                                else:
                                    if x[3048] <= 0.4803921729:
                                        results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            if x[2158] <= 0.4470588267:
                                if x[168] <= 0.4666666687:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[1697] <= 0.8450980484:
                            if x[698] <= 0.5215686560:
                                if x[1402] <= 0.8039215803:
                                    if x[1249] <= 0.0529411770:
                                        if x[3026] <= 0.3431372568:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2044] <= 0.1901960820:
                                            results.append(1)
                                        else:
                                            if x[2524] <= 0.1882352978:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    if x[1307] <= 0.8705882430:
                                        if x[2071] <= 0.6705882549:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[993] <= 0.4117647111:
                                    if x[1868] <= 0.3411764801:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1254] <= 0.2980392277:
                                        results.append(0)
                                    else:
                                        if x[1689] <= 0.7549019754:
                                            if x[1761] <= 0.3470588326:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[252] <= 0.6156862974:
                                                results.append(1)
                                            else:
                                                results.append(1)
                        else:
                            if x[237] <= 0.4549019635:
                                results.append(0)
                            else:
                                results.append(1)
        else:
            if x[2125] <= 0.6568627656:
                if x[1199] <= 0.3980392218:
                    if x[2350] <= 0.2411764711:
                        if x[232] <= 0.6019608080:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[542] <= 0.5490196347:
                            if x[2251] <= 0.2627451122:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            if x[1944] <= 0.5156863034:
                                if x[839] <= 0.4078431427:
                                    if x[1245] <= 0.6019608080:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[3007] <= 0.6901960969:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[2448] <= 0.5980392396:
                                    results.append(1)
                                else:
                                    results.append(0)
                else:
                    if x[272] <= 0.4882352948:
                        if x[1953] <= 0.4843137413:
                            if x[682] <= 0.4509803951:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
                    else:
                        if x[2266] <= 0.7431372702:
                            if x[1184] <= 0.3882353008:
                                if x[487] <= 0.5411764979:
                                    results.append(1)
                                else:
                                    if x[1764] <= 0.2294117659:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[191] <= 0.5843137503:
                                    if x[91] <= 0.4921568632:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1522] <= 0.1568627506:
                                        results.append(0)
                                    else:
                                        if x[2601] <= 0.6647059023:
                                            results.append(0)
                                        else:
                                            if x[807] <= 0.7705882490:
                                                results.append(0)
                                            else:
                                                results.append(0)
                        else:
                            results.append(0)
            else:
                if x[2512] <= 0.3901960850:
                    results.append(0)
                else:
                    if x[1106] <= 0.4568627477:
                        if x[1892] <= 0.6549019814:
                            results.append(1)
                        else:
                            if x[619] <= 0.5411764979:
                                results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[363] <= 0.6862745285:
                            if x[1038] <= 0.5352941453:
                                if x[2554] <= 0.5843137503:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[1934] <= 0.7352941334:
                                if x[3037] <= 0.8843137324:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[3011] <= 0.9607843161:
                                    results.append(1)
                                else:
                                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 44
    if time.time() < deadline or interrupt_flag.is_set():
        if x[107] <= 0.6450980604:
            if x[1553] <= 0.5039215982:
                if x[2238] <= 0.1000000015:
                    if x[1826] <= 0.1529411823:
                        results.append(1)
                    else:
                        if x[1130] <= 0.4588235319:
                            if x[554] <= 0.2901960909:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2054] <= 0.0764705911:
                        if x[2751] <= 0.4862745255:
                            if x[644] <= 0.2862745225:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1325] <= 0.5470588505:
                            if x[956] <= 0.8392156959:
                                if x[2426] <= 0.0568627454:
                                    if x[2655] <= 0.4843137413:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1416] <= 0.8450980484:
                                        if x[2749] <= 0.1980392188:
                                            if x[1374] <= 0.3392156959:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[2867] <= 0.6666666865:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2847] <= 0.2862745225:
                                if x[1466] <= 0.4568627477:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1460] <= 0.3725490272:
                                    if x[204] <= 0.6901960969:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[894] <= 0.4450980425:
                                        if x[1087] <= 0.5137255043:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[73] <= 0.6960784495:
                                            results.append(1)
                                        else:
                                            results.append(0)
            else:
                if x[2427] <= 0.3607843220:
                    if x[1499] <= 0.5000000149:
                        if x[1492] <= 0.4176470637:
                            if x[676] <= 0.5235294402:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1317] <= 0.3000000119:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[1575] <= 0.8352941275:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[2133] <= 0.6450980604:
                        if x[241] <= 0.5588235557:
                            if x[22] <= 0.3254902065:
                                if x[2487] <= 0.3882353008:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1760] <= 0.2352941185:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[2017] <= 0.4176470637:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2303] <= 0.8313725591:
                            if x[2509] <= 0.4568627477:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
        else:
            if x[1376] <= 0.3431372643:
                if x[2281] <= 0.2372549027:
                    if x[1468] <= 0.3019607961:
                        if x[2064] <= 0.5235294253:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[2081] <= 0.1686274558:
                            results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[555] <= 0.7215686440:
                        if x[1720] <= 0.4607843161:
                            if x[1369] <= 0.1921568662:
                                results.append(1)
                            else:
                                if x[2178] <= 0.4352941215:
                                    results.append(0)
                                else:
                                    if x[2312] <= 0.3431372643:
                                        results.append(1)
                                    else:
                                        results.append(0)
                        else:
                            if x[1105] <= 0.5333333611:
                                if x[1766] <= 0.4647058845:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                    else:
                        if x[2316] <= 0.7431372702:
                            if x[2774] <= 0.4039215744:
                                results.append(1)
                            else:
                                if x[479] <= 0.6921568811:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[1102] <= 0.5039215833:
                                results.append(1)
                            else:
                                results.append(1)
            else:
                if x[2463] <= 0.7274509966:
                    if x[1406] <= 0.4000000060:
                        if x[2128] <= 0.4607843161:
                            if x[855] <= 0.9058823586:
                                if x[141] <= 0.7254902124:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2514] <= 0.3980392218:
                                if x[855] <= 0.6196078658:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[502] <= 0.5607843399:
                                    results.append(0)
                                else:
                                    if x[2804] <= 0.3235294223:
                                        results.append(1)
                                    else:
                                        results.append(1)
                    else:
                        if x[2256] <= 0.4176470637:
                            if x[2033] <= 0.9098039269:
                                if x[449] <= 0.1549019665:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[637] <= 0.4117647111:
                                results.append(1)
                            else:
                                if x[1136] <= 0.3313725591:
                                    results.append(1)
                                else:
                                    if x[2772] <= 0.6921568811:
                                        if x[2882] <= 0.2137254924:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(0)
                else:
                    if x[2708] <= 0.9196078479:
                        if x[2562] <= 0.7098039389:
                            results.append(0)
                        else:
                            if x[2260] <= 0.8333333433:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 45
    if time.time() < deadline or interrupt_flag.is_set():
        if x[263] <= 0.6019608080:
            if x[2751] <= 0.1901960820:
                if x[1793] <= 0.3882353008:
                    if x[1242] <= 0.1313725524:
                        results.append(1)
                    else:
                        if x[2314] <= 0.6411764920:
                            if x[3057] <= 0.1392156929:
                                results.append(1)
                            else:
                                if x[2437] <= 0.4000000060:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2130] <= 0.6627451181:
                        if x[715] <= 0.7039215863:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
            else:
                if x[2535] <= 0.2686274648:
                    if x[1914] <= 0.5529412031:
                        if x[437] <= 0.2431372628:
                            if x[1651] <= 0.5843137503:
                                if x[1839] <= 0.2000000030:
                                    results.append(1)
                                else:
                                    if x[1423] <= 0.0980392173:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1467] <= 0.1941176504:
                                results.append(1)
                            else:
                                if x[1819] <= 0.4686274529:
                                    if x[2087] <= 0.2078431398:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[930] <= 0.5705882609:
                            if x[2706] <= 0.3686274588:
                                results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[131] <= 0.5274510086:
                        if x[2373] <= 0.1803921610:
                            if x[1799] <= 0.2568627521:
                                if x[611] <= 0.3137255013:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2244] <= 0.2078431398:
                                if x[3041] <= 0.5607843399:
                                    if x[1343] <= 0.2529411912:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1976] <= 0.1156862751:
                                    if x[2180] <= 0.1372549087:
                                        results.append(0)
                                    else:
                                        if x[879] <= 0.3000000045:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[1673] <= 0.8921568692:
                                        if x[2891] <= 0.0215686280:
                                            results.append(1)
                                        else:
                                            if x[759] <= 0.0745098069:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(1)
                    else:
                        if x[2266] <= 0.2392156869:
                            results.append(0)
                        else:
                            if x[703] <= 0.4490196109:
                                if x[2323] <= 0.5000000149:
                                    if x[1906] <= 0.4352941215:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1552] <= 0.5235294402:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[1300] <= 0.7333333492:
                                    if x[1214] <= 0.1627451032:
                                        results.append(0)
                                    else:
                                        if x[896] <= 0.8921568692:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
        else:
            if x[1028] <= 0.5745098293:
                if x[2919] <= 0.2352941185:
                    if x[308] <= 0.3901960850:
                        results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[2230] <= 0.2647058964:
                        if x[1038] <= 0.5725490451:
                            if x[1263] <= 0.7568627596:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[1379] <= 0.5313725770:
                            if x[2153] <= 0.1098039225:
                                results.append(0)
                            else:
                                if x[1694] <= 0.7705882490:
                                    if x[2286] <= 0.0862745121:
                                        results.append(1)
                                    else:
                                        if x[2274] <= 0.2372549027:
                                            results.append(0)
                                        else:
                                            if x[2102] <= 0.8803921640:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[1527] <= 0.5705882609:
                                if x[503] <= 0.5156862885:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[2152] <= 0.5117647201:
                                    results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[2556] <= 0.7156862915:
                    if x[1049] <= 0.3000000119:
                        results.append(1)
                    else:
                        if x[2421] <= 0.4450980425:
                            if x[2206] <= 0.7941176593:
                                if x[266] <= 0.6294117868:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[1289] <= 0.3588235378:
                                if x[2559] <= 0.4156862795:
                                    results.append(1)
                                else:
                                    if x[2447] <= 0.5901961029:
                                        results.append(1)
                                    else:
                                        results.append(0)
                            else:
                                if x[748] <= 0.4862745106:
                                    results.append(0)
                                else:
                                    if x[89] <= 0.9980392158:
                                        if x[2039] <= 0.7666666806:
                                            results.append(0)
                                        else:
                                            if x[524] <= 0.8372549117:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                    else:
                                        results.append(1)
                else:
                    if x[1860] <= 0.3823529482:
                        results.append(0)
                    else:
                        if x[2911] <= 0.9215686321:
                            if x[1868] <= 0.4215686321:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 46
    if time.time() < deadline or interrupt_flag.is_set():
        if x[248] <= 0.6372549236:
            if x[2563] <= 0.2372549027:
                if x[1610] <= 0.2333333343:
                    if x[1988] <= 0.2666666806:
                        if x[2730] <= 0.1274509840:
                            results.append(0)
                        else:
                            if x[504] <= 0.6941176653:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2074] <= 0.4450980425:
                            results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2872] <= 0.3039215803:
                        if x[1554] <= 0.3843137324:
                            if x[2063] <= 0.4647058845:
                                if x[1598] <= 0.2137254924:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1642] <= 0.2705882490:
                                results.append(1)
                            else:
                                if x[511] <= 0.4686274529:
                                    results.append(0)
                                else:
                                    results.append(1)
                    else:
                        if x[610] <= 0.6627451181:
                            results.append(0)
                        else:
                            results.append(0)
            else:
                if x[1826] <= 0.4843137264:
                    if x[1993] <= 0.1980392188:
                        if x[2684] <= 0.4039215744:
                            if x[632] <= 0.3176470697:
                                if x[1877] <= 0.8254902065:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[2546] <= 0.3039215803:
                                    results.append(0)
                                else:
                                    results.append(1)
                        else:
                            if x[1132] <= 0.3607843220:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[908] <= 0.7843137383:
                            if x[2941] <= 0.1588235348:
                                results.append(0)
                            else:
                                if x[2137] <= 0.1705882400:
                                    if x[1658] <= 0.4372549057:
                                        if x[2701] <= 0.4803921729:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1128] <= 0.0901960805:
                                        results.append(1)
                                    else:
                                        if x[1806] <= 0.2098039240:
                                            if x[1096] <= 0.4176470637:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[2040] <= 0.2333333343:
                                                results.append(1)
                                            else:
                                                results.append(1)
                        else:
                            if x[1492] <= 0.6490196288:
                                results.append(0)
                            else:
                                results.append(1)
                else:
                    if x[2076] <= 0.2901960909:
                        if x[2325] <= 0.4823529571:
                            results.append(0)
                        else:
                            if x[1963] <= 0.2705882490:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[452] <= 0.1431372613:
                            if x[35] <= 0.1431372613:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[1304] <= 0.7098039389:
                                if x[854] <= 0.6137255132:
                                    if x[1993] <= 0.8039215803:
                                        if x[2647] <= 0.8352941275:
                                            if x[838] <= 0.6588235497:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2471] <= 0.5000000149:
                                        if x[220] <= 0.4784313738:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[1563] <= 0.4686274529:
                                            results.append(1)
                                        else:
                                            results.append(1)
                            else:
                                if x[2712] <= 0.3980392218:
                                    results.append(0)
                                else:
                                    if x[2372] <= 0.4666666836:
                                        results.append(1)
                                    else:
                                        results.append(0)
        else:
            if x[1379] <= 0.3431372643:
                if x[2358] <= 0.1941176504:
                    if x[2357] <= 0.0686274543:
                        results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[1479] <= 0.6196078658:
                        if x[694] <= 0.5313725770:
                            if x[1953] <= 0.2882353067:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[1001] <= 0.4254902005:
                                if x[778] <= 0.7764706016:
                                    if x[1173] <= 0.6431372762:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2804] <= 0.5960784554:
                                    if x[1784] <= 0.6078431606:
                                        if x[2551] <= 0.3803921640:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[3057] <= 0.3392156959:
                            results.append(0)
                        else:
                            results.append(0)
            else:
                if x[2433] <= 0.7117647231:
                    if x[110] <= 0.6686274707:
                        if x[385] <= 0.5647059083:
                            if x[80] <= 0.5607843399:
                                results.append(1)
                            else:
                                if x[2492] <= 0.6921568811:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[955] <= 0.6254902184:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2361] <= 0.5588235557:
                            if x[1559] <= 0.4215686321:
                                if x[1604] <= 0.2176470608:
                                    results.append(1)
                                else:
                                    if x[2973] <= 0.3823529482:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[2082] <= 0.0686274543:
                                    results.append(0)
                                else:
                                    if x[2119] <= 0.1509803981:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            if x[629] <= 0.7509804070:
                                results.append(1)
                            else:
                                if x[2987] <= 0.8058823645:
                                    if x[248] <= 0.9294117689:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[2547] <= 0.9333333373:
                        if x[2820] <= 0.6176470816:
                            results.append(0)
                        else:
                            if x[1551] <= 0.4392156899:
                                results.append(0)
                            else:
                                if x[2031] <= 0.5607843399:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 47
    if time.time() < deadline or interrupt_flag.is_set():
        if x[218] <= 0.6098039448:
            if x[2550] <= 0.2686274648:
                if x[2393] <= 0.1450980455:
                    if x[1093] <= 0.1568627506:
                        results.append(0)
                    else:
                        if x[1794] <= 0.3803921640:
                            results.append(1)
                        else:
                            if x[770] <= 0.1156862751:
                                results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[1469] <= 0.4215686321:
                        if x[3054] <= 0.3529411852:
                            if x[1732] <= 0.3137255013:
                                if x[423] <= 0.2862745225:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[2868] <= 0.2980392277:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1166] <= 0.4215686321:
                                if x[2689] <= 0.3078431487:
                                    results.append(1)
                                else:
                                    if x[2125] <= 0.4450980425:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2521] <= 0.4450980425:
                            if x[2340] <= 0.0627450999:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
            else:
                if x[1610] <= 0.6215686500:
                    if x[369] <= 0.9549019635:
                        if x[735] <= 0.1960784346:
                            if x[1070] <= 0.5627451241:
                                if x[1718] <= 0.6019608080:
                                    if x[1554] <= 0.6862745285:
                                        if x[1325] <= 0.2901960909:
                                            results.append(1)
                                        else:
                                            if x[698] <= 0.1725490242:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2344] <= 0.1627451032:
                                if x[1386] <= 0.7294117808:
                                    if x[1368] <= 0.5725490451:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[1876] <= 0.1666666716:
                                    if x[2614] <= 0.4588235319:
                                        if x[2522] <= 0.1333333366:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[1093] <= 0.4156862795:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[320] <= 0.5392157137:
                                        if x[2545] <= 0.2372549027:
                                            if x[1762] <= 0.4549019635:
                                                results.append(1)
                                            else:
                                                results.append(0)
                                        else:
                                            if x[1187] <= 0.5725490451:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[1863] <= 0.4705882370:
                                            results.append(1)
                                        else:
                                            if x[2343] <= 0.4529411793:
                                                results.append(0)
                                            else:
                                                results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[2239] <= 0.6215686500:
                        if x[1020] <= 0.6450980604:
                            if x[58] <= 0.6686274707:
                                if x[1222] <= 0.7352941334:
                                    if x[1775] <= 0.3529411852:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[1533] <= 0.3313725591:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[229] <= 0.2235294133:
                            results.append(1)
                        else:
                            results.append(1)
        else:
            if x[2361] <= 0.3901960850:
                if x[795] <= 0.8431372643:
                    if x[2233] <= 0.5470588505:
                        if x[529] <= 0.2490196154:
                            results.append(1)
                        else:
                            if x[2439] <= 0.6215686500:
                                if x[197] <= 0.6117647290:
                                    if x[2682] <= 0.3196078539:
                                        results.append(1)
                                    else:
                                        if x[1829] <= 0.3098039329:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2876] <= 0.1764705926:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[1490] <= 0.6392157078:
                                    results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[1382] <= 0.5921568871:
                            if x[2240] <= 0.5647059083:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[1497] <= 0.3607843220:
                        results.append(1)
                    else:
                        if x[139] <= 0.9509803951:
                            results.append(1)
                        else:
                            results.append(0)
            else:
                if x[830] <= 0.4843137264:
                    if x[1930] <= 0.3411764801:
                        if x[2733] <= 0.6549019814:
                            if x[2324] <= 0.4137254953:
                                if x[2498] <= 0.3549019694:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
                        else:
                            results.append(1)
                    else:
                        if x[751] <= 0.9078431427:
                            if x[663] <= 0.1686274558:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                else:
                    if x[2403] <= 0.7725490332:
                        if x[610] <= 0.3176470697:
                            results.append(1)
                        else:
                            if x[2351] <= 0.3627451062:
                                if x[2569] <= 0.4901960790:
                                    if x[2894] <= 0.2705882415:
                                        results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1306] <= 0.4450980425:
                                        results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                if x[2907] <= 0.2549019679:
                                    if x[2847] <= 0.2176470608:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1006] <= 0.4098039269:
                                        if x[3061] <= 0.6117647290:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[2048] <= 0.8156862855:
                                            if x[948] <= 0.9235294163:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(0)
                    else:
                        if x[659] <= 0.8529411852:
                            if x[1112] <= 0.7823529541:
                                if x[961] <= 0.6823529601:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[956] <= 0.9313725531:
                                results.append(0)
                            else:
                                if x[851] <= 0.9529411793:
                                    results.append(1)
                                else:
                                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 48
    if time.time() < deadline or interrupt_flag.is_set():
        if x[254] <= 0.6490196288:
            if x[2331] <= 0.2725490332:
                if x[1370] <= 0.5078431666:
                    if x[1655] <= 0.4529411793:
                        if x[2018] <= 0.4176470637:
                            if x[24] <= 0.6803921759:
                                if x[2436] <= 0.1549019665:
                                    if x[1014] <= 0.4549019635:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    if x[2003] <= 0.3901960850:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[282] <= 0.5568627715:
                                if x[928] <= 0.6372549236:
                                    if x[101] <= 0.3450980484:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[2032] <= 0.4784313887:
                            results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2791] <= 0.2333333343:
                        results.append(1)
                    else:
                        if x[6] <= 0.2274509892:
                            results.append(0)
                        else:
                            if x[913] <= 0.7529411912:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[2841] <= 0.1235294156:
                    if x[1011] <= 0.5333333611:
                        results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[2378] <= 0.8098039329:
                        if x[2458] <= 0.0725490227:
                            results.append(0)
                        else:
                            if x[2533] <= 0.1823529452:
                                if x[575] <= 0.3333333433:
                                    if x[2434] <= 0.2745098174:
                                        if x[1396] <= 0.2843137383:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(0)
                                else:
                                    if x[1802] <= 0.3470588326:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[88] <= 0.6450980604:
                                    if x[1313] <= 0.8392156959:
                                        if x[1700] <= 0.8137255013:
                                            if x[1958] <= 0.0431372561:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[1135] <= 0.4784313738:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[2167] <= 0.4117647111:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                else:
                                    if x[1536] <= 0.5666666925:
                                        if x[1826] <= 0.3039215803:
                                            if x[2993] <= 0.3490196168:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[360] <= 0.6823529601:
                                                results.append(0)
                                            else:
                                                results.append(1)
                                    else:
                                        if x[1074] <= 0.7647058964:
                                            if x[654] <= 0.7901960909:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                    else:
                        if x[2016] <= 0.6372549236:
                            results.append(0)
                        else:
                            results.append(1)
        else:
            if x[1286] <= 0.3509804010:
                if x[683] <= 0.6235294342:
                    if x[2557] <= 0.3450980484:
                        if x[645] <= 0.7019608021:
                            if x[15] <= 0.5666666925:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                    else:
                        if x[2272] <= 0.3686274588:
                            results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[2338] <= 0.2823529541:
                        if x[1062] <= 0.3941176534:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[1108] <= 0.4176470637:
                            if x[1281] <= 0.1882352978:
                                results.append(0)
                            else:
                                if x[2904] <= 0.3960784376:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1446] <= 0.8156862855:
                                if x[2342] <= 0.3764705956:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(1)
            else:
                if x[2259] <= 0.5431372821:
                    if x[911] <= 0.9313725531:
                        if x[215] <= 0.3843137324:
                            results.append(0)
                        else:
                            if x[2262] <= 0.5039215982:
                                if x[1657] <= 0.6647059023:
                                    if x[1102] <= 0.2549019754:
                                        results.append(0)
                                    else:
                                        if x[1288] <= 0.3431372643:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2099] <= 0.7274509966:
                                        if x[275] <= 0.7745098174:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[1693] <= 0.5156863034:
                                    results.append(0)
                                else:
                                    if x[2295] <= 0.4392156899:
                                        results.append(1)
                                    else:
                                        results.append(0)
                    else:
                        if x[2566] <= 0.5352941453:
                            if x[1791] <= 0.3588235378:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(1)
                else:
                    if x[2545] <= 0.3274509907:
                        results.append(0)
                    else:
                        if x[490] <= 0.8294117749:
                            if x[1656] <= 0.3372549117:
                                results.append(0)
                            else:
                                if x[821] <= 0.7764706016:
                                    if x[1311] <= 0.7666666806:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[1327] <= 0.6921568811:
                                        results.append(0)
                                    else:
                                        results.append(1)
                        else:
                            if x[560] <= 0.8333333433:
                                results.append(0)
                            else:
                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 49
    if time.time() < deadline or interrupt_flag.is_set():
        if x[116] <= 0.6450980604:
            if x[2514] <= 0.3509804010:
                if x[2824] <= 0.1941176504:
                    if x[1676] <= 0.3137255013:
                        if x[895] <= 0.3803921640:
                            results.append(1)
                        else:
                            if x[190] <= 0.4274509847:
                                results.append(0)
                            else:
                                results.append(1)
                    else:
                        if x[2276] <= 0.3705882430:
                            if x[1682] <= 0.4156862795:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[2415] <= 0.2333333418:
                                if x[1766] <= 0.4549019635:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                else:
                    if x[1351] <= 0.2000000030:
                        if x[2588] <= 0.5686274767:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[1250] <= 0.2529411837:
                            if x[2236] <= 0.1294117682:
                                results.append(0)
                            else:
                                if x[2376] <= 0.6529411972:
                                    if x[865] <= 0.1823529452:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(0)
                        else:
                            if x[2217] <= 0.4392156899:
                                if x[2526] <= 0.3176470697:
                                    if x[1122] <= 0.6058823764:
                                        if x[2269] <= 0.4235294163:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[407] <= 0.2941176593:
                                        results.append(1)
                                    else:
                                        if x[1233] <= 0.5000000149:
                                            results.append(0)
                                        else:
                                            results.append(0)
                            else:
                                if x[2500] <= 0.3137255013:
                                    results.append(0)
                                else:
                                    results.append(1)
            else:
                if x[2170] <= 0.1039215699:
                    if x[1091] <= 0.4745098054:
                        if x[1746] <= 0.4627451003:
                            results.append(0)
                        else:
                            results.append(1)
                    else:
                        results.append(0)
                else:
                    if x[1604] <= 0.8921568692:
                        if x[2235] <= 0.1411764771:
                            if x[1425] <= 0.4705882519:
                                results.append(1)
                            else:
                                results.append(0)
                        else:
                            if x[2142] <= 0.2450980395:
                                if x[1574] <= 0.3274509907:
                                    if x[1673] <= 0.1137254946:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[849] <= 0.3568627536:
                                        results.append(0)
                                    else:
                                        results.append(1)
                            else:
                                if x[2185] <= 0.8686274588:
                                    if x[1984] <= 0.1470588297:
                                        if x[2767] <= 0.4784313887:
                                            results.append(1)
                                        else:
                                            results.append(0)
                                    else:
                                        if x[1796] <= 0.8509804010:
                                            if x[749] <= 0.6588235497:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
                    else:
                        if x[801] <= 0.4411764741:
                            results.append(0)
                        else:
                            results.append(1)
        else:
            if x[1109] <= 0.3549019694:
                if x[2230] <= 0.3431372643:
                    if x[2938] <= 0.5941176713:
                        if x[2662] <= 0.5117647350:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(1)
                else:
                    if x[1429] <= 0.2921568751:
                        if x[1613] <= 0.2568627521:
                            results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[1310] <= 0.6568627656:
                            if x[2155] <= 0.2274509817:
                                results.append(1)
                            else:
                                if x[1460] <= 0.1039215699:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            results.append(1)
            else:
                if x[95] <= 0.4450980425:
                    if x[2272] <= 0.3137255013:
                        results.append(0)
                    else:
                        if x[130] <= 0.7901960909:
                            results.append(1)
                        else:
                            results.append(1)
                else:
                    if x[2329] <= 0.3725490272:
                        if x[1504] <= 0.1941176504:
                            results.append(0)
                        else:
                            if x[1325] <= 0.2901960909:
                                if x[1010] <= 0.5078431517:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[188] <= 0.6313725710:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[3026] <= 0.2960784435:
                            if x[2940] <= 0.2980392277:
                                if x[2077] <= 0.3686274588:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[1113] <= 0.6372549236:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[1001] <= 0.3313725591:
                                if x[184] <= 0.7666666806:
                                    results.append(0)
                                else:
                                    results.append(1)
                            else:
                                if x[1893] <= 0.5960784554:
                                    if x[2845] <= 0.4490196109:
                                        if x[2848] <= 0.4039215744:
                                            results.append(0)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[2243] <= 0.9039215744:
                                            results.append(0)
                                        else:
                                            results.append(0)
                                else:
                                    if x[2565] <= 0.5372549295:
                                        results.append(0)
                                    else:
                                        if x[3050] <= 0.6372549236:
                                            results.append(1)
                                        else:
                                            if x[909] <= 0.8784313798:
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
