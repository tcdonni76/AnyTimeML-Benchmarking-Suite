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
        if x[346] <= 0.0058823533:
            if x[323] <= 0.6490196288:
                if x[156] <= 0.0098039219:
                    if x[460] <= 0.0843137279:
                        if x[433] <= 0.3450980484:
                            if x[399] <= 0.0117647061:
                                if x[179] <= 0.9392156899:
                                    results.append(7)
                                else:
                                    results.append(2)
                            else:
                                if x[241] <= 0.2549019679:
                                    results.append(6)
                                else:
                                    results.append(0)
                        else:
                            if x[239] <= 0.4176470637:
                                if x[378] <= 0.9411764741:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(3)
                    else:
                        if x[236] <= 0.0588235315:
                            if x[386] <= 0.1254902035:
                                if x[259] <= 0.1294117682:
                                    results.append(1)
                                else:
                                    results.append(4)
                            else:
                                results.append(6)
                        else:
                            if x[382] <= 0.9901960790:
                                if x[371] <= 0.2686274573:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[314] <= 0.0274509811:
                                    results.append(9)
                                else:
                                    results.append(9)
                else:
                    if x[377] <= 0.4039215744:
                        if x[341] <= 0.0176470596:
                            if x[460] <= 0.0117647061:
                                if x[630] <= 0.2588235363:
                                    results.append(2)
                                else:
                                    results.append(0)
                            else:
                                if x[155] <= 0.1882352978:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            if x[239] <= 0.2196078487:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[462] <= 0.8196078539:
                            if x[658] <= 0.1607843190:
                                if x[564] <= 0.1254902035:
                                    results.append(6)
                                else:
                                    results.append(3)
                            else:
                                if x[161] <= 0.0098039219:
                                    results.append(3)
                                else:
                                    results.append(8)
                        else:
                            if x[628] <= 0.7235294282:
                                results.append(8)
                            else:
                                results.append(8)
            else:
                if x[551] <= 0.0098039219:
                    if x[604] <= 0.5117647201:
                        if x[492] <= 0.3862745166:
                            if x[237] <= 0.2588235363:
                                if x[463] <= 0.5058823824:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[627] <= 0.8294117749:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[491] <= 0.6098039448:
                                results.append(3)
                            else:
                                results.append(1)
                    else:
                        if x[208] <= 0.0490196091:
                            if x[432] <= 0.3392156959:
                                results.append(3)
                            else:
                                results.append(4)
                        else:
                            if x[515] <= 0.0392156877:
                                if x[631] <= 0.9901960790:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(8)
                else:
                    if x[686] <= 0.4019607902:
                        if x[582] <= 0.2686274573:
                            if x[577] <= 0.8352941275:
                                results.append(2)
                            else:
                                if x[464] <= 0.3215686381:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            results.append(2)
                    else:
                        results.append(8)
        else:
            if x[380] <= 0.0039215689:
                if x[511] <= 0.3000000119:
                    if x[411] <= 0.0274509815:
                        if x[358] <= 0.0529411770:
                            if x[263] <= 0.0058823531:
                                if x[205] <= 0.7274509966:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[597] <= 0.6941176504:
                                    results.append(5)
                                else:
                                    results.append(5)
                        else:
                            results.append(0)
                    else:
                        if x[299] <= 0.0764705921:
                            if x[514] <= 0.1392156873:
                                results.append(3)
                            else:
                                if x[517] <= 0.8882353008:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[240] <= 0.0529411770:
                                if x[427] <= 0.4039215744:
                                    results.append(0)
                                else:
                                    results.append(4)
                            else:
                                if x[329] <= 0.0176470596:
                                    results.append(0)
                                else:
                                    results.append(7)
                else:
                    if x[182] <= 0.0039215689:
                        if x[344] <= 0.4078431427:
                            results.append(6)
                        else:
                            results.append(0)
                    else:
                        if x[628] <= 0.0196078438:
                            results.append(6)
                        else:
                            if x[372] <= 0.1705882400:
                                results.append(0)
                            else:
                                if x[296] <= 0.4470588416:
                                    results.append(0)
                                else:
                                    results.append(0)
            else:
                if x[496] <= 0.0901960805:
                    if x[487] <= 0.1294117682:
                        if x[434] <= 0.3470588326:
                            if x[464] <= 0.5078431666:
                                if x[238] <= 0.0392156877:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[374] <= 0.1549019665:
                                    results.append(7)
                                else:
                                    results.append(9)
                        else:
                            if x[240] <= 0.2549019679:
                                if x[155] <= 0.0705882390:
                                    results.append(4)
                                else:
                                    results.append(8)
                            else:
                                if x[291] <= 0.1921568662:
                                    results.append(4)
                                else:
                                    results.append(9)
                    else:
                        if x[429] <= 0.0843137279:
                            if x[684] <= 0.0058823531:
                                if x[437] <= 0.1823529452:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                        else:
                            if x[713] <= 0.8176470697:
                                if x[688] <= 0.9372549057:
                                    results.append(4)
                                else:
                                    results.append(9)
                            else:
                                results.append(9)
                else:
                    if x[659] <= 0.0156862754:
                        if x[572] <= 0.5784313977:
                            if x[379] <= 0.9274509847:
                                if x[433] <= 0.2274509817:
                                    results.append(6)
                                else:
                                    results.append(4)
                            else:
                                results.append(2)
                        else:
                            if x[350] <= 0.9823529422:
                                if x[578] <= 0.0058823531:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(0)
                    else:
                        if x[268] <= 0.0392156867:
                            if x[579] <= 0.6274510026:
                                results.append(4)
                            else:
                                if x[577] <= 0.2490196154:
                                    results.append(3)
                                else:
                                    results.append(5)
                        else:
                            if x[518] <= 0.0333333351:
                                if x[187] <= 0.2980392203:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[207] <= 0.6745098084:
                                    results.append(8)
                                else:
                                    results.append(9)
    
    else:
      return vote_logic(results)
    
    # Tree 1
    if time.time() < deadline or interrupt_flag.is_set():
        if x[461] <= 0.0176470596:
            if x[455] <= 0.0372549035:
                if x[595] <= 0.0137254903:
                    if x[155] <= 0.0058823531:
                        if x[328] <= 0.0098039219:
                            if x[270] <= 0.6784313917:
                                if x[318] <= 0.5568627715:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[430] <= 0.0352941193:
                                    results.append(7)
                                else:
                                    results.append(9)
                        else:
                            if x[259] <= 0.0764705893:
                                if x[209] <= 0.5666666925:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[379] <= 0.0607843157:
                                    results.append(7)
                                else:
                                    results.append(7)
                    else:
                        if x[268] <= 0.1529411785:
                            if x[205] <= 0.4176470637:
                                if x[350] <= 0.0431372561:
                                    results.append(0)
                                else:
                                    results.append(3)
                            else:
                                results.append(5)
                        else:
                            if x[469] <= 0.6901960969:
                                if x[213] <= 0.5980392396:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(5)
                else:
                    if x[319] <= 0.4686274529:
                        if x[324] <= 0.2117647156:
                            if x[346] <= 0.0549019612:
                                results.append(2)
                            else:
                                results.append(5)
                        else:
                            if x[570] <= 0.3117647097:
                                results.append(3)
                            else:
                                results.append(3)
                    else:
                        if x[150] <= 0.3745098114:
                            if x[512] <= 0.2882353067:
                                if x[321] <= 0.0529411770:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(5)
                        else:
                            results.append(3)
            else:
                if x[464] <= 0.4666666836:
                    if x[379] <= 0.3803921789:
                        if x[539] <= 0.2627451122:
                            if x[466] <= 0.0725490227:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[300] <= 0.0058823531:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[440] <= 0.7529411912:
                            results.append(5)
                        else:
                            results.append(3)
                else:
                    if x[607] <= 0.1078431420:
                        if x[269] <= 0.2803921625:
                            if x[464] <= 0.9901960790:
                                results.append(4)
                            else:
                                results.append(6)
                        else:
                            if x[539] <= 0.0235294122:
                                results.append(4)
                            else:
                                results.append(5)
                    else:
                        results.append(2)
        else:
            if x[569] <= 0.0176470596:
                if x[290] <= 0.0058823531:
                    if x[465] <= 0.0176470596:
                        if x[378] <= 0.6313725710:
                            if x[601] <= 0.9431372583:
                                results.append(8)
                            else:
                                results.append(7)
                        else:
                            if x[402] <= 0.0098039219:
                                if x[377] <= 0.9862745106:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(6)
                    else:
                        if x[607] <= 0.0176470592:
                            if x[372] <= 0.0333333351:
                                if x[403] <= 0.0196078438:
                                    results.append(7)
                                else:
                                    results.append(4)
                            else:
                                results.append(4)
                        else:
                            if x[315] <= 0.1607843190:
                                if x[520] <= 0.8784313798:
                                    results.append(3)
                                else:
                                    results.append(1)
                            else:
                                if x[288] <= 0.8392156959:
                                    results.append(9)
                                else:
                                    results.append(4)
                else:
                    if x[212] <= 0.5274510086:
                        if x[70] <= 0.0019607844:
                            if x[543] <= 0.6843137443:
                                if x[238] <= 0.9470588267:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[379] <= 0.8784313798:
                                    results.append(6)
                                else:
                                    results.append(4)
                        else:
                            results.append(6)
                    else:
                        if x[715] <= 0.0764705893:
                            if x[327] <= 0.2862745225:
                                if x[684] <= 0.0039215689:
                                    results.append(4)
                                else:
                                    results.append(5)
                            else:
                                if x[599] <= 0.5705882609:
                                    results.append(9)
                                else:
                                    results.append(7)
                        else:
                            if x[299] <= 0.0294117648:
                                results.append(9)
                            else:
                                if x[549] <= 0.6039215922:
                                    results.append(9)
                                else:
                                    results.append(9)
            else:
                if x[347] <= 0.1333333366:
                    if x[153] <= 0.0490196105:
                        if x[351] <= 0.8058823645:
                            if x[371] <= 0.1431372617:
                                if x[520] <= 0.4509804025:
                                    results.append(7)
                                else:
                                    results.append(2)
                            else:
                                results.append(6)
                        else:
                            if x[625] <= 0.4352941215:
                                results.append(6)
                            else:
                                if x[349] <= 0.0117647066:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[427] <= 0.9862745106:
                            if x[569] <= 0.8764705956:
                                if x[126] <= 0.0666666701:
                                    results.append(3)
                                else:
                                    results.append(2)
                            else:
                                if x[329] <= 0.2823529467:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            results.append(6)
                else:
                    if x[457] <= 0.0843137279:
                        if x[542] <= 0.3784313947:
                            results.append(5)
                        else:
                            if x[321] <= 0.9019607902:
                                if x[401] <= 0.8686274588:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                    else:
                        if x[629] <= 0.1117647104:
                            if x[566] <= 0.0039215689:
                                if x[428] <= 0.9941176474:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(6)
                        else:
                            if x[602] <= 0.9862745106:
                                if x[466] <= 0.4156862944:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                if x[244] <= 0.0901960805:
                                    results.append(6)
                                else:
                                    results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 2
    if time.time() < deadline or interrupt_flag.is_set():
        if x[405] <= 0.0313725499:
            if x[408] <= 0.0019607844:
                if x[456] <= 0.5313725770:
                    if x[539] <= 0.0333333341:
                        if x[153] <= 0.0098039219:
                            if x[288] <= 0.0686274543:
                                results.append(5)
                            else:
                                if x[401] <= 0.3843137324:
                                    results.append(7)
                                else:
                                    results.append(5)
                        else:
                            if x[651] <= 0.0137254903:
                                if x[487] <= 0.0372549035:
                                    results.append(5)
                                else:
                                    results.append(6)
                            else:
                                results.append(3)
                    else:
                        if x[301] <= 0.0156862754:
                            if x[483] <= 0.2960784361:
                                if x[125] <= 0.7470588386:
                                    results.append(5)
                                else:
                                    results.append(3)
                            else:
                                results.append(6)
                        else:
                            if x[608] <= 0.5274509937:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[690] <= 0.3156862855:
                        if x[316] <= 0.0196078434:
                            if x[495] <= 0.2078431398:
                                results.append(5)
                            else:
                                if x[264] <= 0.2647058889:
                                    results.append(6)
                                else:
                                    results.append(0)
                        else:
                            if x[627] <= 0.0176470596:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        results.append(7)
            else:
                if x[152] <= 0.0078431377:
                    if x[427] <= 0.0078431377:
                        if x[402] <= 0.1901960820:
                            if x[268] <= 0.0215686280:
                                if x[238] <= 0.2627451047:
                                    results.append(2)
                                else:
                                    results.append(7)
                            else:
                                if x[518] <= 0.9941176474:
                                    results.append(7)
                                else:
                                    results.append(7)
                        else:
                            if x[570] <= 0.0176470596:
                                if x[431] <= 0.3117647171:
                                    results.append(9)
                                else:
                                    results.append(4)
                            else:
                                results.append(6)
                    else:
                        if x[568] <= 0.1470588259:
                            if x[347] <= 0.1941176541:
                                if x[211] <= 0.0196078438:
                                    results.append(4)
                                else:
                                    results.append(9)
                            else:
                                if x[321] <= 0.1078431420:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[356] <= 0.7196078598:
                                if x[545] <= 0.9019607902:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(0)
                else:
                    if x[326] <= 0.6411764920:
                        if x[544] <= 0.0098039219:
                            if x[464] <= 0.5627451241:
                                if x[524] <= 0.0980392173:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(1)
                        else:
                            if x[267] <= 0.1274509877:
                                if x[373] <= 0.2941176593:
                                    results.append(2)
                                else:
                                    results.append(6)
                            else:
                                results.append(2)
                    else:
                        if x[469] <= 0.8490196168:
                            results.append(2)
                        else:
                            results.append(2)
        else:
            if x[490] <= 0.0019607844:
                if x[657] <= 0.0058823531:
                    if x[570] <= 0.0372549035:
                        if x[264] <= 0.0235294122:
                            if x[180] <= 0.0901960805:
                                if x[434] <= 0.6156862825:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                results.append(9)
                        else:
                            if x[429] <= 0.1215686314:
                                results.append(5)
                            else:
                                if x[744] <= 0.0333333351:
                                    results.append(9)
                                else:
                                    results.append(9)
                    else:
                        if x[271] <= 0.0176470596:
                            if x[410] <= 0.0137254903:
                                results.append(2)
                            else:
                                results.append(6)
                        else:
                            if x[403] <= 0.9901960790:
                                if x[565] <= 0.6823529452:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                results.append(5)
                else:
                    if x[149] <= 0.0254901964:
                        if x[352] <= 0.6450980604:
                            if x[356] <= 0.1117647067:
                                if x[296] <= 0.0588235315:
                                    results.append(5)
                                else:
                                    results.append(8)
                            else:
                                if x[567] <= 0.3372549117:
                                    results.append(9)
                                else:
                                    results.append(8)
                        else:
                            if x[317] <= 0.0098039219:
                                if x[297] <= 0.6137255132:
                                    results.append(8)
                                else:
                                    results.append(3)
                            else:
                                if x[354] <= 0.5333333462:
                                    results.append(8)
                                else:
                                    results.append(5)
                    else:
                        if x[288] <= 0.0039215689:
                            if x[431] <= 0.5647059083:
                                results.append(3)
                            else:
                                if x[625] <= 0.2254901975:
                                    results.append(3)
                                else:
                                    results.append(2)
                        else:
                            if x[570] <= 0.7058823705:
                                results.append(5)
                            else:
                                results.append(5)
            else:
                if x[319] <= 0.1490196139:
                    if x[437] <= 0.0039215689:
                        if x[205] <= 0.0039215689:
                            if x[430] <= 0.1745098094:
                                if x[654] <= 0.9941176474:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(8)
                        else:
                            if x[372] <= 0.0058823531:
                                if x[208] <= 0.7901960909:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                results.append(6)
                    else:
                        if x[100] <= 0.0137254903:
                            if x[316] <= 0.1098039225:
                                if x[176] <= 0.0176470596:
                                    results.append(1)
                                else:
                                    results.append(2)
                            else:
                                if x[552] <= 0.6862745285:
                                    results.append(4)
                                else:
                                    results.append(8)
                        else:
                            results.append(2)
                else:
                    if x[102] <= 0.0490196086:
                        if x[180] <= 0.0313725495:
                            if x[348] <= 0.9529411793:
                                if x[214] <= 0.0235294122:
                                    results.append(4)
                                else:
                                    results.append(9)
                            else:
                                if x[457] <= 0.0019607844:
                                    results.append(5)
                                else:
                                    results.append(4)
                        else:
                            if x[496] <= 0.2000000067:
                                if x[429] <= 0.9568627477:
                                    results.append(8)
                                else:
                                    results.append(4)
                            else:
                                if x[98] <= 0.2588235438:
                                    results.append(4)
                                else:
                                    results.append(6)
                    else:
                        results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 3
    if time.time() < deadline or interrupt_flag.is_set():
        if x[406] <= 0.0019607844:
            if x[437] <= 0.2411764711:
                if x[331] <= 0.0039215689:
                    if x[516] <= 0.2176470608:
                        if x[352] <= 0.0490196086:
                            if x[657] <= 0.0235294122:
                                results.append(0)
                            else:
                                if x[150] <= 0.7980392277:
                                    results.append(0)
                                else:
                                    results.append(3)
                        else:
                            if x[205] <= 0.0784313735:
                                results.append(3)
                            else:
                                if x[212] <= 0.4254902005:
                                    results.append(3)
                                else:
                                    results.append(5)
                    else:
                        if x[431] <= 0.7254902124:
                            results.append(8)
                        else:
                            results.append(6)
                else:
                    if x[211] <= 0.0509803928:
                        results.append(0)
                    else:
                        if x[273] <= 0.3235294223:
                            results.append(0)
                        else:
                            results.append(0)
            else:
                if x[567] <= 0.0235294122:
                    if x[456] <= 0.1333333366:
                        if x[326] <= 0.0137254908:
                            if x[268] <= 0.0901960805:
                                results.append(6)
                            else:
                                if x[237] <= 0.0450980403:
                                    results.append(3)
                                else:
                                    results.append(7)
                        else:
                            if x[183] <= 0.6235294342:
                                if x[264] <= 0.0411764719:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                if x[327] <= 0.5058823675:
                                    results.append(9)
                                else:
                                    results.append(7)
                    else:
                        if x[542] <= 0.1098039225:
                            if x[375] <= 0.0078431377:
                                if x[272] <= 0.7960784435:
                                    results.append(4)
                                else:
                                    results.append(9)
                            else:
                                results.append(4)
                        else:
                            if x[240] <= 0.1901960825:
                                results.append(6)
                            else:
                                results.append(9)
                else:
                    if x[348] <= 0.1941176504:
                        if x[462] <= 0.1549019683:
                            results.append(0)
                        else:
                            if x[327] <= 0.1745098121:
                                results.append(6)
                            else:
                                results.append(2)
                    else:
                        if x[269] <= 0.7647058964:
                            if x[655] <= 0.0176470596:
                                results.append(6)
                            else:
                                if x[571] <= 0.7156862915:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[210] <= 0.0294117657:
                                results.append(3)
                            else:
                                results.append(3)
        else:
            if x[438] <= 0.0019607844:
                if x[402] <= 0.0039215689:
                    if x[683] <= 0.0941176489:
                        if x[608] <= 0.0352941193:
                            if x[521] <= 0.0372549035:
                                if x[218] <= 0.0529411770:
                                    results.append(1)
                                else:
                                    results.append(5)
                            else:
                                if x[264] <= 0.4921568632:
                                    results.append(6)
                                else:
                                    results.append(1)
                        else:
                            if x[408] <= 0.1352941208:
                                results.append(2)
                            else:
                                results.append(2)
                    else:
                        if x[488] <= 0.1862745136:
                            if x[322] <= 0.2196078524:
                                if x[291] <= 0.3725490272:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                results.append(1)
                        else:
                            if x[347] <= 0.0137254903:
                                if x[324] <= 0.5058823824:
                                    results.append(8)
                                else:
                                    results.append(7)
                            else:
                                results.append(8)
                else:
                    if x[485] <= 0.8078431487:
                        if x[515] <= 0.0764705911:
                            if x[379] <= 0.0196078438:
                                if x[188] <= 0.0176470596:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[177] <= 0.0117647061:
                                    results.append(9)
                                else:
                                    results.append(3)
                        else:
                            if x[216] <= 0.0627451017:
                                results.append(5)
                            else:
                                if x[548] <= 0.2725490220:
                                    results.append(8)
                                else:
                                    results.append(8)
                    else:
                        if x[374] <= 0.2745098174:
                            if x[213] <= 0.1941176541:
                                results.append(2)
                            else:
                                results.append(2)
                        else:
                            if x[215] <= 0.3000000119:
                                results.append(6)
                            else:
                                results.append(8)
            else:
                if x[350] <= 0.7274509966:
                    if x[240] <= 0.4352941215:
                        if x[543] <= 0.7058823705:
                            if x[463] <= 0.7549019754:
                                if x[346] <= 0.5098039359:
                                    results.append(4)
                                else:
                                    results.append(5)
                            else:
                                if x[356] <= 0.6058823764:
                                    results.append(4)
                                else:
                                    results.append(8)
                        else:
                            if x[186] <= 0.4607843310:
                                if x[155] <= 0.0039215689:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                if x[261] <= 0.1745098121:
                                    results.append(2)
                                else:
                                    results.append(8)
                    else:
                        if x[570] <= 0.0627450999:
                            if x[155] <= 0.0019607844:
                                if x[517] <= 0.8000000119:
                                    results.append(9)
                                else:
                                    results.append(7)
                            else:
                                if x[153] <= 0.0823529419:
                                    results.append(4)
                                else:
                                    results.append(3)
                        else:
                            if x[326] <= 0.0176470596:
                                if x[595] <= 0.4764706045:
                                    results.append(6)
                                else:
                                    results.append(5)
                            else:
                                if x[152] <= 0.0137254903:
                                    results.append(9)
                                else:
                                    results.append(2)
                else:
                    if x[488] <= 0.2098039240:
                        if x[288] <= 0.6058823764:
                            if x[262] <= 0.8137255013:
                                if x[213] <= 0.0784313753:
                                    results.append(5)
                                else:
                                    results.append(3)
                            else:
                                if x[346] <= 0.9215686321:
                                    results.append(3)
                                else:
                                    results.append(5)
                        else:
                            if x[315] <= 0.3882353008:
                                results.append(3)
                            else:
                                results.append(7)
                    else:
                        if x[129] <= 0.7137255073:
                            if x[457] <= 0.0352941183:
                                if x[599] <= 0.9294117689:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(5)
                        else:
                            results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 4
    if time.time() < deadline or interrupt_flag.is_set():
        if x[542] <= 0.3098039329:
            if x[625] <= 0.1098039225:
                if x[466] <= 0.0039215689:
                    if x[381] <= 0.0274509806:
                        if x[245] <= 0.0607843138:
                            if x[235] <= 0.8549019694:
                                if x[294] <= 0.0588235315:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(8)
                        else:
                            if x[606] <= 0.0823529442:
                                results.append(5)
                            else:
                                results.append(0)
                    else:
                        if x[606] <= 0.0843137279:
                            if x[267] <= 0.2509803995:
                                if x[402] <= 0.1215686314:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[433] <= 0.2039215714:
                                    results.append(7)
                                else:
                                    results.append(9)
                        else:
                            if x[298] <= 0.1941176504:
                                results.append(3)
                            else:
                                results.append(3)
                else:
                    if x[240] <= 0.2176470608:
                        if x[271] <= 0.0058823531:
                            if x[126] <= 0.0725490227:
                                if x[407] <= 0.3039215729:
                                    results.append(3)
                                else:
                                    results.append(4)
                            else:
                                results.append(6)
                        else:
                            if x[294] <= 0.5156862885:
                                if x[605] <= 0.9901960790:
                                    results.append(4)
                                else:
                                    results.append(9)
                            else:
                                results.append(7)
                    else:
                        if x[345] <= 0.0039215689:
                            if x[355] <= 0.0176470592:
                                if x[574] <= 0.2490196154:
                                    results.append(3)
                                else:
                                    results.append(7)
                            else:
                                if x[242] <= 0.2529411837:
                                    results.append(9)
                                else:
                                    results.append(7)
                        else:
                            if x[524] <= 0.0274509815:
                                if x[202] <= 0.1666666716:
                                    results.append(9)
                                else:
                                    results.append(7)
                            else:
                                if x[517] <= 0.4215686396:
                                    results.append(3)
                                else:
                                    results.append(8)
            else:
                if x[301] <= 0.3549019694:
                    if x[296] <= 0.4921568781:
                        if x[346] <= 0.1274509840:
                            if x[378] <= 0.1470588259:
                                if x[155] <= 0.4803921580:
                                    results.append(7)
                                else:
                                    results.append(2)
                            else:
                                if x[593] <= 0.1235294119:
                                    results.append(5)
                                else:
                                    results.append(3)
                        else:
                            if x[292] <= 0.9509803951:
                                if x[289] <= 0.1686274558:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[484] <= 0.9843137264:
                                    results.append(5)
                                else:
                                    results.append(0)
                    else:
                        if x[630] <= 0.0215686285:
                            if x[323] <= 0.8215686381:
                                results.append(7)
                            else:
                                results.append(1)
                        else:
                            if x[513] <= 0.6215686500:
                                if x[490] <= 0.1176470630:
                                    results.append(3)
                                else:
                                    results.append(1)
                            else:
                                results.append(8)
                else:
                    if x[470] <= 0.0039215689:
                        if x[434] <= 0.0705882385:
                            if x[539] <= 0.6843137443:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[487] <= 0.0098039219:
                                if x[489] <= 0.7921568751:
                                    results.append(5)
                                else:
                                    results.append(7)
                            else:
                                if x[550] <= 0.1509803981:
                                    results.append(8)
                                else:
                                    results.append(8)
                    else:
                        if x[409] <= 0.5450980403:
                            results.append(0)
                        else:
                            results.append(3)
        else:
            if x[684] <= 0.0156862750:
                if x[428] <= 0.0039215689:
                    if x[403] <= 0.1529411823:
                        if x[551] <= 0.0411764719:
                            if x[633] <= 0.2647058964:
                                if x[436] <= 0.8666666746:
                                    results.append(1)
                                else:
                                    results.append(2)
                            else:
                                results.append(2)
                        else:
                            if x[434] <= 0.2960784435:
                                results.append(3)
                            else:
                                if x[490] <= 0.7470588386:
                                    results.append(2)
                                else:
                                    results.append(2)
                    else:
                        if x[328] <= 0.0843137261:
                            if x[270] <= 0.0254901964:
                                if x[514] <= 0.3156862780:
                                    results.append(5)
                                else:
                                    results.append(6)
                            else:
                                if x[514] <= 0.9549019635:
                                    results.append(8)
                                else:
                                    results.append(1)
                        else:
                            if x[407] <= 0.9450980425:
                                results.append(5)
                            else:
                                results.append(8)
                else:
                    if x[462] <= 0.0196078438:
                        if x[215] <= 0.0294117648:
                            if x[239] <= 0.0039215689:
                                results.append(6)
                            else:
                                results.append(0)
                        else:
                            if x[574] <= 0.1156862751:
                                results.append(5)
                            else:
                                if x[492] <= 0.9352941215:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[299] <= 0.2019607872:
                            if x[325] <= 0.4980392307:
                                if x[187] <= 0.0745098051:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(2)
                        else:
                            if x[357] <= 0.5647058934:
                                if x[324] <= 0.2372549102:
                                    results.append(2)
                                else:
                                    results.append(6)
                            else:
                                results.append(6)
            else:
                if x[405] <= 0.2450980470:
                    if x[463] <= 0.0647058859:
                        if x[153] <= 0.2215686329:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(7)
                else:
                    if x[684] <= 0.4568627477:
                        if x[626] <= 0.9431372583:
                            results.append(8)
                        else:
                            results.append(2)
                    else:
                        if x[600] <= 0.6803921759:
                            results.append(8)
                        else:
                            results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 5
    if time.time() < deadline or interrupt_flag.is_set():
        if x[456] <= 0.0098039219:
            if x[289] <= 0.0019607844:
                if x[437] <= 0.0039215689:
                    if x[634] <= 0.0098039219:
                        if x[292] <= 0.4372549057:
                            if x[355] <= 0.0176470596:
                                if x[513] <= 0.7588235438:
                                    results.append(1)
                                else:
                                    results.append(2)
                            else:
                                if x[187] <= 0.0117647061:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[568] <= 0.3941176683:
                                if x[543] <= 0.0058823531:
                                    results.append(1)
                                else:
                                    results.append(8)
                            else:
                                if x[461] <= 0.5098039359:
                                    results.append(5)
                                else:
                                    results.append(8)
                    else:
                        if x[318] <= 0.0411764719:
                            if x[379] <= 0.1254902035:
                                results.append(3)
                            else:
                                if x[487] <= 0.7647058964:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            results.append(8)
                else:
                    if x[322] <= 0.0784313753:
                        if x[125] <= 0.1705882419:
                            if x[432] <= 0.0686274515:
                                if x[243] <= 0.4411764741:
                                    results.append(2)
                                else:
                                    results.append(7)
                            else:
                                if x[318] <= 0.0431372561:
                                    results.append(3)
                                else:
                                    results.append(9)
                        else:
                            if x[402] <= 0.2019607946:
                                if x[462] <= 0.0862745121:
                                    results.append(3)
                                else:
                                    results.append(2)
                            else:
                                results.append(6)
                    else:
                        if x[461] <= 0.3803921640:
                            if x[655] <= 0.6215686500:
                                if x[215] <= 0.6411764771:
                                    results.append(5)
                                else:
                                    results.append(3)
                            else:
                                if x[379] <= 0.2333333418:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[353] <= 0.0254901964:
                                results.append(6)
                            else:
                                results.append(1)
            else:
                if x[405] <= 0.1803921610:
                    if x[538] <= 0.0215686285:
                        if x[96] <= 0.0058823531:
                            if x[578] <= 0.1450980455:
                                if x[429] <= 0.1784313768:
                                    results.append(7)
                                else:
                                    results.append(4)
                            else:
                                if x[379] <= 0.0647058859:
                                    results.append(7)
                                else:
                                    results.append(3)
                        else:
                            results.append(6)
                    else:
                        if x[425] <= 0.1509803983:
                            results.append(5)
                        else:
                            if x[183] <= 0.8372549117:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[318] <= 0.2647058889:
                        if x[596] <= 0.0745098069:
                            if x[211] <= 0.0549019617:
                                results.append(4)
                            else:
                                if x[399] <= 0.0019607844:
                                    results.append(1)
                                else:
                                    results.append(9)
                        else:
                            results.append(3)
                    else:
                        if x[487] <= 0.0117647066:
                            if x[578] <= 0.0568627473:
                                if x[409] <= 0.0176470596:
                                    results.append(5)
                                else:
                                    results.append(9)
                            else:
                                if x[325] <= 0.0941176489:
                                    results.append(5)
                                else:
                                    results.append(8)
                        else:
                            if x[220] <= 0.0058823531:
                                if x[181] <= 0.0882352963:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
        else:
            if x[512] <= 0.1862745136:
                if x[98] <= 0.0490196086:
                    if x[267] <= 0.2156862766:
                        if x[184] <= 0.0882352963:
                            if x[437] <= 0.7901960909:
                                if x[399] <= 0.9882352948:
                                    results.append(6)
                                else:
                                    results.append(4)
                            else:
                                if x[439] <= 0.0372549039:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[551] <= 0.1686274558:
                                if x[658] <= 0.1803921610:
                                    results.append(4)
                                else:
                                    results.append(9)
                            else:
                                if x[549] <= 0.0078431377:
                                    results.append(5)
                                else:
                                    results.append(3)
                    else:
                        if x[595] <= 0.4333333522:
                            if x[434] <= 0.0627451017:
                                if x[548] <= 0.8137255013:
                                    results.append(5)
                                else:
                                    results.append(7)
                            else:
                                if x[273] <= 0.9901960790:
                                    results.append(9)
                                else:
                                    results.append(3)
                        else:
                            results.append(0)
                else:
                    results.append(6)
            else:
                if x[656] <= 0.0745098051:
                    if x[594] <= 0.6647059023:
                        if x[413] <= 0.0058823531:
                            if x[627] <= 0.9784313738:
                                if x[127] <= 0.7019608021:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(6)
                        else:
                            if x[408] <= 0.0078431377:
                                if x[462] <= 0.0490196086:
                                    results.append(0)
                                else:
                                    results.append(2)
                            else:
                                if x[633] <= 0.3784313947:
                                    results.append(6)
                                else:
                                    results.append(4)
                    else:
                        if x[401] <= 0.6117647290:
                            results.append(2)
                        else:
                            results.append(2)
                else:
                    if x[487] <= 0.0313725509:
                        if x[456] <= 0.7921568751:
                            if x[372] <= 0.5607843399:
                                results.append(8)
                            else:
                                results.append(0)
                        else:
                            if x[372] <= 0.1450980417:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[461] <= 0.0254901964:
                            if x[551] <= 0.4666666836:
                                results.append(0)
                            else:
                                results.append(3)
                        else:
                            if x[654] <= 0.9098039269:
                                if x[268] <= 0.0921568647:
                                    results.append(4)
                                else:
                                    results.append(6)
                            else:
                                results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 6
    if time.time() < deadline or interrupt_flag.is_set():
        if x[455] <= 0.0078431375:
            if x[318] <= 0.0098039219:
                if x[410] <= 0.0960784331:
                    if x[176] <= 0.0156862754:
                        if x[580] <= 0.0254901964:
                            if x[232] <= 0.0196078438:
                                if x[550] <= 0.1137254946:
                                    results.append(1)
                                else:
                                    results.append(3)
                            else:
                                results.append(7)
                        else:
                            if x[238] <= 0.1352941208:
                                results.append(2)
                            else:
                                results.append(2)
                    else:
                        if x[541] <= 0.0137254903:
                            if x[463] <= 0.9254902005:
                                results.append(3)
                            else:
                                results.append(3)
                        else:
                            if x[409] <= 0.1313725524:
                                results.append(2)
                            else:
                                results.append(2)
                else:
                    if x[492] <= 0.5745098293:
                        if x[152] <= 0.0901960805:
                            if x[371] <= 0.4647058994:
                                if x[516] <= 0.2117647082:
                                    results.append(3)
                                else:
                                    results.append(6)
                            else:
                                results.append(9)
                        else:
                            if x[440] <= 0.0274509806:
                                if x[652] <= 0.1901960820:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                results.append(3)
                    else:
                        if x[264] <= 0.1215686314:
                            if x[512] <= 0.4529411795:
                                if x[486] <= 0.0176470596:
                                    results.append(9)
                                else:
                                    results.append(4)
                            else:
                                results.append(2)
                        else:
                            if x[405] <= 0.2176470682:
                                if x[261] <= 0.2137254924:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                results.append(3)
            else:
                if x[403] <= 0.0039215689:
                    if x[293] <= 0.4333333373:
                        if x[98] <= 0.0058823531:
                            if x[515] <= 0.3941176534:
                                if x[268] <= 0.3843137324:
                                    results.append(9)
                                else:
                                    results.append(7)
                            else:
                                if x[321] <= 0.1411764771:
                                    results.append(2)
                                else:
                                    results.append(8)
                        else:
                            results.append(6)
                    else:
                        if x[288] <= 0.3333333433:
                            if x[631] <= 0.4627451003:
                                results.append(7)
                            else:
                                if x[183] <= 0.9156862795:
                                    results.append(3)
                                else:
                                    results.append(8)
                        else:
                            if x[523] <= 0.7862745225:
                                results.append(7)
                            else:
                                results.append(7)
                else:
                    if x[98] <= 0.0215686280:
                        if x[488] <= 0.2686274648:
                            if x[598] <= 0.0156862750:
                                if x[490] <= 0.0803921595:
                                    results.append(9)
                                else:
                                    results.append(9)
                            else:
                                if x[324] <= 0.6960784495:
                                    results.append(5)
                                else:
                                    results.append(3)
                        else:
                            if x[377] <= 0.8372549117:
                                if x[658] <= 0.1196078435:
                                    results.append(6)
                                else:
                                    results.append(8)
                            else:
                                if x[266] <= 0.4333333373:
                                    results.append(8)
                                else:
                                    results.append(8)
                    else:
                        if x[345] <= 0.0058823531:
                            results.append(6)
                        else:
                            results.append(6)
        else:
            if x[380] <= 0.0039215689:
                if x[184] <= 0.1745098084:
                    if x[509] <= 0.5274509937:
                        if x[235] <= 0.3980392218:
                            if x[295] <= 0.0235294122:
                                results.append(4)
                            else:
                                results.append(5)
                        else:
                            if x[382] <= 0.5235294253:
                                if x[152] <= 0.0098039219:
                                    results.append(6)
                                else:
                                    results.append(0)
                            else:
                                results.append(9)
                    else:
                        results.append(2)
                else:
                    if x[462] <= 0.0196078438:
                        if x[427] <= 0.0529411780:
                            if x[299] <= 0.4411764815:
                                results.append(6)
                            else:
                                results.append(0)
                        else:
                            if x[551] <= 0.9941176474:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[272] <= 0.0980392173:
                            if x[293] <= 0.1686274563:
                                results.append(5)
                            else:
                                results.append(6)
                        else:
                            results.append(2)
            else:
                if x[568] <= 0.1392156892:
                    if x[551] <= 0.1392156929:
                        if x[188] <= 0.0176470596:
                            if x[207] <= 0.1294117719:
                                if x[686] <= 0.8941176534:
                                    results.append(4)
                                else:
                                    results.append(9)
                            else:
                                if x[546] <= 0.0274509806:
                                    results.append(9)
                                else:
                                    results.append(4)
                        else:
                            if x[576] <= 0.0156862754:
                                if x[457] <= 0.6686274707:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                results.append(4)
                    else:
                        if x[545] <= 0.2352941185:
                            if x[208] <= 0.2058823556:
                                results.append(4)
                            else:
                                if x[463] <= 0.2627450991:
                                    results.append(2)
                                else:
                                    results.append(9)
                        else:
                            if x[182] <= 0.2392156944:
                                results.append(6)
                            else:
                                results.append(2)
                else:
                    if x[603] <= 0.0215686280:
                        if x[157] <= 0.0117647061:
                            results.append(2)
                        else:
                            results.append(2)
                    else:
                        if x[325] <= 0.8647058904:
                            if x[573] <= 0.9803921580:
                                results.append(2)
                            else:
                                if x[629] <= 0.0215686280:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[242] <= 0.9607843161:
                                results.append(6)
                            else:
                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 7
    if time.time() < deadline or interrupt_flag.is_set():
        if x[154] <= 0.0058823533:
            if x[429] <= 0.0254901964:
                if x[465] <= 0.0372549035:
                    if x[350] <= 0.2098039240:
                        if x[415] <= 0.4431372583:
                            if x[405] <= 0.0647058859:
                                if x[268] <= 0.2588235326:
                                    results.append(5)
                                else:
                                    results.append(7)
                            else:
                                if x[318] <= 0.0176470596:
                                    results.append(1)
                                else:
                                    results.append(8)
                        else:
                            results.append(0)
                    else:
                        if x[347] <= 0.1901960829:
                            if x[206] <= 0.0921568656:
                                if x[161] <= 0.4745098203:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[543] <= 0.6098039299:
                                if x[491] <= 0.2725490332:
                                    results.append(5)
                                else:
                                    results.append(9)
                            else:
                                results.append(8)
                else:
                    if x[287] <= 0.0039215689:
                        if x[231] <= 0.0411764719:
                            if x[546] <= 0.7568627596:
                                if x[487] <= 0.0470588244:
                                    results.append(3)
                                else:
                                    results.append(6)
                            else:
                                if x[405] <= 0.1941176504:
                                    results.append(7)
                                else:
                                    results.append(9)
                        else:
                            if x[574] <= 0.6392157078:
                                results.append(7)
                            else:
                                results.append(7)
                    else:
                        if x[267] <= 0.1196078472:
                            if x[316] <= 0.1352941254:
                                results.append(3)
                            else:
                                results.append(9)
                        else:
                            if x[378] <= 0.5098039359:
                                results.append(7)
                            else:
                                results.append(5)
            else:
                if x[568] <= 0.0294117657:
                    if x[492] <= 0.0764705911:
                        if x[514] <= 0.1039215736:
                            if x[216] <= 0.2803921625:
                                if x[322] <= 0.9372549057:
                                    results.append(9)
                                else:
                                    results.append(3)
                            else:
                                if x[576] <= 0.0215686280:
                                    results.append(4)
                                else:
                                    results.append(5)
                        else:
                            if x[427] <= 0.0156862754:
                                results.append(6)
                            else:
                                results.append(5)
                    else:
                        if x[462] <= 0.8215686381:
                            if x[455] <= 0.5549019873:
                                if x[431] <= 0.1470588259:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[292] <= 0.8490196168:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[182] <= 0.0784313735:
                                if x[240] <= 0.2431372628:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[266] <= 0.7686274648:
                                    results.append(9)
                                else:
                                    results.append(5)
                else:
                    if x[454] <= 0.0901960805:
                        if x[269] <= 0.3666666746:
                            if x[243] <= 0.0333333351:
                                if x[344] <= 0.5352941193:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(8)
                        else:
                            if x[248] <= 0.0686274543:
                                if x[411] <= 0.0568627454:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(5)
                    else:
                        if x[354] <= 0.6098039448:
                            if x[538] <= 0.9882352948:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(2)
        else:
            if x[655] <= 0.1019607857:
                if x[185] <= 0.2156862766:
                    if x[318] <= 0.0196078438:
                        if x[485] <= 0.0156862754:
                            if x[182] <= 0.5000000149:
                                results.append(6)
                            else:
                                if x[630] <= 0.5745098144:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[631] <= 0.0352941193:
                                results.append(2)
                            else:
                                results.append(0)
                    else:
                        if x[263] <= 0.2705882490:
                            if x[349] <= 0.3764706030:
                                results.append(4)
                            else:
                                results.append(3)
                        else:
                            if x[261] <= 0.8745098114:
                                if x[324] <= 0.0117647061:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(6)
                else:
                    if x[436] <= 0.1019607857:
                        if x[461] <= 0.7392157018:
                            if x[322] <= 0.0235294122:
                                if x[158] <= 0.7137255073:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(5)
                        else:
                            results.append(2)
                    else:
                        if x[570] <= 0.0039215689:
                            if x[601] <= 0.1647058884:
                                results.append(4)
                            else:
                                results.append(8)
                        else:
                            if x[320] <= 0.6882353127:
                                if x[323] <= 0.6686274707:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                if x[215] <= 0.2549019754:
                                    results.append(6)
                                else:
                                    results.append(5)
            else:
                if x[428] <= 0.2568627521:
                    if x[291] <= 0.0392156877:
                        if x[494] <= 0.0215686280:
                            if x[569] <= 0.1117647067:
                                if x[152] <= 0.2313725501:
                                    results.append(1)
                                else:
                                    results.append(7)
                            else:
                                if x[629] <= 0.9137254953:
                                    results.append(8)
                                else:
                                    results.append(2)
                        else:
                            if x[514] <= 0.2470588274:
                                if x[269] <= 0.0117647061:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[547] <= 0.8686274588:
                                    results.append(8)
                                else:
                                    results.append(2)
                    else:
                        if x[355] <= 0.2627451122:
                            if x[511] <= 0.0941176489:
                                if x[401] <= 0.0784313753:
                                    results.append(8)
                                else:
                                    results.append(5)
                            else:
                                results.append(5)
                        else:
                            if x[412] <= 0.2000000048:
                                if x[435] <= 0.8392156959:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                if x[634] <= 0.2843137402:
                                    results.append(8)
                                else:
                                    results.append(3)
                else:
                    if x[567] <= 0.0058823531:
                        if x[235] <= 0.1137254909:
                            results.append(3)
                        else:
                            if x[512] <= 0.2745098099:
                                results.append(5)
                            else:
                                results.append(0)
                    else:
                        if x[301] <= 0.0039215689:
                            results.append(0)
                        else:
                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 8
    if time.time() < deadline or interrupt_flag.is_set():
        if x[551] <= 0.0019607844:
            if x[327] <= 0.0019607844:
                if x[437] <= 0.0058823531:
                    if x[290] <= 0.0529411770:
                        if x[373] <= 0.0941176489:
                            if x[685] <= 0.9235294163:
                                if x[349] <= 0.8215686381:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(5)
                    else:
                        if x[217] <= 0.0725490227:
                            if x[127] <= 0.0078431377:
                                if x[626] <= 0.0176470596:
                                    results.append(9)
                                else:
                                    results.append(8)
                            else:
                                results.append(1)
                        else:
                            if x[320] <= 0.0627451017:
                                results.append(0)
                            else:
                                results.append(5)
                else:
                    if x[260] <= 0.1843137294:
                        if x[514] <= 0.8078431487:
                            if x[464] <= 0.1980392188:
                                if x[179] <= 0.4058823660:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[437] <= 0.9941176474:
                                    results.append(9)
                                else:
                                    results.append(4)
                        else:
                            if x[512] <= 0.2098039240:
                                if x[520] <= 0.9176470637:
                                    results.append(8)
                                else:
                                    results.append(6)
                            else:
                                if x[243] <= 0.3764705956:
                                    results.append(2)
                                else:
                                    results.append(1)
                    else:
                        if x[401] <= 0.0568627454:
                            if x[239] <= 0.5333333462:
                                results.append(7)
                            else:
                                results.append(7)
                        else:
                            if x[324] <= 0.7568627596:
                                results.append(4)
                            else:
                                results.append(9)
            else:
                if x[155] <= 0.0196078434:
                    if x[373] <= 0.3431372643:
                        if x[711] <= 0.0294117650:
                            if x[740] <= 0.0745098069:
                                if x[376] <= 0.0019607844:
                                    results.append(7)
                                else:
                                    results.append(8)
                            else:
                                results.append(7)
                        else:
                            if x[433] <= 0.5000000149:
                                if x[244] <= 0.0196078438:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                results.append(3)
                    else:
                        if x[210] <= 0.0215686285:
                            if x[293] <= 0.8392156959:
                                if x[353] <= 0.9941176474:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[570] <= 0.1784313768:
                                    results.append(7)
                                else:
                                    results.append(5)
                        else:
                            if x[404] <= 0.0117647061:
                                if x[267] <= 0.3803921640:
                                    results.append(9)
                                else:
                                    results.append(7)
                            else:
                                if x[240] <= 0.4411764741:
                                    results.append(4)
                                else:
                                    results.append(9)
                else:
                    if x[515] <= 0.0921568647:
                        if x[456] <= 0.0156862754:
                            if x[375] <= 0.9901960790:
                                if x[319] <= 0.1058823559:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(4)
                        else:
                            if x[433] <= 0.1509803981:
                                if x[374] <= 0.9666666687:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(2)
                    else:
                        if x[442] <= 0.0078431377:
                            if x[488] <= 0.2490196154:
                                results.append(2)
                            else:
                                if x[124] <= 0.0117647066:
                                    results.append(8)
                                else:
                                    results.append(8)
                        else:
                            results.append(2)
        else:
            if x[657] <= 0.0254901969:
                if x[215] <= 0.0431372561:
                    if x[602] <= 0.0960784331:
                        if x[544] <= 0.2000000067:
                            if x[399] <= 0.3843137324:
                                if x[410] <= 0.7039215714:
                                    results.append(5)
                                else:
                                    results.append(7)
                            else:
                                if x[369] <= 0.0176470596:
                                    results.append(9)
                                else:
                                    results.append(9)
                        else:
                            if x[460] <= 0.8392156959:
                                results.append(6)
                            else:
                                if x[325] <= 0.2274509855:
                                    results.append(2)
                                else:
                                    results.append(2)
                    else:
                        if x[429] <= 0.2196078524:
                            if x[320] <= 0.3549019732:
                                if x[464] <= 0.4470588341:
                                    results.append(0)
                                else:
                                    results.append(2)
                            else:
                                results.append(6)
                        else:
                            if x[408] <= 0.0117647061:
                                if x[524] <= 0.6411764771:
                                    results.append(6)
                                else:
                                    results.append(2)
                            else:
                                if x[179] <= 0.9901960790:
                                    results.append(6)
                                else:
                                    results.append(6)
                else:
                    if x[398] <= 0.0156862754:
                        if x[152] <= 0.0549019631:
                            if x[517] <= 0.7980392277:
                                results.append(6)
                            else:
                                results.append(2)
                        else:
                            if x[488] <= 0.0274509806:
                                results.append(2)
                            else:
                                if x[489] <= 0.8254902065:
                                    results.append(2)
                                else:
                                    results.append(2)
                    else:
                        if x[431] <= 0.0156862754:
                            results.append(0)
                        else:
                            if x[513] <= 0.3745098114:
                                results.append(4)
                            else:
                                results.append(2)
            else:
                if x[407] <= 0.0019607844:
                    if x[352] <= 0.9509803951:
                        if x[462] <= 0.1803921610:
                            if x[455] <= 0.0372549035:
                                if x[242] <= 0.2215686329:
                                    results.append(3)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(5)
                    else:
                        if x[604] <= 0.8725490272:
                            results.append(3)
                        else:
                            if x[208] <= 0.8470588326:
                                results.append(5)
                            else:
                                results.append(5)
                else:
                    if x[543] <= 0.2098039240:
                        if x[296] <= 0.0196078434:
                            if x[353] <= 0.0078431377:
                                if x[293] <= 0.3823529556:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                if x[358] <= 0.3372549117:
                                    results.append(3)
                                else:
                                    results.append(8)
                        else:
                            if x[347] <= 0.0019607844:
                                if x[463] <= 0.8627451062:
                                    results.append(3)
                                else:
                                    results.append(8)
                            else:
                                if x[659] <= 0.9901960790:
                                    results.append(3)
                                else:
                                    results.append(3)
                    else:
                        if x[574] <= 0.5098039359:
                            if x[466] <= 0.0156862754:
                                results.append(8)
                            else:
                                if x[318] <= 0.5705882460:
                                    results.append(8)
                                else:
                                    results.append(8)
                        else:
                            if x[297] <= 0.6843137294:
                                if x[516] <= 0.0215686280:
                                    results.append(5)
                                else:
                                    results.append(4)
                            else:
                                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 9
    if time.time() < deadline or interrupt_flag.is_set():
        if x[377] <= 0.1666666716:
            if x[408] <= 0.0019607844:
                if x[329] <= 0.0078431377:
                    if x[97] <= 0.2098039240:
                        if x[154] <= 0.3372549117:
                            if x[431] <= 0.1196078435:
                                if x[327] <= 0.3921568692:
                                    results.append(5)
                                else:
                                    results.append(7)
                            else:
                                if x[654] <= 0.0196078434:
                                    results.append(4)
                                else:
                                    results.append(5)
                        else:
                            if x[323] <= 0.0274509815:
                                if x[627] <= 0.6254902184:
                                    results.append(6)
                                else:
                                    results.append(0)
                            else:
                                results.append(3)
                    else:
                        results.append(6)
                else:
                    if x[184] <= 0.0176470596:
                        if x[512] <= 0.0490196086:
                            if x[685] <= 0.1254902035:
                                results.append(7)
                            else:
                                results.append(7)
                        else:
                            results.append(0)
                    else:
                        if x[459] <= 0.8509804010:
                            if x[176] <= 0.3352941275:
                                results.append(0)
                            else:
                                if x[358] <= 0.6941176653:
                                    results.append(3)
                                else:
                                    results.append(0)
                        else:
                            results.append(2)
            else:
                if x[428] <= 0.0039215689:
                    if x[157] <= 0.0058823531:
                        if x[405] <= 0.0647058859:
                            if x[552] <= 0.2000000067:
                                if x[350] <= 0.1882352978:
                                    results.append(7)
                                else:
                                    results.append(1)
                            else:
                                results.append(9)
                        else:
                            if x[463] <= 0.9941176474:
                                if x[212] <= 0.2352941260:
                                    results.append(1)
                                else:
                                    results.append(9)
                            else:
                                results.append(4)
                    else:
                        if x[597] <= 0.3843137324:
                            if x[180] <= 0.0431372561:
                                if x[432] <= 0.1509803981:
                                    results.append(1)
                                else:
                                    results.append(4)
                            else:
                                results.append(8)
                        else:
                            if x[245] <= 0.5274509937:
                                if x[656] <= 0.3666666746:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                results.append(8)
                else:
                    if x[715] <= 0.0156862754:
                        if x[571] <= 0.4117647111:
                            if x[211] <= 0.0196078438:
                                if x[176] <= 0.3941176534:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[372] <= 0.0490196086:
                                    results.append(2)
                                else:
                                    results.append(9)
                        else:
                            if x[603] <= 0.0117647061:
                                if x[344] <= 0.0078431377:
                                    results.append(2)
                                else:
                                    results.append(4)
                            else:
                                if x[187] <= 0.9274509847:
                                    results.append(6)
                                else:
                                    results.append(2)
                    else:
                        if x[243] <= 0.9549019635:
                            results.append(9)
                        else:
                            results.append(9)
        else:
            if x[542] <= 0.1000000015:
                if x[551] <= 0.0078431377:
                    if x[430] <= 0.0196078438:
                        if x[465] <= 0.0156862754:
                            if x[403] <= 0.0960784331:
                                if x[376] <= 0.4450980574:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[324] <= 0.7431372702:
                                    results.append(8)
                                else:
                                    results.append(9)
                        else:
                            if x[151] <= 0.2666666806:
                                if x[376] <= 0.8000000119:
                                    results.append(3)
                                else:
                                    results.append(9)
                            else:
                                results.append(3)
                    else:
                        if x[538] <= 0.0411764719:
                            if x[239] <= 0.0725490227:
                                if x[323] <= 0.1039215699:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[209] <= 0.0039215689:
                                    results.append(4)
                                else:
                                    results.append(9)
                        else:
                            if x[269] <= 0.4333333373:
                                results.append(8)
                            else:
                                results.append(5)
                else:
                    if x[260] <= 0.7313725650:
                        if x[297] <= 0.1392156892:
                            if x[321] <= 0.3058823645:
                                if x[440] <= 0.0745098051:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                if x[214] <= 0.0725490227:
                                    results.append(3)
                                else:
                                    results.append(5)
                        else:
                            if x[290] <= 0.3039215729:
                                if x[347] <= 0.0019607844:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(8)
                    else:
                        if x[656] <= 0.4098039269:
                            if x[239] <= 0.4666666836:
                                results.append(4)
                            else:
                                results.append(8)
                        else:
                            if x[348] <= 0.7705882490:
                                results.append(3)
                            else:
                                results.append(5)
            else:
                if x[207] <= 0.0058823531:
                    if x[265] <= 0.2764705941:
                        if x[433] <= 0.9274509847:
                            if x[405] <= 0.5313725621:
                                results.append(3)
                            else:
                                results.append(8)
                        else:
                            if x[437] <= 0.0882352963:
                                if x[595] <= 0.1137254946:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                    else:
                        if x[658] <= 0.1274509840:
                            if x[566] <= 0.2607843168:
                                if x[487] <= 0.6098039448:
                                    results.append(5)
                                else:
                                    results.append(6)
                            else:
                                results.append(5)
                        else:
                            if x[466] <= 0.0294117648:
                                if x[518] <= 0.5176470727:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                if x[597] <= 0.9137254953:
                                    results.append(6)
                                else:
                                    results.append(8)
                else:
                    if x[511] <= 0.0862745121:
                        if x[270] <= 0.0117647061:
                            if x[684] <= 0.1843137294:
                                if x[543] <= 0.9862745106:
                                    results.append(5)
                                else:
                                    results.append(6)
                            else:
                                results.append(8)
                        else:
                            if x[175] <= 0.1294117663:
                                if x[488] <= 0.0490196086:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                    else:
                        if x[290] <= 0.8431372643:
                            if x[188] <= 0.7784313858:
                                results.append(2)
                            else:
                                results.append(5)
                        else:
                            if x[428] <= 0.7000000030:
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
