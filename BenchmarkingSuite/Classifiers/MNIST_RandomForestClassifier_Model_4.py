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
        if x[154] <= 0.0058823533:
            if x[400] <= 0.0019607844:
                if x[206] <= 0.0078431375:
                    if x[406] <= 0.5000000149:
                        if x[460] <= 0.0117647061:
                            if x[289] <= 0.0647058841:
                                results.append(5)
                            else:
                                if x[464] <= 0.0686274543:
                                    results.append(7)
                                else:
                                    results.append(7)
                        else:
                            if x[543] <= 0.1254901998:
                                if x[684] <= 0.1117647067:
                                    results.append(4)
                                else:
                                    results.append(0)
                            else:
                                results.append(6)
                    else:
                        if x[317] <= 0.0078431377:
                            if x[408] <= 0.9941176474:
                                if x[374] <= 0.3156862892:
                                    if x[134] <= 0.2019607872:
                                        if x[512] <= 0.0098039219:
                                            if x[632] <= 0.4058823586:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(5)
                            else:
                                if x[375] <= 0.5352941453:
                                    results.append(3)
                                else:
                                    results.append(9)
                        else:
                            if x[238] <= 0.3843137324:
                                results.append(8)
                            else:
                                if x[326] <= 0.0137254903:
                                    results.append(5)
                                else:
                                    if x[711] <= 0.1176470630:
                                        if x[185] <= 0.6058823764:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(9)
                else:
                    if x[519] <= 0.3843137324:
                        if x[656] <= 0.7607843280:
                            if x[403] <= 0.0313725509:
                                if x[466] <= 0.2823529541:
                                    if x[323] <= 0.1921568662:
                                        results.append(0)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[291] <= 0.2215686329:
                                    results.append(3)
                                else:
                                    results.append(4)
                        else:
                            results.append(5)
                    else:
                        if x[406] <= 0.5294117928:
                            if x[576] <= 0.7725490332:
                                if x[687] <= 0.7333333492:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                if x[602] <= 0.9803921580:
                                    results.append(4)
                                else:
                                    results.append(7)
                        else:
                            if x[260] <= 0.1254901963:
                                if x[492] <= 0.8019607961:
                                    results.append(4)
                                else:
                                    results.append(1)
                            else:
                                results.append(7)
            else:
                if x[326] <= 0.0274509815:
                    if x[653] <= 0.5313725770:
                        if x[300] <= 0.0352941193:
                            if x[514] <= 0.0294117648:
                                if x[409] <= 0.8705882430:
                                    if x[381] <= 0.0411764719:
                                        results.append(5)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(9)
                            else:
                                if x[411] <= 0.1313725561:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[598] <= 0.1254901998:
                                results.append(4)
                            else:
                                results.append(0)
                    else:
                        if x[548] <= 0.4705882519:
                            results.append(5)
                        else:
                            results.append(5)
                else:
                    if x[210] <= 0.0215686285:
                        if x[469] <= 0.8098039329:
                            if x[540] <= 0.6941176653:
                                if x[268] <= 0.9019607902:
                                    if x[322] <= 0.0588235306:
                                        if x[383] <= 0.9941176474:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[262] <= 0.9509803951:
                                        results.append(4)
                                    else:
                                        results.append(7)
                            else:
                                results.append(0)
                        else:
                            if x[471] <= 0.0078431377:
                                results.append(0)
                            else:
                                results.append(6)
                    else:
                        if x[379] <= 0.0254901964:
                            if x[468] <= 0.0666666706:
                                if x[434] <= 0.1509803981:
                                    if x[297] <= 0.2823529467:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(4)
                            else:
                                if x[466] <= 0.5960784554:
                                    results.append(0)
                                else:
                                    results.append(4)
                        else:
                            if x[350] <= 0.9686274529:
                                if x[381] <= 0.8137255013:
                                    results.append(9)
                                else:
                                    if x[384] <= 0.8411764801:
                                        if x[431] <= 0.1803921610:
                                            results.append(9)
                                        else:
                                            if x[490] <= 0.9901960790:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                    else:
                                        results.append(9)
                            else:
                                results.append(5)
        else:
            if x[514] <= 0.0843137279:
                if x[179] <= 0.2431372553:
                    if x[567] <= 0.0078431377:
                        if x[403] <= 0.4235294163:
                            if x[294] <= 0.1941176504:
                                results.append(2)
                            else:
                                if x[129] <= 0.2392156944:
                                    if x[491] <= 0.0568627464:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[657] <= 0.6823529601:
                                if x[661] <= 0.0647058859:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                results.append(5)
                    else:
                        if x[344] <= 0.0313725509:
                            if x[326] <= 0.0313725509:
                                if x[404] <= 0.6490196288:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                if x[349] <= 0.5098039359:
                                    results.append(2)
                                else:
                                    results.append(3)
                        else:
                            if x[323] <= 0.0352941193:
                                if x[566] <= 0.7235294282:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(3)
                else:
                    if x[483] <= 0.8000000119:
                        if x[518] <= 0.0588235315:
                            if x[298] <= 0.0098039221:
                                if x[295] <= 0.3333333433:
                                    if x[150] <= 0.0078431377:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    if x[325] <= 0.6666666716:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[576] <= 0.9901960790:
                                    if x[523] <= 0.9941176474:
                                        if x[628] <= 0.3725490272:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    if x[382] <= 0.7450980544:
                                        results.append(0)
                                    else:
                                        results.append(3)
                        else:
                            if x[659] <= 0.6725490391:
                                if x[297] <= 0.0941176489:
                                    results.append(1)
                                else:
                                    results.append(3)
                            else:
                                results.append(8)
                    else:
                        if x[565] <= 0.3568627611:
                            if x[375] <= 0.1000000015:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(2)
            else:
                if x[407] <= 0.0058823533:
                    if x[490] <= 0.0431372565:
                        if x[378] <= 0.8764705956:
                            if x[239] <= 0.0039215689:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(6)
                    else:
                        if x[100] <= 0.0490196091:
                            if x[462] <= 0.9333333373:
                                if x[374] <= 0.0039215689:
                                    results.append(2)
                                else:
                                    results.append(0)
                            else:
                                results.append(2)
                        else:
                            if x[349] <= 0.0333333351:
                                results.append(6)
                            else:
                                results.append(6)
                else:
                    if x[653] <= 0.2117647082:
                        if x[378] <= 0.9529411793:
                            if x[374] <= 0.4156862795:
                                if x[100] <= 0.6117647290:
                                    if x[659] <= 0.1196078439:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    if x[433] <= 0.9235294163:
                                        results.append(6)
                                    else:
                                        results.append(2)
                            else:
                                if x[296] <= 0.0058823531:
                                    if x[545] <= 0.0254901969:
                                        results.append(6)
                                    else:
                                        if x[545] <= 0.9882352948:
                                            results.append(6)
                                        else:
                                            results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[655] <= 0.0196078438:
                                if x[293] <= 0.0294117657:
                                    results.append(2)
                                else:
                                    if x[291] <= 0.8882353008:
                                        results.append(5)
                                    else:
                                        results.append(6)
                            else:
                                if x[517] <= 0.3647058904:
                                    if x[411] <= 0.1823529452:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(1)
                    else:
                        if x[353] <= 0.9901960790:
                            if x[405] <= 0.1352941245:
                                results.append(2)
                            else:
                                if x[523] <= 0.0862745130:
                                    results.append(8)
                                else:
                                    results.append(8)
                        else:
                            if x[160] <= 0.0568627454:
                                results.append(2)
                            else:
                                results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 1
    if time.time() < deadline or interrupt_flag.is_set():
        if x[485] <= 0.0039215689:
            if x[594] <= 0.0019607844:
                if x[378] <= 0.1176470630:
                    if x[268] <= 0.5352941453:
                        if x[299] <= 0.0921568647:
                            if x[545] <= 0.5509804189:
                                if x[298] <= 0.0137254903:
                                    if x[543] <= 0.1843137294:
                                        if x[438] <= 0.4509804100:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(6)
                                else:
                                    if x[463] <= 0.7156862915:
                                        results.append(9)
                                    else:
                                        results.append(4)
                            else:
                                if x[210] <= 0.9098039269:
                                    results.append(6)
                                else:
                                    results.append(8)
                        else:
                            if x[487] <= 0.0078431377:
                                if x[182] <= 0.7529411912:
                                    if x[218] <= 0.1529411767:
                                        if x[545] <= 0.9725490212:
                                            if x[402] <= 0.3588235378:
                                                results.append(7)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(8)
                            else:
                                if x[626] <= 0.5235294141:
                                    if x[409] <= 0.9686274529:
                                        results.append(9)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(8)
                    else:
                        if x[184] <= 0.0843137279:
                            if x[606] <= 0.3862745315:
                                if x[375] <= 0.2784313783:
                                    results.append(7)
                                else:
                                    results.append(4)
                            else:
                                if x[288] <= 0.8647058904:
                                    results.append(7)
                                else:
                                    results.append(7)
                        else:
                            if x[401] <= 0.0862745102:
                                results.append(7)
                            else:
                                if x[606] <= 0.0235294122:
                                    results.append(9)
                                else:
                                    results.append(3)
                else:
                    if x[290] <= 0.0019607844:
                        if x[208] <= 0.0176470596:
                            if x[466] <= 0.1823529452:
                                if x[459] <= 0.2921568751:
                                    if x[408] <= 0.3627451062:
                                        results.append(1)
                                    else:
                                        if x[573] <= 0.6156862825:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[436] <= 0.0372549035:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[627] <= 0.1431372613:
                                    results.append(4)
                                else:
                                    results.append(3)
                        else:
                            if x[292] <= 0.3176470697:
                                if x[289] <= 0.0098039219:
                                    if x[178] <= 0.4117647260:
                                        results.append(7)
                                    else:
                                        if x[350] <= 0.9117647111:
                                            if x[153] <= 0.7745098174:
                                                results.append(3)
                                            else:
                                                results.append(2)
                                        else:
                                            if x[438] <= 0.5117647201:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                else:
                                    results.append(9)
                            else:
                                if x[347] <= 0.0666666683:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[403] <= 0.4568627477:
                            if x[656] <= 0.6254902184:
                                if x[604] <= 0.4901960939:
                                    results.append(9)
                                else:
                                    results.append(2)
                            else:
                                if x[515] <= 0.0078431377:
                                    if x[374] <= 0.0980392210:
                                        results.append(1)
                                    else:
                                        results.append(5)
                                else:
                                    if x[182] <= 0.4529411942:
                                        results.append(8)
                                    else:
                                        results.append(8)
                        else:
                            if x[523] <= 0.6333333552:
                                if x[209] <= 0.1078431420:
                                    if x[320] <= 0.1352941208:
                                        if x[373] <= 0.9901960790:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(8)
                                else:
                                    if x[433] <= 0.9941176474:
                                        if x[603] <= 0.9901960790:
                                            if x[381] <= 0.5411764979:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(8)
                            else:
                                if x[435] <= 0.6235294342:
                                    if x[319] <= 0.7372549176:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(6)
            else:
                if x[344] <= 0.5666666925:
                    if x[490] <= 0.4705882370:
                        if x[247] <= 0.0078431377:
                            if x[236] <= 0.1274509840:
                                if x[635] <= 0.4313725680:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[298] <= 0.4274509884:
                                    if x[566] <= 0.5392157137:
                                        results.append(3)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(3)
                        else:
                            results.append(5)
                    else:
                        if x[215] <= 0.6411764920:
                            results.append(2)
                        else:
                            if x[299] <= 0.0039215689:
                                results.append(5)
                            else:
                                results.append(3)
                else:
                    if x[379] <= 0.0862745121:
                        if x[491] <= 0.3666666746:
                            if x[575] <= 0.0509803947:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[289] <= 0.8843137324:
                            results.append(5)
                        else:
                            results.append(5)
        else:
            if x[372] <= 0.0352941183:
                if x[207] <= 0.0196078443:
                    if x[122] <= 0.2039215751:
                        if x[374] <= 0.0039215689:
                            if x[269] <= 0.5745098293:
                                if x[457] <= 0.7156862915:
                                    results.append(8)
                                else:
                                    if x[544] <= 0.9254902005:
                                        results.append(2)
                                    else:
                                        results.append(2)
                            else:
                                if x[293] <= 0.0549019612:
                                    if x[159] <= 0.0392156886:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[572] <= 0.0098039219:
                                if x[459] <= 0.5784313977:
                                    results.append(3)
                                else:
                                    results.append(4)
                            else:
                                if x[271] <= 0.1098039225:
                                    if x[627] <= 0.0392156867:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    if x[602] <= 0.5901960880:
                                        results.append(4)
                                    else:
                                        results.append(0)
                    else:
                        if x[409] <= 0.0058823531:
                            results.append(2)
                        else:
                            results.append(2)
                else:
                    if x[655] <= 0.1078431420:
                        if x[544] <= 0.0039215689:
                            if x[458] <= 0.7058823705:
                                results.append(9)
                            else:
                                results.append(2)
                        else:
                            if x[242] <= 0.0627451017:
                                if x[183] <= 0.3882353008:
                                    results.append(6)
                                else:
                                    results.append(2)
                            else:
                                if x[430] <= 0.0019607844:
                                    results.append(2)
                                else:
                                    results.append(2)
                    else:
                        if x[291] <= 0.3098039329:
                            if x[150] <= 0.5745098144:
                                results.append(2)
                            else:
                                results.append(2)
                        else:
                            if x[211] <= 0.9823529422:
                                if x[377] <= 0.7607843280:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
            else:
                if x[407] <= 0.0196078438:
                    if x[568] <= 0.1000000015:
                        if x[385] <= 0.3862745166:
                            if x[488] <= 0.4176470637:
                                if x[602] <= 0.4117647111:
                                    results.append(7)
                                else:
                                    results.append(6)
                            else:
                                if x[440] <= 0.0411764719:
                                    results.append(5)
                                else:
                                    if x[342] <= 0.1352941208:
                                        results.append(4)
                                    else:
                                        results.append(4)
                        else:
                            results.append(0)
                    else:
                        if x[436] <= 0.2647058889:
                            if x[543] <= 0.9901960790:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(6)
                else:
                    if x[498] <= 0.0098039221:
                        if x[125] <= 0.0882352982:
                            if x[238] <= 0.0274509815:
                                if x[441] <= 0.2333333418:
                                    if x[490] <= 0.0098039219:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(6)
                            else:
                                if x[600] <= 0.9764705896:
                                    if x[598] <= 0.1470588297:
                                        if x[321] <= 0.0078431377:
                                            if x[410] <= 0.7294117808:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(8)
                                else:
                                    if x[435] <= 0.9764705896:
                                        results.append(6)
                                    else:
                                        results.append(4)
                        else:
                            if x[546] <= 0.9588235319:
                                results.append(6)
                            else:
                                results.append(6)
                    else:
                        if x[687] <= 0.2392156869:
                            if x[514] <= 0.0745098079:
                                results.append(8)
                            else:
                                if x[296] <= 0.2803921700:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            results.append(5)
    
    else:
      return vote_logic(results)
    
    # Tree 2
    if time.time() < deadline or interrupt_flag.is_set():
        if x[319] <= 0.0019607844:
            if x[317] <= 0.0058823531:
                if x[354] <= 0.0058823531:
                    if x[267] <= 0.0882352963:
                        if x[324] <= 0.1313725561:
                            if x[542] <= 0.8705882430:
                                if x[597] <= 0.2254901975:
                                    results.append(1)
                                else:
                                    results.append(0)
                            else:
                                results.append(2)
                        else:
                            if x[659] <= 0.0352941193:
                                if x[517] <= 0.1294117682:
                                    results.append(1)
                                else:
                                    results.append(5)
                            else:
                                if x[550] <= 0.5921568722:
                                    results.append(3)
                                else:
                                    results.append(3)
                    else:
                        if x[555] <= 0.0313725509:
                            if x[577] <= 0.1098039225:
                                if x[322] <= 0.1764705926:
                                    results.append(1)
                                else:
                                    if x[436] <= 0.8117647171:
                                        if x[569] <= 0.3607843295:
                                            if x[461] <= 0.2254902050:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[636] <= 0.0215686280:
                                    if x[600] <= 0.3254902065:
                                        results.append(1)
                                    else:
                                        if x[209] <= 0.0725490209:
                                            results.append(6)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(2)
                        else:
                            results.append(2)
                else:
                    if x[238] <= 0.3058823645:
                        if x[155] <= 0.1235294123:
                            if x[543] <= 0.9764705896:
                                if x[492] <= 0.6686274707:
                                    results.append(3)
                                else:
                                    results.append(6)
                            else:
                                results.append(1)
                        else:
                            if x[650] <= 0.0058823531:
                                if x[322] <= 0.1137254946:
                                    if x[630] <= 0.9588235319:
                                        if x[155] <= 0.4450980425:
                                            results.append(2)
                                        else:
                                            results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(3)
                            else:
                                if x[655] <= 0.9235294163:
                                    results.append(2)
                                else:
                                    results.append(3)
                    else:
                        if x[154] <= 0.0078431377:
                            if x[433] <= 0.5431372821:
                                if x[265] <= 0.0019607844:
                                    results.append(7)
                                else:
                                    if x[545] <= 0.0313725509:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[543] <= 0.0156862754:
                                    if x[381] <= 0.9901960790:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(1)
                        else:
                            if x[656] <= 0.0117647061:
                                if x[157] <= 0.9882352948:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                if x[208] <= 0.2941176519:
                                    results.append(8)
                                else:
                                    if x[185] <= 0.8117647171:
                                        results.append(3)
                                    else:
                                        results.append(3)
            else:
                if x[96] <= 0.0019607844:
                    if x[380] <= 0.0176470596:
                        if x[381] <= 0.0215686280:
                            if x[154] <= 0.0215686280:
                                results.append(0)
                            else:
                                if x[329] <= 0.4705882519:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(9)
                    else:
                        if x[209] <= 0.0117647061:
                            if x[410] <= 0.2882353067:
                                results.append(6)
                            else:
                                if x[519] <= 0.2019607872:
                                    results.append(4)
                                else:
                                    if x[343] <= 0.2549019679:
                                        results.append(4)
                                    else:
                                        results.append(4)
                        else:
                            if x[179] <= 0.1529411823:
                                if x[205] <= 0.0352941197:
                                    if x[438] <= 0.8901960850:
                                        results.append(9)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(9)
                            else:
                                if x[351] <= 0.0823529419:
                                    results.append(9)
                                else:
                                    results.append(8)
                else:
                    results.append(6)
        else:
            if x[468] <= 0.3058823645:
                if x[597] <= 0.0039215689:
                    if x[460] <= 0.0254901964:
                        if x[342] <= 0.1176470630:
                            if x[431] <= 0.1470588297:
                                if x[317] <= 0.2686274648:
                                    if x[494] <= 0.0882352963:
                                        if x[269] <= 0.5137255043:
                                            results.append(1)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(3)
                                else:
                                    if x[377] <= 0.2000000030:
                                        if x[239] <= 0.3215686306:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        if x[574] <= 0.3901960924:
                                            results.append(5)
                                        else:
                                            results.append(8)
                            else:
                                if x[210] <= 0.2568627521:
                                    if x[270] <= 0.9156862795:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[408] <= 0.9921568632:
                                        results.append(6)
                                    else:
                                        results.append(9)
                        else:
                            results.append(7)
                    else:
                        if x[378] <= 0.7980392277:
                            if x[353] <= 0.1137254946:
                                if x[354] <= 0.0117647061:
                                    if x[573] <= 0.1862745145:
                                        if x[658] <= 0.7254902124:
                                            results.append(4)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(6)
                                else:
                                    if x[400] <= 0.9862745106:
                                        results.append(9)
                                    else:
                                        results.append(4)
                            else:
                                if x[212] <= 0.0431372561:
                                    if x[215] <= 0.0549019622:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[371] <= 0.0627451017:
                                        if x[488] <= 0.6235294342:
                                            if x[299] <= 0.8450980484:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            if x[242] <= 0.3862745240:
                                                results.append(4)
                                            else:
                                                results.append(7)
                                    else:
                                        results.append(9)
                        else:
                            if x[401] <= 0.3529411852:
                                if x[379] <= 0.7450980544:
                                    results.append(1)
                                else:
                                    if x[380] <= 0.9941176474:
                                        if x[577] <= 0.5980392247:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                    else:
                                        results.append(9)
                            else:
                                if x[384] <= 0.1372549087:
                                    results.append(9)
                                else:
                                    results.append(4)
                else:
                    if x[686] <= 0.0039215689:
                        if x[327] <= 0.0039215689:
                            if x[460] <= 0.4411764741:
                                if x[549] <= 0.8431372643:
                                    if x[218] <= 0.2019607872:
                                        if x[627] <= 0.9901960790:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    if x[154] <= 0.6274510026:
                                        results.append(5)
                                    else:
                                        results.append(3)
                            else:
                                if x[548] <= 0.1490196139:
                                    results.append(8)
                                else:
                                    if x[217] <= 0.2549019679:
                                        results.append(6)
                                    else:
                                        results.append(5)
                        else:
                            if x[240] <= 0.9686274529:
                                if x[655] <= 0.0509803931:
                                    if x[494] <= 0.2666666731:
                                        if x[371] <= 0.0607843138:
                                            results.append(2)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(3)
                                else:
                                    if x[462] <= 0.1352941245:
                                        results.append(3)
                                    else:
                                        if x[318] <= 0.1019607857:
                                            results.append(8)
                                        else:
                                            if x[383] <= 0.7843137383:
                                                results.append(8)
                                            else:
                                                results.append(8)
                            else:
                                if x[213] <= 0.6980392337:
                                    results.append(7)
                                else:
                                    if x[156] <= 0.5588235408:
                                        results.append(0)
                                    else:
                                        results.append(2)
                    else:
                        if x[372] <= 0.2411764786:
                            if x[207] <= 0.9901960790:
                                if x[628] <= 0.9686274529:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                        else:
                            if x[324] <= 0.3254902139:
                                results.append(5)
                            else:
                                results.append(3)
            else:
                if x[216] <= 0.7098039389:
                    if x[99] <= 0.0019607844:
                        if x[456] <= 0.7549019754:
                            if x[180] <= 0.0058823531:
                                if x[231] <= 0.0588235299:
                                    if x[633] <= 0.0705882385:
                                        results.append(5)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(7)
                            else:
                                if x[235] <= 0.3117647097:
                                    if x[551] <= 0.6764706075:
                                        if x[605] <= 0.8098039329:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    if x[377] <= 0.0568627454:
                                        if x[516] <= 0.7549019754:
                                            results.append(0)
                                        else:
                                            results.append(6)
                                    else:
                                        if x[326] <= 0.2745098174:
                                            results.append(5)
                                        else:
                                            results.append(3)
                        else:
                            if x[271] <= 0.7568627596:
                                if x[569] <= 0.2627450991:
                                    results.append(0)
                                else:
                                    results.append(6)
                            else:
                                if x[209] <= 0.9627451003:
                                    results.append(4)
                                else:
                                    results.append(0)
                    else:
                        if x[440] <= 0.3372549117:
                            results.append(6)
                        else:
                            results.append(6)
                else:
                    if x[274] <= 0.0117647061:
                        if x[263] <= 0.6450980604:
                            results.append(3)
                        else:
                            if x[244] <= 0.9568627477:
                                results.append(5)
                            else:
                                results.append(0)
                    else:
                        if x[406] <= 0.2941176593:
                            if x[679] <= 0.1529411841:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 3
    if time.time() < deadline or interrupt_flag.is_set():
        if x[153] <= 0.0019607844:
            if x[465] <= 0.0098039221:
                if x[346] <= 0.0039215689:
                    if x[237] <= 0.2549019754:
                        if x[455] <= 0.4490196146:
                            if x[686] <= 0.1490196101:
                                if x[491] <= 0.5196078718:
                                    if x[434] <= 0.9568627477:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[184] <= 0.9098039269:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(6)
                    else:
                        if x[302] <= 0.1196078444:
                            if x[293] <= 0.7352941334:
                                if x[459] <= 0.0274509806:
                                    if x[573] <= 0.8803921640:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(3)
                            else:
                                if x[299] <= 0.0117647061:
                                    results.append(1)
                                else:
                                    results.append(8)
                        else:
                            if x[460] <= 0.0019607844:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[576] <= 0.0196078438:
                        if x[380] <= 0.1117647067:
                            results.append(5)
                        else:
                            if x[236] <= 0.1176470630:
                                if x[455] <= 0.0627451017:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[374] <= 0.8686274588:
                                    if x[599] <= 0.5254902095:
                                        results.append(9)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(4)
                    else:
                        if x[495] <= 0.0156862754:
                            if x[220] <= 0.0235294122:
                                if x[409] <= 0.1235294119:
                                    results.append(8)
                                else:
                                    results.append(4)
                            else:
                                results.append(5)
                        else:
                            if x[406] <= 0.3431372652:
                                if x[654] <= 0.1098039225:
                                    results.append(6)
                                else:
                                    results.append(0)
                            else:
                                results.append(6)
            else:
                if x[431] <= 0.0686274543:
                    if x[403] <= 0.1274509840:
                        if x[442] <= 0.3058823571:
                            if x[426] <= 0.0529411770:
                                if x[596] <= 0.6313725561:
                                    if x[263] <= 0.0196078438:
                                        results.append(7)
                                    else:
                                        if x[515] <= 0.7254902124:
                                            if x[580] <= 0.3431372643:
                                                results.append(7)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(3)
                            else:
                                if x[300] <= 0.3039215803:
                                    results.append(9)
                                else:
                                    results.append(7)
                        else:
                            if x[525] <= 0.0921568666:
                                results.append(0)
                            else:
                                results.append(6)
                    else:
                        if x[288] <= 0.5843137503:
                            if x[408] <= 0.9901960790:
                                if x[522] <= 0.7627451122:
                                    if x[625] <= 0.1803921610:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    if x[382] <= 0.3392156959:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                results.append(4)
                        else:
                            results.append(8)
                else:
                    if x[320] <= 0.5901961029:
                        if x[182] <= 0.0549019631:
                            if x[717] <= 0.4980392307:
                                if x[400] <= 0.3980392218:
                                    if x[265] <= 0.0784313735:
                                        if x[345] <= 0.1098039262:
                                            if x[461] <= 0.4254902005:
                                                results.append(5)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[215] <= 0.8470588326:
                                            results.append(9)
                                        else:
                                            results.append(3)
                                else:
                                    if x[713] <= 0.3901960924:
                                        if x[405] <= 0.8647058904:
                                            results.append(4)
                                        else:
                                            if x[186] <= 0.1666666716:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                    else:
                                        results.append(9)
                            else:
                                results.append(9)
                        else:
                            if x[409] <= 0.9509803951:
                                if x[652] <= 0.0882352963:
                                    if x[655] <= 0.1372549089:
                                        if x[206] <= 0.2627451010:
                                            if x[522] <= 0.0901960824:
                                                results.append(4)
                                            else:
                                                results.append(2)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(3)
                            else:
                                if x[236] <= 0.2529411837:
                                    results.append(4)
                                else:
                                    if x[515] <= 0.0784313735:
                                        if x[318] <= 0.0529411770:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(9)
                    else:
                        if x[491] <= 0.9901960790:
                            if x[355] <= 0.1235294119:
                                if x[626] <= 0.9098039269:
                                    if x[130] <= 0.0078431377:
                                        if x[210] <= 0.7235294282:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(5)
                            else:
                                if x[520] <= 0.7882353067:
                                    results.append(4)
                                else:
                                    results.append(0)
                        else:
                            if x[131] <= 0.1647058874:
                                if x[378] <= 0.3431372643:
                                    results.append(4)
                                else:
                                    results.append(9)
                            else:
                                results.append(6)
        else:
            if x[656] <= 0.2431372628:
                if x[597] <= 0.1666666716:
                    if x[468] <= 0.0058823531:
                        if x[574] <= 0.6117647290:
                            if x[541] <= 0.5745098293:
                                if x[296] <= 0.7176470757:
                                    results.append(4)
                                else:
                                    results.append(8)
                            else:
                                results.append(2)
                        else:
                            if x[543] <= 0.2745098174:
                                if x[349] <= 0.5803921819:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(6)
                    else:
                        if x[543] <= 0.0882352963:
                            results.append(4)
                        else:
                            if x[204] <= 0.0411764719:
                                if x[567] <= 0.0058823531:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(6)
                else:
                    if x[318] <= 0.4509803951:
                        if x[514] <= 0.2450980470:
                            if x[330] <= 0.2176470645:
                                if x[523] <= 0.6509804130:
                                    if x[410] <= 0.0333333341:
                                        results.append(4)
                                    else:
                                        if x[465] <= 0.3176470697:
                                            results.append(2)
                                        else:
                                            results.append(2)
                                else:
                                    results.append(3)
                            else:
                                results.append(0)
                        else:
                            results.append(2)
                    else:
                        if x[430] <= 0.3666666746:
                            results.append(3)
                        else:
                            results.append(6)
            else:
                if x[380] <= 0.0078431377:
                    if x[330] <= 0.0078431377:
                        if x[435] <= 0.0235294122:
                            if x[211] <= 0.4117647111:
                                if x[382] <= 0.6568627656:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[345] <= 0.0666666701:
                                    results.append(0)
                                else:
                                    if x[290] <= 0.9176470637:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            if x[523] <= 0.3176470702:
                                if x[153] <= 0.1960784346:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(3)
                    else:
                        if x[441] <= 0.1039215699:
                            results.append(4)
                        else:
                            results.append(0)
                else:
                    if x[460] <= 0.3235294223:
                        if x[290] <= 0.0254901974:
                            if x[354] <= 0.9901960790:
                                if x[573] <= 0.8117647171:
                                    if x[155] <= 0.9941176474:
                                        if x[578] <= 0.0352941193:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(3)
                        else:
                            if x[299] <= 0.0058823531:
                                if x[526] <= 0.0549019631:
                                    if x[268] <= 0.1921568662:
                                        results.append(5)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[624] <= 0.4411764890:
                                    results.append(8)
                                else:
                                    if x[291] <= 0.6450980604:
                                        results.append(3)
                                    else:
                                        results.append(3)
                    else:
                        if x[602] <= 0.9686274529:
                            if x[264] <= 0.0156862754:
                                if x[317] <= 0.3392156959:
                                    results.append(2)
                                else:
                                    if x[490] <= 0.1156862751:
                                        results.append(8)
                                    else:
                                        results.append(8)
                            else:
                                if x[379] <= 0.4509804100:
                                    results.append(8)
                                else:
                                    if x[514] <= 0.2313725576:
                                        results.append(8)
                                    else:
                                        results.append(8)
                        else:
                            if x[178] <= 0.6098039448:
                                if x[268] <= 0.4568627477:
                                    if x[594] <= 0.1294117719:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(1)
                            else:
                                results.append(3)
    
    else:
      return vote_logic(results)
    
    # Tree 4
    if time.time() < deadline or interrupt_flag.is_set():
        if x[155] <= 0.0098039219:
            if x[377] <= 0.0039215689:
                if x[429] <= 0.0058823531:
                    if x[468] <= 0.5313725621:
                        if x[514] <= 0.0803921605:
                            if x[354] <= 0.0117647061:
                                if x[212] <= 0.5764705986:
                                    results.append(1)
                                else:
                                    results.append(7)
                            else:
                                if x[266] <= 0.0274509806:
                                    results.append(7)
                                else:
                                    results.append(7)
                        else:
                            if x[209] <= 0.8411764801:
                                results.append(4)
                            else:
                                results.append(9)
                    else:
                        if x[414] <= 0.1000000015:
                            results.append(4)
                        else:
                            if x[293] <= 0.2098039240:
                                results.append(6)
                            else:
                                results.append(0)
                else:
                    if x[212] <= 0.0254901964:
                        if x[68] <= 0.0215686280:
                            if x[351] <= 0.3058823571:
                                if x[354] <= 0.0058823531:
                                    results.append(5)
                                else:
                                    if x[403] <= 0.0058823531:
                                        if x[324] <= 0.1098039225:
                                            if x[488] <= 0.9803921580:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(7)
                                    else:
                                        if x[573] <= 0.9941176474:
                                            results.append(4)
                                        else:
                                            results.append(4)
                            else:
                                results.append(9)
                        else:
                            results.append(6)
                    else:
                        if x[191] <= 0.0470588254:
                            if x[354] <= 0.0509803928:
                                if x[439] <= 0.2529411837:
                                    results.append(5)
                                else:
                                    results.append(2)
                            else:
                                if x[433] <= 0.2823529467:
                                    if x[429] <= 0.8607843220:
                                        results.append(7)
                                    else:
                                        results.append(0)
                                else:
                                    if x[431] <= 0.9450980425:
                                        results.append(9)
                                    else:
                                        if x[187] <= 0.0980392173:
                                            if x[428] <= 0.8843137324:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                        else:
                            results.append(5)
            else:
                if x[345] <= 0.0039215689:
                    if x[539] <= 0.0333333341:
                        if x[235] <= 0.0058823531:
                            if x[630] <= 0.6960784495:
                                if x[437] <= 0.3529411852:
                                    if x[520] <= 0.1529411785:
                                        if x[654] <= 0.0039215689:
                                            if x[433] <= 0.8529411852:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(6)
                            else:
                                if x[349] <= 0.5333333462:
                                    results.append(9)
                                else:
                                    results.append(1)
                        else:
                            if x[291] <= 0.5254902244:
                                if x[182] <= 0.0352941193:
                                    results.append(9)
                                else:
                                    if x[380] <= 0.7568627596:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[522] <= 0.0647058859:
                                    results.append(8)
                                else:
                                    results.append(5)
                    else:
                        if x[460] <= 0.4019607902:
                            results.append(5)
                        else:
                            if x[525] <= 0.4823529460:
                                if x[382] <= 0.1274509840:
                                    results.append(1)
                                else:
                                    results.append(8)
                            else:
                                results.append(2)
                else:
                    if x[190] <= 0.5666666925:
                        if x[209] <= 0.3431372643:
                            if x[598] <= 0.9882352948:
                                if x[552] <= 0.0450980403:
                                    if x[267] <= 0.0137254903:
                                        if x[317] <= 0.7882353067:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[438] <= 0.9372549057:
                                            results.append(5)
                                        else:
                                            results.append(4)
                                else:
                                    if x[486] <= 0.2156862840:
                                        results.append(3)
                                    else:
                                        results.append(6)
                            else:
                                results.append(5)
                        else:
                            if x[408] <= 0.5725490451:
                                if x[385] <= 0.4039215744:
                                    if x[628] <= 0.9470588267:
                                        results.append(2)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(6)
                            else:
                                if x[231] <= 0.2156862803:
                                    if x[597] <= 0.1078431392:
                                        if x[348] <= 0.4921568632:
                                            if x[575] <= 0.0705882385:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(3)
                    else:
                        if x[460] <= 0.2215686366:
                            results.append(5)
                        else:
                            results.append(8)
        else:
            if x[407] <= 0.0019607844:
                if x[330] <= 0.0529411770:
                    if x[345] <= 0.0176470596:
                        if x[657] <= 0.0215686280:
                            if x[350] <= 0.1862745136:
                                if x[625] <= 0.0411764719:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                if x[513] <= 0.1980392188:
                                    results.append(3)
                                else:
                                    results.append(2)
                        else:
                            if x[655] <= 0.2333333343:
                                results.append(1)
                            else:
                                if x[603] <= 0.5372549146:
                                    results.append(5)
                                else:
                                    if x[578] <= 0.3039215803:
                                        results.append(3)
                                    else:
                                        results.append(3)
                    else:
                        if x[244] <= 0.0078431377:
                            if x[214] <= 0.0372549035:
                                if x[597] <= 0.9039215744:
                                    if x[348] <= 0.5254902095:
                                        results.append(6)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[239] <= 0.8764705956:
                                    if x[208] <= 0.8745098114:
                                        results.append(8)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(0)
                        else:
                            if x[661] <= 0.1745098094:
                                if x[493] <= 0.9333333373:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[148] <= 0.0117647061:
                        if x[593] <= 0.9549019635:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(0)
            else:
                if x[514] <= 0.0568627454:
                    if x[625] <= 0.0490196086:
                        if x[605] <= 0.0862745121:
                            if x[465] <= 0.1254902035:
                                if x[436] <= 0.1941176504:
                                    results.append(1)
                                else:
                                    if x[575] <= 0.8764705956:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[456] <= 0.0764705911:
                                    results.append(3)
                                else:
                                    results.append(4)
                        else:
                            if x[373] <= 0.2745098174:
                                if x[488] <= 0.3941176608:
                                    results.append(3)
                                else:
                                    results.append(8)
                            else:
                                results.append(5)
                    else:
                        if x[296] <= 0.0294117657:
                            if x[353] <= 0.2274509817:
                                if x[606] <= 0.2470588246:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                if x[655] <= 0.0686274543:
                                    results.append(2)
                                else:
                                    if x[177] <= 0.5078431517:
                                        if x[655] <= 0.9901960790:
                                            results.append(8)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(3)
                        else:
                            if x[437] <= 0.0039215689:
                                results.append(3)
                            else:
                                if x[490] <= 0.4372549206:
                                    if x[346] <= 0.9803921580:
                                        if x[372] <= 0.1156862788:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(5)
                else:
                    if x[655] <= 0.1196078472:
                        if x[320] <= 0.0039215689:
                            if x[315] <= 0.0117647061:
                                if x[498] <= 0.9294117689:
                                    if x[379] <= 0.9941176474:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(6)
                        else:
                            if x[434] <= 0.1627451032:
                                results.append(8)
                            else:
                                if x[215] <= 0.5176470652:
                                    if x[318] <= 0.3274509907:
                                        if x[550] <= 0.6901960969:
                                            results.append(1)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(6)
                    else:
                        if x[439] <= 0.5215686560:
                            if x[492] <= 0.0019607844:
                                if x[188] <= 0.9215686321:
                                    if x[346] <= 0.0294117648:
                                        if x[607] <= 0.3196078539:
                                            results.append(1)
                                        else:
                                            results.append(2)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(8)
                            else:
                                if x[294] <= 0.3823529482:
                                    if x[601] <= 0.9803921580:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(3)
                        else:
                            if x[377] <= 0.9901960790:
                                results.append(5)
                            else:
                                results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 5
    if time.time() < deadline or interrupt_flag.is_set():
        if x[378] <= 0.6568627656:
            if x[595] <= 0.0098039219:
                if x[97] <= 0.0450980403:
                    if x[269] <= 0.9000000060:
                        if x[571] <= 0.5019607991:
                            if x[239] <= 0.1941176504:
                                if x[432] <= 0.3450980410:
                                    if x[461] <= 0.2411764748:
                                        if x[604] <= 0.3627451062:
                                            results.append(7)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[209] <= 0.1156862751:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                else:
                                    if x[634] <= 0.1352941245:
                                        if x[299] <= 0.0313725499:
                                            if x[457] <= 0.0039215689:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[287] <= 0.6215686500:
                                            results.append(5)
                                        else:
                                            results.append(4)
                            else:
                                if x[381] <= 0.0274509806:
                                    if x[468] <= 0.0039215689:
                                        if x[350] <= 0.0254901964:
                                            results.append(5)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    if x[266] <= 0.9607843161:
                                        if x[457] <= 0.0117647061:
                                            if x[243] <= 0.9725490212:
                                                results.append(9)
                                            else:
                                                results.append(7)
                                        else:
                                            if x[268] <= 0.9431372583:
                                                results.append(9)
                                            else:
                                                results.append(2)
                                    else:
                                        if x[434] <= 0.5196078569:
                                            results.append(7)
                                        else:
                                            results.append(4)
                        else:
                            if x[101] <= 0.0392156877:
                                if x[488] <= 0.4980392307:
                                    if x[652] <= 0.0019607844:
                                        if x[263] <= 0.0137254903:
                                            if x[271] <= 0.3313725609:
                                                results.append(3)
                                            else:
                                                results.append(6)
                                        else:
                                            if x[497] <= 0.0725490209:
                                                results.append(0)
                                            else:
                                                results.append(0)
                                    else:
                                        results.append(4)
                                else:
                                    if x[686] <= 0.0058823531:
                                        if x[655] <= 0.0627451017:
                                            results.append(2)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(8)
                            else:
                                if x[510] <= 0.1137254946:
                                    results.append(6)
                                else:
                                    results.append(6)
                    else:
                        if x[461] <= 0.0470588244:
                            if x[569] <= 0.1450980417:
                                if x[270] <= 0.8901960850:
                                    results.append(7)
                                else:
                                    if x[401] <= 0.6215686500:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                results.append(0)
                        else:
                            if x[627] <= 0.3764705956:
                                if x[188] <= 0.0176470596:
                                    if x[267] <= 0.1117647085:
                                        results.append(4)
                                    else:
                                        if x[401] <= 0.2843137383:
                                            results.append(3)
                                        else:
                                            if x[634] <= 0.1411764771:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                else:
                                    results.append(4)
                            else:
                                if x[266] <= 0.4705882519:
                                    if x[684] <= 0.3921568692:
                                        results.append(2)
                                    else:
                                        results.append(8)
                                else:
                                    if x[711] <= 0.2000000104:
                                        results.append(7)
                                    else:
                                        results.append(7)
                else:
                    if x[212] <= 0.0470588244:
                        if x[101] <= 0.0176470596:
                            results.append(6)
                        else:
                            results.append(2)
                    else:
                        results.append(2)
            else:
                if x[330] <= 0.3549019694:
                    if x[518] <= 0.0098039219:
                        if x[513] <= 0.0078431377:
                            if x[243] <= 0.1725490242:
                                if x[567] <= 0.4627451003:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[373] <= 0.3941176534:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[468] <= 0.3686274597:
                                results.append(5)
                            else:
                                results.append(0)
                    else:
                        if x[488] <= 0.0627450985:
                            if x[265] <= 0.4745098203:
                                if x[375] <= 0.2294117734:
                                    results.append(2)
                                else:
                                    results.append(5)
                            else:
                                if x[624] <= 0.5843137354:
                                    results.append(6)
                                else:
                                    results.append(0)
                        else:
                            if x[345] <= 0.2607843280:
                                results.append(2)
                            else:
                                results.append(2)
                else:
                    if x[599] <= 0.0176470596:
                        results.append(8)
                    else:
                        if x[381] <= 0.0509803947:
                            results.append(0)
                        else:
                            results.append(0)
        else:
            if x[206] <= 0.0019607844:
                if x[290] <= 0.0019607844:
                    if x[410] <= 0.2509803995:
                        if x[578] <= 0.1372549050:
                            if x[489] <= 0.1745098084:
                                if x[436] <= 0.0627450999:
                                    results.append(1)
                                else:
                                    if x[377] <= 0.8294117749:
                                        results.append(1)
                                    else:
                                        results.append(5)
                            else:
                                if x[134] <= 0.0156862754:
                                    if x[517] <= 0.1666666716:
                                        results.append(1)
                                    else:
                                        if x[326] <= 0.9862745106:
                                            if x[512] <= 0.0098039219:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[124] <= 0.7490196228:
                                if x[460] <= 0.2568627521:
                                    results.append(3)
                                else:
                                    results.append(6)
                            else:
                                results.append(2)
                    else:
                        if x[489] <= 0.1431372613:
                            if x[652] <= 0.0960784331:
                                if x[265] <= 0.4901960790:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                results.append(3)
                        else:
                            if x[299] <= 0.0686274543:
                                results.append(8)
                            else:
                                results.append(2)
                else:
                    if x[497] <= 0.0058823531:
                        if x[511] <= 0.3549019769:
                            if x[514] <= 0.0098039219:
                                if x[685] <= 0.3039215803:
                                    if x[515] <= 0.0098039219:
                                        if x[216] <= 0.4725490287:
                                            results.append(9)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(4)
                                else:
                                    if x[375] <= 0.8294117749:
                                        results.append(9)
                                    else:
                                        results.append(9)
                            else:
                                if x[325] <= 0.6294117868:
                                    results.append(8)
                                else:
                                    results.append(8)
                        else:
                            results.append(5)
                    else:
                        if x[323] <= 0.3901960850:
                            results.append(6)
                        else:
                            results.append(4)
            else:
                if x[489] <= 0.0470588244:
                    if x[187] <= 0.7117647231:
                        if x[492] <= 0.9862745106:
                            if x[316] <= 0.5862745196:
                                if x[457] <= 0.6137255132:
                                    if x[128] <= 0.9176470637:
                                        if x[597] <= 0.9941176474:
                                            if x[241] <= 0.3039215729:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(8)
                            else:
                                if x[630] <= 0.1627451051:
                                    results.append(9)
                                else:
                                    results.append(5)
                        else:
                            if x[403] <= 0.1823529452:
                                results.append(1)
                            else:
                                if x[372] <= 0.2509804070:
                                    results.append(8)
                                else:
                                    results.append(9)
                    else:
                        if x[261] <= 0.6705882549:
                            if x[265] <= 0.1411764771:
                                if x[375] <= 0.0686274543:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                results.append(5)
                        else:
                            if x[495] <= 0.8823529482:
                                results.append(5)
                            else:
                                if x[547] <= 0.0725490237:
                                    results.append(5)
                                else:
                                    results.append(3)
                else:
                    if x[511] <= 0.0784313753:
                        if x[685] <= 0.0254901964:
                            if x[546] <= 0.6666666865:
                                if x[521] <= 0.1176470593:
                                    results.append(2)
                                else:
                                    results.append(8)
                            else:
                                if x[354] <= 0.7529411912:
                                    results.append(4)
                                else:
                                    results.append(6)
                        else:
                            if x[375] <= 0.9862745106:
                                if x[543] <= 0.1568627506:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                    else:
                        if x[574] <= 0.7843137383:
                            if x[151] <= 0.0392156877:
                                results.append(2)
                            else:
                                results.append(2)
                        else:
                            results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 6
    if time.time() < deadline or interrupt_flag.is_set():
        if x[100] <= 0.0254901964:
            if x[354] <= 0.0039215689:
                if x[482] <= 0.0372549035:
                    if x[578] <= 0.0039215689:
                        if x[402] <= 0.0039215689:
                            if x[235] <= 0.0176470596:
                                if x[409] <= 0.0039215689:
                                    if x[350] <= 0.4588235319:
                                        if x[543] <= 0.6529411972:
                                            results.append(7)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[685] <= 0.8686274588:
                                            if x[323] <= 0.0725490232:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[376] <= 0.9529411793:
                                    if x[204] <= 0.0568627454:
                                        if x[495] <= 0.2607843205:
                                            results.append(1)
                                        else:
                                            results.append(2)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(8)
                        else:
                            if x[220] <= 0.0098039219:
                                if x[605] <= 0.0117647061:
                                    if x[685] <= 0.0137254903:
                                        if x[185] <= 0.4549019784:
                                            if x[236] <= 0.0352941183:
                                                results.append(5)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(6)
                                    else:
                                        if x[214] <= 0.1078431383:
                                            results.append(9)
                                        else:
                                            results.append(8)
                                else:
                                    if x[208] <= 0.0333333351:
                                        results.append(4)
                                    else:
                                        results.append(8)
                            else:
                                if x[318] <= 0.8490196168:
                                    results.append(5)
                                else:
                                    results.append(5)
                    else:
                        if x[652] <= 0.2862745225:
                            if x[514] <= 0.1000000015:
                                if x[151] <= 0.0509803947:
                                    if x[347] <= 0.0137254903:
                                        if x[577] <= 0.6039215922:
                                            results.append(5)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[294] <= 0.0372549035:
                                            if x[435] <= 0.1725490242:
                                                results.append(5)
                                            else:
                                                results.append(5)
                                        else:
                                            results.append(5)
                                else:
                                    if x[232] <= 0.2470588312:
                                        if x[522] <= 0.3705882430:
                                            results.append(1)
                                        else:
                                            if x[240] <= 0.1156862751:
                                                results.append(1)
                                            else:
                                                results.append(3)
                                    else:
                                        results.append(8)
                            else:
                                if x[244] <= 0.5901961029:
                                    if x[375] <= 0.4431372657:
                                        if x[655] <= 0.0627450999:
                                            results.append(2)
                                        else:
                                            results.append(2)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(8)
                        else:
                            if x[349] <= 0.8980392218:
                                results.append(5)
                            else:
                                if x[467] <= 0.9901960790:
                                    results.append(3)
                                else:
                                    results.append(3)
                else:
                    if x[436] <= 0.1764705889:
                        if x[399] <= 0.2529411912:
                            if x[625] <= 0.7235294282:
                                results.append(2)
                            else:
                                results.append(0)
                        else:
                            if x[538] <= 0.0254901964:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[466] <= 0.0803921595:
                            results.append(5)
                        else:
                            if x[434] <= 0.8117647171:
                                results.append(6)
                            else:
                                results.append(2)
            else:
                if x[433] <= 0.0254901964:
                    if x[153] <= 0.0215686280:
                        if x[155] <= 0.0058823531:
                            if x[398] <= 0.0843137279:
                                if x[485] <= 0.0294117648:
                                    if x[374] <= 0.0215686283:
                                        if x[323] <= 0.6862745285:
                                            if x[184] <= 0.6647059023:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        if x[210] <= 0.7549019754:
                                            if x[604] <= 0.0254901964:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                        else:
                                            results.append(5)
                                else:
                                    if x[237] <= 0.0921568647:
                                        results.append(6)
                                    else:
                                        if x[292] <= 0.0686274543:
                                            results.append(7)
                                        else:
                                            results.append(9)
                            else:
                                if x[401] <= 0.9000000060:
                                    if x[267] <= 0.8254902065:
                                        results.append(6)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(4)
                        else:
                            if x[606] <= 0.6039215773:
                                if x[463] <= 0.0176470596:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(4)
                    else:
                        if x[323] <= 0.1627451070:
                            if x[408] <= 0.1000000015:
                                if x[608] <= 0.1784313777:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[401] <= 0.1313725561:
                                    if x[491] <= 0.5529411808:
                                        results.append(3)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(6)
                        else:
                            if x[291] <= 0.0333333341:
                                if x[182] <= 0.5725490302:
                                    results.append(3)
                                else:
                                    if x[599] <= 0.8313725591:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[159] <= 0.6294117868:
                                    if x[551] <= 0.9176470637:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(5)
                else:
                    if x[155] <= 0.1823529452:
                        if x[240] <= 0.0019607844:
                            if x[414] <= 0.3764706105:
                                if x[437] <= 0.9235294163:
                                    if x[243] <= 0.9901960790:
                                        if x[570] <= 0.4509804100:
                                            if x[211] <= 0.4607843310:
                                                results.append(4)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(2)
                                    else:
                                        results.append(1)
                                else:
                                    if x[381] <= 0.9901960790:
                                        results.append(4)
                                    else:
                                        if x[462] <= 0.9647058845:
                                            results.append(4)
                                        else:
                                            results.append(4)
                            else:
                                results.append(6)
                        else:
                            if x[317] <= 0.0098039221:
                                if x[542] <= 0.0294117648:
                                    if x[594] <= 0.1450980455:
                                        if x[686] <= 0.9098039269:
                                            if x[214] <= 0.5784313977:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[430] <= 0.5098039284:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    if x[270] <= 0.9725490212:
                                        results.append(8)
                                    else:
                                        if x[323] <= 0.6823529601:
                                            results.append(7)
                                        else:
                                            results.append(1)
                            else:
                                if x[441] <= 0.4529411942:
                                    if x[247] <= 0.1843137303:
                                        if x[579] <= 0.4490196258:
                                            if x[377] <= 0.6372549236:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(6)
                    else:
                        if x[377] <= 0.2372549102:
                            if x[402] <= 0.2529411837:
                                if x[186] <= 0.8117647171:
                                    results.append(2)
                                else:
                                    if x[408] <= 0.8490196168:
                                        results.append(2)
                                    else:
                                        results.append(2)
                            else:
                                if x[577] <= 0.1019607857:
                                    results.append(8)
                                else:
                                    results.append(2)
                        else:
                            if x[514] <= 0.0176470596:
                                if x[271] <= 0.2294117659:
                                    if x[177] <= 0.4411764890:
                                        results.append(9)
                                    else:
                                        results.append(5)
                                else:
                                    if x[686] <= 0.3352941200:
                                        if x[215] <= 0.8588235378:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[411] <= 0.8019607961:
                                    if x[323] <= 0.7882353067:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(8)
        else:
            if x[346] <= 0.0215686280:
                if x[349] <= 0.5705882460:
                    if x[539] <= 0.0156862754:
                        results.append(2)
                    else:
                        results.append(2)
                else:
                    results.append(6)
            else:
                if x[538] <= 0.4960784391:
                    if x[410] <= 0.0254901964:
                        results.append(6)
                    else:
                        if x[462] <= 0.9941176474:
                            results.append(6)
                        else:
                            results.append(6)
                else:
                    results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 7
    if time.time() < deadline or interrupt_flag.is_set():
        if x[597] <= 0.0313725499:
            if x[373] <= 0.0490196086:
                if x[377] <= 0.0039215689:
                    if x[513] <= 0.0137254903:
                        if x[581] <= 0.0137254903:
                            if x[432] <= 0.1588235348:
                                if x[237] <= 0.0588235296:
                                    if x[433] <= 0.0137254903:
                                        if x[546] <= 0.0431372563:
                                            results.append(4)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(1)
                                else:
                                    if x[269] <= 0.2803921700:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[411] <= 0.0490196086:
                                    results.append(9)
                                else:
                                    results.append(7)
                        else:
                            results.append(3)
                    else:
                        if x[409] <= 0.0333333351:
                            results.append(0)
                        else:
                            if x[457] <= 0.8215686381:
                                if x[355] <= 0.1705882419:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[438] <= 0.7901960909:
                                    results.append(6)
                                else:
                                    results.append(4)
                else:
                    if x[350] <= 0.6156862974:
                        if x[348] <= 0.5176470727:
                            if x[291] <= 0.5058823675:
                                if x[455] <= 0.1666666716:
                                    if x[184] <= 0.0980392210:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(2)
                            else:
                                results.append(9)
                        else:
                            if x[326] <= 0.0549019617:
                                if x[655] <= 0.2196078449:
                                    results.append(6)
                                else:
                                    results.append(5)
                            else:
                                if x[516] <= 0.9294117689:
                                    results.append(8)
                                else:
                                    results.append(8)
                    else:
                        if x[493] <= 0.0176470596:
                            if x[514] <= 0.1901960820:
                                if x[262] <= 0.0647058859:
                                    if x[320] <= 0.5745098144:
                                        if x[435] <= 0.2294117734:
                                            if x[600] <= 0.1039215717:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(9)
                            else:
                                results.append(2)
                        else:
                            if x[544] <= 0.0176470596:
                                if x[268] <= 0.9745098054:
                                    if x[323] <= 0.8607843220:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(9)
                            else:
                                results.append(8)
            else:
                if x[544] <= 0.3647058904:
                    if x[353] <= 0.0235294122:
                        if x[413] <= 0.2647058889:
                            if x[212] <= 0.1372549087:
                                if x[404] <= 0.1156862751:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[461] <= 0.9823529422:
                                    if x[348] <= 0.7117647082:
                                        if x[399] <= 0.4784313887:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(9)
                        else:
                            results.append(0)
                    else:
                        if x[208] <= 0.0372549035:
                            if x[460] <= 0.0686274543:
                                if x[326] <= 0.9901960790:
                                    if x[237] <= 0.3725490272:
                                        results.append(4)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(7)
                            else:
                                if x[522] <= 0.0078431377:
                                    if x[483] <= 0.5490196198:
                                        if x[407] <= 0.6529411823:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[442] <= 0.0352941193:
                                if x[239] <= 0.1921568736:
                                    if x[154] <= 0.2862745114:
                                        if x[490] <= 0.0176470596:
                                            results.append(5)
                                        else:
                                            if x[547] <= 0.9568627477:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    if x[231] <= 0.2352941185:
                                        if x[572] <= 0.3431372643:
                                            if x[298] <= 0.0313725509:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(7)
                            else:
                                results.append(4)
                else:
                    if x[244] <= 0.0039215689:
                        if x[633] <= 0.9588235319:
                            if x[656] <= 0.0333333351:
                                if x[405] <= 0.7666666806:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(4)
                        else:
                            if x[548] <= 0.3235294223:
                                results.append(0)
                            else:
                                results.append(4)
                    else:
                        if x[626] <= 0.7411764860:
                            if x[428] <= 0.4058823586:
                                if x[409] <= 0.8313725591:
                                    results.append(9)
                                else:
                                    results.append(8)
                            else:
                                if x[655] <= 0.2901960909:
                                    results.append(2)
                                else:
                                    results.append(4)
                        else:
                            if x[570] <= 0.1803921647:
                                results.append(4)
                            else:
                                results.append(4)
        else:
            if x[441] <= 0.0921568647:
                if x[101] <= 0.0098039219:
                    if x[291] <= 0.0078431377:
                        if x[323] <= 0.6117647290:
                            if x[272] <= 0.9941176474:
                                if x[461] <= 0.9607843161:
                                    if x[513] <= 0.0137254903:
                                        if x[653] <= 0.8529411852:
                                            if x[567] <= 0.0078431377:
                                                results.append(3)
                                            else:
                                                results.append(5)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[382] <= 0.3372549042:
                                            results.append(2)
                                        else:
                                            results.append(2)
                                else:
                                    if x[630] <= 0.0725490227:
                                        results.append(1)
                                    else:
                                        if x[628] <= 0.9235294163:
                                            if x[345] <= 0.3039215803:
                                                results.append(8)
                                            else:
                                                results.append(8)
                                        else:
                                            results.append(2)
                            else:
                                results.append(6)
                        else:
                            if x[180] <= 0.0568627454:
                                if x[379] <= 0.8941176534:
                                    results.append(1)
                                else:
                                    if x[629] <= 0.0176470592:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[439] <= 0.0215686280:
                                    if x[270] <= 0.5392156914:
                                        results.append(2)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                    else:
                        if x[318] <= 0.3254902065:
                            if x[547] <= 0.4784313738:
                                if x[326] <= 0.0117647061:
                                    results.append(5)
                                else:
                                    if x[209] <= 0.5666666925:
                                        if x[460] <= 0.3803921640:
                                            results.append(7)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[485] <= 0.1274509877:
                                            results.append(3)
                                        else:
                                            results.append(8)
                            else:
                                if x[321] <= 0.1941176504:
                                    results.append(2)
                                else:
                                    if x[404] <= 0.5921568871:
                                        results.append(0)
                                    else:
                                        results.append(5)
                        else:
                            if x[406] <= 0.3509804010:
                                if x[242] <= 0.0372549025:
                                    if x[597] <= 0.9098039269:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    if x[327] <= 0.4058823586:
                                        results.append(3)
                                    else:
                                        if x[463] <= 0.4588235356:
                                            results.append(0)
                                        else:
                                            results.append(7)
                            else:
                                if x[486] <= 0.0019607844:
                                    if x[544] <= 0.5980392396:
                                        if x[270] <= 0.6411764920:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(8)
                                else:
                                    if x[656] <= 0.6941176653:
                                        if x[487] <= 0.2431372628:
                                            results.append(5)
                                        else:
                                            results.append(8)
                                    else:
                                        results.append(8)
                else:
                    if x[265] <= 0.0078431377:
                        results.append(2)
                    else:
                        if x[376] <= 0.5196078569:
                            results.append(0)
                        else:
                            results.append(6)
            else:
                if x[436] <= 0.1470588297:
                    if x[322] <= 0.5431372821:
                        if x[461] <= 0.2431372553:
                            if x[408] <= 0.0235294122:
                                if x[296] <= 0.3941176534:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(5)
                        else:
                            if x[373] <= 0.9000000060:
                                results.append(2)
                            else:
                                results.append(6)
                    else:
                        if x[159] <= 0.0313725495:
                            if x[235] <= 0.1607843190:
                                if x[597] <= 0.9568627477:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(0)
                        else:
                            results.append(5)
                else:
                    if x[292] <= 0.0078431377:
                        if x[604] <= 0.0294117648:
                            results.append(2)
                        else:
                            if x[207] <= 0.1274509840:
                                results.append(2)
                            else:
                                results.append(3)
                    else:
                        if x[246] <= 0.0803921595:
                            if x[207] <= 0.7607843280:
                                results.append(6)
                            else:
                                results.append(5)
                        else:
                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 8
    if time.time() < deadline or interrupt_flag.is_set():
        if x[346] <= 0.0078431375:
            if x[262] <= 0.0098039221:
                if x[568] <= 0.0568627473:
                    if x[409] <= 0.0137254903:
                        if x[663] <= 0.0392156877:
                            if x[271] <= 0.1117647067:
                                if x[177] <= 0.0411764719:
                                    if x[486] <= 0.3705882430:
                                        if x[520] <= 0.9039215744:
                                            if x[683] <= 0.4764706045:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(3)
                            else:
                                results.append(1)
                        else:
                            results.append(0)
                    else:
                        if x[544] <= 0.0313725509:
                            if x[652] <= 0.0549019612:
                                if x[436] <= 0.9941176474:
                                    if x[550] <= 0.1784313731:
                                        results.append(7)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(4)
                            else:
                                if x[300] <= 0.4764706045:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[215] <= 0.0254901964:
                                results.append(6)
                            else:
                                if x[434] <= 0.7960784435:
                                    results.append(7)
                                else:
                                    results.append(8)
                else:
                    if x[349] <= 0.0039215689:
                        if x[154] <= 0.0039215689:
                            results.append(1)
                        else:
                            if x[302] <= 0.1980392197:
                                if x[571] <= 0.0333333351:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(2)
                    else:
                        if x[264] <= 0.0176470596:
                            if x[434] <= 0.8372549117:
                                if x[151] <= 0.0705882385:
                                    results.append(6)
                                else:
                                    results.append(2)
                            else:
                                if x[213] <= 0.3039215803:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[515] <= 0.1078431383:
                                results.append(3)
                            else:
                                results.append(8)
            else:
                if x[712] <= 0.0058823531:
                    if x[541] <= 0.1843137294:
                        if x[656] <= 0.6666666865:
                            if x[370] <= 0.2274509892:
                                if x[551] <= 0.0078431377:
                                    if x[234] <= 0.8274509907:
                                        if x[299] <= 0.0352941193:
                                            results.append(1)
                                        else:
                                            results.append(7)
                                    else:
                                        if x[241] <= 0.3901960850:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                else:
                                    if x[544] <= 0.0411764719:
                                        results.append(4)
                                    else:
                                        results.append(2)
                            else:
                                if x[245] <= 0.2980392277:
                                    if x[460] <= 0.7431372702:
                                        results.append(9)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(0)
                        else:
                            if x[548] <= 0.0803921614:
                                results.append(8)
                            else:
                                if x[321] <= 0.1196078472:
                                    if x[211] <= 0.9509803951:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                    else:
                        if x[342] <= 0.2274509817:
                            if x[377] <= 0.5843137503:
                                if x[596] <= 0.4450980425:
                                    if x[214] <= 0.5588235334:
                                        results.append(6)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(2)
                            else:
                                if x[383] <= 0.2803921700:
                                    results.append(2)
                                else:
                                    results.append(8)
                        else:
                            if x[180] <= 0.4333333373:
                                results.append(8)
                            else:
                                if x[632] <= 0.9156862795:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[547] <= 0.0117647061:
                        results.append(3)
                    else:
                        if x[268] <= 0.1784313768:
                            results.append(7)
                        else:
                            if x[265] <= 0.4921568781:
                                results.append(7)
                            else:
                                if x[380] <= 0.9901960790:
                                    results.append(7)
                                else:
                                    results.append(7)
        else:
            if x[325] <= 0.0039215689:
                if x[215] <= 0.0039215689:
                    if x[573] <= 0.4117647111:
                        if x[517] <= 0.0352941193:
                            if x[401] <= 0.3549019769:
                                if x[323] <= 0.2568627596:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[380] <= 0.3431372643:
                                    results.append(0)
                                else:
                                    results.append(5)
                        else:
                            if x[299] <= 0.2039215788:
                                results.append(6)
                            else:
                                results.append(4)
                    else:
                        if x[426] <= 0.8686274588:
                            if x[489] <= 0.0411764719:
                                if x[627] <= 0.2294117659:
                                    results.append(6)
                                else:
                                    results.append(5)
                            else:
                                results.append(6)
                        else:
                            results.append(4)
                else:
                    if x[301] <= 0.1549019665:
                        if x[216] <= 0.0686274543:
                            if x[269] <= 0.0058823531:
                                results.append(5)
                            else:
                                if x[433] <= 0.0137254903:
                                    results.append(0)
                                else:
                                    results.append(3)
                        else:
                            if x[543] <= 0.5705882609:
                                if x[572] <= 0.9745098054:
                                    if x[240] <= 0.1078431383:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(6)
                    else:
                        if x[382] <= 0.9313725531:
                            if x[488] <= 0.1960784364:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[371] <= 0.0078431377:
                                if x[330] <= 0.2921568789:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(9)
            else:
                if x[350] <= 0.7509804070:
                    if x[542] <= 0.3019607961:
                        if x[433] <= 0.0137254903:
                            if x[429] <= 0.8058823645:
                                if x[269] <= 0.3019607887:
                                    if x[629] <= 0.6274509877:
                                        results.append(7)
                                    else:
                                        results.append(5)
                                else:
                                    if x[296] <= 0.1313725524:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                results.append(4)
                        else:
                            if x[209] <= 0.0039215689:
                                if x[320] <= 0.3411764801:
                                    if x[636] <= 0.0529411770:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[295] <= 0.6098039299:
                                        if x[544] <= 0.1333333347:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(5)
                            else:
                                if x[296] <= 0.0078431377:
                                    if x[490] <= 0.0098039219:
                                        results.append(9)
                                    else:
                                        if x[343] <= 0.4980392307:
                                            if x[402] <= 0.7607843280:
                                                results.append(8)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(9)
                                else:
                                    if x[581] <= 0.0529411770:
                                        if x[467] <= 0.1372549050:
                                            if x[381] <= 0.1784313777:
                                                results.append(3)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(8)
                    else:
                        if x[271] <= 0.0078431377:
                            if x[573] <= 0.2078431398:
                                results.append(8)
                            else:
                                if x[299] <= 0.1745098084:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[440] <= 0.2352941260:
                                if x[379] <= 0.1960784346:
                                    results.append(5)
                                else:
                                    if x[545] <= 0.4745098203:
                                        if x[410] <= 0.3176470697:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                    else:
                                        results.append(8)
                            else:
                                if x[358] <= 0.3607843295:
                                    results.append(0)
                                else:
                                    results.append(6)
                else:
                    if x[488] <= 0.0156862754:
                        if x[596] <= 0.0098039219:
                            if x[513] <= 0.0372549035:
                                if x[524] <= 0.1098039243:
                                    if x[263] <= 0.2156862803:
                                        results.append(7)
                                    else:
                                        if x[182] <= 0.6254902184:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(3)
                            else:
                                results.append(8)
                        else:
                            if x[323] <= 0.7019608021:
                                results.append(5)
                            else:
                                if x[289] <= 0.4431372732:
                                    if x[211] <= 0.1607843190:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(5)
                    else:
                        if x[270] <= 0.4078431427:
                            results.append(4)
                        else:
                            if x[158] <= 0.3705882505:
                                results.append(8)
                            else:
                                results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 9
    if time.time() < deadline or interrupt_flag.is_set():
        if x[461] <= 0.0176470596:
            if x[625] <= 0.0176470592:
                if x[740] <= 0.0450980403:
                    if x[570] <= 0.0372549025:
                        if x[679] <= 0.0529411770:
                            if x[377] <= 0.0333333351:
                                if x[630] <= 0.0058823531:
                                    if x[544] <= 0.7117647231:
                                        if x[237] <= 0.9529411793:
                                            if x[239] <= 0.5215686560:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(0)
                                else:
                                    if x[374] <= 0.0764705914:
                                        if x[519] <= 0.9941176474:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[385] <= 0.0960784350:
                                    if x[156] <= 0.0098039219:
                                        if x[523] <= 0.1392156929:
                                            if x[210] <= 0.0254901964:
                                                results.append(4)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(4)
                        else:
                            results.append(3)
                    else:
                        if x[270] <= 0.6882353127:
                            if x[323] <= 0.4529411942:
                                if x[601] <= 0.2568627596:
                                    results.append(7)
                                else:
                                    if x[551] <= 0.9549019635:
                                        if x[410] <= 0.8823529482:
                                            results.append(6)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(0)
                            else:
                                if x[320] <= 0.8098039329:
                                    results.append(5)
                                else:
                                    results.append(3)
                        else:
                            if x[206] <= 0.5058823824:
                                results.append(8)
                            else:
                                results.append(0)
                else:
                    if x[261] <= 0.1725490242:
                        results.append(7)
                    else:
                        results.append(7)
            else:
                if x[485] <= 0.0372549035:
                    if x[398] <= 0.1392156892:
                        if x[352] <= 0.6470588446:
                            if x[152] <= 0.1627451037:
                                if x[708] <= 0.4568627477:
                                    if x[217] <= 0.7019608021:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(7)
                            else:
                                if x[267] <= 0.3235294223:
                                    if x[270] <= 0.1686274558:
                                        if x[595] <= 0.1490196139:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[651] <= 0.0725490227:
                                if x[318] <= 0.8725490272:
                                    if x[655] <= 0.3647058904:
                                        results.append(3)
                                    else:
                                        if x[153] <= 0.4215686470:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(5)
                            else:
                                results.append(3)
                    else:
                        if x[409] <= 0.9568627477:
                            if x[427] <= 0.1980392262:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(5)
                else:
                    if x[517] <= 0.8176470697:
                        if x[329] <= 0.0176470596:
                            if x[597] <= 0.9725490212:
                                if x[318] <= 0.3882353082:
                                    results.append(2)
                                else:
                                    results.append(0)
                            else:
                                if x[352] <= 0.6098039448:
                                    results.append(5)
                                else:
                                    results.append(8)
                        else:
                            results.append(0)
                    else:
                        results.append(2)
        else:
            if x[457] <= 0.0019607844:
                if x[234] <= 0.0078431377:
                    if x[318] <= 0.0058823531:
                        if x[517] <= 0.0019607844:
                            if x[465] <= 0.3784313798:
                                results.append(3)
                            else:
                                results.append(3)
                        else:
                            if x[512] <= 0.0607843138:
                                if x[378] <= 0.4450980425:
                                    if x[153] <= 0.1568627506:
                                        results.append(8)
                                    else:
                                        results.append(6)
                                else:
                                    if x[320] <= 0.9333333373:
                                        if x[295] <= 0.1823529452:
                                            if x[353] <= 0.6058823615:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[125] <= 0.4843137413:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(8)
                            else:
                                results.append(2)
                    else:
                        if x[376] <= 0.8000000119:
                            if x[429] <= 0.0196078438:
                                if x[271] <= 0.7823529541:
                                    results.append(9)
                                else:
                                    results.append(7)
                            else:
                                if x[356] <= 0.2823529541:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[324] <= 0.1392156892:
                                results.append(5)
                            else:
                                results.append(8)
                else:
                    if x[346] <= 0.0039215689:
                        if x[127] <= 0.6000000238:
                            if x[403] <= 0.1117647067:
                                if x[241] <= 0.5196078569:
                                    if x[324] <= 0.3509803936:
                                        results.append(1)
                                    else:
                                        if x[431] <= 0.0921568647:
                                            results.append(8)
                                        else:
                                            results.append(2)
                                else:
                                    if x[186] <= 0.0843137261:
                                        if x[181] <= 0.0039215689:
                                            results.append(7)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(8)
                            else:
                                results.append(3)
                        else:
                            if x[188] <= 0.1764705926:
                                results.append(2)
                            else:
                                results.append(2)
                    else:
                        if x[515] <= 0.0980392173:
                            if x[606] <= 0.0607843157:
                                if x[243] <= 0.9901960790:
                                    if x[344] <= 0.1745098094:
                                        results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(7)
                            else:
                                results.append(8)
                        else:
                            if x[376] <= 0.1862745136:
                                results.append(8)
                            else:
                                results.append(8)
            else:
                if x[543] <= 0.3686274588:
                    if x[238] <= 0.1470588297:
                        if x[654] <= 0.2333333343:
                            if x[428] <= 0.8058823645:
                                if x[154] <= 0.0137254903:
                                    if x[260] <= 0.2529411837:
                                        if x[316] <= 0.0235294122:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(2)
                            else:
                                if x[572] <= 0.5450980514:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[207] <= 0.6411764920:
                                if x[240] <= 0.0745098069:
                                    results.append(4)
                                else:
                                    results.append(2)
                            else:
                                results.append(8)
                    else:
                        if x[541] <= 0.0274509806:
                            if x[326] <= 0.0254901964:
                                if x[191] <= 0.2568627521:
                                    if x[374] <= 0.1176470611:
                                        results.append(9)
                                    else:
                                        if x[207] <= 0.5019607991:
                                            results.append(4)
                                        else:
                                            results.append(5)
                                else:
                                    results.append(5)
                            else:
                                if x[407] <= 0.8254902065:
                                    if x[235] <= 0.2058823630:
                                        if x[186] <= 0.6450980604:
                                            results.append(4)
                                        else:
                                            results.append(2)
                                    else:
                                        if x[405] <= 0.0568627459:
                                            results.append(9)
                                        else:
                                            results.append(3)
                                else:
                                    if x[183] <= 0.9490196109:
                                        if x[355] <= 0.9803921580:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(9)
                        else:
                            if x[327] <= 0.0431372561:
                                if x[520] <= 0.3862745240:
                                    results.append(6)
                                else:
                                    results.append(7)
                            else:
                                if x[652] <= 0.8372549117:
                                    results.append(8)
                                else:
                                    results.append(8)
                else:
                    if x[345] <= 0.0058823531:
                        if x[348] <= 0.0274509806:
                            if x[510] <= 0.0117647061:
                                results.append(2)
                            else:
                                results.append(2)
                        else:
                            if x[381] <= 0.8627451062:
                                if x[517] <= 0.7039215863:
                                    results.append(6)
                                else:
                                    results.append(4)
                            else:
                                results.append(8)
                    else:
                        if x[246] <= 0.0039215689:
                            if x[609] <= 0.0098039219:
                                if x[300] <= 0.0392156877:
                                    if x[407] <= 0.9941176474:
                                        if x[495] <= 0.0725490232:
                                            results.append(6)
                                        else:
                                            results.append(6)
                                    else:
                                        if x[382] <= 0.9882352948:
                                            results.append(6)
                                        else:
                                            results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(6)
                        else:
                            results.append(4)
    
    else:
      return vote_logic(results)
    
    # Tree 10
    if time.time() < deadline or interrupt_flag.is_set():
        if x[386] <= 0.0294117657:
            if x[289] <= 0.0019607844:
                if x[178] <= 0.0019607844:
                    if x[522] <= 0.0137254908:
                        if x[438] <= 0.0078431377:
                            if x[292] <= 0.0235294122:
                                if x[235] <= 0.0588235296:
                                    if x[374] <= 0.0078431377:
                                        if x[604] <= 0.4803921729:
                                            if x[381] <= 0.0686274525:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(7)
                            else:
                                if x[157] <= 0.9196078479:
                                    if x[464] <= 0.0274509806:
                                        if x[213] <= 0.2470588274:
                                            if x[518] <= 0.9941176474:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(8)
                                    else:
                                        if x[374] <= 0.0274509806:
                                            if x[182] <= 0.8019607961:
                                                results.append(7)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[272] <= 0.1470588259:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                else:
                                    if x[627] <= 0.7784313858:
                                        results.append(8)
                                    else:
                                        if x[159] <= 0.0647058841:
                                            results.append(8)
                                        else:
                                            results.append(8)
                        else:
                            if x[407] <= 0.8647058904:
                                if x[606] <= 0.1411764771:
                                    if x[240] <= 0.4862745255:
                                        if x[401] <= 0.1549019627:
                                            results.append(2)
                                        else:
                                            if x[432] <= 0.5019607991:
                                                results.append(0)
                                            else:
                                                results.append(4)
                                    else:
                                        if x[601] <= 0.8431372643:
                                            results.append(7)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(6)
                            else:
                                results.append(9)
                    else:
                        if x[514] <= 0.1019607875:
                            if x[155] <= 0.3078431413:
                                if x[346] <= 0.0137254903:
                                    results.append(3)
                                else:
                                    if x[566] <= 0.0411764719:
                                        results.append(4)
                                    else:
                                        results.append(5)
                            else:
                                if x[349] <= 0.4058823660:
                                    results.append(2)
                                else:
                                    if x[380] <= 0.7921568751:
                                        if x[292] <= 0.9000000060:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(5)
                        else:
                            if x[215] <= 0.0725490209:
                                if x[241] <= 0.7000000179:
                                    if x[152] <= 0.0803921577:
                                        if x[520] <= 0.9901960790:
                                            results.append(6)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(2)
                            else:
                                if x[377] <= 0.8568627536:
                                    if x[509] <= 0.0705882385:
                                        results.append(0)
                                    else:
                                        results.append(2)
                                else:
                                    if x[598] <= 0.8156862855:
                                        results.append(8)
                                    else:
                                        results.append(5)
                else:
                    if x[513] <= 0.0411764719:
                        if x[544] <= 0.4294117838:
                            if x[629] <= 0.6764706075:
                                if x[376] <= 0.0254901964:
                                    if x[382] <= 0.4176470712:
                                        results.append(1)
                                    else:
                                        results.append(9)
                                else:
                                    if x[242] <= 0.0450980403:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[351] <= 0.2960784361:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[606] <= 0.9137254953:
                                if x[682] <= 0.2509804070:
                                    results.append(6)
                                else:
                                    results.append(7)
                            else:
                                results.append(2)
                    else:
                        if x[632] <= 0.3823529482:
                            if x[411] <= 0.9705882370:
                                if x[596] <= 0.0666666683:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(2)
                        else:
                            if x[186] <= 0.5823529661:
                                results.append(3)
                            else:
                                results.append(8)
            else:
                if x[406] <= 0.2333333343:
                    if x[596] <= 0.0313725499:
                        if x[403] <= 0.1235294156:
                            if x[184] <= 0.2823529467:
                                if x[524] <= 0.3568627536:
                                    if x[426] <= 0.0176470596:
                                        if x[407] <= 0.0431372561:
                                            if x[490] <= 0.2470588312:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                        else:
                                            if x[461] <= 0.5392157137:
                                                results.append(7)
                                            else:
                                                results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[577] <= 0.6705882400:
                                        results.append(5)
                                    else:
                                        results.append(6)
                            else:
                                if x[606] <= 0.1803921610:
                                    if x[517] <= 0.5823529661:
                                        results.append(9)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(4)
                        else:
                            if x[267] <= 0.9705882370:
                                if x[656] <= 0.8764705956:
                                    if x[244] <= 0.1803921610:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(5)
                            else:
                                results.append(7)
                    else:
                        if x[463] <= 0.7921568751:
                            if x[159] <= 0.0117647061:
                                results.append(0)
                            else:
                                if x[521] <= 0.8588235378:
                                    results.append(5)
                                else:
                                    results.append(0)
                        else:
                            results.append(2)
                else:
                    if x[542] <= 0.0254901964:
                        if x[189] <= 0.5294117928:
                            if x[348] <= 0.6568627656:
                                if x[235] <= 0.0392156877:
                                    if x[437] <= 0.8588235378:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[353] <= 0.0137254903:
                                        if x[212] <= 0.9725490212:
                                            results.append(5)
                                        else:
                                            results.append(8)
                                    else:
                                        if x[211] <= 0.0764705893:
                                            if x[352] <= 0.9901960790:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            if x[609] <= 0.0235294122:
                                                results.append(9)
                                            else:
                                                results.append(2)
                            else:
                                if x[322] <= 0.2254902050:
                                    results.append(5)
                                else:
                                    results.append(8)
                        else:
                            if x[518] <= 0.2117647119:
                                if x[240] <= 0.9333333373:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(4)
                    else:
                        if x[683] <= 0.0078431377:
                            if x[574] <= 0.0705882385:
                                if x[156] <= 0.0352941193:
                                    results.append(9)
                                else:
                                    if x[288] <= 0.7117647231:
                                        results.append(8)
                                    else:
                                        results.append(8)
                            else:
                                if x[568] <= 0.0274509806:
                                    results.append(6)
                                else:
                                    if x[209] <= 0.9901960790:
                                        results.append(5)
                                    else:
                                        results.append(2)
                        else:
                            if x[219] <= 0.1039215736:
                                if x[266] <= 0.9901960790:
                                    if x[179] <= 0.9745098054:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(5)
                            else:
                                results.append(5)
        else:
            if x[407] <= 0.0156862754:
                if x[399] <= 0.0705882357:
                    if x[469] <= 0.7588235438:
                        results.append(0)
                    else:
                        results.append(3)
                else:
                    if x[122] <= 0.0607843138:
                        if x[459] <= 0.3215686306:
                            if x[215] <= 0.0019607844:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(6)
            else:
                if x[498] <= 0.0078431377:
                    if x[567] <= 0.0784313753:
                        if x[430] <= 0.6274510026:
                            if x[259] <= 0.3098039329:
                                results.append(6)
                            else:
                                results.append(7)
                        else:
                            if x[601] <= 0.8509804010:
                                results.append(4)
                            else:
                                results.append(4)
                    else:
                        if x[625] <= 0.8686274588:
                            results.append(6)
                        else:
                            results.append(8)
                else:
                    if x[267] <= 0.4921568781:
                        if x[411] <= 0.9901960790:
                            results.append(6)
                        else:
                            results.append(6)
                    else:
                        results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 11
    if time.time() < deadline or interrupt_flag.is_set():
        if x[510] <= 0.2196078449:
            if x[657] <= 0.2274509817:
                if x[373] <= 0.0137254908:
                    if x[354] <= 0.0117647061:
                        if x[466] <= 0.0392156886:
                            if x[458] <= 0.3666666746:
                                if x[322] <= 0.0176470596:
                                    results.append(9)
                                else:
                                    if x[128] <= 0.8843137324:
                                        if x[489] <= 0.0078431377:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[520] <= 0.3156862780:
                                    results.append(6)
                                else:
                                    results.append(2)
                        else:
                            if x[375] <= 0.4137255102:
                                if x[602] <= 0.0411764719:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                results.append(6)
                    else:
                        if x[542] <= 0.4137254953:
                            if x[485] <= 0.0137254903:
                                if x[157] <= 0.1000000015:
                                    if x[432] <= 0.0980392173:
                                        if x[681] <= 0.5960784554:
                                            if x[152] <= 0.2509804070:
                                                results.append(7)
                                            else:
                                                results.append(2)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(3)
                            else:
                                if x[217] <= 0.2529411837:
                                    if x[342] <= 0.2215686329:
                                        if x[486] <= 0.7686274648:
                                            results.append(2)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[316] <= 0.1862745173:
                                            results.append(0)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(4)
                        else:
                            if x[350] <= 0.0098039219:
                                if x[428] <= 0.0725490227:
                                    if x[655] <= 0.3333333470:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(2)
                            else:
                                if x[184] <= 0.6607843190:
                                    if x[217] <= 0.4862745255:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(8)
                else:
                    if x[497] <= 0.0098039219:
                        if x[459] <= 0.0686274543:
                            if x[495] <= 0.2000000067:
                                if x[345] <= 0.9901960790:
                                    if x[379] <= 0.8490196168:
                                        if x[435] <= 0.8019607961:
                                            results.append(7)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(7)
                            else:
                                results.append(6)
                        else:
                            if x[543] <= 0.7960784435:
                                if x[232] <= 0.5843137503:
                                    if x[240] <= 0.0372549025:
                                        if x[208] <= 0.3196078539:
                                            if x[316] <= 0.4686274678:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            if x[264] <= 0.8196078539:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                    else:
                                        if x[403] <= 0.1058823541:
                                            if x[206] <= 0.1196078472:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            if x[520] <= 0.5705882460:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                else:
                                    if x[399] <= 0.4215686396:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                if x[242] <= 0.0254901964:
                                    results.append(6)
                                else:
                                    results.append(6)
                    else:
                        if x[243] <= 0.0352941193:
                            if x[544] <= 0.2411764786:
                                results.append(6)
                            else:
                                results.append(6)
                        else:
                            results.append(2)
            else:
                if x[578] <= 0.0862745121:
                    if x[430] <= 0.0058823531:
                        if x[270] <= 0.2823529541:
                            if x[436] <= 0.5803921819:
                                if x[520] <= 0.5411764830:
                                    if x[323] <= 0.9784313738:
                                        if x[489] <= 0.7372549176:
                                            results.append(7)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(3)
                            else:
                                if x[405] <= 0.7549019754:
                                    results.append(9)
                                else:
                                    if x[322] <= 0.0313725509:
                                        results.append(8)
                                    else:
                                        results.append(3)
                        else:
                            if x[624] <= 0.0352941195:
                                if x[488] <= 0.3725490272:
                                    if x[264] <= 0.1352941245:
                                        results.append(7)
                                    else:
                                        if x[264] <= 0.5705882609:
                                            results.append(7)
                                        else:
                                            if x[268] <= 0.3529411852:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                else:
                                    results.append(8)
                            else:
                                if x[623] <= 0.6196078658:
                                    results.append(8)
                                else:
                                    results.append(3)
                    else:
                        if x[182] <= 0.7666666806:
                            if x[237] <= 0.2509803995:
                                if x[541] <= 0.1098039243:
                                    if x[519] <= 0.7529411912:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(1)
                            else:
                                if x[188] <= 0.4627451003:
                                    if x[320] <= 0.9627451003:
                                        if x[658] <= 0.9901960790:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(5)
                        else:
                            if x[433] <= 0.0156862754:
                                results.append(5)
                            else:
                                if x[378] <= 0.7843137383:
                                    if x[382] <= 0.9000000060:
                                        results.append(9)
                                    else:
                                        results.append(8)
                                else:
                                    if x[547] <= 0.5176470727:
                                        results.append(8)
                                    else:
                                        results.append(8)
                else:
                    if x[262] <= 0.0372549035:
                        if x[287] <= 0.4803921729:
                            if x[462] <= 0.9803921580:
                                if x[293] <= 0.5294117928:
                                    if x[151] <= 0.5117647350:
                                        if x[375] <= 0.4431372732:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    if x[468] <= 0.2627451122:
                                        results.append(5)
                                    else:
                                        results.append(3)
                            else:
                                results.append(8)
                        else:
                            results.append(8)
                    else:
                        if x[298] <= 0.0117647061:
                            if x[268] <= 0.7901960909:
                                if x[605] <= 0.5784313977:
                                    results.append(8)
                                else:
                                    if x[659] <= 0.4784313887:
                                        results.append(5)
                                    else:
                                        if x[150] <= 0.7392157018:
                                            results.append(5)
                                        else:
                                            results.append(5)
                            else:
                                results.append(3)
                        else:
                            if x[456] <= 0.3000000119:
                                if x[317] <= 0.1960784346:
                                    if x[206] <= 0.5490196198:
                                        results.append(8)
                                    else:
                                        if x[318] <= 0.2862745151:
                                            if x[599] <= 0.4450980574:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(8)
                                else:
                                    if x[431] <= 0.1941176541:
                                        results.append(8)
                                    else:
                                        if x[375] <= 0.7411764860:
                                            results.append(8)
                                        else:
                                            results.append(8)
                            else:
                                if x[321] <= 0.7196078598:
                                    results.append(0)
                                else:
                                    results.append(0)
        else:
            if x[380] <= 0.1039215699:
                if x[434] <= 0.0686274543:
                    if x[213] <= 0.8647058904:
                        if x[387] <= 0.0941176489:
                            if x[129] <= 0.7294117808:
                                if x[268] <= 0.0254901964:
                                    results.append(0)
                                else:
                                    results.append(7)
                            else:
                                results.append(6)
                        else:
                            if x[210] <= 0.9215686321:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[204] <= 0.8333333433:
                            if x[149] <= 0.0450980412:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[320] <= 0.1352941189:
                        results.append(2)
                    else:
                        results.append(5)
            else:
                if x[456] <= 0.0039215689:
                    if x[571] <= 0.8254902065:
                        if x[292] <= 0.6137254983:
                            results.append(3)
                        else:
                            results.append(5)
                    else:
                        results.append(5)
                else:
                    if x[516] <= 0.0117647061:
                        if x[633] <= 0.2274509817:
                            if x[240] <= 0.2705882415:
                                results.append(4)
                            else:
                                results.append(4)
                        else:
                            results.append(8)
                    else:
                        if x[442] <= 0.9588235319:
                            if x[330] <= 0.0745098069:
                                if x[321] <= 0.0078431377:
                                    if x[547] <= 0.3764705956:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(4)
                            else:
                                results.append(8)
                        else:
                            results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 12
    if time.time() < deadline or interrupt_flag.is_set():
        if x[461] <= 0.0039215689:
            if x[350] <= 0.0372549035:
                if x[408] <= 0.1549019665:
                    if x[382] <= 0.9901960790:
                        if x[208] <= 0.0607843157:
                            if x[401] <= 0.1352941208:
                                results.append(7)
                            else:
                                if x[454] <= 0.1960784355:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[382] <= 0.8627451062:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[183] <= 0.2352941185:
                            results.append(7)
                        else:
                            results.append(0)
                else:
                    if x[261] <= 0.0921568666:
                        if x[269] <= 0.0098039219:
                            if x[522] <= 0.1745098103:
                                results.append(3)
                            else:
                                if x[355] <= 0.0372549035:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[573] <= 0.1000000034:
                                results.append(4)
                            else:
                                if x[183] <= 0.0686274543:
                                    results.append(5)
                                else:
                                    if x[542] <= 0.0568627459:
                                        results.append(7)
                                    else:
                                        results.append(2)
                    else:
                        if x[517] <= 0.1372549050:
                            if x[265] <= 0.5450980514:
                                if x[523] <= 0.2960784435:
                                    if x[353] <= 0.8490196168:
                                        results.append(5)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(6)
                            else:
                                if x[208] <= 0.1313725561:
                                    results.append(7)
                                else:
                                    results.append(7)
                        else:
                            results.append(7)
            else:
                if x[179] <= 0.0098039219:
                    if x[208] <= 0.0960784331:
                        if x[155] <= 0.5235294402:
                            if x[187] <= 0.0549019612:
                                if x[321] <= 0.9352941215:
                                    if x[245] <= 0.2274509817:
                                        results.append(9)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(7)
                            else:
                                if x[273] <= 0.2411764786:
                                    results.append(6)
                                else:
                                    results.append(0)
                        else:
                            if x[325] <= 0.8235294223:
                                if x[539] <= 0.0137254903:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                results.append(3)
                    else:
                        if x[602] <= 0.5196078569:
                            if x[270] <= 0.3196078464:
                                results.append(9)
                            else:
                                results.append(9)
                        else:
                            if x[327] <= 0.0372549035:
                                results.append(5)
                            else:
                                results.append(9)
                else:
                    if x[316] <= 0.4980392307:
                        if x[269] <= 0.0215686280:
                            if x[236] <= 0.9823529422:
                                if x[353] <= 0.0078431377:
                                    results.append(5)
                                else:
                                    if x[430] <= 0.5078431517:
                                        if x[354] <= 0.7058823705:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(8)
                            else:
                                results.append(5)
                        else:
                            if x[458] <= 0.6901960969:
                                results.append(3)
                            else:
                                results.append(8)
                    else:
                        if x[299] <= 0.0568627454:
                            if x[374] <= 0.9352941215:
                                results.append(5)
                            else:
                                results.append(5)
                        else:
                            if x[404] <= 0.6607843339:
                                results.append(0)
                            else:
                                results.append(9)
        else:
            if x[326] <= 0.0098039219:
                if x[430] <= 0.0274509806:
                    if x[522] <= 0.1627451032:
                        if x[483] <= 0.1039215699:
                            if x[347] <= 0.5392156988:
                                if x[325] <= 0.1078431420:
                                    results.append(1)
                                else:
                                    if x[432] <= 0.4647058845:
                                        if x[353] <= 0.1313725524:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(8)
                        else:
                            results.append(9)
                    else:
                        if x[157] <= 0.2411764786:
                            if x[350] <= 0.9862745106:
                                if x[465] <= 0.3509804010:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                results.append(8)
                        else:
                            results.append(6)
                else:
                    if x[439] <= 0.0078431377:
                        if x[524] <= 0.3215686381:
                            if x[485] <= 0.4235294312:
                                if x[218] <= 0.0078431377:
                                    if x[543] <= 0.0470588244:
                                        if x[264] <= 0.0647058832:
                                            results.append(3)
                                        else:
                                            if x[296] <= 0.2000000030:
                                                results.append(5)
                                            else:
                                                results.append(9)
                                    else:
                                        if x[243] <= 0.0941176489:
                                            results.append(6)
                                        else:
                                            results.append(8)
                                else:
                                    if x[492] <= 0.8725490272:
                                        results.append(5)
                                    else:
                                        results.append(5)
                            else:
                                results.append(6)
                        else:
                            if x[263] <= 0.0019607844:
                                results.append(2)
                            else:
                                results.append(2)
                    else:
                        if x[571] <= 0.0176470596:
                            if x[509] <= 0.2921568751:
                                if x[318] <= 0.2941176593:
                                    results.append(4)
                                else:
                                    results.append(6)
                            else:
                                results.append(2)
                        else:
                            if x[347] <= 0.0803921595:
                                results.append(2)
                            else:
                                if x[207] <= 0.8156862855:
                                    if x[626] <= 0.4549019784:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(6)
            else:
                if x[399] <= 0.0117647061:
                    if x[375] <= 0.0058823531:
                        if x[125] <= 0.0313725499:
                            if x[514] <= 0.0588235315:
                                if x[460] <= 0.0843137279:
                                    if x[433] <= 0.1372549096:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    if x[430] <= 0.9058823586:
                                        if x[409] <= 0.7078431547:
                                            results.append(3)
                                        else:
                                            results.append(7)
                                    else:
                                        if x[405] <= 0.1960784420:
                                            results.append(9)
                                        else:
                                            results.append(9)
                            else:
                                if x[378] <= 0.6882353127:
                                    if x[237] <= 0.9745098054:
                                        if x[517] <= 0.9529411793:
                                            results.append(2)
                                        else:
                                            results.append(2)
                                    else:
                                        results.append(7)
                                else:
                                    if x[658] <= 0.0431372561:
                                        if x[595] <= 0.7509804070:
                                            if x[513] <= 0.1901960820:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[625] <= 0.0980392173:
                                            results.append(3)
                                        else:
                                            results.append(8)
                        else:
                            if x[656] <= 0.4333333522:
                                if x[437] <= 0.1686274596:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(8)
                    else:
                        if x[514] <= 0.0137254903:
                            if x[183] <= 0.3333333433:
                                if x[211] <= 0.1823529471:
                                    if x[187] <= 0.6411764920:
                                        if x[490] <= 0.7745098174:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(9)
                            else:
                                if x[516] <= 0.7392157018:
                                    if x[546] <= 0.1117647067:
                                        if x[653] <= 0.5803921670:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[322] <= 0.2666666731:
                                            if x[490] <= 0.9941176474:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(8)
                        else:
                            if x[99] <= 0.0039215689:
                                if x[265] <= 0.9803921580:
                                    if x[484] <= 0.0686274515:
                                        results.append(8)
                                    else:
                                        if x[320] <= 0.3647058830:
                                            results.append(2)
                                        else:
                                            if x[404] <= 0.9862745106:
                                                results.append(4)
                                            else:
                                                results.append(8)
                                else:
                                    if x[267] <= 0.0588235315:
                                        results.append(4)
                                    else:
                                        results.append(8)
                            else:
                                results.append(6)
                else:
                    if x[210] <= 0.0196078443:
                        if x[600] <= 0.6235294342:
                            if x[515] <= 0.7607843280:
                                results.append(4)
                            else:
                                results.append(4)
                        else:
                            if x[492] <= 0.6725490391:
                                if x[574] <= 0.6627451181:
                                    results.append(4)
                                else:
                                    results.append(6)
                            else:
                                results.append(4)
                    else:
                        if x[543] <= 0.6470588446:
                            if x[573] <= 0.9882352948:
                                if x[469] <= 0.1333333403:
                                    if x[516] <= 0.1039215736:
                                        results.append(9)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(4)
                            else:
                                if x[544] <= 0.5450980663:
                                    results.append(4)
                                else:
                                    results.append(9)
                        else:
                            if x[271] <= 0.0254901964:
                                results.append(6)
                            else:
                                results.append(7)
    
    else:
      return vote_logic(results)
    
    # Tree 13
    if time.time() < deadline or interrupt_flag.is_set():
        if x[378] <= 0.4450980425:
            if x[597] <= 0.2960784435:
                if x[429] <= 0.0333333351:
                    if x[348] <= 0.2392156944:
                        if x[552] <= 0.0078431377:
                            if x[187] <= 0.0254901964:
                                if x[237] <= 0.0039215689:
                                    if x[323] <= 0.2666666824:
                                        results.append(2)
                                    else:
                                        results.append(7)
                                else:
                                    if x[488] <= 0.2960784435:
                                        if x[262] <= 0.2019607872:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[271] <= 0.3215686381:
                                    if x[208] <= 0.0509803947:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[293] <= 0.0098039219:
                                        results.append(8)
                                    else:
                                        results.append(7)
                        else:
                            if x[344] <= 0.6588235497:
                                results.append(3)
                            else:
                                results.append(0)
                    else:
                        if x[186] <= 0.4431372583:
                            if x[271] <= 0.0098039219:
                                if x[213] <= 0.0882352963:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                if x[207] <= 0.0215686280:
                                    results.append(7)
                                else:
                                    results.append(8)
                        else:
                            if x[546] <= 0.0509803928:
                                results.append(5)
                            else:
                                results.append(8)
                else:
                    if x[211] <= 0.0098039219:
                        if x[243] <= 0.0117647061:
                            if x[574] <= 0.0098039219:
                                if x[689] <= 0.1254902035:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[404] <= 0.0392156881:
                                    if x[151] <= 0.0352941193:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(4)
                        else:
                            if x[296] <= 0.1686274558:
                                if x[185] <= 0.1607843190:
                                    results.append(4)
                                else:
                                    if x[490] <= 0.7490196228:
                                        results.append(4)
                                    else:
                                        results.append(2)
                            else:
                                results.append(7)
                    else:
                        if x[468] <= 0.0313725499:
                            if x[406] <= 0.1450980455:
                                if x[465] <= 0.1686274521:
                                    results.append(5)
                                else:
                                    if x[208] <= 0.0078431377:
                                        if x[355] <= 0.0784313753:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[260] <= 0.0235294122:
                                            results.append(9)
                                        else:
                                            results.append(7)
                            else:
                                if x[190] <= 0.0333333351:
                                    if x[433] <= 0.6843137443:
                                        results.append(9)
                                    else:
                                        if x[599] <= 0.5039215833:
                                            if x[661] <= 0.9588235319:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(5)
                        else:
                            if x[101] <= 0.0882352963:
                                if x[437] <= 0.6647059023:
                                    if x[511] <= 0.2000000030:
                                        results.append(5)
                                    else:
                                        results.append(0)
                                else:
                                    if x[263] <= 0.7196078598:
                                        results.append(4)
                                    else:
                                        results.append(7)
                            else:
                                results.append(6)
            else:
                if x[462] <= 0.0098039219:
                    if x[358] <= 0.0039215689:
                        if x[486] <= 0.0254901964:
                            if x[427] <= 0.0588235296:
                                if x[127] <= 0.5019607991:
                                    results.append(5)
                                else:
                                    results.append(3)
                            else:
                                results.append(0)
                        else:
                            if x[323] <= 0.0529411780:
                                if x[385] <= 0.1392156929:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(5)
                    else:
                        if x[209] <= 0.0156862754:
                            results.append(0)
                        else:
                            if x[186] <= 0.0176470596:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[292] <= 0.0431372561:
                        if x[152] <= 0.5529412031:
                            if x[485] <= 0.0098039219:
                                if x[579] <= 0.1490196157:
                                    results.append(1)
                                else:
                                    results.append(2)
                            else:
                                if x[539] <= 0.6039215922:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            results.append(2)
                    else:
                        if x[625] <= 0.0686274548:
                            if x[523] <= 0.2764706016:
                                results.append(6)
                            else:
                                results.append(6)
                        else:
                            if x[541] <= 0.0176470596:
                                results.append(4)
                            else:
                                if x[628] <= 0.6509804130:
                                    if x[409] <= 0.9627451003:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    if x[321] <= 0.1078431420:
                                        results.append(8)
                                    else:
                                        results.append(6)
        else:
            if x[461] <= 0.3039215803:
                if x[290] <= 0.0941176489:
                    if x[427] <= 0.4745098203:
                        if x[219] <= 0.0274509806:
                            if x[518] <= 0.2549019679:
                                if x[296] <= 0.1529411823:
                                    if x[344] <= 0.0431372561:
                                        if x[320] <= 0.1117647067:
                                            if x[624] <= 0.5235294178:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(8)
                                    else:
                                        results.append(5)
                                else:
                                    if x[580] <= 0.9862745106:
                                        if x[494] <= 0.6058823764:
                                            if x[406] <= 0.5823529512:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[570] <= 0.5666666776:
                                    if x[490] <= 0.7705882490:
                                        results.append(9)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(3)
                        else:
                            results.append(5)
                    else:
                        if x[258] <= 0.1882352978:
                            results.append(2)
                        else:
                            results.append(4)
                else:
                    if x[187] <= 0.2941176593:
                        if x[607] <= 0.0176470596:
                            if x[205] <= 0.3549019694:
                                if x[212] <= 0.5431372672:
                                    if x[596] <= 0.3176470734:
                                        results.append(6)
                                    else:
                                        results.append(5)
                                else:
                                    if x[236] <= 0.1725490242:
                                        results.append(9)
                                    else:
                                        results.append(9)
                            else:
                                results.append(4)
                        else:
                            if x[485] <= 0.1784313768:
                                if x[344] <= 0.7921568751:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                results.append(8)
                    else:
                        if x[355] <= 0.1196078435:
                            if x[684] <= 0.2862745225:
                                results.append(5)
                            else:
                                results.append(5)
                        else:
                            if x[651] <= 0.0431372570:
                                if x[348] <= 0.9823529422:
                                    results.append(4)
                                else:
                                    results.append(5)
                            else:
                                results.append(3)
            else:
                if x[577] <= 0.0039215689:
                    if x[465] <= 0.0019607844:
                        if x[264] <= 0.4941176623:
                            if x[660] <= 0.7156862915:
                                if x[512] <= 0.0098039219:
                                    if x[380] <= 0.9901960790:
                                        if x[435] <= 0.5862745345:
                                            if x[574] <= 0.3960784376:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[511] <= 0.0294117648:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(2)
                        else:
                            if x[574] <= 0.4254902005:
                                results.append(4)
                            else:
                                if x[379] <= 0.9764705896:
                                    results.append(8)
                                else:
                                    results.append(8)
                    else:
                        if x[517] <= 0.3529411852:
                            if x[628] <= 0.8117647171:
                                results.append(9)
                            else:
                                results.append(3)
                        else:
                            if x[486] <= 0.9921568632:
                                results.append(2)
                            else:
                                results.append(6)
                else:
                    if x[101] <= 0.0431372561:
                        if x[657] <= 0.7941176593:
                            if x[459] <= 0.1294117719:
                                if x[318] <= 0.2784313783:
                                    if x[238] <= 0.1333333347:
                                        results.append(3)
                                    else:
                                        if x[376] <= 0.0686274515:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(0)
                            else:
                                if x[181] <= 0.2666666806:
                                    if x[543] <= 0.0137254903:
                                        results.append(4)
                                    else:
                                        results.append(6)
                                else:
                                    if x[344] <= 0.4980392307:
                                        if x[551] <= 0.2372549102:
                                            if x[377] <= 0.5764705986:
                                                results.append(2)
                                            else:
                                                results.append(8)
                                        else:
                                            if x[551] <= 0.8470588326:
                                                results.append(2)
                                            else:
                                                results.append(2)
                                    else:
                                        results.append(9)
                        else:
                            if x[231] <= 0.0196078438:
                                if x[515] <= 0.0411764719:
                                    results.append(8)
                                else:
                                    if x[492] <= 0.0196078438:
                                        results.append(8)
                                    else:
                                        if x[466] <= 0.9411764741:
                                            results.append(8)
                                        else:
                                            results.append(8)
                            else:
                                results.append(8)
                    else:
                        if x[489] <= 0.6352941245:
                            results.append(6)
                        else:
                            results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 14
    if time.time() < deadline or interrupt_flag.is_set():
        if x[517] <= 0.0019607844:
            if x[330] <= 0.0725490227:
                if x[377] <= 0.0117647061:
                    if x[456] <= 0.0490196086:
                        if x[271] <= 0.0235294122:
                            if x[156] <= 0.0137254903:
                                if x[374] <= 0.0607843138:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[344] <= 0.4098039269:
                                    results.append(5)
                                else:
                                    results.append(5)
                        else:
                            if x[183] <= 0.5235294402:
                                if x[404] <= 0.0941176489:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                results.append(3)
                    else:
                        if x[460] <= 0.0019607844:
                            if x[300] <= 0.5196078718:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[240] <= 0.0176470596:
                                if x[659] <= 0.0784313753:
                                    results.append(2)
                                else:
                                    results.append(4)
                            else:
                                if x[403] <= 0.3196078464:
                                    if x[243] <= 0.8176470697:
                                        if x[239] <= 0.5843137503:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(5)
                else:
                    if x[290] <= 0.1019607857:
                        if x[625] <= 0.0647058841:
                            if x[179] <= 0.6450980604:
                                if x[322] <= 0.8196078539:
                                    if x[407] <= 0.1882352978:
                                        results.append(9)
                                    else:
                                        if x[574] <= 0.0098039219:
                                            results.append(4)
                                        else:
                                            results.append(6)
                                else:
                                    if x[240] <= 0.0196078438:
                                        results.append(8)
                                    else:
                                        results.append(3)
                            else:
                                if x[491] <= 0.3176470697:
                                    if x[372] <= 0.0019607844:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(1)
                        else:
                            if x[486] <= 0.9745098054:
                                if x[232] <= 0.9862745106:
                                    if x[184] <= 0.2137254961:
                                        if x[159] <= 0.0313725509:
                                            results.append(5)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[568] <= 0.5078431666:
                                            if x[293] <= 0.6117647141:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                        else:
                                            if x[296] <= 0.6254902184:
                                                results.append(2)
                                            else:
                                                results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(2)
                    else:
                        if x[652] <= 0.0274509815:
                            if x[237] <= 0.4725490212:
                                if x[436] <= 0.9901960790:
                                    if x[488] <= 0.0098039219:
                                        if x[158] <= 0.0294117657:
                                            if x[243] <= 0.4058823660:
                                                results.append(0)
                                            else:
                                                results.append(8)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(8)
                                else:
                                    if x[207] <= 0.7568627596:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                if x[522] <= 0.3411764801:
                                    if x[266] <= 0.2686274657:
                                        results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    if x[467] <= 0.8235294223:
                                        if x[485] <= 0.0941176489:
                                            if x[323] <= 0.1588235348:
                                                results.append(5)
                                            else:
                                                results.append(7)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(3)
                        else:
                            if x[296] <= 0.3411764801:
                                if x[434] <= 0.9470588267:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(5)
            else:
                if x[497] <= 0.0627450999:
                    if x[294] <= 0.4411764890:
                        if x[377] <= 0.6078431606:
                            if x[567] <= 0.0666666701:
                                results.append(9)
                            else:
                                results.append(0)
                        else:
                            results.append(8)
                    else:
                        results.append(7)
                else:
                    if x[454] <= 0.0058823531:
                        results.append(0)
                    else:
                        if x[213] <= 0.1882353052:
                            results.append(0)
                        else:
                            if x[592] <= 0.0431372570:
                                results.append(0)
                            else:
                                results.append(0)
        else:
            if x[351] <= 0.9470588267:
                if x[570] <= 0.0039215689:
                    if x[428] <= 0.0078431377:
                        if x[234] <= 0.0196078438:
                            if x[214] <= 0.0627451017:
                                if x[376] <= 0.4725490361:
                                    if x[547] <= 0.9882352948:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(9)
                            else:
                                if x[350] <= 0.0725490209:
                                    results.append(4)
                                else:
                                    results.append(8)
                        else:
                            if x[579] <= 0.0176470596:
                                if x[405] <= 0.2980392277:
                                    if x[602] <= 0.0921568647:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(8)
                            else:
                                results.append(6)
                    else:
                        if x[373] <= 0.9686274529:
                            if x[469] <= 0.0058823531:
                                if x[317] <= 0.5019607991:
                                    if x[380] <= 0.0490196086:
                                        results.append(5)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(9)
                            else:
                                if x[207] <= 0.2313725501:
                                    if x[573] <= 0.2705882490:
                                        results.append(4)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(7)
                        else:
                            if x[239] <= 0.9254902005:
                                if x[545] <= 0.9823529422:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[403] <= 0.1137254946:
                                    results.append(9)
                                else:
                                    results.append(4)
                else:
                    if x[401] <= 0.0078431377:
                        if x[681] <= 0.0352941193:
                            if x[377] <= 0.0058823531:
                                if x[343] <= 0.4333333373:
                                    if x[99] <= 0.8882353008:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(7)
                            else:
                                if x[236] <= 0.4745098203:
                                    if x[292] <= 0.0392156877:
                                        results.append(2)
                                    else:
                                        results.append(6)
                                else:
                                    if x[354] <= 0.0196078438:
                                        results.append(5)
                                    else:
                                        if x[655] <= 0.9254902005:
                                            results.append(8)
                                        else:
                                            results.append(8)
                        else:
                            if x[657] <= 0.4254902080:
                                if x[213] <= 0.0254901964:
                                    results.append(7)
                                else:
                                    if x[264] <= 0.9686274529:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                results.append(8)
                    else:
                        if x[442] <= 0.0176470596:
                            if x[550] <= 0.4039215818:
                                if x[567] <= 0.6196078658:
                                    if x[604] <= 0.2215686329:
                                        if x[709] <= 0.1254902035:
                                            if x[318] <= 0.5607843399:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(8)
                                else:
                                    if x[549] <= 0.0117647061:
                                        results.append(2)
                                    else:
                                        results.append(0)
                            else:
                                if x[271] <= 0.0137254903:
                                    if x[568] <= 0.8254902065:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    if x[318] <= 0.2745098099:
                                        results.append(2)
                                    else:
                                        results.append(0)
                        else:
                            if x[243] <= 0.0431372561:
                                if x[205] <= 0.0470588244:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(2)
            else:
                if x[151] <= 0.0137254903:
                    if x[493] <= 0.3529411852:
                        if x[262] <= 0.0941176489:
                            if x[547] <= 0.6862745285:
                                if x[354] <= 0.5509804189:
                                    if x[681] <= 0.7980392277:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[266] <= 0.9352941215:
                                    results.append(3)
                                else:
                                    results.append(1)
                        else:
                            results.append(4)
                    else:
                        if x[180] <= 0.2803921700:
                            results.append(3)
                        else:
                            results.append(8)
                else:
                    if x[127] <= 0.9411764741:
                        if x[633] <= 0.0098039219:
                            results.append(6)
                        else:
                            results.append(8)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 15
    if time.time() < deadline or interrupt_flag.is_set():
        if x[435] <= 0.0019607844:
            if x[567] <= 0.5725490451:
                if x[513] <= 0.6294117868:
                    if x[378] <= 0.0078431377:
                        if x[438] <= 0.3784313798:
                            if x[523] <= 0.0117647061:
                                if x[345] <= 0.3862745166:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                if x[594] <= 0.1745098084:
                                    results.append(7)
                                else:
                                    results.append(0)
                        else:
                            if x[286] <= 0.0431372570:
                                if x[468] <= 0.0941176494:
                                    if x[520] <= 0.7960784435:
                                        results.append(0)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(4)
                            else:
                                results.append(7)
                    else:
                        if x[631] <= 0.0294117648:
                            if x[494] <= 0.0980392173:
                                if x[461] <= 0.9098039269:
                                    results.append(5)
                                else:
                                    results.append(1)
                            else:
                                results.append(4)
                        else:
                            if x[606] <= 0.9686274529:
                                if x[570] <= 0.9705882370:
                                    if x[655] <= 0.3215686381:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(8)
                            else:
                                if x[412] <= 0.4725490287:
                                    if x[239] <= 0.4117647111:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(3)
                else:
                    if x[518] <= 0.1529411785:
                        if x[377] <= 0.6784313768:
                            if x[348] <= 0.6627451181:
                                if x[465] <= 0.0313725509:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(8)
                    else:
                        if x[410] <= 0.2156862766:
                            results.append(6)
                        else:
                            results.append(4)
            else:
                if x[237] <= 0.1745098084:
                    if x[409] <= 0.4470588267:
                        if x[326] <= 0.0058823531:
                            if x[207] <= 0.6588235497:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(2)
                    else:
                        results.append(3)
                else:
                    if x[330] <= 0.0196078438:
                        if x[405] <= 0.1529411785:
                            if x[240] <= 0.0745098051:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(3)
                    else:
                        results.append(0)
        else:
            if x[346] <= 0.0058823533:
                if x[465] <= 0.0019607844:
                    if x[179] <= 0.0294117648:
                        if x[606] <= 0.1098039225:
                            if x[409] <= 0.3333333433:
                                if x[459] <= 0.9450980425:
                                    if x[353] <= 0.6333333552:
                                        if x[216] <= 0.3039215729:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[653] <= 0.9901960790:
                                    if x[596] <= 0.0745098069:
                                        results.append(7)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(8)
                        else:
                            results.append(3)
                    else:
                        if x[294] <= 0.0196078438:
                            if x[495] <= 0.0588235296:
                                if x[157] <= 0.0058823531:
                                    results.append(7)
                                else:
                                    if x[607] <= 0.4450980574:
                                        results.append(2)
                                    else:
                                        results.append(2)
                            else:
                                results.append(6)
                        else:
                            if x[156] <= 0.0039215689:
                                if x[123] <= 0.0392156877:
                                    results.append(8)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                else:
                    if x[711] <= 0.0686274546:
                        if x[155] <= 0.0470588249:
                            if x[377] <= 0.1647058837:
                                if x[402] <= 0.0254901964:
                                    if x[241] <= 0.0921568666:
                                        if x[546] <= 0.2764705941:
                                            results.append(6)
                                        else:
                                            results.append(2)
                                    else:
                                        if x[371] <= 0.7392157018:
                                            if x[352] <= 0.1529411785:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                        else:
                                            results.append(9)
                                else:
                                    if x[235] <= 0.2823529467:
                                        if x[431] <= 0.9254902005:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(9)
                            else:
                                if x[462] <= 0.6843137443:
                                    if x[519] <= 0.9372549057:
                                        if x[409] <= 0.9313725531:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(9)
                                else:
                                    if x[213] <= 0.9196078479:
                                        results.append(1)
                                    else:
                                        results.append(8)
                        else:
                            if x[484] <= 0.0235294122:
                                if x[571] <= 0.6588235497:
                                    if x[543] <= 0.1568627506:
                                        if x[350] <= 0.0372549035:
                                            results.append(3)
                                        else:
                                            if x[184] <= 0.8117647171:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                    else:
                                        results.append(2)
                                else:
                                    if x[126] <= 0.1509803999:
                                        results.append(8)
                                    else:
                                        if x[578] <= 0.8705882430:
                                            results.append(3)
                                        else:
                                            results.append(2)
                            else:
                                if x[685] <= 0.0725490227:
                                    if x[654] <= 0.7078431547:
                                        if x[186] <= 0.1901960820:
                                            if x[550] <= 0.8882353008:
                                                results.append(2)
                                            else:
                                                results.append(2)
                                        else:
                                            if x[299] <= 0.1921568662:
                                                results.append(2)
                                            else:
                                                results.append(2)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(8)
                    else:
                        if x[405] <= 0.0098039219:
                            if x[462] <= 0.7313725650:
                                results.append(7)
                            else:
                                results.append(7)
                        else:
                            results.append(7)
            else:
                if x[428] <= 0.1980392188:
                    if x[655] <= 0.2078431398:
                        if x[544] <= 0.1137254946:
                            if x[598] <= 0.9450980425:
                                if x[267] <= 0.9000000060:
                                    if x[212] <= 0.1431372622:
                                        results.append(4)
                                    else:
                                        if x[296] <= 0.3549019694:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(7)
                            else:
                                results.append(5)
                        else:
                            if x[430] <= 0.4686274678:
                                if x[301] <= 0.2431372553:
                                    results.append(8)
                                else:
                                    results.append(5)
                            else:
                                if x[544] <= 0.6117647290:
                                    results.append(6)
                                else:
                                    if x[572] <= 0.6627451032:
                                        results.append(6)
                                    else:
                                        results.append(6)
                    else:
                        if x[290] <= 0.0019607844:
                            if x[430] <= 0.8372549117:
                                if x[179] <= 0.3294117749:
                                    results.append(8)
                                else:
                                    results.append(3)
                            else:
                                results.append(4)
                        else:
                            if x[153] <= 0.0156862754:
                                if x[486] <= 0.0294117648:
                                    if x[550] <= 0.0666666683:
                                        if x[437] <= 0.0117647061:
                                            results.append(8)
                                        else:
                                            if x[405] <= 0.1019607857:
                                                results.append(7)
                                            else:
                                                results.append(9)
                                    else:
                                        if x[244] <= 0.3921568710:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                else:
                                    if x[654] <= 0.8980392218:
                                        results.append(8)
                                    else:
                                        results.append(8)
                            else:
                                if x[439] <= 0.0254901964:
                                    if x[320] <= 0.9862745106:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    if x[659] <= 0.7647058964:
                                        results.append(5)
                                    else:
                                        results.append(8)
                else:
                    if x[568] <= 0.0176470596:
                        if x[213] <= 0.2078431472:
                            if x[326] <= 0.0235294122:
                                if x[515] <= 0.5843137354:
                                    results.append(4)
                                else:
                                    results.append(6)
                            else:
                                if x[710] <= 0.6411764920:
                                    if x[436] <= 0.8294117749:
                                        results.append(4)
                                    else:
                                        if x[320] <= 0.8784313798:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                else:
                                    results.append(7)
                        else:
                            if x[156] <= 0.5254902244:
                                if x[551] <= 0.0137254903:
                                    if x[487] <= 0.0549019631:
                                        if x[183] <= 0.0980392173:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[211] <= 0.4313725531:
                                            results.append(9)
                                        else:
                                            if x[300] <= 0.0470588244:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                else:
                                    if x[633] <= 0.9196078479:
                                        results.append(4)
                                    else:
                                        if x[437] <= 0.9901960790:
                                            results.append(9)
                                        else:
                                            results.append(3)
                            else:
                                results.append(4)
                    else:
                        if x[243] <= 0.0156862754:
                            if x[497] <= 0.0058823531:
                                results.append(6)
                            else:
                                results.append(6)
                        else:
                            if x[537] <= 0.3647058904:
                                if x[214] <= 0.9274509847:
                                    results.append(5)
                                else:
                                    results.append(8)
                            else:
                                results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 16
    if time.time() < deadline or interrupt_flag.is_set():
        if x[462] <= 0.0333333341:
            if x[464] <= 0.6294117868:
                if x[455] <= 0.0274509815:
                    if x[261] <= 0.0215686280:
                        if x[438] <= 0.0117647061:
                            if x[513] <= 0.1058823541:
                                results.append(3)
                            else:
                                results.append(2)
                        else:
                            if x[514] <= 0.1137254946:
                                if x[378] <= 0.0078431377:
                                    results.append(5)
                                else:
                                    if x[406] <= 0.9901960790:
                                        if x[572] <= 0.4254902005:
                                            if x[401] <= 0.8098039329:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[598] <= 0.9901960790:
                                            results.append(3)
                                        else:
                                            if x[350] <= 0.7627451122:
                                                results.append(5)
                                            else:
                                                results.append(3)
                            else:
                                if x[238] <= 0.5176470727:
                                    results.append(0)
                                else:
                                    results.append(6)
                    else:
                        if x[159] <= 0.0196078434:
                            if x[601] <= 0.9901960790:
                                if x[487] <= 0.2960784435:
                                    if x[207] <= 0.4960784465:
                                        if x[521] <= 0.7215686440:
                                            results.append(8)
                                        else:
                                            results.append(7)
                                    else:
                                        if x[208] <= 0.9862745106:
                                            results.append(3)
                                        else:
                                            if x[374] <= 0.4901960939:
                                                results.append(3)
                                            else:
                                                results.append(5)
                                else:
                                    results.append(8)
                            else:
                                if x[439] <= 0.9921568632:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[375] <= 0.1196078472:
                                results.append(3)
                            else:
                                if x[681] <= 0.0470588254:
                                    results.append(5)
                                else:
                                    results.append(5)
                else:
                    if x[406] <= 0.1098039234:
                        if x[570] <= 0.0274509806:
                            if x[595] <= 0.2901960909:
                                results.append(5)
                            else:
                                results.append(0)
                        else:
                            if x[548] <= 0.9941176474:
                                if x[688] <= 0.3274509832:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[634] <= 0.0941176498:
                            if x[217] <= 0.0254901964:
                                results.append(6)
                            else:
                                results.append(3)
                        else:
                            results.append(5)
            else:
                if x[350] <= 0.1862745136:
                    if x[430] <= 0.0392156877:
                        if x[267] <= 0.5607843399:
                            results.append(7)
                        else:
                            if x[296] <= 0.8490196168:
                                results.append(7)
                            else:
                                results.append(7)
                    else:
                        if x[595] <= 0.0196078441:
                            if x[406] <= 0.4058823586:
                                results.append(6)
                            else:
                                if x[265] <= 0.1019607857:
                                    results.append(4)
                                else:
                                    results.append(9)
                        else:
                            results.append(5)
                else:
                    if x[629] <= 0.5431372672:
                        if x[266] <= 0.2686274648:
                            if x[327] <= 0.1117647067:
                                results.append(9)
                            else:
                                results.append(2)
                        else:
                            results.append(9)
                    else:
                        if x[290] <= 0.1627451032:
                            if x[628] <= 0.9549019635:
                                results.append(3)
                            else:
                                results.append(3)
                        else:
                            results.append(8)
        else:
            if x[456] <= 0.0215686280:
                if x[409] <= 0.1862745136:
                    if x[346] <= 0.0078431377:
                        if x[578] <= 0.1117647104:
                            if x[272] <= 0.1568627469:
                                if x[205] <= 0.2588235438:
                                    if x[376] <= 0.9862745106:
                                        if x[462] <= 0.3666666746:
                                            results.append(1)
                                        else:
                                            if x[490] <= 0.7941176593:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(3)
                            else:
                                if x[326] <= 0.9784313738:
                                    results.append(8)
                                else:
                                    results.append(2)
                        else:
                            if x[598] <= 0.3921568692:
                                results.append(3)
                            else:
                                if x[581] <= 0.0156862754:
                                    results.append(3)
                                else:
                                    results.append(2)
                    else:
                        if x[180] <= 0.0196078434:
                            if x[379] <= 0.4470588341:
                                results.append(5)
                            else:
                                if x[685] <= 0.4980392307:
                                    results.append(1)
                                else:
                                    results.append(8)
                        else:
                            if x[216] <= 0.0392156877:
                                if x[348] <= 0.9294117689:
                                    if x[578] <= 0.7529411912:
                                        results.append(8)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(3)
                            else:
                                if x[516] <= 0.0078431377:
                                    results.append(8)
                                else:
                                    results.append(8)
                else:
                    if x[578] <= 0.0058823531:
                        if x[459] <= 0.0725490209:
                            if x[432] <= 0.0254901964:
                                if x[377] <= 0.3745098114:
                                    if x[573] <= 0.4666666687:
                                        results.append(7)
                                    else:
                                        if x[240] <= 0.3686274588:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[324] <= 0.1647058874:
                                    results.append(4)
                                else:
                                    if x[431] <= 0.1156862751:
                                        results.append(8)
                                    else:
                                        if x[492] <= 0.6098039299:
                                            results.append(9)
                                        else:
                                            results.append(9)
                        else:
                            if x[330] <= 0.0901960805:
                                if x[625] <= 0.5078431517:
                                    if x[238] <= 0.2627451047:
                                        if x[213] <= 0.0803921595:
                                            results.append(6)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[380] <= 0.5509804189:
                                            results.append(4)
                                        else:
                                            if x[381] <= 0.9941176474:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                else:
                                    if x[632] <= 0.2352941185:
                                        if x[492] <= 0.5666666701:
                                            results.append(1)
                                        else:
                                            results.append(2)
                                    else:
                                        results.append(8)
                            else:
                                results.append(8)
                    else:
                        if x[656] <= 0.4000000060:
                            if x[347] <= 0.0352941193:
                                if x[464] <= 0.9705882370:
                                    if x[576] <= 0.8078431487:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    if x[185] <= 0.5745098144:
                                        results.append(9)
                                    else:
                                        results.append(2)
                            else:
                                if x[345] <= 0.3392156959:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[347] <= 0.0313725509:
                                if x[488] <= 0.2333333418:
                                    results.append(3)
                                else:
                                    results.append(8)
                            else:
                                if x[687] <= 0.3078431487:
                                    results.append(8)
                                else:
                                    results.append(8)
            else:
                if x[566] <= 0.0039215689:
                    if x[99] <= 0.0019607844:
                        if x[409] <= 0.3784313798:
                            if x[218] <= 0.3176470734:
                                if x[574] <= 0.8156862855:
                                    if x[401] <= 0.1431372557:
                                        results.append(2)
                                    else:
                                        if x[179] <= 0.0627451017:
                                            results.append(4)
                                        else:
                                            results.append(8)
                                else:
                                    results.append(6)
                            else:
                                results.append(5)
                        else:
                            if x[212] <= 0.0235294127:
                                if x[499] <= 0.0254901964:
                                    if x[455] <= 0.0098039219:
                                        results.append(4)
                                    else:
                                        if x[486] <= 0.0098039219:
                                            results.append(4)
                                        else:
                                            if x[495] <= 0.8372549117:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                else:
                                    results.append(6)
                            else:
                                if x[468] <= 0.0098039219:
                                    if x[403] <= 0.9098039269:
                                        if x[215] <= 0.9843137264:
                                            if x[208] <= 0.0215686280:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(4)
                                else:
                                    if x[399] <= 0.0666666683:
                                        if x[486] <= 0.5450980514:
                                            results.append(5)
                                        else:
                                            results.append(6)
                                    else:
                                        if x[178] <= 0.0333333351:
                                            if x[235] <= 0.0176470596:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(8)
                    else:
                        if x[123] <= 0.5686274767:
                            if x[526] <= 0.0470588254:
                                results.append(6)
                            else:
                                results.append(6)
                        else:
                            results.append(2)
                else:
                    if x[292] <= 0.3529411852:
                        if x[233] <= 0.7254902124:
                            results.append(2)
                        else:
                            results.append(4)
                    else:
                        if x[469] <= 0.9509803951:
                            if x[405] <= 0.8058823645:
                                results.append(2)
                            else:
                                results.append(8)
                        else:
                            results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 17
    if time.time() < deadline or interrupt_flag.is_set():
        if x[428] <= 0.1980392188:
            if x[376] <= 0.0156862750:
                if x[461] <= 0.0411764719:
                    if x[470] <= 0.1058823541:
                        if x[152] <= 0.1117647067:
                            if x[260] <= 0.1313725524:
                                if x[271] <= 0.1686274558:
                                    results.append(3)
                                else:
                                    if x[299] <= 0.8470588326:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[324] <= 0.9196078479:
                                    if x[299] <= 0.2000000030:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(7)
                        else:
                            if x[631] <= 0.0176470596:
                                results.append(2)
                            else:
                                if x[157] <= 0.0980392173:
                                    results.append(1)
                                else:
                                    results.append(3)
                    else:
                        if x[245] <= 0.6509804130:
                            results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[350] <= 0.0686274525:
                        if x[126] <= 0.0137254903:
                            if x[266] <= 0.9450980425:
                                if x[594] <= 0.0058823531:
                                    if x[405] <= 0.0686274543:
                                        if x[318] <= 0.0960784331:
                                            if x[655] <= 0.0019607844:
                                                results.append(5)
                                            else:
                                                results.append(7)
                                        else:
                                            if x[547] <= 0.6568627656:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                    else:
                                        if x[658] <= 0.0058823531:
                                            results.append(1)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(2)
                            else:
                                if x[549] <= 0.3000000129:
                                    results.append(7)
                                else:
                                    results.append(7)
                        else:
                            if x[625] <= 0.0039215689:
                                results.append(2)
                            else:
                                results.append(2)
                    else:
                        if x[579] <= 0.4960784465:
                            if x[521] <= 0.0039215689:
                                if x[263] <= 0.1117647067:
                                    if x[268] <= 0.0431372561:
                                        if x[152] <= 0.0470588244:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[323] <= 0.6843137443:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[655] <= 0.4058823604:
                                    results.append(7)
                                else:
                                    results.append(8)
                        else:
                            results.append(2)
            else:
                if x[463] <= 0.0411764719:
                    if x[153] <= 0.0058823531:
                        if x[462] <= 0.1862745136:
                            if x[488] <= 0.3843137324:
                                if x[567] <= 0.0019607844:
                                    if x[260] <= 0.1352941208:
                                        results.append(3)
                                    else:
                                        results.append(9)
                                else:
                                    if x[182] <= 0.9392156899:
                                        results.append(5)
                                    else:
                                        results.append(3)
                            else:
                                results.append(6)
                        else:
                            if x[408] <= 0.0490196105:
                                results.append(1)
                            else:
                                results.append(1)
                    else:
                        if x[515] <= 0.0098039219:
                            if x[159] <= 0.0254901964:
                                if x[540] <= 0.0843137279:
                                    if x[379] <= 0.7274509966:
                                        if x[605] <= 0.5627451241:
                                            results.append(0)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    if x[548] <= 0.3549019694:
                                        if x[596] <= 0.5745098144:
                                            results.append(8)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[633] <= 0.7725490332:
                                    if x[184] <= 0.0901960824:
                                        results.append(5)
                                    else:
                                        if x[621] <= 0.6196078509:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    if x[568] <= 0.6509804130:
                                        results.append(5)
                                    else:
                                        results.append(5)
                        else:
                            if x[289] <= 0.0450980403:
                                if x[207] <= 0.4627451152:
                                    results.append(2)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                else:
                    if x[318] <= 0.0294117657:
                        if x[578] <= 0.0529411770:
                            if x[295] <= 0.6254902184:
                                if x[299] <= 0.0098039219:
                                    if x[431] <= 0.3450980559:
                                        if x[629] <= 0.6098039299:
                                            results.append(1)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(8)
                                else:
                                    if x[320] <= 0.0803921577:
                                        results.append(3)
                                    else:
                                        if x[516] <= 0.1705882400:
                                            results.append(4)
                                        else:
                                            results.append(8)
                            else:
                                if x[465] <= 0.1686274577:
                                    if x[458] <= 0.2058823593:
                                        if x[264] <= 0.2117647082:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[485] <= 0.4372549206:
                                if x[658] <= 0.0647058859:
                                    results.append(6)
                                else:
                                    if x[320] <= 0.2490196154:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                results.append(2)
                    else:
                        if x[461] <= 0.1078431383:
                            if x[606] <= 0.1686274558:
                                if x[183] <= 0.2862745225:
                                    if x[379] <= 0.6725490391:
                                        results.append(5)
                                    else:
                                        results.append(4)
                                else:
                                    if x[378] <= 0.5960784554:
                                        results.append(9)
                                    else:
                                        results.append(9)
                            else:
                                results.append(8)
                        else:
                            if x[627] <= 0.0098039219:
                                if x[571] <= 0.0176470596:
                                    if x[603] <= 0.7490196228:
                                        results.append(8)
                                    else:
                                        if x[545] <= 0.1333333347:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(6)
                            else:
                                if x[292] <= 0.9941176474:
                                    if x[514] <= 0.0098039219:
                                        if x[625] <= 0.1372549050:
                                            results.append(8)
                                        else:
                                            results.append(5)
                                    else:
                                        if x[327] <= 0.0039215689:
                                            if x[655] <= 0.3019607961:
                                                results.append(8)
                                            else:
                                                results.append(8)
                                        else:
                                            if x[347] <= 0.9941176474:
                                                results.append(8)
                                            else:
                                                results.append(8)
                                else:
                                    results.append(5)
        else:
            if x[492] <= 0.1921568662:
                if x[515] <= 0.2784313783:
                    if x[324] <= 0.1921568662:
                        if x[379] <= 0.0490196086:
                            if x[438] <= 0.7588235438:
                                if x[523] <= 0.1745098084:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(7)
                        else:
                            if x[467] <= 0.4274509847:
                                results.append(6)
                            else:
                                results.append(5)
                    else:
                        if x[433] <= 0.0980392173:
                            if x[353] <= 0.9470588267:
                                results.append(5)
                            else:
                                results.append(3)
                        else:
                            if x[403] <= 0.6803921759:
                                results.append(9)
                            else:
                                if x[271] <= 0.4490196109:
                                    results.append(3)
                                else:
                                    results.append(5)
                else:
                    if x[270] <= 0.2784313783:
                        if x[602] <= 0.2000000067:
                            results.append(6)
                        else:
                            results.append(6)
                    else:
                        if x[408] <= 0.4431372583:
                            results.append(0)
                        else:
                            results.append(2)
            else:
                if x[598] <= 0.0098039221:
                    if x[266] <= 0.0078431377:
                        if x[510] <= 0.5333333462:
                            if x[181] <= 0.2450980432:
                                if x[318] <= 0.0431372551:
                                    if x[465] <= 0.9843137264:
                                        results.append(6)
                                    else:
                                        if x[523] <= 0.5529411808:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                else:
                                    if x[440] <= 0.5274509937:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                if x[492] <= 0.8039215803:
                                    results.append(4)
                                else:
                                    results.append(9)
                        else:
                            results.append(2)
                    else:
                        if x[453] <= 0.0411764719:
                            if x[241] <= 0.1490196139:
                                if x[462] <= 0.9803921580:
                                    if x[345] <= 0.9254902005:
                                        results.append(2)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(4)
                            else:
                                if x[521] <= 0.9901960790:
                                    if x[345] <= 0.6019607931:
                                        results.append(4)
                                    else:
                                        if x[487] <= 0.0156862754:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    if x[211] <= 0.6470588297:
                                        results.append(5)
                                    else:
                                        results.append(9)
                        else:
                            if x[429] <= 0.7254901975:
                                results.append(4)
                            else:
                                results.append(4)
                else:
                    if x[123] <= 0.0058823531:
                        if x[548] <= 0.9803921580:
                            if x[162] <= 0.0509803928:
                                if x[681] <= 0.2196078524:
                                    if x[246] <= 0.3862745315:
                                        if x[547] <= 0.1000000034:
                                            results.append(8)
                                        else:
                                            if x[376] <= 0.0215686280:
                                                results.append(6)
                                            else:
                                                results.append(2)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(9)
                            else:
                                if x[325] <= 0.0627451017:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[217] <= 0.0411764719:
                                if x[242] <= 0.9862745106:
                                    if x[291] <= 0.9764705896:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(0)
                            else:
                                if x[328] <= 0.2784313783:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[624] <= 0.0627451017:
                            results.append(6)
                        else:
                            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 18
    if time.time() < deadline or interrupt_flag.is_set():
        if x[433] <= 0.0039215689:
            if x[512] <= 0.0470588244:
                if x[596] <= 0.0058823531:
                    if x[154] <= 0.0568627454:
                        if x[243] <= 0.0156862754:
                            if x[265] <= 0.3352941275:
                                if x[152] <= 0.1176470593:
                                    if x[238] <= 0.0686274525:
                                        results.append(7)
                                    else:
                                        if x[236] <= 0.9117647111:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(6)
                            else:
                                if x[354] <= 0.0117647061:
                                    results.append(1)
                                else:
                                    if x[402] <= 0.0274509806:
                                        results.append(7)
                                    else:
                                        results.append(7)
                        else:
                            if x[456] <= 0.1921568662:
                                if x[324] <= 0.9470588267:
                                    if x[183] <= 0.4862745255:
                                        if x[402] <= 0.1450980455:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(7)
                            else:
                                results.append(7)
                    else:
                        if x[514] <= 0.0960784350:
                            if x[379] <= 0.1705882400:
                                results.append(0)
                            else:
                                if x[633] <= 0.7470588386:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[605] <= 0.3823529556:
                                results.append(6)
                            else:
                                results.append(6)
                else:
                    if x[399] <= 0.6176470816:
                        if x[323] <= 0.7078431547:
                            if x[572] <= 0.8725490272:
                                if x[273] <= 0.2666666806:
                                    if x[266] <= 0.1058823541:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(0)
                            else:
                                results.append(2)
                        else:
                            if x[152] <= 0.4901960790:
                                results.append(5)
                            else:
                                if x[346] <= 0.9901960790:
                                    results.append(3)
                                else:
                                    results.append(3)
                    else:
                        results.append(0)
            else:
                if x[436] <= 0.0176470596:
                    if x[378] <= 0.0294117650:
                        if x[519] <= 0.9862745106:
                            if x[541] <= 0.0254901964:
                                if x[602] <= 0.9509803951:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[465] <= 0.7000000179:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[542] <= 0.1607843153:
                            results.append(5)
                        else:
                            results.append(3)
                else:
                    if x[350] <= 0.4627451152:
                        if x[497] <= 0.4568627477:
                            if x[514] <= 0.4588235319:
                                if x[623] <= 0.0039215689:
                                    results.append(6)
                                else:
                                    results.append(0)
                            else:
                                if x[153] <= 0.3549019699:
                                    if x[402] <= 0.0333333337:
                                        results.append(9)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(2)
                        else:
                            if x[204] <= 0.1294117682:
                                results.append(6)
                            else:
                                results.append(6)
                    else:
                        if x[353] <= 0.0156862754:
                            results.append(5)
                        else:
                            results.append(3)
        else:
            if x[350] <= 0.4019607902:
                if x[152] <= 0.0647058841:
                    if x[237] <= 0.0254901964:
                        if x[542] <= 0.0568627454:
                            if x[543] <= 0.0117647061:
                                if x[636] <= 0.1764705889:
                                    if x[324] <= 0.9352941215:
                                        results.append(4)
                                    else:
                                        if x[430] <= 0.9941176474:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                else:
                                    results.append(4)
                            else:
                                results.append(1)
                        else:
                            if x[159] <= 0.0450980403:
                                results.append(5)
                            else:
                                if x[596] <= 0.1745098084:
                                    results.append(1)
                                else:
                                    results.append(2)
                    else:
                        if x[132] <= 0.0254901964:
                            if x[241] <= 0.0725490227:
                                if x[215] <= 0.0960784331:
                                    if x[300] <= 0.2568627596:
                                        if x[297] <= 0.0215686280:
                                            if x[485] <= 0.0352941193:
                                                results.append(3)
                                            else:
                                                results.append(6)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[547] <= 0.2607843205:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                else:
                                    if x[157] <= 0.0529411770:
                                        results.append(4)
                                    else:
                                        if x[659] <= 0.7921568751:
                                            if x[375] <= 0.4862745255:
                                                results.append(8)
                                            else:
                                                results.append(8)
                                        else:
                                            results.append(5)
                            else:
                                if x[355] <= 0.0137254905:
                                    if x[490] <= 0.1058823578:
                                        if x[351] <= 0.4411764890:
                                            if x[380] <= 0.5666666925:
                                                results.append(5)
                                            else:
                                                results.append(5)
                                        else:
                                            results.append(8)
                                    else:
                                        if x[261] <= 0.7450980544:
                                            if x[483] <= 0.0901960810:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(7)
                                else:
                                    if x[187] <= 0.8411764801:
                                        if x[438] <= 0.2470588312:
                                            if x[625] <= 0.2470588274:
                                                results.append(9)
                                            else:
                                                results.append(7)
                                        else:
                                            if x[212] <= 0.2117647082:
                                                results.append(7)
                                            else:
                                                results.append(9)
                                    else:
                                        if x[596] <= 0.0392156877:
                                            results.append(9)
                                        else:
                                            results.append(8)
                        else:
                            if x[266] <= 0.8843137324:
                                results.append(5)
                            else:
                                results.append(6)
                else:
                    if x[569] <= 0.1078431420:
                        if x[516] <= 0.3215686455:
                            if x[511] <= 0.0666666701:
                                if x[317] <= 0.1980392206:
                                    results.append(3)
                                else:
                                    results.append(4)
                            else:
                                results.append(2)
                        else:
                            if x[99] <= 0.0411764719:
                                if x[124] <= 0.3843137324:
                                    results.append(8)
                                else:
                                    results.append(6)
                            else:
                                results.append(6)
                    else:
                        if x[318] <= 0.2745098099:
                            if x[491] <= 0.0039215689:
                                results.append(2)
                            else:
                                if x[630] <= 0.5509804189:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            if x[242] <= 0.0588235296:
                                if x[289] <= 0.8588235378:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(8)
            else:
                if x[437] <= 0.0039215689:
                    if x[298] <= 0.2039215714:
                        if x[607] <= 0.7313725650:
                            if x[319] <= 0.6392157078:
                                if x[290] <= 0.0254901964:
                                    if x[520] <= 0.9196078479:
                                        if x[353] <= 0.2725490332:
                                            if x[155] <= 0.9941176474:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(8)
                        else:
                            results.append(2)
                    else:
                        if x[604] <= 0.0058823531:
                            if x[602] <= 0.2372549102:
                                if x[326] <= 0.2666666694:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(5)
                        else:
                            if x[265] <= 0.0235294122:
                                if x[521] <= 0.1137254946:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                if x[316] <= 0.3294117749:
                                    results.append(8)
                                else:
                                    results.append(8)
                else:
                    if x[211] <= 0.8568627536:
                        if x[543] <= 0.0215686280:
                            if x[578] <= 0.0666666673:
                                results.append(4)
                            else:
                                if x[579] <= 0.4372549057:
                                    if x[244] <= 0.1921568662:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(1)
                        else:
                            if x[294] <= 0.5725490227:
                                if x[384] <= 0.2470588312:
                                    if x[658] <= 0.0431372561:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(4)
                            else:
                                results.append(5)
                    else:
                        if x[542] <= 0.1843137294:
                            if x[523] <= 0.0039215689:
                                if x[269] <= 0.1078431387:
                                    results.append(3)
                                else:
                                    if x[408] <= 0.9901960790:
                                        results.append(3)
                                    else:
                                        results.append(9)
                            else:
                                if x[345] <= 0.8294117749:
                                    if x[654] <= 0.4725490361:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(5)
                        else:
                            if x[298] <= 0.0588235296:
                                if x[212] <= 0.9470588267:
                                    results.append(2)
                                else:
                                    results.append(6)
                            else:
                                if x[408] <= 0.9882352948:
                                    results.append(8)
                                else:
                                    results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 19
    if time.time() < deadline or interrupt_flag.is_set():
        if x[409] <= 0.0019607844:
            if x[525] <= 0.0078431377:
                if x[317] <= 0.0117647061:
                    if x[521] <= 0.0039215689:
                        if x[347] <= 0.3588235378:
                            if x[150] <= 0.0372549035:
                                if x[178] <= 0.1745098084:
                                    if x[327] <= 0.1000000034:
                                        if x[654] <= 0.9941176474:
                                            if x[404] <= 0.7470588386:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(2)
                            else:
                                results.append(2)
                        else:
                            if x[211] <= 0.6470588297:
                                results.append(5)
                            else:
                                results.append(8)
                    else:
                        if x[353] <= 0.0784313753:
                            if x[547] <= 0.8843137324:
                                if x[463] <= 0.9901960790:
                                    if x[603] <= 0.8745098114:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[629] <= 0.0627450999:
                                results.append(3)
                            else:
                                if x[487] <= 0.5117647350:
                                    results.append(8)
                                else:
                                    results.append(8)
                else:
                    if x[440] <= 0.3784313798:
                        if x[323] <= 0.0098039219:
                            if x[542] <= 0.0529411770:
                                if x[264] <= 0.9862745106:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(6)
                        else:
                            if x[290] <= 0.0058823531:
                                results.append(5)
                            else:
                                if x[543] <= 0.0098039219:
                                    results.append(8)
                                else:
                                    if x[577] <= 0.5901960880:
                                        results.append(8)
                                    else:
                                        results.append(8)
                    else:
                        if x[512] <= 0.1235294156:
                            if x[182] <= 0.8647058904:
                                results.append(7)
                            else:
                                results.append(0)
                        else:
                            if x[400] <= 0.9941176474:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[263] <= 0.0960784331:
                    if x[486] <= 0.4607843161:
                        if x[234] <= 0.2294117734:
                            if x[375] <= 0.7901960909:
                                results.append(0)
                            else:
                                results.append(3)
                        else:
                            results.append(0)
                    else:
                        if x[179] <= 0.1039215699:
                            results.append(6)
                        else:
                            if x[632] <= 0.0647058859:
                                results.append(2)
                            else:
                                results.append(0)
                else:
                    if x[98] <= 0.0196078438:
                        if x[345] <= 0.5490196347:
                            if x[369] <= 0.1431372613:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(6)
        else:
            if x[571] <= 0.0176470596:
                if x[323] <= 0.9627451003:
                    if x[183] <= 0.0686274543:
                        if x[238] <= 0.2431372628:
                            if x[435] <= 0.1470588259:
                                if x[324] <= 0.1215686314:
                                    results.append(4)
                                else:
                                    results.append(7)
                            else:
                                if x[461] <= 0.2294117697:
                                    if x[271] <= 0.5313725621:
                                        results.append(6)
                                    else:
                                        results.append(4)
                                else:
                                    if x[494] <= 0.1411764771:
                                        if x[456] <= 0.0411764719:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(4)
                        else:
                            if x[260] <= 0.2980392277:
                                if x[688] <= 0.2294117734:
                                    if x[434] <= 0.0411764719:
                                        results.append(7)
                                    else:
                                        if x[600] <= 0.6549019814:
                                            if x[289] <= 0.0431372561:
                                                results.append(3)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(4)
                                else:
                                    results.append(9)
                            else:
                                if x[688] <= 0.9901960790:
                                    if x[461] <= 0.3352941275:
                                        if x[353] <= 0.2000000067:
                                            results.append(7)
                                        else:
                                            if x[324] <= 0.6764706075:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(7)
                    else:
                        if x[345] <= 0.0039215689:
                            if x[491] <= 0.8294117749:
                                if x[297] <= 0.0745098051:
                                    if x[217] <= 0.2098039277:
                                        results.append(3)
                                    else:
                                        results.append(8)
                                else:
                                    if x[239] <= 0.7666666806:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[568] <= 0.0039215689:
                                    results.append(9)
                                else:
                                    results.append(2)
                        else:
                            if x[627] <= 0.3588235378:
                                if x[156] <= 0.1333333366:
                                    if x[406] <= 0.0039215689:
                                        results.append(4)
                                    else:
                                        if x[413] <= 0.0960784331:
                                            if x[493] <= 0.3882353008:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    if x[181] <= 0.4313725606:
                                        results.append(4)
                                    else:
                                        results.append(8)
                            else:
                                if x[545] <= 0.0490196086:
                                    if x[682] <= 0.0392156877:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(8)
                else:
                    if x[488] <= 0.0156862754:
                        if x[626] <= 0.1254902035:
                            results.append(3)
                        else:
                            if x[236] <= 0.4803921729:
                                results.append(3)
                            else:
                                results.append(3)
                    else:
                        if x[429] <= 0.2431372553:
                            results.append(8)
                        else:
                            results.append(4)
            else:
                if x[347] <= 0.0019607844:
                    if x[485] <= 0.0078431377:
                        if x[404] <= 0.0470588249:
                            if x[154] <= 0.2803921625:
                                if x[263] <= 0.0705882385:
                                    results.append(1)
                                else:
                                    results.append(7)
                            else:
                                if x[543] <= 0.9490196109:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            if x[237] <= 0.7392157018:
                                if x[438] <= 0.2450980395:
                                    results.append(8)
                                else:
                                    results.append(9)
                            else:
                                results.append(9)
                    else:
                        if x[624] <= 0.0019607844:
                            if x[185] <= 0.0431372561:
                                if x[431] <= 0.4705882519:
                                    if x[569] <= 0.6803921759:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(2)
                        else:
                            if x[406] <= 0.9901960790:
                                results.append(2)
                            else:
                                if x[594] <= 0.4333333373:
                                    results.append(1)
                                else:
                                    results.append(2)
                else:
                    if x[487] <= 0.0078431377:
                        if x[356] <= 0.0686274525:
                            if x[269] <= 0.2627451047:
                                if x[544] <= 0.5098039359:
                                    if x[347] <= 0.9941176474:
                                        if x[627] <= 0.9274509847:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    if x[355] <= 0.0176470596:
                                        results.append(6)
                                    else:
                                        results.append(5)
                            else:
                                if x[246] <= 0.5529411882:
                                    if x[460] <= 0.0529411770:
                                        if x[579] <= 0.0647058859:
                                            if x[297] <= 0.8372549117:
                                                results.append(7)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(5)
                        else:
                            if x[623] <= 0.3568627536:
                                if x[351] <= 0.0313725499:
                                    if x[400] <= 0.6000000089:
                                        if x[245] <= 0.2686274517:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(4)
                                else:
                                    if x[572] <= 0.9901960790:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                if x[496] <= 0.4039215744:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[244] <= 0.0196078438:
                            if x[627] <= 0.0098039219:
                                if x[465] <= 0.9862745106:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                if x[377] <= 0.6941176653:
                                    if x[242] <= 0.0313725509:
                                        results.append(6)
                                    else:
                                        results.append(0)
                                else:
                                    if x[151] <= 0.0490196086:
                                        if x[265] <= 0.5764705986:
                                            if x[234] <= 0.5862745196:
                                                results.append(6)
                                            else:
                                                results.append(8)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(8)
                        else:
                            if x[659] <= 0.2078431472:
                                if x[185] <= 0.6627451181:
                                    if x[540] <= 0.3607843220:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[457] <= 0.1352941208:
                                        results.append(8)
                                    else:
                                        results.append(0)
                            else:
                                if x[410] <= 0.7372549176:
                                    results.append(8)
                                else:
                                    results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 20
    if time.time() < deadline or interrupt_flag.is_set():
        if x[429] <= 0.0294117657:
            if x[288] <= 0.0411764719:
                if x[437] <= 0.0039215689:
                    if x[552] <= 0.0078431377:
                        if x[207] <= 0.0058823531:
                            if x[347] <= 0.0352941183:
                                if x[458] <= 0.0215686285:
                                    if x[569] <= 0.0647058832:
                                        if x[408] <= 0.8647058904:
                                            if x[323] <= 0.3764705956:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[271] <= 0.0803921595:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[597] <= 0.7352941334:
                                        results.append(2)
                                    else:
                                        results.append(1)
                            else:
                                if x[350] <= 0.2823529467:
                                    results.append(5)
                                else:
                                    if x[656] <= 0.6392157078:
                                        results.append(8)
                                    else:
                                        results.append(8)
                        else:
                            if x[242] <= 0.0156862754:
                                if x[375] <= 0.3450980522:
                                    if x[349] <= 0.9745098054:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(5)
                            else:
                                if x[574] <= 0.0509803928:
                                    results.append(2)
                                else:
                                    if x[128] <= 0.1803921610:
                                        results.append(8)
                                    else:
                                        results.append(3)
                    else:
                        if x[405] <= 0.6372549236:
                            if x[374] <= 0.4921568781:
                                if x[205] <= 0.0823529437:
                                    results.append(5)
                                else:
                                    results.append(3)
                            else:
                                results.append(3)
                        else:
                            results.append(2)
                else:
                    if x[467] <= 0.0960784331:
                        if x[183] <= 0.0039215689:
                            if x[409] <= 0.9039215744:
                                if x[597] <= 0.8333333433:
                                    if x[375] <= 0.3254902065:
                                        results.append(7)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(1)
                            else:
                                if x[352] <= 0.8196078539:
                                    if x[261] <= 0.0156862754:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(2)
                        else:
                            if x[657] <= 0.0019607844:
                                if x[182] <= 0.8450980484:
                                    if x[602] <= 0.1019607857:
                                        results.append(9)
                                    else:
                                        results.append(6)
                                else:
                                    if x[266] <= 0.2372549046:
                                        results.append(2)
                                    else:
                                        results.append(2)
                            else:
                                if x[494] <= 0.2000000030:
                                    if x[348] <= 0.7627451122:
                                        if x[654] <= 0.0686274543:
                                            results.append(9)
                                        else:
                                            if x[572] <= 0.5313725509:
                                                results.append(3)
                                            else:
                                                results.append(7)
                                    else:
                                        if x[328] <= 0.1549019665:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                else:
                                    if x[152] <= 0.6666666865:
                                        if x[571] <= 0.2686274648:
                                            results.append(5)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(3)
                    else:
                        if x[458] <= 0.1058823541:
                            if x[150] <= 0.0235294122:
                                if x[546] <= 0.9901960790:
                                    if x[297] <= 0.2627451131:
                                        if x[348] <= 0.8411764801:
                                            results.append(3)
                                        else:
                                            results.append(5)
                                    else:
                                        if x[378] <= 0.3686274663:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(7)
                            else:
                                if x[375] <= 0.1176470593:
                                    results.append(3)
                                else:
                                    if x[493] <= 0.8862745166:
                                        results.append(3)
                                    else:
                                        results.append(3)
                        else:
                            if x[319] <= 0.0019607844:
                                results.append(2)
                            else:
                                results.append(8)
            else:
                if x[482] <= 0.1686274521:
                    if x[154] <= 0.0039215689:
                        if x[377] <= 0.1431372622:
                            if x[456] <= 0.4823529460:
                                if x[187] <= 0.1745098084:
                                    if x[267] <= 0.4215686321:
                                        results.append(3)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(8)
                            else:
                                results.append(4)
                        else:
                            if x[460] <= 0.4117647111:
                                if x[402] <= 0.2431372553:
                                    results.append(5)
                                else:
                                    results.append(9)
                            else:
                                results.append(8)
                    else:
                        if x[404] <= 0.0254901964:
                            if x[549] <= 0.3372549042:
                                results.append(2)
                            else:
                                results.append(2)
                        else:
                            if x[439] <= 0.4941176623:
                                if x[515] <= 0.0941176489:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                if x[374] <= 0.2235294133:
                                    results.append(3)
                                else:
                                    results.append(5)
                else:
                    if x[329] <= 0.5000000149:
                        results.append(5)
                    else:
                        if x[210] <= 0.1549019665:
                            results.append(0)
                        else:
                            results.append(0)
        else:
            if x[538] <= 0.1254901998:
                if x[541] <= 0.0686274525:
                    if x[349] <= 0.7490196228:
                        if x[189] <= 0.0509803928:
                            if x[497] <= 0.0588235315:
                                if x[208] <= 0.0058823531:
                                    if x[710] <= 0.0745098069:
                                        if x[239] <= 0.9862745106:
                                            if x[344] <= 0.1470588297:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            if x[520] <= 0.8235294223:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    if x[211] <= 0.6176470816:
                                        if x[661] <= 0.1568627525:
                                            if x[413] <= 0.0117647061:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[372] <= 0.5490196347:
                                            if x[428] <= 0.1882352978:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            if x[288] <= 0.0117647061:
                                                results.append(9)
                                            else:
                                                results.append(9)
                            else:
                                if x[516] <= 0.0333333351:
                                    results.append(3)
                                else:
                                    if x[544] <= 0.9901960790:
                                        results.append(6)
                                    else:
                                        results.append(6)
                        else:
                            if x[428] <= 0.1862745136:
                                if x[266] <= 0.0529411789:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[299] <= 0.1294117682:
                                    results.append(5)
                                else:
                                    if x[681] <= 0.9901960790:
                                        if x[212] <= 0.0941176489:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(4)
                    else:
                        if x[654] <= 0.4000000209:
                            if x[601] <= 0.9882352948:
                                results.append(5)
                            else:
                                results.append(3)
                        else:
                            if x[655] <= 0.9450980425:
                                results.append(3)
                            else:
                                results.append(3)
                else:
                    if x[272] <= 0.0039215689:
                        if x[624] <= 0.0882352982:
                            if x[573] <= 0.4235294163:
                                if x[373] <= 0.0862745121:
                                    results.append(2)
                                else:
                                    if x[493] <= 0.2117647082:
                                        results.append(5)
                                    else:
                                        results.append(0)
                            else:
                                if x[374] <= 0.0568627473:
                                    results.append(2)
                                else:
                                    if x[215] <= 0.0607843138:
                                        if x[408] <= 0.0078431377:
                                            results.append(6)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(6)
                        else:
                            if x[316] <= 0.0588235315:
                                results.append(2)
                            else:
                                results.append(5)
                    else:
                        if x[625] <= 0.0196078438:
                            if x[549] <= 0.9294117689:
                                results.append(4)
                            else:
                                results.append(0)
                        else:
                            if x[183] <= 0.9117647111:
                                if x[435] <= 0.3764705956:
                                    results.append(0)
                                else:
                                    results.append(8)
                            else:
                                if x[377] <= 0.2450980470:
                                    if x[581] <= 0.0529411770:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(8)
            else:
                if x[125] <= 0.1764705926:
                    if x[600] <= 0.8568627536:
                        if x[490] <= 0.5215686411:
                            if x[406] <= 0.0921568647:
                                results.append(0)
                            else:
                                if x[485] <= 0.0274509806:
                                    results.append(3)
                                else:
                                    results.append(8)
                        else:
                            if x[214] <= 0.0176470596:
                                results.append(2)
                            else:
                                if x[496] <= 0.1607843190:
                                    results.append(2)
                                else:
                                    results.append(2)
                    else:
                        if x[460] <= 0.3450980559:
                            if x[187] <= 0.1176470630:
                                results.append(5)
                            else:
                                if x[579] <= 0.7549019754:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(6)
                else:
                    if x[435] <= 0.0215686280:
                        results.append(0)
                    else:
                        if x[514] <= 0.0313725509:
                            results.append(2)
                        else:
                            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 21
    if time.time() < deadline or interrupt_flag.is_set():
        if x[429] <= 0.0098039219:
            if x[354] <= 0.0039215689:
                if x[437] <= 0.0098039219:
                    if x[290] <= 0.0529411770:
                        if x[315] <= 0.0686274543:
                            if x[272] <= 0.0058823531:
                                if x[580] <= 0.0764705911:
                                    if x[128] <= 0.2764706016:
                                        if x[324] <= 0.9941176474:
                                            if x[207] <= 0.8705882430:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[518] <= 0.2392156869:
                                            results.append(1)
                                        else:
                                            if x[657] <= 0.0274509806:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    results.append(2)
                            else:
                                results.append(5)
                        else:
                            results.append(0)
                    else:
                        if x[455] <= 0.0313725509:
                            if x[213] <= 0.2039215751:
                                results.append(2)
                            else:
                                if x[686] <= 0.6196078658:
                                    results.append(5)
                                else:
                                    results.append(8)
                        else:
                            results.append(0)
                else:
                    if x[152] <= 0.1843137294:
                        if x[518] <= 0.1215686314:
                            if x[655] <= 0.0215686280:
                                if x[599] <= 0.0019607844:
                                    results.append(9)
                                else:
                                    results.append(6)
                            else:
                                if x[289] <= 0.4235294238:
                                    results.append(2)
                                else:
                                    results.append(5)
                        else:
                            if x[403] <= 0.1686274558:
                                results.append(7)
                            else:
                                results.append(5)
                    else:
                        if x[463] <= 0.4254902005:
                            if x[129] <= 0.5352941453:
                                if x[236] <= 0.2784313858:
                                    if x[466] <= 0.9901960790:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(5)
                        else:
                            results.append(8)
            else:
                if x[182] <= 0.0333333341:
                    if x[541] <= 0.0098039219:
                        if x[315] <= 0.1274509840:
                            if x[152] <= 0.1235294119:
                                if x[349] <= 0.2196078487:
                                    if x[186] <= 0.0215686280:
                                        if x[355] <= 0.0156862754:
                                            results.append(7)
                                        else:
                                            if x[381] <= 0.6254902184:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(9)
                            else:
                                results.append(3)
                        else:
                            if x[268] <= 0.4784313887:
                                results.append(7)
                            else:
                                results.append(7)
                    else:
                        if x[382] <= 0.8294117749:
                            if x[239] <= 0.4529411867:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[381] <= 0.7862745225:
                                results.append(9)
                            else:
                                results.append(6)
                else:
                    if x[459] <= 0.0117647066:
                        if x[263] <= 0.0647058832:
                            if x[438] <= 0.0470588244:
                                if x[626] <= 0.7568627596:
                                    results.append(2)
                                else:
                                    results.append(8)
                            else:
                                if x[546] <= 0.4686274678:
                                    if x[184] <= 0.3313725591:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    if x[270] <= 0.9882352948:
                                        results.append(3)
                                    else:
                                        results.append(2)
                        else:
                            if x[462] <= 0.0392156867:
                                if x[494] <= 0.8882353008:
                                    if x[577] <= 0.7156862915:
                                        results.append(9)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(3)
                            else:
                                if x[461] <= 0.4156862795:
                                    if x[376] <= 0.3176470697:
                                        if x[683] <= 0.0019607844:
                                            results.append(2)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(9)
                                else:
                                    if x[656] <= 0.5078431517:
                                        results.append(2)
                                    else:
                                        if x[325] <= 0.9176470637:
                                            results.append(8)
                                        else:
                                            if x[545] <= 0.9901960790:
                                                results.append(3)
                                            else:
                                                results.append(4)
                    else:
                        if x[593] <= 0.2823529541:
                            if x[377] <= 0.0196078438:
                                if x[124] <= 0.0980392173:
                                    if x[155] <= 0.0156862754:
                                        results.append(9)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(2)
                            else:
                                if x[684] <= 0.4431372583:
                                    if x[211] <= 0.6156862974:
                                        if x[433] <= 0.9705882370:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                    else:
                                        if x[185] <= 0.9254902005:
                                            results.append(3)
                                        else:
                                            results.append(8)
                                else:
                                    results.append(8)
                        else:
                            if x[629] <= 0.1862745173:
                                results.append(2)
                            else:
                                results.append(3)
        else:
            if x[157] <= 0.0176470596:
                if x[96] <= 0.0058823531:
                    if x[211] <= 0.3450980484:
                        if x[296] <= 0.3588235378:
                            if x[379] <= 0.8725490272:
                                if x[459] <= 0.1000000015:
                                    if x[489] <= 0.1862745136:
                                        results.append(6)
                                    else:
                                        results.append(4)
                                else:
                                    if x[349] <= 0.2686274648:
                                        if x[411] <= 0.0098039219:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                if x[385] <= 0.0529411770:
                                    results.append(4)
                                else:
                                    results.append(6)
                        else:
                            if x[275] <= 0.0725490199:
                                if x[266] <= 0.0509803928:
                                    if x[268] <= 0.1725490205:
                                        results.append(9)
                                    else:
                                        results.append(4)
                                else:
                                    if x[325] <= 0.1411764780:
                                        results.append(5)
                                    else:
                                        if x[430] <= 0.5509804040:
                                            results.append(9)
                                        else:
                                            results.append(7)
                            else:
                                if x[655] <= 0.0117647061:
                                    results.append(5)
                                else:
                                    results.append(5)
                    else:
                        if x[220] <= 0.0098039219:
                            if x[568] <= 0.0274509806:
                                if x[626] <= 0.0215686280:
                                    if x[270] <= 0.0235294127:
                                        if x[352] <= 0.1156862751:
                                            results.append(5)
                                        else:
                                            if x[486] <= 0.4000000060:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                    else:
                                        if x[205] <= 0.3098039255:
                                            if x[238] <= 0.9941176474:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    if x[657] <= 0.6725490391:
                                        if x[711] <= 0.2313725501:
                                            results.append(9)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(3)
                            else:
                                if x[435] <= 0.2019607872:
                                    results.append(0)
                                else:
                                    results.append(2)
                        else:
                            results.append(5)
                else:
                    if x[435] <= 0.0725490227:
                        results.append(6)
                    else:
                        results.append(6)
            else:
                if x[434] <= 0.0039215689:
                    if x[325] <= 0.7823529541:
                        if x[380] <= 0.1176470593:
                            if x[244] <= 0.0215686280:
                                if x[654] <= 0.0647058859:
                                    results.append(6)
                                else:
                                    results.append(0)
                            else:
                                if x[264] <= 0.3588235378:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[458] <= 0.3647058979:
                                results.append(5)
                            else:
                                results.append(6)
                    else:
                        if x[579] <= 0.9098039269:
                            results.append(8)
                        else:
                            results.append(3)
                else:
                    if x[347] <= 0.0019607844:
                        if x[686] <= 0.0137254903:
                            if x[152] <= 0.0803921595:
                                if x[483] <= 0.3196078539:
                                    results.append(4)
                                else:
                                    results.append(2)
                            else:
                                if x[491] <= 0.3431372643:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            results.append(8)
                    else:
                        if x[683] <= 0.0078431377:
                            if x[326] <= 0.0196078438:
                                if x[464] <= 0.9901960790:
                                    if x[631] <= 0.6156862974:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    if x[569] <= 0.5745098293:
                                        results.append(4)
                                    else:
                                        results.append(6)
                            else:
                                if x[299] <= 0.1196078472:
                                    if x[540] <= 0.2627451010:
                                        results.append(4)
                                    else:
                                        results.append(6)
                                else:
                                    if x[606] <= 0.0588235315:
                                        results.append(2)
                                    else:
                                        results.append(8)
                        else:
                            if x[467] <= 0.0098039219:
                                if x[686] <= 0.0882352963:
                                    results.append(9)
                                else:
                                    results.append(8)
                            else:
                                if x[383] <= 0.0274509806:
                                    results.append(5)
                                else:
                                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 22
    if time.time() < deadline or interrupt_flag.is_set():
        if x[511] <= 0.1196078435:
            if x[406] <= 0.1941176504:
                if x[267] <= 0.3941176534:
                    if x[154] <= 0.0215686280:
                        if x[400] <= 0.0274509806:
                            if x[604] <= 0.8333333433:
                                if x[177] <= 0.5529411882:
                                    if x[261] <= 0.1098039225:
                                        results.append(7)
                                    else:
                                        if x[710] <= 0.5137255043:
                                            if x[238] <= 0.8686274588:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                        else:
                                            results.append(7)
                                else:
                                    results.append(3)
                            else:
                                results.append(6)
                        else:
                            if x[491] <= 0.4941176623:
                                if x[265] <= 0.0882352972:
                                    results.append(5)
                                else:
                                    results.append(9)
                            else:
                                if x[184] <= 0.0372549035:
                                    if x[245] <= 0.8058823645:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(4)
                    else:
                        if x[319] <= 0.0294117657:
                            if x[413] <= 0.0705882385:
                                if x[547] <= 0.0431372561:
                                    results.append(3)
                                else:
                                    if x[183] <= 0.7509804070:
                                        results.append(2)
                                    else:
                                        results.append(2)
                            else:
                                results.append(0)
                        else:
                            if x[486] <= 0.0568627454:
                                if x[382] <= 0.9470588267:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[212] <= 0.3941176683:
                                    results.append(6)
                                else:
                                    results.append(0)
                else:
                    if x[258] <= 0.0176470596:
                        if x[236] <= 0.1568627506:
                            if x[300] <= 0.3823529482:
                                if x[520] <= 0.5352941304:
                                    results.append(3)
                                else:
                                    if x[459] <= 0.9823529422:
                                        results.append(2)
                                    else:
                                        results.append(4)
                            else:
                                if x[323] <= 0.1823529489:
                                    results.append(4)
                                else:
                                    results.append(7)
                        else:
                            if x[550] <= 0.1333333366:
                                if x[653] <= 0.7176470757:
                                    if x[373] <= 0.8960784376:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(7)
                            else:
                                results.append(0)
                    else:
                        if x[260] <= 0.9941176474:
                            if x[661] <= 0.9588235319:
                                results.append(7)
                            else:
                                results.append(7)
                        else:
                            results.append(7)
            else:
                if x[262] <= 0.0019607844:
                    if x[465] <= 0.0078431377:
                        if x[609] <= 0.0039215689:
                            if x[374] <= 0.2490196154:
                                if x[323] <= 0.1176470630:
                                    if x[546] <= 0.4941176623:
                                        results.append(8)
                                    else:
                                        results.append(1)
                                else:
                                    if x[236] <= 0.8235294223:
                                        if x[543] <= 0.9980392158:
                                            if x[626] <= 0.8607843220:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(3)
                            else:
                                if x[491] <= 0.4254902005:
                                    results.append(4)
                                else:
                                    results.append(9)
                        else:
                            if x[259] <= 0.0803921595:
                                if x[128] <= 0.0666666701:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                results.append(8)
                    else:
                        if x[178] <= 0.0137254903:
                            if x[513] <= 0.4784313887:
                                if x[596] <= 0.3568627462:
                                    if x[460] <= 0.1862745136:
                                        results.append(4)
                                    else:
                                        if x[318] <= 0.0156862754:
                                            results.append(6)
                                        else:
                                            results.append(9)
                                else:
                                    if x[438] <= 0.6431372613:
                                        if x[379] <= 0.8529411852:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[319] <= 0.3686274663:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[516] <= 0.2803921718:
                                if x[229] <= 0.3039215803:
                                    if x[463] <= 0.9901960790:
                                        if x[578] <= 0.1725490242:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[625] <= 0.6098039448:
                                    results.append(8)
                                else:
                                    results.append(2)
                else:
                    if x[543] <= 0.0058823531:
                        if x[622] <= 0.3529411852:
                            if x[205] <= 0.1686274558:
                                if x[155] <= 0.0019607844:
                                    if x[220] <= 0.1901960820:
                                        if x[285] <= 0.4098039269:
                                            if x[574] <= 0.1745098084:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(5)
                                else:
                                    if x[688] <= 0.0941176489:
                                        results.append(3)
                                    else:
                                        results.append(4)
                            else:
                                if x[354] <= 0.0392156867:
                                    if x[289] <= 0.6764706075:
                                        results.append(3)
                                    else:
                                        results.append(5)
                                else:
                                    if x[401] <= 0.0568627464:
                                        results.append(8)
                                    else:
                                        if x[270] <= 0.6509804130:
                                            results.append(4)
                                        else:
                                            results.append(4)
                        else:
                            if x[627] <= 0.9568627477:
                                results.append(3)
                            else:
                                results.append(3)
                    else:
                        if x[573] <= 0.4156862795:
                            if x[126] <= 0.4607843310:
                                if x[372] <= 0.2333333418:
                                    if x[268] <= 0.9862745106:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    if x[686] <= 0.3490196178:
                                        results.append(4)
                                    else:
                                        results.append(8)
                            else:
                                results.append(8)
                        else:
                            if x[269] <= 0.0647058841:
                                if x[684] <= 0.0980392173:
                                    if x[160] <= 0.0313725509:
                                        results.append(6)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(8)
                            else:
                                if x[157] <= 0.9117647111:
                                    if x[463] <= 0.9901960790:
                                        if x[232] <= 0.2803921588:
                                            results.append(8)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[655] <= 0.8078431487:
                                            results.append(9)
                                        else:
                                            results.append(7)
                                else:
                                    results.append(2)
        else:
            if x[434] <= 0.0039215689:
                if x[350] <= 0.5078431517:
                    if x[400] <= 0.4137254953:
                        if x[462] <= 0.0274509806:
                            if x[511] <= 0.3705882430:
                                results.append(0)
                            else:
                                if x[186] <= 0.2372549102:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(2)
                    else:
                        if x[627] <= 0.0490196086:
                            results.append(0)
                        else:
                            if x[625] <= 0.3490196168:
                                results.append(0)
                            else:
                                if x[381] <= 0.1117647104:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[382] <= 0.6803921759:
                        if x[126] <= 0.1882352978:
                            results.append(0)
                        else:
                            results.append(5)
                    else:
                        if x[153] <= 0.9803921580:
                            results.append(3)
                        else:
                            results.append(3)
            else:
                if x[555] <= 0.1549019665:
                    if x[373] <= 0.0372549035:
                        if x[518] <= 0.1450980455:
                            if x[495] <= 0.3725490272:
                                if x[302] <= 0.0019607844:
                                    results.append(9)
                                else:
                                    results.append(8)
                            else:
                                results.append(2)
                        else:
                            if x[127] <= 0.0725490227:
                                if x[623] <= 0.6784313917:
                                    if x[405] <= 0.5941176713:
                                        results.append(2)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(8)
                            else:
                                if x[126] <= 0.6901960969:
                                    results.append(2)
                                else:
                                    results.append(2)
                    else:
                        if x[191] <= 0.3901960850:
                            if x[270] <= 0.5568627715:
                                if x[272] <= 0.1117647067:
                                    if x[215] <= 0.1254901979:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(8)
                            else:
                                if x[570] <= 0.0509803947:
                                    if x[513] <= 0.6764705926:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(0)
                        else:
                            if x[218] <= 0.9098039269:
                                results.append(5)
                            else:
                                results.append(4)
                else:
                    if x[472] <= 0.2196078524:
                        if x[102] <= 0.0058823531:
                            results.append(2)
                        else:
                            results.append(2)
                    else:
                        results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 23
    if time.time() < deadline or interrupt_flag.is_set():
        if x[289] <= 0.0019607844:
            if x[378] <= 0.5431372821:
                if x[101] <= 0.0058823531:
                    if x[455] <= 0.0235294132:
                        if x[346] <= 0.0098039219:
                            if x[514] <= 0.7647058964:
                                if x[234] <= 0.6411764920:
                                    if x[403] <= 0.0137254903:
                                        if x[463] <= 0.0568627454:
                                            results.append(3)
                                        else:
                                            if x[212] <= 0.2843137309:
                                                results.append(1)
                                            else:
                                                results.append(7)
                                    else:
                                        if x[320] <= 0.6470588446:
                                            results.append(3)
                                        else:
                                            results.append(8)
                                else:
                                    if x[179] <= 0.6901960969:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[179] <= 0.5725490451:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            if x[150] <= 0.0568627454:
                                if x[603] <= 0.4117647111:
                                    if x[541] <= 0.0156862754:
                                        if x[267] <= 0.6352941394:
                                            if x[606] <= 0.1078431383:
                                                results.append(4)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(5)
                                else:
                                    if x[209] <= 0.7901960909:
                                        if x[430] <= 0.9392156899:
                                            results.append(5)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(8)
                            else:
                                results.append(3)
                    else:
                        if x[413] <= 0.0333333351:
                            if x[156] <= 0.8098039329:
                                if x[354] <= 0.0490196086:
                                    results.append(5)
                                else:
                                    if x[436] <= 0.7254902124:
                                        results.append(0)
                                    else:
                                        if x[328] <= 0.7117647231:
                                            if x[355] <= 0.3843137473:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(4)
                            else:
                                if x[463] <= 0.8980392218:
                                    results.append(4)
                                else:
                                    results.append(2)
                        else:
                            if x[375] <= 0.8411764801:
                                if x[437] <= 0.5235294402:
                                    results.append(2)
                                else:
                                    results.append(4)
                            else:
                                if x[216] <= 0.4215686470:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[596] <= 0.2705882415:
                        if x[183] <= 0.1098039262:
                            results.append(2)
                        else:
                            results.append(6)
                    else:
                        if x[354] <= 0.2215686366:
                            results.append(2)
                        else:
                            if x[459] <= 0.0686274543:
                                results.append(2)
                            else:
                                results.append(2)
            else:
                if x[348] <= 0.2549019754:
                    if x[577] <= 0.0254901964:
                        if x[263] <= 0.0078431377:
                            if x[179] <= 0.0862745121:
                                if x[464] <= 0.3686274588:
                                    if x[272] <= 0.2352941260:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                        else:
                            if x[432] <= 0.5470588505:
                                results.append(9)
                            else:
                                results.append(6)
                    else:
                        if x[607] <= 0.5627451092:
                            if x[513] <= 0.5705882460:
                                if x[266] <= 0.5215686411:
                                    results.append(3)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(2)
                else:
                    if x[439] <= 0.0372549035:
                        if x[319] <= 0.0411764719:
                            if x[355] <= 0.0607843138:
                                if x[125] <= 0.4176470786:
                                    if x[431] <= 0.4254902154:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(2)
                            else:
                                results.append(3)
                        else:
                            if x[573] <= 0.8411764801:
                                if x[574] <= 0.9274509847:
                                    if x[486] <= 0.0078431377:
                                        results.append(3)
                                    else:
                                        if x[353] <= 0.8529411852:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                else:
                                    results.append(9)
                            else:
                                if x[656] <= 0.4254902154:
                                    if x[347] <= 0.9843137264:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(8)
                    else:
                        if x[430] <= 0.9784313738:
                            if x[324] <= 0.0215686280:
                                results.append(2)
                            else:
                                if x[435] <= 0.7078431547:
                                    if x[155] <= 0.1294117682:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[656] <= 0.2294117659:
                                results.append(6)
                            else:
                                results.append(3)
        else:
            if x[432] <= 0.0098039219:
                if x[596] <= 0.0333333351:
                    if x[182] <= 0.0235294122:
                        if x[487] <= 0.0882352963:
                            if x[442] <= 0.0725490227:
                                if x[605] <= 0.9215686321:
                                    if x[685] <= 0.0176470596:
                                        if x[292] <= 0.9901960790:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    if x[493] <= 0.8490196168:
                                        results.append(4)
                                    else:
                                        results.append(7)
                            else:
                                results.append(6)
                        else:
                            if x[518] <= 0.6000000089:
                                results.append(3)
                            else:
                                results.append(6)
                    else:
                        if x[126] <= 0.1490196157:
                            if x[386] <= 0.4450980444:
                                if x[544] <= 0.4882353097:
                                    if x[460] <= 0.3313725591:
                                        if x[295] <= 0.7784313858:
                                            results.append(5)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(7)
                            else:
                                results.append(0)
                        else:
                            if x[442] <= 0.0039215689:
                                results.append(6)
                            else:
                                results.append(6)
                else:
                    if x[571] <= 0.4196078479:
                        if x[429] <= 0.0470588244:
                            if x[177] <= 0.2431372590:
                                if x[348] <= 0.8980392218:
                                    results.append(0)
                                else:
                                    results.append(5)
                            else:
                                results.append(3)
                        else:
                            if x[272] <= 0.0490196086:
                                results.append(5)
                            else:
                                if x[623] <= 0.8921568692:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[372] <= 0.0078431377:
                            results.append(0)
                        else:
                            if x[381] <= 0.2725490332:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[428] <= 0.0372549035:
                    if x[603] <= 0.9941176474:
                        if x[514] <= 0.0098039219:
                            if x[546] <= 0.0862745121:
                                if x[374] <= 0.8294117749:
                                    if x[180] <= 0.4411764741:
                                        results.append(4)
                                    else:
                                        results.append(3)
                                else:
                                    if x[381] <= 0.6980392337:
                                        results.append(5)
                                    else:
                                        results.append(9)
                            else:
                                if x[296] <= 0.8960784376:
                                    if x[686] <= 0.5098039359:
                                        if x[517] <= 0.2960784435:
                                            results.append(9)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(8)
                        else:
                            if x[658] <= 0.0254901964:
                                if x[296] <= 0.6784313917:
                                    results.append(8)
                                else:
                                    results.append(2)
                            else:
                                if x[240] <= 0.9627451003:
                                    if x[553] <= 0.3627451137:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    if x[435] <= 0.9647058845:
                                        results.append(8)
                                    else:
                                        results.append(2)
                    else:
                        if x[353] <= 0.9941176474:
                            results.append(8)
                        else:
                            results.append(9)
                else:
                    if x[240] <= 0.2431372628:
                        if x[96] <= 0.0254901964:
                            if x[184] <= 0.1039215699:
                                if x[400] <= 0.6568627656:
                                    results.append(4)
                                else:
                                    if x[466] <= 0.2490196154:
                                        if x[576] <= 0.1862745136:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[211] <= 0.2294117734:
                                            results.append(4)
                                        else:
                                            results.append(4)
                            else:
                                if x[130] <= 0.0078431377:
                                    results.append(9)
                                else:
                                    results.append(6)
                        else:
                            if x[150] <= 0.5549019873:
                                results.append(6)
                            else:
                                results.append(6)
                    else:
                        if x[409] <= 0.1960784346:
                            if x[159] <= 0.6784313768:
                                results.append(5)
                            else:
                                results.append(0)
                        else:
                            if x[348] <= 0.0666666673:
                                if x[490] <= 0.9901960790:
                                    if x[374] <= 0.0980392173:
                                        if x[235] <= 0.1921568736:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[318] <= 0.8705882430:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(4)
                            else:
                                if x[246] <= 0.6274510026:
                                    if x[243] <= 0.8450980484:
                                        results.append(4)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(5)
    
    else:
      return vote_logic(results)
    
    # Tree 24
    if time.time() < deadline or interrupt_flag.is_set():
        if x[374] <= 0.0058823533:
            if x[437] <= 0.0039215689:
                if x[399] <= 0.0725490227:
                    if x[580] <= 0.0176470596:
                        if x[353] <= 0.5921568871:
                            if x[484] <= 0.0235294122:
                                if x[576] <= 0.3882353008:
                                    if x[378] <= 0.6725490391:
                                        results.append(1)
                                    else:
                                        if x[492] <= 0.2901960909:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[241] <= 0.2764706016:
                                        if x[211] <= 0.7156862915:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(3)
                            else:
                                results.append(2)
                        else:
                            if x[268] <= 0.9176470637:
                                if x[320] <= 0.1333333366:
                                    results.append(7)
                                else:
                                    if x[187] <= 0.0450980403:
                                        results.append(8)
                                    else:
                                        results.append(8)
                            else:
                                if x[436] <= 0.0921568666:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[347] <= 0.2823529541:
                            if x[379] <= 0.1294117719:
                                results.append(0)
                            else:
                                results.append(2)
                        else:
                            results.append(5)
                else:
                    if x[214] <= 0.0686274543:
                        if x[454] <= 0.7588235438:
                            results.append(0)
                        else:
                            results.append(6)
                    else:
                        results.append(0)
            else:
                if x[378] <= 0.5058823675:
                    if x[267] <= 0.2803921700:
                        if x[371] <= 0.0882352963:
                            if x[540] <= 0.0823529437:
                                if x[124] <= 0.2019607872:
                                    if x[242] <= 0.2549019679:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(2)
                            else:
                                if x[629] <= 0.9215686321:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            if x[236] <= 0.9529411793:
                                if x[414] <= 0.0588235315:
                                    if x[352] <= 0.2235294133:
                                        if x[606] <= 0.5960784405:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(6)
                            else:
                                results.append(6)
                    else:
                        if x[570] <= 0.8764705956:
                            if x[371] <= 0.8058823645:
                                if x[686] <= 0.0117647061:
                                    if x[487] <= 0.6352941394:
                                        if x[625] <= 0.9588235319:
                                            if x[266] <= 0.9941176474:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(7)
                            else:
                                results.append(9)
                        else:
                            results.append(2)
                else:
                    if x[489] <= 0.0372549035:
                        if x[351] <= 0.8980392218:
                            if x[383] <= 0.1705882438:
                                if x[566] <= 0.0568627454:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(9)
                        else:
                            if x[630] <= 0.9901960790:
                                if x[657] <= 0.9294117689:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(3)
                    else:
                        if x[180] <= 0.1509803981:
                            if x[465] <= 0.0352941193:
                                if x[513] <= 0.2921568751:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(9)
                        else:
                            if x[600] <= 0.8901960850:
                                results.append(8)
                            else:
                                if x[550] <= 0.8803921640:
                                    results.append(8)
                                else:
                                    results.append(8)
        else:
            if x[380] <= 0.0039215689:
                if x[568] <= 0.1000000015:
                    if x[487] <= 0.3058823645:
                        if x[329] <= 0.0960784350:
                            if x[289] <= 0.0078431377:
                                if x[154] <= 0.0392156879:
                                    results.append(5)
                                else:
                                    if x[185] <= 0.4254902005:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[461] <= 0.4568627626:
                                    results.append(6)
                                else:
                                    results.append(5)
                        else:
                            if x[405] <= 0.1568627506:
                                results.append(7)
                            else:
                                results.append(9)
                    else:
                        if x[269] <= 0.1000000015:
                            if x[572] <= 0.2647058964:
                                results.append(4)
                            else:
                                results.append(6)
                        else:
                            if x[461] <= 0.0509803928:
                                results.append(0)
                            else:
                                results.append(5)
                else:
                    if x[427] <= 0.7843137383:
                        if x[290] <= 0.3568627536:
                            if x[412] <= 0.0431372561:
                                if x[405] <= 0.7607843280:
                                    if x[156] <= 0.3862745166:
                                        results.append(5)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(5)
                            else:
                                if x[271] <= 0.0470588244:
                                    results.append(6)
                                else:
                                    results.append(0)
                        else:
                            if x[218] <= 0.0372549035:
                                if x[455] <= 0.2039215714:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(8)
                    else:
                        if x[595] <= 0.0019607844:
                            results.append(0)
                        else:
                            if x[539] <= 0.7352941334:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[550] <= 0.2000000030:
                    if x[514] <= 0.0274509815:
                        if x[579] <= 0.0588235296:
                            if x[572] <= 0.3862745166:
                                if x[292] <= 0.0156862750:
                                    if x[209] <= 0.0117647061:
                                        results.append(4)
                                    else:
                                        if x[687] <= 0.3235294297:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    if x[378] <= 0.0235294122:
                                        if x[402] <= 0.8470588326:
                                            results.append(9)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[494] <= 0.1078431401:
                                            if x[714] <= 0.6627451181:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                            else:
                                if x[406] <= 0.1333333366:
                                    if x[427] <= 0.1058823578:
                                        results.append(7)
                                    else:
                                        results.append(4)
                                else:
                                    if x[319] <= 0.9392156899:
                                        if x[299] <= 0.9862745106:
                                            if x[382] <= 0.4450980574:
                                                results.append(8)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[181] <= 0.0901960805:
                                            if x[293] <= 0.7176470757:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(4)
                        else:
                            results.append(3)
                    else:
                        if x[596] <= 0.4313725531:
                            if x[377] <= 0.2196078449:
                                if x[375] <= 0.3450980484:
                                    results.append(9)
                                else:
                                    if x[324] <= 0.0313725495:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                if x[657] <= 0.5823529661:
                                    if x[546] <= 0.0431372561:
                                        results.append(2)
                                    else:
                                        results.append(6)
                                else:
                                    if x[543] <= 0.5274509937:
                                        results.append(8)
                                    else:
                                        results.append(8)
                        else:
                            if x[515] <= 0.4509804100:
                                results.append(3)
                            else:
                                if x[375] <= 0.4725490361:
                                    results.append(8)
                                else:
                                    results.append(8)
                else:
                    if x[544] <= 0.5450980663:
                        if x[627] <= 0.0196078438:
                            if x[234] <= 0.7254902124:
                                if x[412] <= 0.7921568751:
                                    if x[412] <= 0.1098039262:
                                        if x[186] <= 0.2019607872:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(4)
                            else:
                                results.append(9)
                        else:
                            if x[491] <= 0.7470588386:
                                if x[155] <= 0.3823529482:
                                    if x[346] <= 0.6764706075:
                                        if x[326] <= 0.2588235307:
                                            results.append(5)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[185] <= 0.6254902035:
                                            results.append(3)
                                        else:
                                            if x[181] <= 0.2941176593:
                                                results.append(5)
                                            else:
                                                results.append(5)
                                else:
                                    if x[458] <= 0.0372549035:
                                        if x[429] <= 0.5607843250:
                                            if x[319] <= 0.8000000119:
                                                results.append(3)
                                            else:
                                                results.append(5)
                                        else:
                                            results.append(2)
                                    else:
                                        if x[602] <= 0.6313725710:
                                            results.append(8)
                                        else:
                                            results.append(3)
                            else:
                                if x[624] <= 0.1764705926:
                                    results.append(8)
                                else:
                                    results.append(6)
                    else:
                        if x[547] <= 0.2529411912:
                            if x[523] <= 0.7941176593:
                                results.append(8)
                            else:
                                results.append(6)
                        else:
                            if x[657] <= 0.0235294122:
                                if x[243] <= 0.0156862754:
                                    if x[178] <= 0.8019607961:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(2)
                            else:
                                results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 25
    if time.time() < deadline or interrupt_flag.is_set():
        if x[428] <= 0.1980392188:
            if x[461] <= 0.2803921700:
                if x[379] <= 0.5647059083:
                    if x[268] <= 0.1078431383:
                        if x[409] <= 0.2039215714:
                            if x[481] <= 0.4254902005:
                                if x[405] <= 0.0960784331:
                                    if x[206] <= 0.4921568707:
                                        results.append(0)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(5)
                            else:
                                results.append(0)
                        else:
                            if x[459] <= 0.0803921595:
                                if x[627] <= 0.0156862754:
                                    results.append(9)
                                else:
                                    results.append(5)
                            else:
                                if x[348] <= 0.0196078438:
                                    results.append(6)
                                else:
                                    results.append(6)
                    else:
                        if x[378] <= 0.0058823531:
                            if x[597] <= 0.1509803981:
                                if x[183] <= 0.0803921577:
                                    if x[327] <= 0.0098039219:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[411] <= 0.0078431377:
                                    if x[297] <= 0.8509804010:
                                        results.append(0)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(5)
                        else:
                            if x[157] <= 0.1490196101:
                                if x[241] <= 0.6921568811:
                                    results.append(5)
                                else:
                                    results.append(3)
                            else:
                                if x[659] <= 0.0117647061:
                                    results.append(3)
                                else:
                                    results.append(3)
                else:
                    if x[623] <= 0.1647058874:
                        if x[598] <= 0.3137255013:
                            if x[467] <= 0.9372549057:
                                if x[238] <= 0.2823529541:
                                    if x[604] <= 0.8274509907:
                                        if x[376] <= 0.7862745225:
                                            results.append(7)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(3)
                                else:
                                    if x[345] <= 0.2137254924:
                                        if x[380] <= 0.5901960880:
                                            results.append(1)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(9)
                            else:
                                results.append(3)
                        else:
                            if x[298] <= 0.0137254903:
                                if x[239] <= 0.8647058904:
                                    if x[493] <= 0.0431372561:
                                        results.append(5)
                                    else:
                                        if x[212] <= 0.7176470608:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                else:
                                    results.append(3)
                            else:
                                if x[268] <= 0.0372549039:
                                    results.append(8)
                                else:
                                    if x[511] <= 0.0058823531:
                                        if x[496] <= 0.4156862795:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(5)
                    else:
                        if x[317] <= 0.5862745345:
                            if x[186] <= 0.0215686280:
                                results.append(3)
                            else:
                                if x[551] <= 0.9862745106:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[352] <= 0.6411764920:
                                results.append(5)
                            else:
                                results.append(3)
            else:
                if x[151] <= 0.0137254908:
                    if x[235] <= 0.0039215689:
                        if x[438] <= 0.0058823531:
                            if x[375] <= 0.1156862788:
                                if x[594] <= 0.0274509811:
                                    if x[492] <= 0.7294117808:
                                        if x[658] <= 0.9901960790:
                                            if x[517] <= 0.0960784331:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[191] <= 0.2156862784:
                                    if x[323] <= 0.8313725591:
                                        results.append(8)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(5)
                        else:
                            if x[354] <= 0.0705882385:
                                if x[570] <= 0.1352941208:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(2)
                    else:
                        if x[570] <= 0.0215686285:
                            if x[438] <= 0.8960784376:
                                if x[352] <= 0.1254901998:
                                    if x[216] <= 0.0725490227:
                                        if x[289] <= 0.9313725531:
                                            results.append(3)
                                        else:
                                            results.append(8)
                                    else:
                                        if x[604] <= 0.8960784376:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                else:
                                    if x[374] <= 0.2705882378:
                                        if x[295] <= 0.4450980574:
                                            if x[188] <= 0.1588235348:
                                                results.append(7)
                                            else:
                                                results.append(8)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[713] <= 0.3039215803:
                                            results.append(4)
                                        else:
                                            results.append(9)
                            else:
                                if x[521] <= 0.5921568722:
                                    results.append(7)
                                else:
                                    results.append(9)
                        else:
                            if x[233] <= 0.9156862795:
                                if x[552] <= 0.0549019612:
                                    if x[460] <= 0.4960784316:
                                        if x[320] <= 0.4627451040:
                                            results.append(7)
                                        else:
                                            results.append(5)
                                    else:
                                        if x[655] <= 0.1705882438:
                                            results.append(2)
                                        else:
                                            if x[131] <= 0.0490196086:
                                                results.append(8)
                                            else:
                                                results.append(8)
                                else:
                                    results.append(2)
                            else:
                                results.append(7)
                else:
                    if x[123] <= 0.3549019694:
                        if x[630] <= 0.2843137383:
                            if x[487] <= 0.0235294122:
                                results.append(3)
                            else:
                                if x[541] <= 0.3784313798:
                                    results.append(6)
                                else:
                                    results.append(2)
                        else:
                            if x[348] <= 0.2843137383:
                                if x[241] <= 0.4823529422:
                                    results.append(1)
                                else:
                                    if x[573] <= 0.9843137264:
                                        results.append(2)
                                    else:
                                        results.append(2)
                            else:
                                if x[465] <= 0.1372549087:
                                    results.append(8)
                                else:
                                    results.append(8)
                    else:
                        if x[320] <= 0.0372549035:
                            results.append(2)
                        else:
                            results.append(1)
        else:
            if x[381] <= 0.0313725499:
                if x[463] <= 0.0196078438:
                    if x[628] <= 0.0372549035:
                        results.append(4)
                    else:
                        if x[353] <= 0.1647058874:
                            if x[599] <= 0.0039215689:
                                results.append(0)
                            else:
                                if x[349] <= 0.6450980604:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(6)
                else:
                    if x[524] <= 0.0196078443:
                        if x[236] <= 0.8058823645:
                            if x[320] <= 0.4705882519:
                                results.append(2)
                            else:
                                results.append(5)
                        else:
                            results.append(5)
                    else:
                        if x[571] <= 0.0705882385:
                            results.append(3)
                        else:
                            if x[485] <= 0.9411764741:
                                results.append(6)
                            else:
                                results.append(6)
            else:
                if x[598] <= 0.0078431377:
                    if x[497] <= 0.7490196228:
                        if x[268] <= 0.0254901974:
                            if x[212] <= 0.0196078438:
                                if x[465] <= 0.5352941304:
                                    results.append(4)
                                else:
                                    if x[428] <= 0.8607843220:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                results.append(9)
                        else:
                            if x[156] <= 0.1392156892:
                                if x[295] <= 0.9705882370:
                                    if x[180] <= 0.2882352993:
                                        if x[714] <= 0.1294117719:
                                            if x[373] <= 0.0549019631:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                        else:
                                            if x[605] <= 0.0019607844:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                    else:
                                        if x[456] <= 0.2705882415:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(7)
                            else:
                                results.append(4)
                    else:
                        if x[457] <= 0.9901960790:
                            results.append(2)
                        else:
                            results.append(6)
                else:
                    if x[626] <= 0.0509803928:
                        if x[158] <= 0.9901960790:
                            if x[414] <= 0.3313725591:
                                results.append(6)
                            else:
                                results.append(6)
                        else:
                            results.append(6)
                    else:
                        if x[101] <= 0.0078431377:
                            if x[523] <= 0.0862745140:
                                if x[548] <= 0.4333333522:
                                    if x[233] <= 0.2137254924:
                                        if x[573] <= 0.9686274529:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(0)
                            else:
                                if x[483] <= 0.8137255013:
                                    if x[177] <= 0.3607843257:
                                        results.append(5)
                                    else:
                                        results.append(3)
                                else:
                                    if x[269] <= 0.9901960790:
                                        results.append(6)
                                    else:
                                        results.append(0)
                        else:
                            if x[264] <= 0.1490196139:
                                results.append(2)
                            else:
                                if x[373] <= 0.8627451062:
                                    results.append(6)
                                else:
                                    results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 26
    if time.time() < deadline or interrupt_flag.is_set():
        if x[463] <= 0.0568627473:
            if x[377] <= 0.1078431383:
                if x[496] <= 0.0568627473:
                    if x[458] <= 0.0294117657:
                        if x[290] <= 0.0196078438:
                            if x[233] <= 0.4607843161:
                                results.append(3)
                            else:
                                results.append(0)
                        else:
                            if x[658] <= 0.6000000238:
                                results.append(7)
                            else:
                                results.append(7)
                    else:
                        if x[465] <= 0.0470588244:
                            results.append(5)
                        else:
                            if x[406] <= 0.2019607872:
                                results.append(0)
                            else:
                                results.append(9)
                else:
                    if x[629] <= 0.4352941215:
                        if x[317] <= 0.4862745255:
                            if x[239] <= 0.0274509815:
                                results.append(6)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[294] <= 0.9000000060:
                            if x[208] <= 0.2666666806:
                                results.append(0)
                            else:
                                if x[215] <= 0.9901960790:
                                    results.append(0)
                                else:
                                    if x[190] <= 0.0137254903:
                                        results.append(0)
                                    else:
                                        results.append(0)
                        else:
                            results.append(0)
            else:
                if x[152] <= 0.0215686280:
                    if x[348] <= 0.0254901964:
                        if x[375] <= 0.1254902035:
                            if x[575] <= 0.1392156873:
                                if x[237] <= 0.1627451070:
                                    if x[601] <= 0.1411764771:
                                        if x[325] <= 0.2058823593:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(6)
                        else:
                            results.append(5)
                    else:
                        if x[243] <= 0.7019608021:
                            if x[654] <= 0.1215686295:
                                if x[296] <= 0.2411764786:
                                    if x[295] <= 0.0862745121:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    if x[372] <= 0.1529411841:
                                        results.append(8)
                                    else:
                                        results.append(9)
                            else:
                                if x[209] <= 0.4000000060:
                                    results.append(1)
                                else:
                                    results.append(5)
                        else:
                            if x[328] <= 0.0294117648:
                                if x[244] <= 0.9686274529:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                results.append(0)
                else:
                    if x[290] <= 0.6588235497:
                        if x[316] <= 0.1490196101:
                            if x[457] <= 0.5705882609:
                                if x[488] <= 0.4039215818:
                                    if x[128] <= 0.9607843161:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(2)
                            else:
                                results.append(2)
                        else:
                            if x[260] <= 0.7725490332:
                                results.append(5)
                            else:
                                results.append(5)
                    else:
                        if x[183] <= 0.4156862795:
                            results.append(6)
                        else:
                            if x[241] <= 0.8725490272:
                                if x[524] <= 0.7607843280:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(0)
        else:
            if x[430] <= 0.0235294122:
                if x[262] <= 0.0058823531:
                    if x[205] <= 0.0607843138:
                        if x[512] <= 0.0058823531:
                            if x[405] <= 0.0333333351:
                                results.append(7)
                            else:
                                if x[437] <= 0.5235294253:
                                    if x[294] <= 0.0490196086:
                                        if x[519] <= 0.1313725524:
                                            if x[515] <= 0.8392156959:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[291] <= 0.0647058841:
                                            if x[214] <= 0.9901960790:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(9)
                        else:
                            if x[239] <= 0.5254902095:
                                if x[124] <= 0.0568627454:
                                    results.append(5)
                                else:
                                    results.append(2)
                            else:
                                results.append(5)
                    else:
                        if x[517] <= 0.0215686280:
                            if x[579] <= 0.2196078449:
                                results.append(3)
                            else:
                                results.append(3)
                        else:
                            if x[317] <= 0.0411764719:
                                if x[209] <= 0.6509804130:
                                    results.append(2)
                                else:
                                    results.append(7)
                            else:
                                results.append(8)
                else:
                    if x[239] <= 0.5156863034:
                        if x[442] <= 0.1470588297:
                            if x[348] <= 0.4352941364:
                                if x[569] <= 0.2313725576:
                                    if x[516] <= 0.1372549050:
                                        if x[351] <= 0.5470588244:
                                            results.append(7)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(2)
                            else:
                                if x[242] <= 0.0137254903:
                                    results.append(5)
                                else:
                                    if x[514] <= 0.0176470596:
                                        results.append(8)
                                    else:
                                        results.append(8)
                        else:
                            if x[288] <= 0.3686274588:
                                results.append(6)
                            else:
                                results.append(6)
                    else:
                        if x[155] <= 0.0764705911:
                            if x[375] <= 0.1980392188:
                                if x[461] <= 0.8803921640:
                                    if x[523] <= 0.3294117767:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    if x[318] <= 0.1529411785:
                                        results.append(7)
                                    else:
                                        results.append(9)
                            else:
                                if x[189] <= 0.0078431377:
                                    results.append(9)
                                else:
                                    results.append(8)
                        else:
                            if x[316] <= 0.0725490227:
                                results.append(8)
                            else:
                                results.append(5)
            else:
                if x[568] <= 0.0019607844:
                    if x[209] <= 0.1627451032:
                        if x[294] <= 0.2745098174:
                            if x[124] <= 0.1529411823:
                                if x[317] <= 0.5980392396:
                                    if x[237] <= 0.0882352963:
                                        if x[187] <= 0.0313725509:
                                            if x[605] <= 0.4666666724:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(4)
                            else:
                                results.append(6)
                        else:
                            if x[546] <= 0.0352941193:
                                if x[263] <= 0.0019607844:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[355] <= 0.0666666683:
                                    if x[241] <= 0.9941176474:
                                        results.append(1)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(4)
                    else:
                        if x[325] <= 0.0098039219:
                            if x[635] <= 0.0176470596:
                                if x[551] <= 0.2098039240:
                                    if x[515] <= 0.3627451099:
                                        if x[410] <= 0.9000000060:
                                            results.append(5)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(6)
                            else:
                                if x[213] <= 0.5058823824:
                                    results.append(2)
                                else:
                                    results.append(5)
                        else:
                            if x[184] <= 0.0313725499:
                                if x[187] <= 0.0529411789:
                                    if x[518] <= 0.9254902005:
                                        if x[549] <= 0.9705882370:
                                            if x[269] <= 0.2588235363:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[436] <= 0.7509804070:
                                    if x[243] <= 0.3000000007:
                                        results.append(9)
                                    else:
                                        results.append(8)
                                else:
                                    if x[516] <= 0.7549019754:
                                        if x[372] <= 0.0156862754:
                                            results.append(9)
                                        else:
                                            if x[412] <= 0.0117647061:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                    else:
                                        results.append(9)
                else:
                    if x[73] <= 0.0078431377:
                        if x[266] <= 0.0372549035:
                            if x[684] <= 0.0843137279:
                                if x[490] <= 0.2274509892:
                                    if x[240] <= 0.4627451152:
                                        results.append(3)
                                    else:
                                        results.append(2)
                                else:
                                    if x[373] <= 0.4313725680:
                                        results.append(2)
                                    else:
                                        results.append(2)
                            else:
                                if x[462] <= 0.8607843220:
                                    results.append(8)
                                else:
                                    results.append(8)
                        else:
                            if x[631] <= 0.4333333373:
                                if x[354] <= 0.0313725509:
                                    if x[184] <= 0.0078431377:
                                        results.append(5)
                                    else:
                                        results.append(6)
                                else:
                                    if x[434] <= 0.2274509836:
                                        results.append(0)
                                    else:
                                        if x[491] <= 0.9686274529:
                                            if x[347] <= 0.8117647171:
                                                results.append(3)
                                            else:
                                                results.append(6)
                                        else:
                                            results.append(2)
                            else:
                                if x[493] <= 0.9823529422:
                                    if x[379] <= 0.9901960790:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(6)
                    else:
                        if x[373] <= 0.7196078598:
                            results.append(6)
                        else:
                            results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 27
    if time.time() < deadline or interrupt_flag.is_set():
        if x[488] <= 0.1156862751:
            if x[187] <= 0.0098039219:
                if x[568] <= 0.0568627454:
                    if x[378] <= 0.0901960805:
                        if x[487] <= 0.0196078438:
                            if x[271] <= 0.1372549087:
                                if x[460] <= 0.1705882400:
                                    if x[348] <= 0.0784313763:
                                        if x[288] <= 0.0686274543:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(4)
                            else:
                                if x[267] <= 0.2509803995:
                                    if x[573] <= 0.7058823705:
                                        if x[549] <= 0.0372549035:
                                            results.append(9)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(7)
                                else:
                                    if x[370] <= 0.9627451003:
                                        if x[579] <= 0.2117647156:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(7)
                        else:
                            if x[490] <= 0.3843137324:
                                if x[598] <= 0.0862745121:
                                    results.append(9)
                                else:
                                    results.append(0)
                            else:
                                results.append(6)
                    else:
                        if x[402] <= 0.0137254903:
                            if x[231] <= 0.0333333351:
                                if x[269] <= 0.1254901998:
                                    if x[152] <= 0.5823529512:
                                        if x[602] <= 0.6921568811:
                                            if x[548] <= 0.0215686280:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    if x[625] <= 0.0039215689:
                                        results.append(1)
                                    else:
                                        results.append(3)
                            else:
                                results.append(3)
                        else:
                            if x[653] <= 0.0137254903:
                                if x[543] <= 0.4764706045:
                                    if x[152] <= 0.0117647061:
                                        if x[237] <= 0.1098039225:
                                            results.append(4)
                                        else:
                                            if x[607] <= 0.1803921610:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(6)
                            else:
                                if x[631] <= 0.2960784435:
                                    results.append(5)
                                else:
                                    if x[428] <= 0.3176470622:
                                        results.append(3)
                                    else:
                                        results.append(3)
                else:
                    if x[295] <= 0.0156862754:
                        if x[99] <= 0.0039215689:
                            if x[483] <= 0.8901960850:
                                if x[241] <= 0.8843137324:
                                    results.append(5)
                                else:
                                    if x[572] <= 0.2647058889:
                                        results.append(2)
                                    else:
                                        results.append(0)
                            else:
                                if x[213] <= 0.9019607902:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[572] <= 0.7294117659:
                                results.append(6)
                            else:
                                results.append(6)
                    else:
                        if x[184] <= 0.0117647061:
                            results.append(5)
                        else:
                            if x[580] <= 0.7960784435:
                                if x[264] <= 0.0509803947:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(3)
            else:
                if x[428] <= 0.3529411852:
                    if x[317] <= 0.0058823531:
                        if x[320] <= 0.9901960790:
                            if x[550] <= 0.4352941364:
                                if x[564] <= 0.0098039219:
                                    if x[513] <= 0.5333333611:
                                        if x[295] <= 0.0294117648:
                                            results.append(5)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(3)
                            else:
                                if x[236] <= 0.9901960790:
                                    if x[297] <= 0.4509804100:
                                        results.append(3)
                                    else:
                                        if x[490] <= 0.0156862754:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(3)
                        else:
                            results.append(5)
                    else:
                        if x[271] <= 0.0078431377:
                            if x[273] <= 0.0450980403:
                                if x[207] <= 0.9941176474:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(0)
                        else:
                            if x[349] <= 0.7627451122:
                                if x[323] <= 0.0745098069:
                                    if x[318] <= 0.3254902065:
                                        results.append(0)
                                    else:
                                        if x[212] <= 0.5509803966:
                                            results.append(4)
                                        else:
                                            results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[300] <= 0.0411764719:
                                    results.append(8)
                                else:
                                    results.append(5)
                else:
                    if x[408] <= 0.1627450995:
                        if x[599] <= 0.0176470596:
                            results.append(0)
                        else:
                            if x[231] <= 0.4843137264:
                                if x[291] <= 0.2549019679:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[234] <= 0.5000000149:
                            if x[537] <= 0.2882353067:
                                if x[291] <= 0.3803921714:
                                    if x[656] <= 0.3627451062:
                                        results.append(4)
                                    else:
                                        results.append(3)
                                else:
                                    if x[380] <= 0.8372549117:
                                        results.append(5)
                                    else:
                                        results.append(9)
                            else:
                                results.append(2)
                        else:
                            if x[491] <= 0.0098039219:
                                results.append(5)
                            else:
                                results.append(4)
        else:
            if x[271] <= 0.0039215689:
                if x[551] <= 0.0215686280:
                    if x[290] <= 0.0274509806:
                        if x[459] <= 0.3274509907:
                            if x[295] <= 0.2137254924:
                                results.append(1)
                            else:
                                if x[462] <= 0.5333333611:
                                    results.append(1)
                                else:
                                    if x[660] <= 0.1470588259:
                                        results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            if x[549] <= 0.2078431472:
                                if x[186] <= 0.9196078479:
                                    if x[124] <= 0.1490196139:
                                        results.append(5)
                                    else:
                                        results.append(2)
                                else:
                                    if x[431] <= 0.3647058904:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[492] <= 0.9941176474:
                                    results.append(6)
                                else:
                                    results.append(4)
                    else:
                        if x[656] <= 0.1607843190:
                            if x[296] <= 0.6431372762:
                                if x[515] <= 0.7509804070:
                                    results.append(9)
                                else:
                                    results.append(6)
                            else:
                                results.append(4)
                        else:
                            if x[543] <= 0.0392156877:
                                results.append(5)
                            else:
                                if x[183] <= 0.5686274618:
                                    results.append(8)
                                else:
                                    results.append(8)
                else:
                    if x[151] <= 0.0078431377:
                        if x[574] <= 0.7588235438:
                            if x[518] <= 0.7411764860:
                                if x[598] <= 0.0666666701:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(2)
                        else:
                            if x[406] <= 0.0313725499:
                                results.append(6)
                            else:
                                results.append(6)
                    else:
                        if x[346] <= 0.1901960820:
                            if x[182] <= 0.0117647061:
                                results.append(6)
                            else:
                                if x[571] <= 0.1686274558:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            if x[546] <= 0.4862745181:
                                results.append(8)
                            else:
                                results.append(6)
            else:
                if x[375] <= 0.0078431375:
                    if x[155] <= 0.2117647082:
                        if x[401] <= 0.0137254903:
                            if x[550] <= 0.0745098069:
                                if x[378] <= 0.4313725680:
                                    if x[262] <= 0.8588235378:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    if x[349] <= 0.5509804040:
                                        if x[405] <= 0.7039215863:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(8)
                            else:
                                results.append(2)
                        else:
                            if x[598] <= 0.0019607844:
                                if x[378] <= 0.3313725591:
                                    if x[373] <= 0.9372549057:
                                        if x[374] <= 0.0176470596:
                                            if x[245] <= 0.2549019754:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(9)
                            else:
                                results.append(0)
                    else:
                        if x[683] <= 0.1000000015:
                            if x[569] <= 0.5764706135:
                                if x[433] <= 0.0215686280:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(2)
                        else:
                            results.append(8)
                else:
                    if x[183] <= 0.4647058994:
                        if x[457] <= 0.6137255132:
                            if x[460] <= 0.6392157078:
                                if x[294] <= 0.0156862754:
                                    results.append(4)
                                else:
                                    results.append(5)
                            else:
                                if x[353] <= 0.6980392337:
                                    results.append(8)
                                else:
                                    results.append(8)
                        else:
                            if x[401] <= 0.9098039269:
                                results.append(4)
                            else:
                                if x[296] <= 0.0196078438:
                                    results.append(4)
                                else:
                                    results.append(4)
                    else:
                        if x[510] <= 0.0411764719:
                            if x[436] <= 0.0058823531:
                                results.append(0)
                            else:
                                if x[430] <= 0.9705882370:
                                    if x[601] <= 0.8039215803:
                                        results.append(8)
                                    else:
                                        if x[345] <= 0.1627451042:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                else:
                                    if x[540] <= 0.1490196139:
                                        results.append(9)
                                    else:
                                        results.append(8)
                        else:
                            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 28
    if time.time() < deadline or interrupt_flag.is_set():
        if x[523] <= 0.0058823533:
            if x[264] <= 0.0137254908:
                if x[438] <= 0.0039215689:
                    if x[207] <= 0.0098039219:
                        if x[347] <= 0.4686274678:
                            if x[152] <= 0.4235294312:
                                if x[406] <= 0.8627451062:
                                    results.append(1)
                                else:
                                    if x[459] <= 0.9549019635:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(2)
                        else:
                            if x[429] <= 0.4254902154:
                                results.append(5)
                            else:
                                results.append(4)
                    else:
                        if x[488] <= 0.0137254908:
                            if x[409] <= 0.2392156888:
                                if x[399] <= 0.0725490227:
                                    if x[241] <= 0.8725490272:
                                        results.append(1)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(0)
                            else:
                                results.append(4)
                        else:
                            if x[684] <= 0.4431372583:
                                if x[375] <= 0.0078431377:
                                    if x[515] <= 0.7901960909:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                else:
                    if x[180] <= 0.0058823531:
                        if x[409] <= 0.9941176474:
                            if x[484] <= 0.0137254908:
                                if x[289] <= 0.1549019665:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                results.append(2)
                        else:
                            if x[457] <= 0.1411764773:
                                results.append(4)
                            else:
                                results.append(4)
                    else:
                        if x[491] <= 0.6941176653:
                            if x[372] <= 0.0156862754:
                                if x[183] <= 0.7803921700:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                results.append(5)
                        else:
                            if x[543] <= 0.8725490272:
                                results.append(7)
                            else:
                                results.append(2)
            else:
                if x[232] <= 0.3392156959:
                    if x[400] <= 0.0333333341:
                        if x[515] <= 0.2470588312:
                            if x[623] <= 0.0313725499:
                                if x[742] <= 0.0098039219:
                                    if x[572] <= 0.7058823705:
                                        if x[293] <= 0.9784313738:
                                            if x[436] <= 0.4411764741:
                                                results.append(5)
                                            else:
                                                results.append(9)
                                        else:
                                            if x[240] <= 0.3058823571:
                                                results.append(1)
                                            else:
                                                results.append(7)
                                    else:
                                        if x[433] <= 0.6176470667:
                                            if x[244] <= 0.7803921700:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                        else:
                                            if x[631] <= 0.0058823531:
                                                results.append(4)
                                            else:
                                                results.append(1)
                                else:
                                    results.append(7)
                            else:
                                if x[593] <= 0.7901960909:
                                    if x[521] <= 0.2745098062:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(3)
                        else:
                            if x[544] <= 0.9862745106:
                                if x[462] <= 0.4117647111:
                                    if x[297] <= 0.0705882357:
                                        results.append(6)
                                    else:
                                        results.append(8)
                                else:
                                    if x[403] <= 0.0039215689:
                                        results.append(8)
                                    else:
                                        if x[430] <= 0.5627451092:
                                            results.append(8)
                                        else:
                                            results.append(8)
                            else:
                                if x[159] <= 0.5431372821:
                                    if x[262] <= 0.4882353097:
                                        results.append(4)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(2)
                    else:
                        if x[568] <= 0.0333333341:
                            if x[189] <= 0.0607843157:
                                if x[430] <= 0.2392156869:
                                    if x[266] <= 0.8509804010:
                                        results.append(4)
                                    else:
                                        if x[604] <= 0.1000000015:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                else:
                                    if x[157] <= 0.0352941193:
                                        if x[468] <= 0.0137254903:
                                            if x[381] <= 0.8294117749:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                if x[409] <= 0.4215686321:
                                    results.append(5)
                                else:
                                    if x[432] <= 0.5509804189:
                                        results.append(4)
                                    else:
                                        results.append(4)
                        else:
                            if x[540] <= 0.7078431547:
                                if x[374] <= 0.9901960790:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[266] <= 0.2039215788:
                                    results.append(6)
                                else:
                                    results.append(0)
                else:
                    if x[185] <= 0.9235294163:
                        if x[303] <= 0.0549019612:
                            if x[373] <= 0.3156862855:
                                if x[381] <= 0.3490196168:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                results.append(7)
                        else:
                            results.append(8)
                    else:
                        results.append(0)
        else:
            if x[656] <= 0.0333333341:
                if x[292] <= 0.1588235348:
                    if x[343] <= 0.0019607844:
                        if x[155] <= 0.0470588249:
                            if x[460] <= 0.8960784376:
                                if x[150] <= 0.0039215689:
                                    results.append(3)
                                else:
                                    results.append(6)
                            else:
                                results.append(2)
                        else:
                            if x[516] <= 0.0078431377:
                                if x[512] <= 0.3235294223:
                                    results.append(3)
                                else:
                                    results.append(2)
                            else:
                                if x[238] <= 0.7333333492:
                                    results.append(2)
                                else:
                                    results.append(2)
                    else:
                        if x[574] <= 0.4039215744:
                            if x[242] <= 0.7588235438:
                                if x[209] <= 0.4607843310:
                                    results.append(4)
                                else:
                                    if x[523] <= 0.7980392277:
                                        if x[353] <= 0.6901960969:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(5)
                            else:
                                if x[411] <= 0.7705882490:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[380] <= 0.0666666701:
                                if x[315] <= 0.9941176474:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[543] <= 0.2862745225:
                                    results.append(6)
                                else:
                                    results.append(6)
                else:
                    if x[574] <= 0.2490196116:
                        if x[461] <= 0.2686274648:
                            if x[269] <= 0.6254902184:
                                results.append(7)
                            else:
                                results.append(7)
                        else:
                            if x[233] <= 0.0117647061:
                                if x[455] <= 0.2254901975:
                                    results.append(9)
                                else:
                                    results.append(4)
                            else:
                                results.append(9)
                    else:
                        if x[301] <= 0.8588235378:
                            if x[272] <= 0.1235294119:
                                if x[288] <= 0.4196078479:
                                    if x[578] <= 0.9941176474:
                                        if x[517] <= 0.5666666925:
                                            if x[514] <= 0.1235294156:
                                                results.append(6)
                                            else:
                                                results.append(6)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(7)
                            else:
                                results.append(5)
                        else:
                            results.append(0)
            else:
                if x[378] <= 0.0274509806:
                    if x[385] <= 0.0235294122:
                        if x[400] <= 0.4137255102:
                            if x[263] <= 0.0058823531:
                                results.append(3)
                            else:
                                results.append(2)
                        else:
                            results.append(5)
                    else:
                        if x[187] <= 0.0078431377:
                            if x[267] <= 0.7588235438:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[595] <= 0.7313725650:
                                if x[483] <= 0.9411764741:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[543] <= 0.5411764979:
                        if x[261] <= 0.0215686280:
                            if x[262] <= 0.1666666716:
                                if x[292] <= 0.9509803951:
                                    if x[402] <= 0.9901960790:
                                        results.append(3)
                                    else:
                                        if x[606] <= 0.9235294163:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(5)
                        else:
                            if x[298] <= 0.1470588259:
                                if x[607] <= 0.0235294122:
                                    if x[464] <= 0.0470588244:
                                        results.append(5)
                                    else:
                                        results.append(3)
                                else:
                                    if x[347] <= 0.8137255013:
                                        results.append(5)
                                    else:
                                        results.append(5)
                            else:
                                if x[319] <= 0.6568627656:
                                    if x[344] <= 0.0450980412:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    if x[686] <= 0.8058823645:
                                        results.append(0)
                                    else:
                                        results.append(8)
                    else:
                        if x[522] <= 0.7274509966:
                            results.append(8)
                        else:
                            if x[541] <= 0.5078431517:
                                results.append(8)
                            else:
                                results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 29
    if time.time() < deadline or interrupt_flag.is_set():
        if x[488] <= 0.0039215689:
            if x[380] <= 0.6294117868:
                if x[181] <= 0.0078431377:
                    if x[410] <= 0.2000000030:
                        if x[568] <= 0.1352941245:
                            if x[347] <= 0.0372549035:
                                if x[629] <= 0.8450980484:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[577] <= 0.5235294253:
                                    results.append(9)
                                else:
                                    results.append(5)
                        else:
                            if x[484] <= 0.3078431413:
                                if x[405] <= 0.3862745166:
                                    results.append(5)
                                else:
                                    if x[318] <= 0.3176470622:
                                        results.append(5)
                                    else:
                                        results.append(5)
                            else:
                                results.append(0)
                    else:
                        if x[569] <= 0.0882352963:
                            if x[405] <= 0.1686274568:
                                if x[259] <= 0.0137254903:
                                    if x[657] <= 0.1568627506:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(7)
                            else:
                                results.append(4)
                        else:
                            results.append(0)
                else:
                    if x[414] <= 0.0274509815:
                        if x[517] <= 0.0647058841:
                            if x[300] <= 0.7568627596:
                                if x[351] <= 0.0843137279:
                                    if x[148] <= 0.0470588247:
                                        if x[430] <= 0.1313725524:
                                            if x[379] <= 0.1039215699:
                                                results.append(5)
                                            else:
                                                results.append(5)
                                        else:
                                            if x[411] <= 0.0490196086:
                                                results.append(5)
                                            else:
                                                results.append(0)
                                    else:
                                        results.append(2)
                                else:
                                    if x[457] <= 0.7470588386:
                                        if x[269] <= 0.2137254998:
                                            if x[183] <= 0.5941176564:
                                                results.append(1)
                                            else:
                                                results.append(5)
                                        else:
                                            if x[205] <= 0.0058823531:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                    else:
                                        results.append(8)
                            else:
                                if x[126] <= 0.1549019665:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[438] <= 0.0098039219:
                                if x[377] <= 0.3549019694:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[244] <= 0.7529411912:
                                    if x[262] <= 0.4294117726:
                                        results.append(2)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(0)
                    else:
                        if x[241] <= 0.0980392173:
                            if x[159] <= 0.2686274573:
                                results.append(6)
                            else:
                                if x[217] <= 0.8960784376:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(0)
            else:
                if x[436] <= 0.5843137503:
                    if x[371] <= 0.0215686283:
                        if x[289] <= 0.2392156944:
                            if x[626] <= 0.0588235315:
                                results.append(6)
                            else:
                                if x[576] <= 0.6058823764:
                                    if x[497] <= 0.6254902184:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    if x[375] <= 0.9941176474:
                                        results.append(3)
                                    else:
                                        results.append(3)
                        else:
                            if x[374] <= 0.9901960790:
                                results.append(3)
                            else:
                                results.append(5)
                    else:
                        if x[349] <= 0.0705882357:
                            results.append(9)
                        else:
                            if x[159] <= 0.0725490227:
                                results.append(5)
                            else:
                                results.append(5)
                else:
                    if x[405] <= 0.0078431377:
                        if x[597] <= 0.0058823531:
                            if x[265] <= 0.0235294132:
                                results.append(7)
                            else:
                                if x[297] <= 0.9823529422:
                                    results.append(7)
                                else:
                                    results.append(7)
                        else:
                            if x[437] <= 0.7529411912:
                                results.append(1)
                            else:
                                results.append(3)
                    else:
                        if x[625] <= 0.0098039219:
                            if x[494] <= 0.8215686381:
                                if x[492] <= 0.3392156959:
                                    results.append(3)
                                else:
                                    if x[435] <= 0.9901960790:
                                        results.append(9)
                                    else:
                                        if x[210] <= 0.0274509806:
                                            results.append(4)
                                        else:
                                            if x[520] <= 0.7215686440:
                                                results.append(9)
                                            else:
                                                results.append(9)
                            else:
                                results.append(4)
                        else:
                            if x[291] <= 0.6764706075:
                                if x[681] <= 0.0019607844:
                                    if x[214] <= 0.1254902035:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[460] <= 0.0607843138:
                                    results.append(4)
                                else:
                                    results.append(9)
        else:
            if x[318] <= 0.0019607844:
                if x[348] <= 0.6039215922:
                    if x[465] <= 0.0078431377:
                        if x[553] <= 0.0098039219:
                            if x[462] <= 0.1450980417:
                                results.append(2)
                            else:
                                if x[236] <= 0.7568627596:
                                    if x[600] <= 0.4843137413:
                                        if x[130] <= 0.0490196086:
                                            if x[546] <= 0.8941176534:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(3)
                        else:
                            if x[400] <= 0.6372549087:
                                if x[576] <= 0.9803921580:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(6)
                    else:
                        if x[681] <= 0.0470588244:
                            if x[126] <= 0.0117647061:
                                if x[509] <= 0.1490196139:
                                    if x[656] <= 0.0196078438:
                                        if x[521] <= 0.1980392197:
                                            results.append(9)
                                        else:
                                            if x[411] <= 0.3490196168:
                                                results.append(2)
                                            else:
                                                results.append(4)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(2)
                            else:
                                if x[490] <= 0.7745098174:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            if x[600] <= 0.9568627477:
                                results.append(7)
                            else:
                                results.append(7)
                else:
                    if x[353] <= 0.0039215689:
                        if x[190] <= 0.0568627454:
                            if x[296] <= 0.4725490361:
                                if x[521] <= 0.5686274767:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(6)
                        else:
                            results.append(5)
                    else:
                        if x[377] <= 0.3666666746:
                            results.append(4)
                        else:
                            if x[293] <= 0.4980392307:
                                results.append(8)
                            else:
                                results.append(8)
            else:
                if x[402] <= 0.7588235438:
                    if x[456] <= 0.0352941193:
                        if x[156] <= 0.0117647066:
                            if x[210] <= 0.2784313858:
                                if x[437] <= 0.6980392337:
                                    results.append(4)
                                else:
                                    results.append(7)
                            else:
                                if x[433] <= 0.8549019694:
                                    results.append(9)
                                else:
                                    if x[545] <= 0.8686274588:
                                        if x[547] <= 0.3647058904:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                    else:
                                        results.append(9)
                        else:
                            if x[319] <= 0.4843137413:
                                if x[347] <= 0.2137254924:
                                    results.append(2)
                                else:
                                    results.append(8)
                            else:
                                if x[467] <= 0.8352941275:
                                    if x[158] <= 0.9627451003:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(8)
                    else:
                        if x[687] <= 0.0078431377:
                            if x[572] <= 0.4568627477:
                                if x[711] <= 0.0980392173:
                                    if x[343] <= 0.0588235296:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(9)
                            else:
                                if x[459] <= 0.2568627596:
                                    if x[238] <= 0.9000000060:
                                        results.append(6)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(3)
                        else:
                            if x[545] <= 0.0607843138:
                                if x[435] <= 0.8921568692:
                                    results.append(9)
                                else:
                                    results.append(9)
                            else:
                                results.append(7)
                else:
                    if x[411] <= 0.0392156867:
                        if x[457] <= 0.1823529452:
                            if x[263] <= 0.9294117689:
                                if x[629] <= 0.8647058904:
                                    results.append(5)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                        else:
                            if x[512] <= 0.1705882363:
                                results.append(4)
                            else:
                                results.append(6)
                    else:
                        if x[541] <= 0.1352941245:
                            if x[271] <= 0.0450980403:
                                if x[550] <= 0.2705882415:
                                    results.append(4)
                                else:
                                    results.append(6)
                            else:
                                if x[244] <= 0.1176470630:
                                    results.append(4)
                                else:
                                    if x[429] <= 0.9901960790:
                                        results.append(4)
                                    else:
                                        results.append(4)
                        else:
                            if x[461] <= 0.1039215736:
                                results.append(0)
                            else:
                                if x[347] <= 0.8509804010:
                                    results.append(6)
                                else:
                                    results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 30
    if time.time() < deadline or interrupt_flag.is_set():
        if x[372] <= 0.0411764719:
            if x[349] <= 0.0019607844:
                if x[540] <= 0.0647058841:
                    if x[265] <= 0.0274509815:
                        if x[373] <= 0.0098039219:
                            if x[176] <= 0.0215686280:
                                if x[406] <= 0.8588235378:
                                    if x[598] <= 0.4000000209:
                                        results.append(7)
                                    else:
                                        results.append(2)
                                else:
                                    if x[354] <= 0.2725490220:
                                        if x[183] <= 0.5000000149:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[233] <= 0.0215686285:
                                    results.append(2)
                                else:
                                    results.append(7)
                        else:
                            if x[598] <= 0.9568627477:
                                if x[572] <= 0.0156862754:
                                    results.append(5)
                                else:
                                    results.append(6)
                            else:
                                results.append(8)
                    else:
                        if x[260] <= 0.0294117648:
                            if x[604] <= 0.1019607857:
                                if x[262] <= 0.0627450983:
                                    results.append(9)
                                else:
                                    if x[437] <= 0.6784313917:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[155] <= 0.2607843205:
                                    results.append(5)
                                else:
                                    if x[655] <= 0.3372549117:
                                        results.append(6)
                                    else:
                                        results.append(8)
                        else:
                            if x[344] <= 0.2823529467:
                                if x[488] <= 0.4803921729:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                results.append(8)
                else:
                    if x[516] <= 0.5725490451:
                        if x[459] <= 0.6901960969:
                            if x[331] <= 0.3882353082:
                                results.append(5)
                            else:
                                results.append(0)
                        else:
                            if x[570] <= 0.6215686500:
                                if x[271] <= 0.5274510086:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(2)
                    else:
                        if x[496] <= 0.7529411912:
                            results.append(2)
                        else:
                            results.append(2)
            else:
                if x[319] <= 0.0019607844:
                    if x[521] <= 0.0431372561:
                        if x[467] <= 0.0137254903:
                            if x[152] <= 0.9607843161:
                                if x[403] <= 0.1176470630:
                                    if x[491] <= 0.5196078718:
                                        results.append(1)
                                    else:
                                        if x[660] <= 0.1098039262:
                                            if x[295] <= 0.2607843205:
                                                results.append(8)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[349] <= 0.9784313738:
                                        results.append(2)
                                    else:
                                        results.append(1)
                            else:
                                results.append(2)
                        else:
                            results.append(3)
                    else:
                        if x[513] <= 0.7117647231:
                            if x[292] <= 0.0431372561:
                                if x[294] <= 0.8529411852:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(1)
                        else:
                            if x[437] <= 0.4745098092:
                                results.append(2)
                            else:
                                results.append(8)
                else:
                    if x[655] <= 0.0137254908:
                        if x[430] <= 0.0333333351:
                            if x[625] <= 0.0078431377:
                                if x[212] <= 0.1235294119:
                                    if x[352] <= 0.3333333433:
                                        results.append(1)
                                    else:
                                        results.append(7)
                                else:
                                    if x[295] <= 0.8313725591:
                                        results.append(9)
                                    else:
                                        results.append(3)
                            else:
                                if x[320] <= 0.9901960790:
                                    results.append(3)
                                else:
                                    results.append(5)
                        else:
                            if x[265] <= 0.7254902124:
                                if x[380] <= 0.4392157048:
                                    results.append(5)
                                else:
                                    results.append(4)
                            else:
                                if x[351] <= 0.8176470697:
                                    if x[520] <= 0.0058823531:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(6)
                    else:
                        if x[323] <= 0.9705882370:
                            if x[325] <= 0.0058823531:
                                if x[466] <= 0.8333333433:
                                    if x[485] <= 0.3607843295:
                                        if x[437] <= 0.9686274529:
                                            if x[319] <= 0.5411764979:
                                                results.append(5)
                                            else:
                                                results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(8)
                                else:
                                    if x[378] <= 0.9235294163:
                                        results.append(3)
                                    else:
                                        results.append(5)
                            else:
                                if x[545] <= 0.9784313738:
                                    if x[510] <= 0.0352941193:
                                        if x[291] <= 0.0607843157:
                                            results.append(8)
                                        else:
                                            if x[601] <= 0.8529411852:
                                                results.append(8)
                                            else:
                                                results.append(8)
                                    else:
                                        results.append(0)
                                else:
                                    if x[433] <= 0.9000000060:
                                        results.append(9)
                                    else:
                                        results.append(4)
                        else:
                            if x[687] <= 0.9862745106:
                                if x[291] <= 0.0607843157:
                                    results.append(3)
                                else:
                                    if x[298] <= 0.1254901998:
                                        results.append(5)
                                    else:
                                        if x[432] <= 0.2588235438:
                                            results.append(3)
                                        else:
                                            results.append(8)
                            else:
                                results.append(8)
        else:
            if x[325] <= 0.0137254908:
                if x[271] <= 0.0666666683:
                    if x[623] <= 0.2941176593:
                        if x[572] <= 0.8058823645:
                            if x[516] <= 0.2215686291:
                                if x[328] <= 0.1745098084:
                                    if x[687] <= 0.1137254946:
                                        if x[352] <= 0.0058823531:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(4)
                            else:
                                results.append(4)
                        else:
                            if x[541] <= 0.3921568692:
                                if x[379] <= 0.9450980425:
                                    results.append(6)
                                else:
                                    results.append(5)
                            else:
                                if x[492] <= 0.9137254953:
                                    results.append(6)
                                else:
                                    results.append(6)
                    else:
                        if x[434] <= 0.1235294119:
                            if x[373] <= 0.8490196168:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(2)
                else:
                    if x[568] <= 0.1137254927:
                        if x[356] <= 0.0137254903:
                            if x[210] <= 0.7901960909:
                                results.append(5)
                            else:
                                results.append(5)
                        else:
                            if x[190] <= 0.0058823531:
                                if x[630] <= 0.8117647171:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                results.append(4)
                    else:
                        if x[378] <= 0.0058823531:
                            if x[357] <= 0.1137254946:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(5)
            else:
                if x[238] <= 0.2411764711:
                    if x[571] <= 0.4568627626:
                        if x[348] <= 0.8078431487:
                            if x[408] <= 0.1352941180:
                                results.append(0)
                            else:
                                if x[655] <= 0.9274509847:
                                    if x[510] <= 0.2568627484:
                                        if x[326] <= 0.9901960790:
                                            results.append(4)
                                        else:
                                            if x[343] <= 0.7470588386:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[290] <= 0.3215686418:
                                if x[428] <= 0.3000000045:
                                    results.append(3)
                                else:
                                    results.append(8)
                            else:
                                results.append(7)
                    else:
                        if x[573] <= 0.8568627536:
                            if x[656] <= 0.3098039255:
                                if x[625] <= 0.0176470596:
                                    results.append(0)
                                else:
                                    results.append(4)
                            else:
                                results.append(8)
                        else:
                            if x[350] <= 0.4627451152:
                                results.append(6)
                            else:
                                results.append(6)
                else:
                    if x[468] <= 0.0039215689:
                        if x[413] <= 0.0156862750:
                            if x[210] <= 0.0156862754:
                                results.append(7)
                            else:
                                if x[681] <= 0.5254902095:
                                    if x[495] <= 0.0058823533:
                                        if x[429] <= 0.0352941179:
                                            results.append(8)
                                        else:
                                            if x[434] <= 0.0509803947:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                    else:
                                        if x[375] <= 0.1627450995:
                                            results.append(9)
                                        else:
                                            results.append(4)
                                else:
                                    results.append(7)
                        else:
                            results.append(4)
                    else:
                        if x[652] <= 0.0196078438:
                            if x[571] <= 0.2117647082:
                                if x[318] <= 0.3470588326:
                                    if x[297] <= 0.8039215803:
                                        results.append(5)
                                    else:
                                        results.append(9)
                                else:
                                    if x[265] <= 0.9941176474:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                if x[326] <= 0.9784313738:
                                    results.append(6)
                                else:
                                    results.append(0)
                        else:
                            if x[455] <= 0.1666666716:
                                if x[344] <= 0.4941176623:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 31
    if time.time() < deadline or interrupt_flag.is_set():
        if x[350] <= 0.4333333373:
            if x[596] <= 0.0470588244:
                if x[428] <= 0.0039215689:
                    if x[259] <= 0.0156862747:
                        if x[270] <= 0.0117647061:
                            if x[656] <= 0.4196078479:
                                if x[660] <= 0.1784313768:
                                    if x[98] <= 0.0117647061:
                                        if x[574] <= 0.3686274588:
                                            results.append(9)
                                        else:
                                            if x[522] <= 0.0803921595:
                                                results.append(6)
                                            else:
                                                results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(4)
                            else:
                                if x[657] <= 0.9254902005:
                                    results.append(9)
                                else:
                                    results.append(5)
                        else:
                            if x[658] <= 0.0607843138:
                                if x[410] <= 0.0725490209:
                                    if x[570] <= 0.3156862855:
                                        results.append(7)
                                    else:
                                        results.append(5)
                                else:
                                    if x[244] <= 0.0078431377:
                                        results.append(2)
                                    else:
                                        if x[208] <= 0.4176470712:
                                            results.append(7)
                                        else:
                                            results.append(7)
                            else:
                                if x[544] <= 0.1529411785:
                                    if x[377] <= 0.2274509817:
                                        if x[401] <= 0.2588235363:
                                            if x[654] <= 0.0529411789:
                                                results.append(7)
                                            else:
                                                results.append(0)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[575] <= 0.0901960805:
                                            results.append(8)
                                        else:
                                            results.append(9)
                                else:
                                    if x[684] <= 0.9941176474:
                                        if x[185] <= 0.2666666806:
                                            results.append(8)
                                        else:
                                            if x[515] <= 0.9196078479:
                                                results.append(8)
                                            else:
                                                results.append(8)
                                    else:
                                        results.append(8)
                    else:
                        if x[381] <= 0.0803921595:
                            results.append(7)
                        else:
                            if x[177] <= 0.6607843339:
                                if x[239] <= 0.2803921700:
                                    results.append(7)
                                else:
                                    if x[211] <= 0.9980392158:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                results.append(7)
                else:
                    if x[572] <= 0.7058823705:
                        if x[461] <= 0.0549019631:
                            if x[352] <= 0.0078431377:
                                if x[491] <= 0.2235294133:
                                    results.append(0)
                                else:
                                    results.append(2)
                            else:
                                if x[300] <= 0.0686274543:
                                    results.append(4)
                                else:
                                    results.append(9)
                        else:
                            if x[210] <= 0.1470588297:
                                if x[514] <= 0.1196078435:
                                    if x[320] <= 0.2098039240:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[659] <= 0.0588235296:
                                        results.append(2)
                                    else:
                                        results.append(4)
                            else:
                                if x[355] <= 0.0019607844:
                                    if x[206] <= 0.0019607844:
                                        if x[461] <= 0.9901960790:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[632] <= 0.7666666806:
                                            results.append(9)
                                        else:
                                            results.append(5)
                                else:
                                    if x[468] <= 0.0235294122:
                                        if x[512] <= 0.2529411782:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[455] <= 0.6627451032:
                                            results.append(9)
                                        else:
                                            results.append(4)
                    else:
                        if x[542] <= 0.0803921595:
                            if x[710] <= 0.0823529437:
                                if x[427] <= 0.6941176504:
                                    results.append(9)
                                else:
                                    results.append(4)
                            else:
                                results.append(7)
                        else:
                            if x[314] <= 0.2745098099:
                                if x[627] <= 0.0980392173:
                                    if x[509] <= 0.0176470596:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
            else:
                if x[381] <= 0.1098039225:
                    if x[263] <= 0.0215686280:
                        if x[631] <= 0.2647058889:
                            if x[434] <= 0.0843137279:
                                results.append(0)
                            else:
                                if x[539] <= 0.5196078718:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            if x[632] <= 0.2098039240:
                                results.append(5)
                            else:
                                results.append(0)
                    else:
                        if x[542] <= 0.2980392277:
                            if x[433] <= 0.0156862754:
                                if x[187] <= 0.0352941193:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(5)
                        else:
                            results.append(0)
                else:
                    if x[375] <= 0.1078431383:
                        if x[386] <= 0.0509803928:
                            if x[155] <= 0.0333333351:
                                if x[461] <= 0.8235294223:
                                    results.append(2)
                                else:
                                    results.append(1)
                            else:
                                if x[656] <= 0.5725490451:
                                    if x[629] <= 0.7254902124:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(3)
                        else:
                            results.append(6)
                    else:
                        if x[401] <= 0.0980392173:
                            if x[217] <= 0.0882352963:
                                results.append(8)
                            else:
                                if x[596] <= 0.9901960790:
                                    results.append(8)
                                else:
                                    results.append(8)
                        else:
                            if x[102] <= 0.0627451017:
                                if x[407] <= 0.0274509806:
                                    results.append(0)
                                else:
                                    if x[655] <= 0.0823529419:
                                        results.append(2)
                                    else:
                                        if x[356] <= 0.0137254903:
                                            results.append(5)
                                        else:
                                            results.append(8)
                            else:
                                if x[213] <= 0.3215686381:
                                    results.append(6)
                                else:
                                    results.append(6)
        else:
            if x[207] <= 0.0098039219:
                if x[436] <= 0.5372549295:
                    if x[462] <= 0.2882353067:
                        if x[485] <= 0.9529411793:
                            if x[489] <= 0.0039215689:
                                if x[292] <= 0.2862745225:
                                    if x[379] <= 0.3901960850:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    if x[625] <= 0.5078431377:
                                        results.append(7)
                                    else:
                                        results.append(3)
                            else:
                                results.append(1)
                        else:
                            results.append(6)
                    else:
                        if x[291] <= 0.1627451032:
                            if x[244] <= 0.9862745106:
                                if x[242] <= 0.9901960790:
                                    if x[459] <= 0.9509803951:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(8)
                else:
                    if x[126] <= 0.0372549035:
                        if x[323] <= 0.1647058874:
                            results.append(5)
                        else:
                            if x[319] <= 0.0745098051:
                                if x[297] <= 0.9745098054:
                                    results.append(6)
                                else:
                                    results.append(1)
                            else:
                                if x[438] <= 0.1019607857:
                                    results.append(9)
                                else:
                                    if x[542] <= 0.2529411912:
                                        results.append(4)
                                    else:
                                        results.append(6)
                    else:
                        if x[461] <= 0.1882352978:
                            results.append(3)
                        else:
                            results.append(1)
            else:
                if x[654] <= 0.1980392188:
                    if x[270] <= 0.0411764719:
                        if x[214] <= 0.0411764723:
                            if x[290] <= 0.6941176653:
                                if x[550] <= 0.5529412031:
                                    if x[631] <= 0.9901960790:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(3)
                            else:
                                if x[661] <= 0.0078431377:
                                    results.append(6)
                                else:
                                    results.append(5)
                        else:
                            if x[406] <= 0.7960784435:
                                results.append(5)
                            else:
                                results.append(5)
                    else:
                        if x[458] <= 0.2392156944:
                            if x[406] <= 0.8098039329:
                                if x[658] <= 0.6176470667:
                                    results.append(9)
                                else:
                                    results.append(3)
                            else:
                                if x[488] <= 0.3058823645:
                                    results.append(3)
                                else:
                                    results.append(8)
                        else:
                            results.append(8)
                else:
                    if x[514] <= 0.0960784331:
                        if x[288] <= 0.2450980470:
                            if x[262] <= 0.4843137413:
                                if x[570] <= 0.6137255132:
                                    if x[318] <= 0.4352941364:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[323] <= 0.8137255013:
                                    results.append(5)
                                else:
                                    results.append(3)
                        else:
                            if x[260] <= 0.9490196109:
                                results.append(5)
                            else:
                                results.append(3)
                    else:
                        if x[624] <= 0.9862745106:
                            if x[485] <= 0.0372549035:
                                if x[373] <= 0.0647058841:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                        else:
                            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 32
    if time.time() < deadline or interrupt_flag.is_set():
        if x[155] <= 0.0098039219:
            if x[458] <= 0.0078431375:
                if x[488] <= 0.5039215982:
                    if x[431] <= 0.0176470596:
                        if x[270] <= 0.2509803995:
                            if x[462] <= 0.4843137413:
                                if x[376] <= 0.1803921610:
                                    if x[269] <= 0.5352941304:
                                        results.append(7)
                                    else:
                                        results.append(0)
                                else:
                                    if x[374] <= 0.4803921729:
                                        results.append(3)
                                    else:
                                        results.append(5)
                            else:
                                if x[322] <= 0.7372549176:
                                    results.append(1)
                                else:
                                    if x[206] <= 0.0137254903:
                                        results.append(1)
                                    else:
                                        results.append(1)
                        else:
                            if x[381] <= 0.0627450999:
                                if x[300] <= 0.1431372557:
                                    results.append(5)
                                else:
                                    if x[631] <= 0.9784313738:
                                        results.append(7)
                                    else:
                                        results.append(0)
                            else:
                                if x[351] <= 0.4607843161:
                                    if x[401] <= 0.4078431427:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    if x[464] <= 0.4764706045:
                                        results.append(7)
                                    else:
                                        results.append(9)
                    else:
                        if x[264] <= 0.6450980604:
                            if x[181] <= 0.5921568871:
                                if x[322] <= 0.2215686366:
                                    results.append(4)
                                else:
                                    results.append(5)
                            else:
                                results.append(3)
                        else:
                            if x[570] <= 0.0196078438:
                                if x[489] <= 0.0411764719:
                                    if x[604] <= 0.0490196105:
                                        results.append(9)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(4)
                            else:
                                if x[354] <= 0.1784313805:
                                    results.append(5)
                                else:
                                    results.append(9)
                else:
                    if x[157] <= 0.1882352978:
                        if x[433] <= 0.9019607902:
                            if x[602] <= 0.3490196168:
                                results.append(9)
                            else:
                                results.append(7)
                        else:
                            if x[265] <= 0.1764705926:
                                if x[487] <= 0.7176470757:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[344] <= 0.2000000030:
                                    results.append(8)
                                else:
                                    results.append(8)
                    else:
                        if x[185] <= 0.9254902005:
                            results.append(1)
                        else:
                            results.append(1)
            else:
                if x[570] <= 0.0156862754:
                    if x[123] <= 0.1588235348:
                        if x[210] <= 0.3058823645:
                            if x[240] <= 0.8745098114:
                                if x[355] <= 0.2019607946:
                                    if x[382] <= 0.0117647061:
                                        results.append(4)
                                    else:
                                        if x[262] <= 0.5078431517:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[576] <= 0.3549019769:
                                    results.append(8)
                                else:
                                    results.append(7)
                        else:
                            if x[206] <= 0.1529411823:
                                if x[320] <= 0.2823529541:
                                    if x[426] <= 0.9627451003:
                                        if x[487] <= 0.9901960790:
                                            if x[239] <= 0.2000000030:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(9)
                                else:
                                    if x[465] <= 0.9901960790:
                                        if x[431] <= 0.9156862795:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(4)
                            else:
                                if x[354] <= 0.5156862885:
                                    if x[209] <= 0.9862745106:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    if x[203] <= 0.2509804070:
                                        if x[412] <= 0.0686274543:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(9)
                    else:
                        results.append(6)
                else:
                    if x[298] <= 0.0117647061:
                        if x[543] <= 0.9352941215:
                            if x[464] <= 0.0411764719:
                                results.append(8)
                            else:
                                if x[435] <= 0.7019608021:
                                    results.append(2)
                                else:
                                    results.append(6)
                        else:
                            if x[468] <= 0.1745098084:
                                results.append(6)
                            else:
                                if x[513] <= 0.2862745151:
                                    results.append(6)
                                else:
                                    results.append(6)
                    else:
                        if x[346] <= 0.1078431383:
                            if x[264] <= 0.4941176474:
                                if x[434] <= 0.6392157078:
                                    results.append(2)
                                else:
                                    results.append(1)
                            else:
                                results.append(8)
                        else:
                            if x[267] <= 0.2058823630:
                                if x[511] <= 0.0411764719:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[439] <= 0.0254901964:
                                    results.append(8)
                                else:
                                    results.append(0)
        else:
            if x[318] <= 0.1450980455:
                if x[488] <= 0.0196078434:
                    if x[270] <= 0.0196078438:
                        if x[149] <= 0.0254901964:
                            if x[540] <= 0.0039215689:
                                if x[517] <= 0.0372549035:
                                    results.append(3)
                                else:
                                    results.append(1)
                            else:
                                if x[631] <= 0.3274509907:
                                    results.append(2)
                                else:
                                    results.append(5)
                        else:
                            results.append(3)
                    else:
                        if x[484] <= 0.0372549035:
                            if x[521] <= 0.0313725509:
                                if x[407] <= 0.8274509907:
                                    results.append(0)
                                else:
                                    results.append(3)
                            else:
                                if x[344] <= 0.1705882363:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[404] <= 0.0215686280:
                                results.append(0)
                            else:
                                if x[660] <= 0.0901960805:
                                    results.append(2)
                                else:
                                    results.append(8)
                else:
                    if x[267] <= 0.9294117689:
                        if x[375] <= 0.0058823531:
                            if x[569] <= 0.2058823556:
                                if x[466] <= 0.0215686280:
                                    results.append(8)
                                else:
                                    if x[151] <= 0.0333333351:
                                        results.append(4)
                                    else:
                                        results.append(2)
                            else:
                                if x[489] <= 0.2352941185:
                                    results.append(2)
                                else:
                                    if x[322] <= 0.1666666716:
                                        if x[259] <= 0.1058823541:
                                            results.append(2)
                                        else:
                                            results.append(2)
                                    else:
                                        results.append(2)
                        else:
                            if x[553] <= 0.0294117648:
                                if x[437] <= 0.0058823531:
                                    if x[517] <= 0.3196078539:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    if x[510] <= 0.1686274558:
                                        if x[597] <= 0.0901960805:
                                            results.append(6)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(2)
                            else:
                                results.append(2)
                    else:
                        if x[180] <= 0.6294117719:
                            if x[656] <= 0.0078431377:
                                if x[403] <= 0.0666666701:
                                    results.append(1)
                                else:
                                    results.append(2)
                            else:
                                results.append(1)
                        else:
                            results.append(2)
            else:
                if x[400] <= 0.1431372613:
                    if x[150] <= 0.5980392396:
                        if x[298] <= 0.0117647061:
                            if x[440] <= 0.1647058874:
                                if x[214] <= 0.2215686366:
                                    results.append(1)
                                else:
                                    if x[162] <= 0.0274509806:
                                        if x[211] <= 0.8196078539:
                                            results.append(8)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(5)
                            else:
                                if x[262] <= 0.5372549035:
                                    results.append(6)
                                else:
                                    results.append(5)
                        else:
                            if x[432] <= 0.0862745102:
                                if x[294] <= 0.6588235348:
                                    results.append(0)
                                else:
                                    results.append(3)
                            else:
                                if x[632] <= 0.9529411793:
                                    if x[461] <= 0.3176470697:
                                        results.append(9)
                                    else:
                                        if x[405] <= 0.8176470697:
                                            results.append(8)
                                        else:
                                            if x[624] <= 0.4294117689:
                                                results.append(8)
                                            else:
                                                results.append(8)
                                else:
                                    results.append(8)
                    else:
                        if x[289] <= 0.4980392307:
                            if x[240] <= 0.1490196148:
                                results.append(3)
                            else:
                                results.append(3)
                        else:
                            if x[432] <= 0.0254901967:
                                results.append(5)
                            else:
                                results.append(0)
                else:
                    if x[244] <= 0.0078431377:
                        if x[414] <= 0.0039215689:
                            if x[463] <= 0.5647058934:
                                if x[270] <= 0.4078431576:
                                    if x[578] <= 0.7431372702:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(0)
                            else:
                                if x[269] <= 0.0196078438:
                                    results.append(6)
                                else:
                                    results.append(4)
                        else:
                            if x[185] <= 0.9901960790:
                                results.append(6)
                            else:
                                results.append(6)
                    else:
                        if x[386] <= 0.0235294122:
                            if x[461] <= 0.3019607998:
                                if x[658] <= 0.2176470682:
                                    results.append(5)
                                else:
                                    results.append(0)
                            else:
                                results.append(8)
                        else:
                            if x[238] <= 0.1000000015:
                                results.append(0)
                            else:
                                if x[579] <= 0.9823529422:
                                    results.append(0)
                                else:
                                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 33
    if time.time() < deadline or interrupt_flag.is_set():
        if x[551] <= 0.0019607844:
            if x[317] <= 0.0019607844:
                if x[232] <= 0.3529411852:
                    if x[409] <= 0.1509803981:
                        if x[594] <= 0.0137254903:
                            if x[635] <= 0.0607843138:
                                if x[290] <= 0.0019607844:
                                    if x[465] <= 0.0450980403:
                                        if x[544] <= 0.2431372628:
                                            if x[406] <= 0.8352941275:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            if x[264] <= 0.0078431377:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(3)
                                else:
                                    if x[293] <= 0.0823529419:
                                        results.append(2)
                                    else:
                                        results.append(5)
                            else:
                                if x[184] <= 0.3509804010:
                                    results.append(1)
                                else:
                                    results.append(2)
                        else:
                            if x[352] <= 0.2784313783:
                                if x[491] <= 0.2392156944:
                                    results.append(0)
                                else:
                                    results.append(5)
                            else:
                                if x[488] <= 0.0627451017:
                                    results.append(3)
                                else:
                                    results.append(2)
                    else:
                        if x[347] <= 0.0607843157:
                            if x[568] <= 0.4960784465:
                                if x[564] <= 0.0196078438:
                                    if x[432] <= 0.0960784340:
                                        if x[576] <= 0.2823529541:
                                            results.append(7)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[269] <= 0.7117647231:
                                            results.append(8)
                                        else:
                                            results.append(1)
                                else:
                                    results.append(3)
                            else:
                                if x[295] <= 0.0431372561:
                                    if x[211] <= 0.8568627536:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(1)
                        else:
                            if x[494] <= 0.0941176526:
                                if x[570] <= 0.0392156877:
                                    if x[355] <= 0.0215686283:
                                        results.append(9)
                                    else:
                                        if x[488] <= 0.7215686440:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                else:
                                    if x[153] <= 0.0019607844:
                                        results.append(0)
                                    else:
                                        results.append(8)
                            else:
                                if x[655] <= 0.2980392277:
                                    if x[352] <= 0.0039215689:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    if x[263] <= 0.2352941260:
                                        results.append(3)
                                    else:
                                        results.append(5)
                else:
                    if x[155] <= 0.5137255043:
                        if x[550] <= 0.1960784346:
                            if x[182] <= 0.4568627626:
                                results.append(7)
                            else:
                                results.append(7)
                        else:
                            results.append(9)
                    else:
                        results.append(2)
            else:
                if x[460] <= 0.0450980412:
                    if x[403] <= 0.0235294122:
                        if x[569] <= 0.1235294156:
                            if x[410] <= 0.2941176593:
                                if x[243] <= 0.7627451122:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                if x[181] <= 0.1176470630:
                                    results.append(7)
                                else:
                                    results.append(7)
                        else:
                            if x[427] <= 0.5607843250:
                                results.append(6)
                            else:
                                results.append(0)
                    else:
                        if x[598] <= 0.9666666687:
                            if x[712] <= 0.0411764719:
                                if x[212] <= 0.0098039219:
                                    if x[543] <= 0.1019607894:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[264] <= 0.0313725499:
                                        results.append(4)
                                    else:
                                        results.append(9)
                            else:
                                if x[546] <= 0.9372549057:
                                    results.append(9)
                                else:
                                    results.append(9)
                        else:
                            if x[236] <= 0.1176470611:
                                results.append(5)
                            else:
                                results.append(0)
                else:
                    if x[155] <= 0.0313725495:
                        if x[239] <= 0.0176470596:
                            if x[491] <= 0.5137255192:
                                if x[457] <= 0.6294117868:
                                    results.append(8)
                                else:
                                    results.append(4)
                            else:
                                if x[490] <= 0.2176470608:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[372] <= 0.1372549050:
                                if x[410] <= 0.6156862974:
                                    if x[243] <= 0.8803921640:
                                        results.append(9)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(9)
                            else:
                                if x[322] <= 0.2705882490:
                                    if x[354] <= 0.0117647061:
                                        results.append(5)
                                    else:
                                        if x[466] <= 0.8607843220:
                                            results.append(9)
                                        else:
                                            if x[292] <= 0.8764705956:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                else:
                                    results.append(8)
                    else:
                        if x[657] <= 0.4843137413:
                            if x[688] <= 0.2196078449:
                                if x[269] <= 0.0490196086:
                                    results.append(6)
                                else:
                                    results.append(8)
                            else:
                                results.append(4)
                        else:
                            if x[576] <= 0.9901960790:
                                if x[655] <= 0.9901960790:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                if x[326] <= 0.9000000060:
                                    results.append(5)
                                else:
                                    results.append(8)
        else:
            if x[517] <= 0.0901960805:
                if x[455] <= 0.0372549035:
                    if x[263] <= 0.3235294223:
                        if x[659] <= 0.0156862750:
                            if x[543] <= 0.6254902184:
                                if x[320] <= 0.0372549035:
                                    if x[628] <= 0.0058823531:
                                        results.append(5)
                                    else:
                                        results.append(2)
                                else:
                                    if x[272] <= 0.1254902035:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                results.append(6)
                        else:
                            if x[180] <= 0.0254901964:
                                results.append(4)
                            else:
                                if x[522] <= 0.4921568781:
                                    if x[538] <= 0.2215686291:
                                        if x[261] <= 0.3941176571:
                                            results.append(3)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(3)
                                else:
                                    if x[286] <= 0.2019607872:
                                        if x[265] <= 0.0784313735:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                    else:
                        if x[326] <= 0.2745098174:
                            if x[631] <= 0.0215686280:
                                results.append(2)
                            else:
                                if x[487] <= 0.0725490232:
                                    if x[376] <= 0.4117647111:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(6)
                        else:
                            if x[211] <= 0.8274509907:
                                if x[569] <= 0.5549019873:
                                    if x[437] <= 0.8921568692:
                                        if x[653] <= 0.3705882505:
                                            results.append(0)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(8)
                            else:
                                if x[381] <= 0.5196078569:
                                    results.append(0)
                                else:
                                    if x[187] <= 0.0529411770:
                                        results.append(3)
                                    else:
                                        results.append(3)
                else:
                    if x[538] <= 0.0274509811:
                        if x[655] <= 0.3372549117:
                            if x[574] <= 0.3078431413:
                                if x[428] <= 0.8549019694:
                                    results.append(7)
                                else:
                                    results.append(4)
                            else:
                                if x[241] <= 0.2588235363:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[343] <= 0.2470588312:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[385] <= 0.0098039219:
                            if x[511] <= 0.9882352948:
                                results.append(5)
                            else:
                                results.append(0)
                        else:
                            if x[537] <= 0.9843137264:
                                if x[382] <= 0.6509804130:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[433] <= 0.0313725509:
                                    results.append(0)
                                else:
                                    results.append(2)
            else:
                if x[186] <= 0.1901960820:
                    if x[374] <= 0.0333333337:
                        if x[387] <= 0.1411764789:
                            if x[316] <= 0.0039215689:
                                if x[494] <= 0.9901960790:
                                    if x[237] <= 0.7686274648:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(3)
                            else:
                                if x[269] <= 0.1392156929:
                                    results.append(6)
                                else:
                                    results.append(9)
                        else:
                            if x[435] <= 0.0313725509:
                                results.append(0)
                            else:
                                results.append(6)
                    else:
                        if x[661] <= 0.0352941193:
                            if x[554] <= 0.6352941245:
                                results.append(6)
                            else:
                                results.append(6)
                        else:
                            results.append(8)
                else:
                    if x[345] <= 0.0235294122:
                        if x[157] <= 0.6117647290:
                            results.append(2)
                        else:
                            if x[468] <= 0.5431372821:
                                results.append(2)
                            else:
                                results.append(2)
                    else:
                        if x[602] <= 0.9411764741:
                            if x[660] <= 0.6862745285:
                                results.append(4)
                            else:
                                results.append(8)
                        else:
                            if x[243] <= 0.9901960790:
                                if x[262] <= 0.2313725501:
                                    results.append(6)
                                else:
                                    results.append(3)
                            else:
                                results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 34
    if time.time() < deadline or interrupt_flag.is_set():
        if x[409] <= 0.1745098084:
            if x[413] <= 0.0274509815:
                if x[493] <= 0.0039215689:
                    if x[609] <= 0.0392156881:
                        if x[271] <= 0.0627450999:
                            if x[177] <= 0.0450980403:
                                if x[489] <= 0.0745098069:
                                    results.append(1)
                                else:
                                    if x[264] <= 0.9176470637:
                                        if x[402] <= 0.0039215689:
                                            if x[685] <= 0.7000000179:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(8)
                            else:
                                results.append(3)
                        else:
                            if x[292] <= 0.0039215689:
                                if x[296] <= 0.6078431606:
                                    results.append(0)
                                else:
                                    if x[626] <= 0.5745098144:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[325] <= 0.0490196096:
                                    results.append(5)
                                else:
                                    results.append(8)
                    else:
                        if x[513] <= 0.1254902035:
                            results.append(2)
                        else:
                            results.append(2)
                else:
                    if x[299] <= 0.0607843143:
                        if x[351] <= 0.0568627454:
                            if x[432] <= 0.7274509966:
                                if x[517] <= 0.4960784465:
                                    results.append(5)
                                else:
                                    results.append(6)
                            else:
                                if x[322] <= 0.0568627454:
                                    results.append(5)
                                else:
                                    results.append(6)
                        else:
                            if x[458] <= 0.1137254946:
                                if x[292] <= 0.9470588267:
                                    if x[406] <= 0.9745098054:
                                        results.append(3)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(1)
                            else:
                                if x[660] <= 0.1784313768:
                                    if x[486] <= 0.9235294163:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(4)
                    else:
                        if x[412] <= 0.0529411770:
                            if x[156] <= 0.0607843157:
                                if x[460] <= 0.5098039284:
                                    results.append(3)
                                else:
                                    results.append(8)
                            else:
                                if x[378] <= 0.8627451062:
                                    results.append(8)
                                else:
                                    if x[241] <= 0.0745098051:
                                        results.append(8)
                                    else:
                                        results.append(8)
                        else:
                            results.append(7)
            else:
                if x[324] <= 0.6196078658:
                    if x[599] <= 0.3196078539:
                        if x[623] <= 0.3921568766:
                            if x[357] <= 0.6490196288:
                                results.append(4)
                            else:
                                results.append(2)
                        else:
                            results.append(0)
                    else:
                        if x[239] <= 0.0490196086:
                            results.append(0)
                        else:
                            if x[300] <= 0.0647058859:
                                if x[186] <= 0.5862745196:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[262] <= 0.1294117682:
                        results.append(3)
                    else:
                        results.append(6)
        else:
            if x[543] <= 0.5705882609:
                if x[597] <= 0.0039215689:
                    if x[235] <= 0.1764705926:
                        if x[427] <= 0.1921568662:
                            if x[405] <= 0.0196078438:
                                if x[434] <= 0.1803921610:
                                    if x[265] <= 0.1411764771:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(4)
                            else:
                                if x[265] <= 0.0549019612:
                                    if x[317] <= 0.5098039284:
                                        results.append(3)
                                    else:
                                        results.append(4)
                                else:
                                    if x[239] <= 0.0627450999:
                                        results.append(4)
                                    else:
                                        if x[350] <= 0.1843137294:
                                            results.append(9)
                                        else:
                                            results.append(4)
                        else:
                            if x[601] <= 0.9901960790:
                                if x[265] <= 0.2823529546:
                                    results.append(4)
                                else:
                                    if x[294] <= 0.2705882490:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                results.append(9)
                    else:
                        if x[430] <= 0.0196078438:
                            if x[350] <= 0.0039215689:
                                if x[268] <= 0.1039215699:
                                    results.append(9)
                                else:
                                    if x[495] <= 0.2627451047:
                                        if x[261] <= 0.2019607946:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[381] <= 0.7529411912:
                                    results.append(7)
                                else:
                                    if x[523] <= 0.3392156959:
                                        results.append(9)
                                    else:
                                        results.append(3)
                        else:
                            if x[218] <= 0.0156862750:
                                if x[212] <= 0.0196078438:
                                    if x[520] <= 0.9745098054:
                                        if x[325] <= 0.9039215744:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(4)
                                else:
                                    if x[634] <= 0.7823529541:
                                        if x[237] <= 0.0098039219:
                                            results.append(4)
                                        else:
                                            if x[516] <= 0.6921568811:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                    else:
                                        results.append(5)
                            else:
                                if x[428] <= 0.9901960790:
                                    results.append(8)
                                else:
                                    results.append(4)
                else:
                    if x[318] <= 0.8568627536:
                        if x[152] <= 0.0117647066:
                            if x[654] <= 0.0313725495:
                                if x[128] <= 0.6313725710:
                                    if x[244] <= 0.2509804070:
                                        results.append(6)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(2)
                            else:
                                if x[460] <= 0.6450980604:
                                    if x[436] <= 0.8235294223:
                                        if x[298] <= 0.0372549035:
                                            results.append(5)
                                        else:
                                            results.append(0)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(8)
                        else:
                            if x[323] <= 0.0235294132:
                                if x[631] <= 0.8921568692:
                                    if x[377] <= 0.1607843190:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(3)
                            else:
                                if x[486] <= 0.6823529452:
                                    if x[521] <= 0.2352941260:
                                        if x[524] <= 0.8960784376:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[322] <= 0.0941176489:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(8)
                    else:
                        if x[270] <= 0.0764705893:
                            if x[463] <= 0.7411764860:
                                if x[212] <= 0.2549019679:
                                    results.append(5)
                                else:
                                    if x[296] <= 0.0078431377:
                                        results.append(5)
                                    else:
                                        results.append(5)
                            else:
                                results.append(6)
                        else:
                            if x[350] <= 0.0666666701:
                                if x[522] <= 0.9372549057:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[568] <= 0.7882353067:
                                    results.append(4)
                                else:
                                    results.append(3)
            else:
                if x[299] <= 0.0117647061:
                    if x[319] <= 0.0196078438:
                        if x[316] <= 0.7705882490:
                            if x[464] <= 0.8901960850:
                                results.append(2)
                            else:
                                results.append(2)
                        else:
                            results.append(6)
                    else:
                        if x[660] <= 0.0607843138:
                            if x[626] <= 0.3980392218:
                                if x[602] <= 0.3686274588:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                if x[517] <= 0.9274509847:
                                    results.append(6)
                                else:
                                    results.append(9)
                        else:
                            results.append(5)
                else:
                    if x[685] <= 0.0313725509:
                        if x[709] <= 0.0725490227:
                            if x[153] <= 0.0196078438:
                                if x[345] <= 0.0196078438:
                                    if x[437] <= 0.3686274663:
                                        results.append(1)
                                    else:
                                        results.append(2)
                                else:
                                    if x[438] <= 0.0509803928:
                                        results.append(6)
                                    else:
                                        results.append(5)
                            else:
                                if x[187] <= 0.0450980403:
                                    if x[290] <= 0.1058823550:
                                        results.append(2)
                                    else:
                                        results.append(6)
                                else:
                                    if x[655] <= 0.3588235453:
                                        results.append(2)
                                    else:
                                        results.append(2)
                        else:
                            if x[405] <= 0.0137254903:
                                results.append(7)
                            else:
                                results.append(7)
                    else:
                        if x[244] <= 0.0470588244:
                            if x[289] <= 0.3294117674:
                                results.append(0)
                            else:
                                results.append(8)
                        else:
                            if x[681] <= 0.2745098099:
                                results.append(8)
                            else:
                                results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 35
    if time.time() < deadline or interrupt_flag.is_set():
        if x[318] <= 0.0058823533:
            if x[410] <= 0.0058823531:
                if x[606] <= 0.0098039219:
                    if x[489] <= 0.0784313753:
                        if x[486] <= 0.0392156867:
                            if x[350] <= 0.2352941185:
                                if x[631] <= 0.0352941193:
                                    results.append(0)
                                else:
                                    results.append(7)
                            else:
                                if x[206] <= 0.0549019612:
                                    results.append(1)
                                else:
                                    results.append(3)
                        else:
                            if x[215] <= 0.3254902139:
                                results.append(6)
                            else:
                                results.append(5)
                    else:
                        if x[513] <= 0.4215686470:
                            if x[347] <= 0.0450980407:
                                if x[625] <= 0.9941176474:
                                    if x[152] <= 0.4882353097:
                                        if x[492] <= 0.6862745285:
                                            if x[406] <= 0.7823529541:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(5)
                        else:
                            if x[186] <= 0.5764706135:
                                if x[522] <= 0.4019607976:
                                    results.append(1)
                                else:
                                    results.append(2)
                            else:
                                results.append(8)
                else:
                    if x[427] <= 0.0431372561:
                        if x[521] <= 0.6470588446:
                            if x[581] <= 0.0333333341:
                                if x[515] <= 0.0980392173:
                                    results.append(3)
                                else:
                                    results.append(2)
                            else:
                                if x[633] <= 0.8607843220:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            if x[461] <= 0.9549019635:
                                if x[491] <= 0.9490196109:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(8)
                    else:
                        if x[154] <= 0.0215686280:
                            if x[573] <= 0.9901960790:
                                results.append(6)
                            else:
                                results.append(6)
                        else:
                            if x[441] <= 0.5588235557:
                                results.append(0)
                            else:
                                results.append(0)
            else:
                if x[126] <= 0.0117647061:
                    if x[351] <= 0.2647058964:
                        if x[709] <= 0.1000000052:
                            if x[569] <= 0.1647058874:
                                if x[405] <= 0.0039215689:
                                    if x[496] <= 0.0529411780:
                                        if x[492] <= 0.6254902184:
                                            results.append(4)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(4)
                                else:
                                    if x[653] <= 0.6666666865:
                                        if x[427] <= 0.4843137413:
                                            if x[400] <= 0.3666666746:
                                                results.append(8)
                                            else:
                                                results.append(9)
                                        else:
                                            if x[464] <= 0.9000000060:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                    else:
                                        results.append(3)
                            else:
                                if x[131] <= 0.0843137279:
                                    if x[407] <= 0.1313725505:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    if x[544] <= 0.8450980484:
                                        results.append(6)
                                    else:
                                        results.append(6)
                        else:
                            if x[519] <= 0.8039215803:
                                results.append(7)
                            else:
                                results.append(7)
                    else:
                        if x[342] <= 0.4058823623:
                            if x[489] <= 0.6901960969:
                                if x[428] <= 0.5666666776:
                                    if x[523] <= 0.0372549039:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(7)
                        else:
                            if x[636] <= 0.2686274573:
                                results.append(4)
                            else:
                                results.append(9)
                else:
                    if x[347] <= 0.0274509806:
                        if x[159] <= 0.9901960790:
                            if x[409] <= 0.4411764741:
                                results.append(2)
                            else:
                                results.append(2)
                        else:
                            results.append(3)
                    else:
                        if x[237] <= 0.2627451010:
                            if x[573] <= 0.1196078472:
                                results.append(3)
                            else:
                                results.append(3)
                        else:
                            results.append(5)
        else:
            if x[441] <= 0.0156862750:
                if x[265] <= 0.0666666683:
                    if x[400] <= 0.6294117868:
                        if x[486] <= 0.0019607844:
                            if x[184] <= 0.0568627454:
                                if x[322] <= 0.1450980455:
                                    results.append(4)
                                else:
                                    results.append(7)
                            else:
                                if x[572] <= 0.3450980484:
                                    if x[318] <= 0.3725490272:
                                        results.append(3)
                                    else:
                                        if x[270] <= 0.1137254909:
                                            results.append(5)
                                        else:
                                            results.append(9)
                                else:
                                    if x[605] <= 0.9803921580:
                                        if x[465] <= 0.2176470645:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                    else:
                                        results.append(5)
                        else:
                            if x[597] <= 0.1352941189:
                                if x[550] <= 0.5058823675:
                                    results.append(4)
                                else:
                                    results.append(6)
                            else:
                                if x[630] <= 0.2294117734:
                                    results.append(2)
                                else:
                                    results.append(8)
                    else:
                        if x[181] <= 0.1843137294:
                            if x[372] <= 0.7333333492:
                                results.append(4)
                            else:
                                if x[686] <= 0.1000000015:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[467] <= 0.2921568640:
                                results.append(9)
                            else:
                                results.append(5)
                else:
                    if x[551] <= 0.0352941183:
                        if x[541] <= 0.0098039219:
                            if x[315] <= 0.3019607961:
                                if x[268] <= 0.3352941275:
                                    if x[155] <= 0.3705882505:
                                        if x[212] <= 0.2019607872:
                                            if x[267] <= 0.0686274525:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            if x[458] <= 0.0098039219:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                    else:
                                        results.append(0)
                                else:
                                    if x[430] <= 0.0392156877:
                                        if x[290] <= 0.8529411852:
                                            results.append(7)
                                        else:
                                            if x[268] <= 0.9725490212:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                    else:
                                        if x[246] <= 0.2588235438:
                                            if x[601] <= 0.5549019724:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(5)
                            else:
                                if x[456] <= 0.1156862751:
                                    if x[398] <= 0.1078431383:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(9)
                        else:
                            if x[435] <= 0.8196078539:
                                if x[431] <= 0.7568627596:
                                    if x[457] <= 0.1627451032:
                                        results.append(3)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(5)
                            else:
                                if x[267] <= 0.4705882519:
                                    if x[323] <= 0.1450980455:
                                        results.append(8)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(5)
                    else:
                        if x[490] <= 0.0078431377:
                            if x[188] <= 0.0176470596:
                                if x[323] <= 0.7411764860:
                                    if x[429] <= 0.4862745181:
                                        results.append(5)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(3)
                            else:
                                if x[235] <= 0.4470588267:
                                    results.append(5)
                                else:
                                    if x[157] <= 0.9686274529:
                                        results.append(5)
                                    else:
                                        results.append(5)
                        else:
                            if x[400] <= 0.9058823586:
                                if x[544] <= 0.7352941334:
                                    if x[631] <= 0.3470588401:
                                        results.append(2)
                                    else:
                                        results.append(8)
                                else:
                                    if x[545] <= 0.9823529422:
                                        results.append(8)
                                    else:
                                        results.append(6)
                            else:
                                results.append(9)
            else:
                if x[627] <= 0.6784313917:
                    if x[461] <= 0.0803921595:
                        if x[510] <= 0.2666666731:
                            if x[513] <= 0.8372549117:
                                results.append(4)
                            else:
                                results.append(6)
                        else:
                            if x[181] <= 0.0098039219:
                                results.append(0)
                            else:
                                if x[384] <= 0.5803921670:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[570] <= 0.1039215699:
                            if x[460] <= 0.8882353008:
                                results.append(6)
                            else:
                                if x[297] <= 0.8000000119:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            if x[469] <= 0.2058823556:
                                results.append(6)
                            else:
                                if x[328] <= 0.9901960790:
                                    results.append(6)
                                else:
                                    results.append(6)
                else:
                    if x[330] <= 0.0411764709:
                        if x[350] <= 0.4235294312:
                            if x[384] <= 0.7960784435:
                                results.append(5)
                            else:
                                if x[345] <= 0.8607843220:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            if x[296] <= 0.2098039240:
                                if x[603] <= 0.8254902065:
                                    results.append(8)
                                else:
                                    results.append(5)
                            else:
                                if x[233] <= 0.8372549117:
                                    results.append(3)
                                else:
                                    results.append(5)
                    else:
                        if x[406] <= 0.4137254963:
                            if x[214] <= 0.4352941364:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 36
    if time.time() < deadline or interrupt_flag.is_set():
        if x[488] <= 0.0039215689:
            if x[455] <= 0.0372549035:
                if x[623] <= 0.0392156877:
                    if x[541] <= 0.0156862754:
                        if x[271] <= 0.0450980403:
                            if x[655] <= 0.1588235311:
                                if x[353] <= 0.0137254903:
                                    if x[491] <= 0.1745098103:
                                        results.append(5)
                                    else:
                                        if x[183] <= 0.9078431427:
                                            if x[292] <= 0.9156862795:
                                                results.append(1)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(1)
                                else:
                                    if x[351] <= 0.6568627656:
                                        if x[295] <= 0.2862745151:
                                            if x[432] <= 0.2254901975:
                                                results.append(6)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(7)
                                    else:
                                        if x[607] <= 0.0352941193:
                                            results.append(9)
                                        else:
                                            results.append(9)
                            else:
                                if x[189] <= 0.0137254903:
                                    if x[380] <= 0.8960784376:
                                        if x[187] <= 0.3098039329:
                                            if x[210] <= 0.2333333343:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(5)
                        else:
                            if x[376] <= 0.0058823531:
                                if x[685] <= 0.0333333351:
                                    if x[406] <= 0.1843137331:
                                        results.append(7)
                                    else:
                                        results.append(9)
                                else:
                                    if x[408] <= 0.9137254953:
                                        results.append(7)
                                    else:
                                        if x[261] <= 0.6647059023:
                                            results.append(9)
                                        else:
                                            results.append(7)
                            else:
                                if x[180] <= 0.5490196347:
                                    if x[406] <= 0.9862745106:
                                        if x[267] <= 0.0019607844:
                                            results.append(9)
                                        else:
                                            if x[410] <= 0.9862745106:
                                                results.append(5)
                                            else:
                                                results.append(7)
                                    else:
                                        results.append(4)
                                else:
                                    if x[373] <= 0.6941176653:
                                        if x[353] <= 0.2372549102:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(9)
                    else:
                        if x[212] <= 0.0215686280:
                            if x[515] <= 0.0588235296:
                                if x[128] <= 0.4058823586:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(6)
                        else:
                            if x[149] <= 0.0470588244:
                                if x[378] <= 0.0843137279:
                                    results.append(0)
                                else:
                                    if x[235] <= 0.0176470596:
                                        results.append(3)
                                    else:
                                        if x[296] <= 0.0470588244:
                                            results.append(5)
                                        else:
                                            results.append(8)
                            else:
                                if x[289] <= 0.0333333341:
                                    if x[405] <= 0.2627451122:
                                        results.append(3)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(8)
                else:
                    if x[288] <= 0.9313725531:
                        if x[191] <= 0.0490196086:
                            if x[546] <= 0.0078431377:
                                if x[354] <= 0.0333333351:
                                    if x[372] <= 0.0431372561:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[158] <= 0.2725490257:
                                    if x[206] <= 0.1117647067:
                                        results.append(3)
                                    else:
                                        results.append(2)
                                else:
                                    if x[263] <= 0.0568627454:
                                        if x[405] <= 0.0960784331:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(5)
                        else:
                            results.append(5)
                    else:
                        results.append(0)
            else:
                if x[405] <= 0.1509803981:
                    if x[596] <= 0.0745098051:
                        if x[601] <= 0.9901960790:
                            if x[154] <= 0.0215686280:
                                if x[521] <= 0.7705882490:
                                    results.append(9)
                                else:
                                    results.append(7)
                            else:
                                results.append(0)
                        else:
                            results.append(6)
                    else:
                        if x[290] <= 0.0019607844:
                            if x[348] <= 0.8568627536:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            if x[428] <= 0.1137254946:
                                results.append(0)
                            else:
                                if x[437] <= 0.9294117689:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[323] <= 0.7235294282:
                        if x[355] <= 0.4254902154:
                            if x[238] <= 0.0980392173:
                                results.append(4)
                            else:
                                if x[407] <= 0.9019607902:
                                    results.append(5)
                                else:
                                    results.append(5)
                        else:
                            if x[657] <= 0.0137254903:
                                if x[577] <= 0.2352941260:
                                    results.append(2)
                                else:
                                    results.append(4)
                            else:
                                results.append(9)
                    else:
                        if x[494] <= 0.3372549117:
                            results.append(8)
                        else:
                            results.append(3)
        else:
            if x[295] <= 0.7705882490:
                if x[659] <= 0.1294117682:
                    if x[297] <= 0.0078431377:
                        if x[272] <= 0.0725490227:
                            if x[577] <= 0.1098039225:
                                if x[457] <= 0.1000000015:
                                    results.append(8)
                                else:
                                    results.append(6)
                            else:
                                if x[543] <= 0.0137254903:
                                    results.append(5)
                                else:
                                    if x[627] <= 0.7235294282:
                                        results.append(6)
                                    else:
                                        results.append(6)
                        else:
                            if x[655] <= 0.0431372561:
                                if x[155] <= 0.4823529571:
                                    if x[488] <= 0.8941176534:
                                        results.append(8)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(2)
                            else:
                                if x[595] <= 0.2156862840:
                                    if x[217] <= 0.5784313977:
                                        results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(8)
                    else:
                        if x[125] <= 0.0313725499:
                            if x[428] <= 0.2588235438:
                                if x[351] <= 0.7980392277:
                                    if x[268] <= 0.6784313917:
                                        if x[373] <= 0.0274509806:
                                            if x[580] <= 0.0254901964:
                                                results.append(4)
                                            else:
                                                results.append(2)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[655] <= 0.2313725539:
                                            results.append(4)
                                        else:
                                            results.append(7)
                                else:
                                    if x[236] <= 0.2490196079:
                                        if x[295] <= 0.1000000015:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[491] <= 0.5666666925:
                                            results.append(3)
                                        else:
                                            results.append(9)
                            else:
                                if x[527] <= 0.1392156929:
                                    if x[239] <= 0.0117647061:
                                        results.append(4)
                                    else:
                                        if x[402] <= 0.2862745225:
                                            results.append(9)
                                        else:
                                            results.append(4)
                                else:
                                    results.append(6)
                        else:
                            if x[429] <= 0.9666666687:
                                results.append(2)
                            else:
                                results.append(2)
                else:
                    if x[572] <= 0.0098039219:
                        if x[627] <= 0.0549019631:
                            if x[401] <= 0.9901960790:
                                if x[716] <= 0.2470588312:
                                    if x[383] <= 0.1058823541:
                                        results.append(1)
                                    else:
                                        if x[514] <= 0.0882352972:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(9)
                            else:
                                if x[263] <= 0.9588235319:
                                    results.append(4)
                                else:
                                    results.append(9)
                        else:
                            if x[541] <= 0.0137254903:
                                if x[290] <= 0.5666666776:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[150] <= 0.3745098114:
                                    if x[660] <= 0.9196078479:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(2)
                    else:
                        if x[687] <= 0.3764705956:
                            if x[294] <= 0.1588235311:
                                if x[319] <= 0.0137254903:
                                    results.append(2)
                                else:
                                    if x[484] <= 0.0039215689:
                                        results.append(8)
                                    else:
                                        results.append(8)
                            else:
                                results.append(0)
                        else:
                            if x[236] <= 0.9607843161:
                                results.append(8)
                            else:
                                if x[627] <= 0.8686274588:
                                    results.append(8)
                                else:
                                    results.append(8)
            else:
                if x[550] <= 0.0843137279:
                    if x[410] <= 0.0823529456:
                        if x[660] <= 0.3117647208:
                            if x[216] <= 0.4627451152:
                                if x[325] <= 0.7039215863:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(1)
                        else:
                            results.append(4)
                    else:
                        if x[326] <= 0.5254902095:
                            results.append(4)
                        else:
                            results.append(7)
                else:
                    if x[486] <= 0.8156862855:
                        if x[468] <= 0.4882353023:
                            if x[207] <= 0.9862745106:
                                results.append(8)
                            else:
                                results.append(8)
                        else:
                            results.append(6)
                    else:
                        if x[608] <= 0.1117647067:
                            results.append(9)
                        else:
                            results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 37
    if time.time() < deadline or interrupt_flag.is_set():
        if x[323] <= 0.6960784495:
            if x[408] <= 0.0039215689:
                if x[462] <= 0.0098039219:
                    if x[569] <= 0.0058823531:
                        if x[567] <= 0.0058823531:
                            if x[286] <= 0.0117647061:
                                results.append(0)
                            else:
                                if x[318] <= 0.0941176498:
                                    results.append(7)
                                else:
                                    results.append(7)
                        else:
                            if x[602] <= 0.5313725621:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[353] <= 0.2686274573:
                            if x[519] <= 0.9901960790:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                else:
                    if x[214] <= 0.1215686314:
                        if x[466] <= 0.0196078438:
                            if x[407] <= 0.1019607875:
                                results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[493] <= 0.3196078539:
                                results.append(6)
                            else:
                                if x[370] <= 0.0058823531:
                                    results.append(2)
                                else:
                                    results.append(4)
                    else:
                        if x[356] <= 0.0156862754:
                            if x[542] <= 0.3156862892:
                                if x[652] <= 0.1823529452:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(8)
                        else:
                            results.append(2)
            else:
                if x[514] <= 0.0803921595:
                    if x[240] <= 0.0196078434:
                        if x[428] <= 0.5274510086:
                            if x[578] <= 0.3686274588:
                                if x[354] <= 0.0156862754:
                                    results.append(5)
                                else:
                                    if x[263] <= 0.5196078569:
                                        if x[457] <= 0.0215686280:
                                            results.append(7)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[298] <= 0.9901960790:
                                            results.append(4)
                                        else:
                                            results.append(4)
                            else:
                                if x[128] <= 0.0196078438:
                                    if x[234] <= 0.0274509806:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(2)
                        else:
                            if x[430] <= 0.2725490332:
                                results.append(6)
                            else:
                                if x[153] <= 0.4078431576:
                                    if x[234] <= 0.9705882370:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(2)
                    else:
                        if x[430] <= 0.0058823531:
                            if x[405] <= 0.2176470682:
                                if x[326] <= 0.2274509892:
                                    if x[375] <= 0.1117647067:
                                        results.append(7)
                                    else:
                                        results.append(5)
                                else:
                                    if x[578] <= 0.2549019642:
                                        if x[240] <= 0.4686274678:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(3)
                            else:
                                if x[347] <= 0.6019608080:
                                    if x[325] <= 0.5960784405:
                                        results.append(9)
                                    else:
                                        results.append(3)
                                else:
                                    if x[488] <= 0.1000000015:
                                        if x[491] <= 0.4352941215:
                                            results.append(5)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(8)
                        else:
                            if x[592] <= 0.1176470630:
                                if x[162] <= 0.0039215689:
                                    if x[211] <= 0.3568627536:
                                        if x[319] <= 0.0352941183:
                                            if x[325] <= 0.9745098054:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            if x[241] <= 0.9745098054:
                                                results.append(5)
                                            else:
                                                results.append(7)
                                    else:
                                        if x[350] <= 0.0490196086:
                                            if x[262] <= 0.1058823541:
                                                results.append(4)
                                            else:
                                                results.append(9)
                                        else:
                                            if x[546] <= 0.7352941334:
                                                results.append(5)
                                            else:
                                                results.append(6)
                                else:
                                    if x[437] <= 0.9313725531:
                                        results.append(5)
                                    else:
                                        results.append(5)
                            else:
                                results.append(3)
                else:
                    if x[346] <= 0.0215686280:
                        if x[569] <= 0.1254901998:
                            if x[576] <= 0.2607843205:
                                if x[377] <= 0.2843137309:
                                    if x[342] <= 0.0392156877:
                                        results.append(7)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(8)
                            else:
                                if x[208] <= 0.7862745225:
                                    if x[370] <= 0.4490196258:
                                        results.append(6)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(9)
                        else:
                            if x[378] <= 0.5137255192:
                                if x[266] <= 0.8607843220:
                                    if x[183] <= 0.0411764723:
                                        results.append(2)
                                    else:
                                        if x[244] <= 0.9901960790:
                                            results.append(2)
                                        else:
                                            results.append(2)
                                else:
                                    results.append(7)
                            else:
                                if x[319] <= 0.0686274543:
                                    if x[571] <= 0.8411764801:
                                        if x[208] <= 0.1176470630:
                                            results.append(2)
                                        else:
                                            results.append(2)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(8)
                    else:
                        if x[660] <= 0.0137254908:
                            if x[681] <= 0.0313725509:
                                if x[246] <= 0.0196078443:
                                    if x[242] <= 0.2176470608:
                                        if x[132] <= 0.4313725531:
                                            results.append(6)
                                        else:
                                            results.append(6)
                                    else:
                                        if x[404] <= 0.4862745255:
                                            results.append(4)
                                        else:
                                            results.append(6)
                                else:
                                    if x[624] <= 0.1980392188:
                                        results.append(4)
                                    else:
                                        results.append(0)
                            else:
                                if x[269] <= 0.0823529456:
                                    if x[405] <= 0.8294117749:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(9)
                        else:
                            if x[485] <= 0.7431372702:
                                if x[552] <= 0.5549019873:
                                    results.append(8)
                                else:
                                    results.append(5)
                            else:
                                if x[403] <= 0.0588235296:
                                    results.append(9)
                                else:
                                    if x[408] <= 0.9215686321:
                                        results.append(8)
                                    else:
                                        results.append(4)
        else:
            if x[354] <= 0.0039215689:
                if x[180] <= 0.3313725591:
                    if x[301] <= 0.1039215699:
                        if x[316] <= 0.0098039219:
                            if x[553] <= 0.0803921595:
                                if x[295] <= 0.7745098174:
                                    if x[380] <= 0.6705882549:
                                        results.append(1)
                                    else:
                                        results.append(9)
                                else:
                                    if x[429] <= 0.0117647061:
                                        if x[208] <= 0.2823529541:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(6)
                            else:
                                results.append(2)
                        else:
                            results.append(8)
                    else:
                        if x[271] <= 0.7450980544:
                            results.append(5)
                        else:
                            results.append(5)
                else:
                    if x[489] <= 0.0078431377:
                        if x[319] <= 0.5843137503:
                            if x[402] <= 0.9901960790:
                                results.append(3)
                            else:
                                results.append(3)
                        else:
                            results.append(5)
                    else:
                        if x[491] <= 0.8156862855:
                            if x[319] <= 0.0039215689:
                                results.append(2)
                            else:
                                results.append(8)
                        else:
                            if x[206] <= 0.6784313917:
                                results.append(1)
                            else:
                                results.append(7)
            else:
                if x[565] <= 0.0098039219:
                    if x[348] <= 0.9803921580:
                        if x[153] <= 0.0254901964:
                            if x[356] <= 0.4176470786:
                                if x[624] <= 0.3039215803:
                                    if x[630] <= 0.1117647067:
                                        results.append(9)
                                    else:
                                        if x[288] <= 0.0294117648:
                                            results.append(9)
                                        else:
                                            results.append(7)
                                else:
                                    results.append(1)
                            else:
                                if x[431] <= 0.1725490242:
                                    results.append(7)
                                else:
                                    results.append(3)
                        else:
                            if x[546] <= 0.7313725650:
                                results.append(5)
                            else:
                                results.append(2)
                    else:
                        if x[230] <= 0.1901960820:
                            if x[289] <= 0.0333333337:
                                if x[626] <= 0.9745098054:
                                    results.append(9)
                                else:
                                    if x[577] <= 0.7980392277:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[211] <= 0.9686274529:
                                    results.append(8)
                                else:
                                    results.append(5)
                        else:
                            results.append(3)
                else:
                    if x[486] <= 0.3784313798:
                        if x[239] <= 0.9901960790:
                            if x[466] <= 0.6235294193:
                                if x[189] <= 0.2509804070:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(3)
                        else:
                            results.append(0)
                    else:
                        results.append(2)
    
    else:
      return vote_logic(results)
    
    # Tree 38
    if time.time() < deadline or interrupt_flag.is_set():
        if x[433] <= 0.0039215689:
            if x[157] <= 0.0117647061:
                if x[457] <= 0.0882352963:
                    if x[149] <= 0.1588235348:
                        if x[327] <= 0.0784313753:
                            if x[715] <= 0.3372549117:
                                if x[567] <= 0.0019607844:
                                    if x[269] <= 0.0411764723:
                                        results.append(5)
                                    else:
                                        if x[181] <= 0.5686274767:
                                            results.append(9)
                                        else:
                                            results.append(3)
                                else:
                                    if x[271] <= 0.2941176519:
                                        results.append(5)
                                    else:
                                        results.append(0)
                            else:
                                results.append(7)
                        else:
                            if x[567] <= 0.0921568647:
                                if x[375] <= 0.9313725531:
                                    if x[298] <= 0.1333333366:
                                        results.append(7)
                                    else:
                                        if x[551] <= 0.4784313887:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                else:
                                    results.append(9)
                            else:
                                results.append(0)
                    else:
                        if x[377] <= 0.1352941245:
                            results.append(0)
                        else:
                            if x[605] <= 0.7274509966:
                                results.append(3)
                            else:
                                results.append(3)
                else:
                    if x[211] <= 0.0509803928:
                        if x[188] <= 0.0882352963:
                            if x[268] <= 0.1901960829:
                                if x[513] <= 0.6352941394:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(5)
                        else:
                            results.append(4)
                    else:
                        if x[154] <= 0.0333333351:
                            if x[327] <= 0.6686274707:
                                results.append(5)
                            else:
                                results.append(9)
                        else:
                            results.append(0)
            else:
                if x[381] <= 0.1274509877:
                    if x[273] <= 0.0098039219:
                        if x[437] <= 0.3647058979:
                            if x[236] <= 0.0039215689:
                                results.append(3)
                            else:
                                results.append(0)
                        else:
                            if x[101] <= 0.0745098069:
                                results.append(3)
                            else:
                                results.append(6)
                    else:
                        if x[215] <= 0.3450980410:
                            results.append(0)
                        else:
                            if x[483] <= 0.2098039240:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[234] <= 0.9411764741:
                        if x[379] <= 0.0882352982:
                            if x[517] <= 0.1764705963:
                                if x[652] <= 0.0196078438:
                                    results.append(0)
                                else:
                                    results.append(5)
                            else:
                                if x[496] <= 0.2529411800:
                                    results.append(2)
                                else:
                                    results.append(6)
                        else:
                            if x[602] <= 0.5392157137:
                                results.append(5)
                            else:
                                if x[549] <= 0.4745098054:
                                    results.append(3)
                                else:
                                    if x[187] <= 0.7352941334:
                                        results.append(3)
                                    else:
                                        results.append(3)
                    else:
                        if x[657] <= 0.4352941364:
                            results.append(2)
                        else:
                            if x[597] <= 0.7666666806:
                                results.append(5)
                            else:
                                results.append(5)
        else:
            if x[346] <= 0.0039215689:
                if x[465] <= 0.0392156877:
                    if x[178] <= 0.0784313753:
                        if x[209] <= 0.0568627473:
                            if x[377] <= 0.0039215689:
                                results.append(1)
                            else:
                                if x[458] <= 0.4666666836:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[381] <= 0.0058823531:
                                if x[459] <= 0.6784313917:
                                    if x[489] <= 0.1882352978:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(8)
                            else:
                                if x[661] <= 0.0078431377:
                                    if x[237] <= 0.9901960790:
                                        if x[272] <= 0.9117647111:
                                            results.append(8)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(0)
                                else:
                                    results.append(3)
                    else:
                        if x[636] <= 0.0607843138:
                            if x[553] <= 0.8803921640:
                                if x[517] <= 0.2431372628:
                                    results.append(3)
                                else:
                                    results.append(6)
                            else:
                                results.append(2)
                        else:
                            if x[231] <= 0.4803921729:
                                results.append(2)
                            else:
                                results.append(2)
                else:
                    if x[182] <= 0.0588235315:
                        if x[233] <= 0.9901960790:
                            if x[568] <= 0.3313725591:
                                if x[428] <= 0.2254902050:
                                    if x[299] <= 0.1294117682:
                                        results.append(3)
                                    else:
                                        results.append(7)
                                else:
                                    if x[437] <= 0.9901960790:
                                        results.append(9)
                                    else:
                                        results.append(9)
                            else:
                                if x[380] <= 0.6529411972:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            results.append(4)
                    else:
                        if x[518] <= 0.1392156929:
                            if x[406] <= 0.5078431517:
                                if x[270] <= 0.0176470596:
                                    results.append(6)
                                else:
                                    results.append(9)
                            else:
                                if x[292] <= 0.4117647260:
                                    if x[381] <= 0.8862745166:
                                        if x[655] <= 0.3333333433:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[599] <= 0.1980392188:
                                            results.append(2)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(8)
                        else:
                            if x[493] <= 0.0215686280:
                                results.append(7)
                            else:
                                if x[155] <= 0.0411764719:
                                    results.append(2)
                                else:
                                    if x[626] <= 0.9901960790:
                                        results.append(2)
                                    else:
                                        results.append(2)
            else:
                if x[568] <= 0.0176470596:
                    if x[240] <= 0.0019607844:
                        if x[463] <= 0.6980392337:
                            if x[655] <= 0.0176470596:
                                if x[496] <= 0.0549019612:
                                    results.append(4)
                                else:
                                    results.append(6)
                            else:
                                if x[570] <= 0.2431372553:
                                    results.append(3)
                                else:
                                    results.append(8)
                        else:
                            if x[128] <= 0.1254902035:
                                if x[437] <= 0.7921568751:
                                    if x[209] <= 0.0823529437:
                                        results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    if x[579] <= 0.1901960857:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                results.append(6)
                    else:
                        if x[428] <= 0.0372549025:
                            if x[515] <= 0.0980392173:
                                if x[318] <= 0.0843137288:
                                    results.append(3)
                                else:
                                    if x[408] <= 0.6470588446:
                                        if x[548] <= 0.4431372732:
                                            results.append(8)
                                        else:
                                            results.append(5)
                                    else:
                                        if x[155] <= 0.0627451017:
                                            if x[289] <= 0.9901960790:
                                                results.append(9)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(8)
                            else:
                                if x[659] <= 0.2941176593:
                                    if x[239] <= 0.7509804070:
                                        results.append(6)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(8)
                        else:
                            if x[263] <= 0.7529411912:
                                if x[208] <= 0.4254902154:
                                    if x[465] <= 0.9313725531:
                                        if x[325] <= 0.8882353008:
                                            results.append(9)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[400] <= 0.9078431427:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                else:
                                    results.append(3)
                            else:
                                if x[242] <= 0.0117647061:
                                    results.append(5)
                                else:
                                    if x[264] <= 0.7509804070:
                                        if x[182] <= 0.5803921670:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[236] <= 0.9901960790:
                                            results.append(9)
                                        else:
                                            if x[687] <= 0.0509803928:
                                                results.append(9)
                                            else:
                                                results.append(9)
                else:
                    if x[400] <= 0.0901960786:
                        if x[206] <= 0.0078431377:
                            if x[573] <= 0.3705882430:
                                if x[543] <= 0.6392157078:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                if x[460] <= 0.1372549087:
                                    if x[598] <= 0.9627451003:
                                        results.append(5)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(6)
                        else:
                            if x[487] <= 0.0568627473:
                                if x[271] <= 0.3098039255:
                                    results.append(5)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                    else:
                        if x[455] <= 0.2372549102:
                            if x[658] <= 0.5725490451:
                                if x[130] <= 0.3372549135:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(3)
                        else:
                            if x[542] <= 0.1666666716:
                                results.append(2)
                            else:
                                if x[298] <= 0.5235294253:
                                    if x[375] <= 0.9901960790:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 39
    if time.time() < deadline or interrupt_flag.is_set():
        if x[457] <= 0.0019607844:
            if x[347] <= 0.1549019665:
                if x[381] <= 0.0176470596:
                    if x[290] <= 0.0529411770:
                        if x[594] <= 0.0196078434:
                            if x[551] <= 0.2509804070:
                                if x[606] <= 0.0960784331:
                                    if x[188] <= 0.0980392192:
                                        if x[241] <= 0.9941176474:
                                            if x[180] <= 0.5666666925:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(0)
                        else:
                            results.append(3)
                    else:
                        if x[434] <= 0.1215686277:
                            if x[539] <= 0.0764705911:
                                results.append(7)
                            else:
                                results.append(0)
                        else:
                            if x[270] <= 0.1725490279:
                                results.append(1)
                            else:
                                results.append(8)
                else:
                    if x[125] <= 0.0392156877:
                        if x[429] <= 0.0235294127:
                            if x[351] <= 0.1784313768:
                                if x[595] <= 0.2019607872:
                                    if x[433] <= 0.2039215788:
                                        if x[270] <= 0.1313725566:
                                            results.append(9)
                                        else:
                                            if x[324] <= 0.6686274707:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(8)
                            else:
                                if x[517] <= 0.2411764786:
                                    if x[325] <= 0.9941176474:
                                        if x[432] <= 0.6862745285:
                                            if x[606] <= 0.1862745136:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(9)
                                else:
                                    if x[522] <= 0.0352941193:
                                        if x[234] <= 0.0411764719:
                                            if x[492] <= 0.0941176489:
                                                results.append(1)
                                            else:
                                                results.append(3)
                                        else:
                                            if x[626] <= 0.5215686560:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                    else:
                                        results.append(2)
                        else:
                            if x[630] <= 0.4470588416:
                                results.append(3)
                            else:
                                results.append(9)
                    else:
                        if x[181] <= 0.9215686321:
                            results.append(3)
                        else:
                            if x[159] <= 0.0823529437:
                                results.append(2)
                            else:
                                results.append(2)
            else:
                if x[433] <= 0.6764706075:
                    if x[178] <= 0.0274509806:
                        if x[376] <= 0.0392156877:
                            if x[596] <= 0.0843137279:
                                if x[289] <= 0.3254902139:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                results.append(0)
                        else:
                            if x[291] <= 0.0176470596:
                                if x[266] <= 0.0549019622:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[712] <= 0.2156862803:
                                    if x[596] <= 0.2882352993:
                                        if x[514] <= 0.1411764715:
                                            if x[405] <= 0.5294117928:
                                                results.append(5)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(6)
                                    else:
                                        if x[180] <= 0.1470588259:
                                            if x[466] <= 0.4568627626:
                                                results.append(5)
                                            else:
                                                results.append(5)
                                        else:
                                            if x[440] <= 0.2803921700:
                                                results.append(5)
                                            else:
                                                results.append(0)
                                else:
                                    results.append(9)
                    else:
                        if x[629] <= 0.1176470593:
                            results.append(9)
                        else:
                            if x[288] <= 0.0039215689:
                                if x[655] <= 0.4549019635:
                                    results.append(5)
                                else:
                                    if x[654] <= 0.2960784435:
                                        results.append(3)
                                    else:
                                        if x[597] <= 0.9901960790:
                                            results.append(3)
                                        else:
                                            results.append(3)
                            else:
                                if x[402] <= 0.2843137383:
                                    results.append(5)
                                else:
                                    results.append(5)
                else:
                    if x[542] <= 0.2705882490:
                        if x[403] <= 0.7215686440:
                            if x[261] <= 0.0647058832:
                                results.append(8)
                            else:
                                results.append(8)
                        else:
                            if x[351] <= 0.1509803999:
                                if x[383] <= 0.0450980403:
                                    if x[179] <= 0.0431372561:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(8)
                            else:
                                if x[578] <= 0.1549019665:
                                    if x[381] <= 0.7470588386:
                                        results.append(8)
                                    else:
                                        results.append(9)
                                else:
                                    if x[261] <= 0.3745098114:
                                        results.append(3)
                                    else:
                                        results.append(3)
                    else:
                        if x[659] <= 0.1823529415:
                            if x[206] <= 0.0313725509:
                                results.append(6)
                            else:
                                results.append(8)
                        else:
                            results.append(8)
        else:
            if x[570] <= 0.0039215689:
                if x[208] <= 0.0274509811:
                    if x[239] <= 0.3313725591:
                        if x[67] <= 0.0352941193:
                            if x[372] <= 0.0333333351:
                                results.append(4)
                            else:
                                if x[349] <= 0.2078431435:
                                    results.append(4)
                                else:
                                    results.append(4)
                        else:
                            results.append(6)
                    else:
                        if x[624] <= 0.2607843280:
                            if x[383] <= 0.3098039329:
                                if x[299] <= 0.0392156867:
                                    if x[519] <= 0.6392157078:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(7)
                            else:
                                results.append(9)
                        else:
                            results.append(5)
                else:
                    if x[212] <= 0.0196078438:
                        if x[353] <= 0.9941176474:
                            if x[322] <= 0.0137254903:
                                if x[233] <= 0.3784313798:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                results.append(3)
                        else:
                            results.append(9)
                    else:
                        if x[626] <= 0.0313725499:
                            if x[298] <= 0.0176470596:
                                if x[408] <= 0.3784313798:
                                    results.append(5)
                                else:
                                    if x[377] <= 0.2960784361:
                                        results.append(9)
                                    else:
                                        results.append(5)
                            else:
                                if x[517] <= 0.8705882430:
                                    if x[440] <= 0.0392156867:
                                        if x[686] <= 0.9901960790:
                                            if x[207] <= 0.9901960790:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[290] <= 0.7019607872:
                                            results.append(3)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(7)
                        else:
                            if x[401] <= 0.3372549117:
                                results.append(8)
                            else:
                                if x[567] <= 0.7431372702:
                                    if x[272] <= 0.4607843310:
                                        if x[159] <= 0.0941176489:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(0)
            else:
                if x[300] <= 0.0078431377:
                    if x[657] <= 0.4313725680:
                        if x[622] <= 0.0019607844:
                            if x[410] <= 0.0941176508:
                                if x[320] <= 0.2686274517:
                                    if x[378] <= 0.0549019622:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(6)
                            else:
                                if x[596] <= 0.0764705893:
                                    if x[458] <= 0.0686274515:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    if x[320] <= 0.1607843190:
                                        results.append(2)
                                    else:
                                        results.append(6)
                        else:
                            results.append(2)
                    else:
                        if x[487] <= 0.0627450985:
                            if x[290] <= 0.0333333341:
                                results.append(3)
                            else:
                                if x[437] <= 0.1058823541:
                                    results.append(5)
                                else:
                                    results.append(5)
                        else:
                            if x[320] <= 0.9176470637:
                                results.append(0)
                            else:
                                results.append(8)
                else:
                    if x[346] <= 0.1607843190:
                        if x[370] <= 0.0921568647:
                            if x[128] <= 0.2882353067:
                                if x[548] <= 0.0215686280:
                                    results.append(8)
                                else:
                                    results.append(2)
                            else:
                                if x[512] <= 0.6254902184:
                                    if x[457] <= 0.6647059023:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(2)
                        else:
                            results.append(0)
                    else:
                        if x[242] <= 0.0411764719:
                            if x[628] <= 0.8215686381:
                                if x[542] <= 0.7549019754:
                                    results.append(4)
                                else:
                                    results.append(6)
                            else:
                                results.append(8)
                        else:
                            if x[432] <= 0.2745098099:
                                if x[599] <= 0.8039215803:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                if x[518] <= 0.0803921595:
                                    results.append(8)
                                else:
                                    results.append(0)
    
    else:
      return vote_logic(results)
    
    # Tree 40
    if time.time() < deadline or interrupt_flag.is_set():
        if x[400] <= 0.0627450999:
            if x[485] <= 0.0411764719:
                if x[290] <= 0.0019607844:
                    if x[521] <= 0.0078431377:
                        if x[406] <= 0.9176470637:
                            if x[470] <= 0.0588235296:
                                if x[156] <= 0.0058823531:
                                    if x[573] <= 0.3784313872:
                                        if x[519] <= 0.2529411837:
                                            results.append(3)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[685] <= 0.3509804010:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                else:
                                    if x[405] <= 0.0862745121:
                                        results.append(2)
                                    else:
                                        results.append(8)
                            else:
                                results.append(0)
                        else:
                            if x[608] <= 0.0490196086:
                                if x[207] <= 0.0823529446:
                                    if x[547] <= 0.1941176504:
                                        if x[683] <= 0.0823529437:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[575] <= 0.1450980417:
                                            results.append(1)
                                        else:
                                            if x[436] <= 0.5156863034:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[596] <= 0.0078431377:
                                    if x[686] <= 0.6784313917:
                                        results.append(2)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(2)
                    else:
                        if x[350] <= 0.7274509966:
                            if x[660] <= 0.2294117734:
                                if x[297] <= 0.8941176534:
                                    if x[515] <= 0.5156862885:
                                        if x[180] <= 0.4862745255:
                                            if x[240] <= 0.2686274536:
                                                results.append(5)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(2)
                            else:
                                results.append(7)
                        else:
                            if x[490] <= 0.4764706045:
                                if x[567] <= 0.9901960790:
                                    if x[181] <= 0.3372549117:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(1)
                else:
                    if x[406] <= 0.4686274529:
                        if x[298] <= 0.1176470593:
                            if x[525] <= 0.8686274588:
                                if x[629] <= 0.0078431377:
                                    results.append(6)
                                else:
                                    if x[158] <= 0.5039215833:
                                        results.append(3)
                                    else:
                                        results.append(5)
                            else:
                                results.append(0)
                        else:
                            if x[347] <= 0.3745098114:
                                if x[184] <= 0.9647058845:
                                    if x[263] <= 0.5921568871:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(7)
                            else:
                                if x[603] <= 0.8960784376:
                                    results.append(9)
                                else:
                                    results.append(0)
                    else:
                        if x[517] <= 0.0137254908:
                            if x[519] <= 0.1078431401:
                                if x[205] <= 0.4705882519:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                if x[264] <= 0.8568627536:
                                    if x[653] <= 0.0294117648:
                                        results.append(1)
                                    else:
                                        results.append(3)
                                else:
                                    if x[576] <= 0.4117647260:
                                        results.append(9)
                                    else:
                                        results.append(9)
                        else:
                            if x[159] <= 0.0196078438:
                                if x[521] <= 0.0509803928:
                                    if x[215] <= 0.3705882430:
                                        if x[404] <= 0.3156862780:
                                            results.append(2)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[377] <= 0.0254901964:
                                            results.append(8)
                                        else:
                                            results.append(9)
                                else:
                                    if x[260] <= 0.1352941180:
                                        if x[403] <= 0.2882353067:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                    else:
                                        results.append(7)
                            else:
                                if x[183] <= 0.9901960790:
                                    results.append(8)
                                else:
                                    results.append(8)
            else:
                if x[655] <= 0.1196078472:
                    if x[128] <= 0.6431372762:
                        if x[292] <= 0.0313725509:
                            if x[126] <= 0.1607843190:
                                if x[541] <= 0.0705882357:
                                    if x[289] <= 0.2078431472:
                                        results.append(7)
                                    else:
                                        results.append(9)
                                else:
                                    if x[548] <= 0.0215686280:
                                        results.append(1)
                                    else:
                                        results.append(2)
                            else:
                                results.append(2)
                        else:
                            if x[632] <= 0.0137254903:
                                if x[575] <= 0.4274509847:
                                    results.append(2)
                                else:
                                    if x[440] <= 0.4019607976:
                                        results.append(6)
                                    else:
                                        results.append(6)
                            else:
                                results.append(3)
                    else:
                        if x[569] <= 0.0392156877:
                            results.append(6)
                        else:
                            if x[375] <= 0.2117647156:
                                if x[517] <= 0.1549019627:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(2)
                else:
                    if x[523] <= 0.6176470816:
                        if x[514] <= 0.0725490209:
                            if x[346] <= 0.3529411778:
                                results.append(3)
                            else:
                                results.append(5)
                        else:
                            if x[406] <= 0.0117647061:
                                results.append(0)
                            else:
                                if x[237] <= 0.0411764719:
                                    if x[402] <= 0.1019607875:
                                        results.append(2)
                                    else:
                                        results.append(8)
                                else:
                                    if x[233] <= 0.6921568811:
                                        results.append(8)
                                    else:
                                        results.append(8)
                    else:
                        if x[520] <= 0.2039215751:
                            results.append(3)
                        else:
                            results.append(2)
        else:
            if x[155] <= 0.0019607844:
                if x[236] <= 0.9294117689:
                    if x[514] <= 0.0490196086:
                        if x[436] <= 0.4411764741:
                            if x[322] <= 0.9882352948:
                                if x[625] <= 0.0098039219:
                                    results.append(9)
                                else:
                                    results.append(5)
                            else:
                                results.append(7)
                        else:
                            if x[460] <= 0.0686274543:
                                if x[519] <= 0.8647058904:
                                    if x[377] <= 0.4333333522:
                                        results.append(4)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(7)
                            else:
                                if x[209] <= 0.1450980455:
                                    if x[211] <= 0.2450980470:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    if x[352] <= 0.0784313763:
                                        results.append(4)
                                    else:
                                        results.append(9)
                    else:
                        if x[122] <= 0.0176470596:
                            if x[267] <= 0.2392156906:
                                if x[460] <= 0.1960784346:
                                    results.append(6)
                                else:
                                    if x[413] <= 0.0294117648:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                if x[244] <= 0.0039215689:
                                    results.append(6)
                                else:
                                    results.append(0)
                        else:
                            if x[499] <= 0.0176470596:
                                results.append(6)
                            else:
                                results.append(6)
                else:
                    if x[512] <= 0.0686274525:
                        if x[459] <= 0.1549019627:
                            if x[432] <= 0.0254901964:
                                if x[288] <= 0.7431372702:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                if x[634] <= 0.1254902035:
                                    results.append(5)
                                else:
                                    results.append(9)
                        else:
                            if x[376] <= 0.7490196228:
                                if x[631] <= 0.0509803928:
                                    results.append(9)
                                else:
                                    if x[243] <= 0.6980392337:
                                        results.append(9)
                                    else:
                                        results.append(9)
                            else:
                                results.append(3)
                    else:
                        if x[492] <= 0.0098039219:
                            results.append(0)
                        else:
                            if x[241] <= 0.1725490279:
                                results.append(4)
                            else:
                                results.append(8)
            else:
                if x[460] <= 0.3705882430:
                    if x[600] <= 0.5882353187:
                        if x[414] <= 0.0039215689:
                            if x[404] <= 0.3745098114:
                                if x[634] <= 0.0254901964:
                                    results.append(3)
                                else:
                                    if x[579] <= 0.8196078539:
                                        results.append(5)
                                    else:
                                        results.append(5)
                            else:
                                if x[345] <= 0.9039215744:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[574] <= 0.3745098114:
                                if x[467] <= 0.3882353008:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(6)
                    else:
                        if x[242] <= 0.2254901975:
                            if x[301] <= 0.2000000030:
                                if x[376] <= 0.9823529422:
                                    if x[538] <= 0.1039215717:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(3)
                            else:
                                results.append(0)
                        else:
                            if x[405] <= 0.3705882467:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[319] <= 0.3882353157:
                        if x[568] <= 0.1372549087:
                            if x[180] <= 0.4137254953:
                                results.append(4)
                            else:
                                results.append(3)
                        else:
                            if x[631] <= 0.3627450988:
                                results.append(2)
                            else:
                                results.append(8)
                    else:
                        if x[411] <= 0.0372549035:
                            if x[126] <= 0.2549019754:
                                results.append(4)
                            else:
                                results.append(6)
                        else:
                            if x[515] <= 0.8352941275:
                                results.append(6)
                            else:
                                results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 41
    if time.time() < deadline or interrupt_flag.is_set():
        if x[461] <= 0.0490196086:
            if x[482] <= 0.0568627454:
                if x[377] <= 0.0019607844:
                    if x[156] <= 0.0019607844:
                        if x[125] <= 0.0156862754:
                            if x[268] <= 0.0333333341:
                                results.append(7)
                            else:
                                if x[263] <= 0.0549019622:
                                    results.append(7)
                                else:
                                    if x[458] <= 0.0117647061:
                                        results.append(7)
                                    else:
                                        results.append(7)
                        else:
                            results.append(6)
                    else:
                        if x[351] <= 0.0882352963:
                            if x[545] <= 0.0901960805:
                                if x[512] <= 0.2215686366:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(2)
                        else:
                            if x[550] <= 0.2254902013:
                                results.append(5)
                            else:
                                results.append(3)
                else:
                    if x[513] <= 0.0372549035:
                        if x[264] <= 0.3352941275:
                            if x[132] <= 0.3823529482:
                                if x[152] <= 0.1392156892:
                                    if x[374] <= 0.3294117749:
                                        results.append(3)
                                    else:
                                        if x[401] <= 0.9098039269:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                else:
                                    if x[655] <= 0.3098039255:
                                        results.append(3)
                                    else:
                                        if x[298] <= 0.0666666701:
                                            if x[323] <= 0.6333333403:
                                                results.append(3)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(3)
                            else:
                                results.append(5)
                        else:
                            if x[578] <= 0.0098039219:
                                if x[570] <= 0.1058823541:
                                    if x[241] <= 0.0901960814:
                                        results.append(4)
                                    else:
                                        if x[208] <= 0.6686274707:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(5)
                            else:
                                if x[268] <= 0.6156862974:
                                    if x[239] <= 0.5058823675:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    if x[344] <= 0.7431372553:
                                        results.append(3)
                                    else:
                                        results.append(7)
                    else:
                        if x[351] <= 0.8588235378:
                            if x[406] <= 0.0333333351:
                                if x[355] <= 0.7372549176:
                                    results.append(6)
                                else:
                                    results.append(0)
                            else:
                                if x[374] <= 0.4039215893:
                                    results.append(2)
                                else:
                                    if x[432] <= 0.4862745255:
                                        results.append(5)
                                    else:
                                        results.append(6)
                        else:
                            if x[298] <= 0.4078431576:
                                results.append(5)
                            else:
                                if x[523] <= 0.0549019631:
                                    results.append(8)
                                else:
                                    results.append(8)
            else:
                if x[653] <= 0.5843137503:
                    if x[210] <= 0.1450980455:
                        if x[289] <= 0.0137254903:
                            if x[430] <= 0.0411764728:
                                results.append(5)
                            else:
                                results.append(2)
                        else:
                            results.append(4)
                    else:
                        if x[358] <= 0.0039215689:
                            if x[456] <= 0.9254902005:
                                if x[496] <= 0.0333333351:
                                    results.append(5)
                                else:
                                    results.append(7)
                            else:
                                results.append(0)
                        else:
                            if x[510] <= 0.0294117648:
                                results.append(0)
                            else:
                                if x[215] <= 0.3745098114:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[436] <= 0.0764705893:
                        if x[565] <= 0.9901960790:
                            results.append(0)
                        else:
                            results.append(0)
                    else:
                        results.append(0)
        else:
            if x[541] <= 0.0235294122:
                if x[326] <= 0.0058823531:
                    if x[381] <= 0.0215686280:
                        if x[345] <= 0.0235294122:
                            if x[431] <= 0.0607843148:
                                if x[294] <= 0.0215686280:
                                    results.append(1)
                                else:
                                    if x[405] <= 0.1176470593:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[319] <= 0.0843137298:
                                    if x[465] <= 0.0313725509:
                                        results.append(1)
                                    else:
                                        results.append(3)
                                else:
                                    if x[241] <= 0.5784313977:
                                        results.append(6)
                                    else:
                                        results.append(8)
                        else:
                            if x[215] <= 0.4490196258:
                                if x[439] <= 0.1490196139:
                                    results.append(5)
                                else:
                                    results.append(4)
                            else:
                                if x[402] <= 0.9862745106:
                                    results.append(5)
                                else:
                                    results.append(5)
                    else:
                        if x[628] <= 0.1843137257:
                            if x[578] <= 0.0215686280:
                                if x[521] <= 0.1039215708:
                                    results.append(4)
                                else:
                                    if x[403] <= 0.6215686500:
                                        results.append(4)
                                    else:
                                        results.append(4)
                            else:
                                if x[522] <= 0.5196078569:
                                    results.append(9)
                                else:
                                    results.append(6)
                        else:
                            if x[208] <= 0.4019607902:
                                results.append(8)
                            else:
                                results.append(3)
                else:
                    if x[213] <= 0.0960784331:
                        if x[296] <= 0.0215686280:
                            if x[625] <= 0.7705882490:
                                if x[516] <= 0.8823529482:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                results.append(2)
                        else:
                            if x[373] <= 0.8470588326:
                                if x[241] <= 0.3764705956:
                                    results.append(9)
                                else:
                                    results.append(7)
                            else:
                                results.append(4)
                    else:
                        if x[210] <= 0.0196078438:
                            if x[239] <= 0.4058823660:
                                if x[625] <= 0.0568627454:
                                    results.append(4)
                                else:
                                    results.append(1)
                            else:
                                results.append(7)
                        else:
                            if x[382] <= 0.1313725561:
                                if x[234] <= 0.8372549117:
                                    if x[597] <= 0.1705882363:
                                        if x[605] <= 0.0254901964:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[438] <= 0.6784313917:
                                    if x[549] <= 0.5215686411:
                                        if x[572] <= 0.9352941215:
                                            if x[712] <= 0.3921568766:
                                                results.append(4)
                                            else:
                                                results.append(9)
                                        else:
                                            if x[433] <= 0.3549019620:
                                                results.append(7)
                                            else:
                                                results.append(9)
                                    else:
                                        if x[289] <= 0.2274509836:
                                            results.append(3)
                                        else:
                                            results.append(8)
                                else:
                                    if x[343] <= 0.0058823531:
                                        if x[405] <= 0.9901960790:
                                            results.append(9)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[517] <= 0.7725490332:
                                            results.append(9)
                                        else:
                                            results.append(9)
            else:
                if x[659] <= 0.0137254908:
                    if x[264] <= 0.0117647066:
                        if x[156] <= 0.0392156886:
                            if x[547] <= 0.0843137279:
                                if x[269] <= 0.9627451003:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[542] <= 0.9509803951:
                                    if x[124] <= 0.0333333351:
                                        results.append(5)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(6)
                        else:
                            if x[376] <= 0.3333333433:
                                if x[518] <= 0.9901960790:
                                    if x[271] <= 0.9901960790:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    if x[380] <= 0.7960784435:
                                        results.append(2)
                                    else:
                                        results.append(2)
                            else:
                                if x[429] <= 0.0117647061:
                                    results.append(1)
                                else:
                                    results.append(2)
                    else:
                        if x[439] <= 0.1039215699:
                            if x[550] <= 0.3960784376:
                                if x[323] <= 0.3235294223:
                                    if x[290] <= 0.6470588446:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(2)
                            else:
                                if x[542] <= 0.8431372643:
                                    results.append(6)
                                else:
                                    results.append(2)
                        else:
                            if x[244] <= 0.2117647082:
                                results.append(6)
                            else:
                                if x[435] <= 0.9196078479:
                                    results.append(2)
                                else:
                                    results.append(8)
                else:
                    if x[320] <= 0.0058823531:
                        if x[431] <= 0.3745098114:
                            results.append(2)
                        else:
                            if x[603] <= 0.9137254953:
                                if x[183] <= 0.9941176474:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(2)
                    else:
                        if x[602] <= 0.9901960790:
                            results.append(8)
                        else:
                            results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 42
    if time.time() < deadline or interrupt_flag.is_set():
        if x[428] <= 0.2823529541:
            if x[515] <= 0.0568627454:
                if x[518] <= 0.1627451032:
                    if x[289] <= 0.0019607844:
                        if x[513] <= 0.6411764920:
                            if x[264] <= 0.6215686500:
                                if x[178] <= 0.0274509806:
                                    if x[243] <= 0.0941176489:
                                        if x[627] <= 0.1117647067:
                                            results.append(7)
                                        else:
                                            results.append(5)
                                    else:
                                        if x[651] <= 0.0078431377:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    if x[541] <= 0.2137254924:
                                        if x[383] <= 0.8901960850:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[268] <= 0.2862745225:
                                    if x[154] <= 0.0019607844:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(3)
                        else:
                            if x[607] <= 0.0764705911:
                                results.append(8)
                            else:
                                results.append(2)
                    else:
                        if x[359] <= 0.0078431377:
                            if x[628] <= 0.2686274573:
                                if x[405] <= 0.0058823531:
                                    if x[355] <= 0.0411764719:
                                        results.append(9)
                                    else:
                                        if x[315] <= 0.1843137303:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                else:
                                    if x[434] <= 0.8882353008:
                                        if x[576] <= 0.4647058919:
                                            results.append(5)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[406] <= 0.8196078539:
                                            results.append(5)
                                        else:
                                            results.append(5)
                            else:
                                if x[375] <= 0.1196078472:
                                    if x[595] <= 0.8235294223:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    if x[235] <= 0.4333333373:
                                        if x[625] <= 0.4294117689:
                                            results.append(8)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[241] <= 0.3000000119:
                                            results.append(5)
                                        else:
                                            results.append(5)
                        else:
                            if x[217] <= 0.6196078658:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[462] <= 0.9529411793:
                        if x[375] <= 0.0058823531:
                            if x[378] <= 0.0333333351:
                                if x[491] <= 0.9862745106:
                                    if x[179] <= 0.0274509806:
                                        if x[518] <= 0.6196078509:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(2)
                                else:
                                    if x[264] <= 0.0647058859:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                results.append(1)
                        else:
                            if x[464] <= 0.5078431517:
                                if x[375] <= 0.4039215744:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[212] <= 0.1745098084:
                                    results.append(4)
                                else:
                                    if x[264] <= 0.4607843310:
                                        results.append(9)
                                    else:
                                        if x[547] <= 0.9901960790:
                                            results.append(9)
                                        else:
                                            results.append(9)
                    else:
                        if x[318] <= 0.0078431377:
                            if x[458] <= 0.0470588244:
                                if x[322] <= 0.2313725576:
                                    results.append(7)
                                else:
                                    if x[212] <= 0.9941176474:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(1)
                        else:
                            if x[635] <= 0.0882352982:
                                if x[657] <= 0.4078431502:
                                    if x[598] <= 0.0019607844:
                                        results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    if x[261] <= 0.1333333347:
                                        results.append(5)
                                    else:
                                        results.append(9)
                            else:
                                results.append(8)
            else:
                if x[658] <= 0.0078431375:
                    if x[319] <= 0.0019607844:
                        if x[151] <= 0.0039215689:
                            if x[324] <= 0.5274510086:
                                if x[382] <= 0.3450980484:
                                    if x[436] <= 0.2313725501:
                                        results.append(1)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(2)
                            else:
                                if x[483] <= 0.0156862754:
                                    if x[630] <= 0.0137254908:
                                        if x[628] <= 0.9803921580:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[541] <= 0.0921568647:
                                results.append(2)
                            else:
                                if x[263] <= 0.0607843138:
                                    results.append(2)
                                else:
                                    results.append(2)
                    else:
                        if x[214] <= 0.5568627715:
                            if x[272] <= 0.0117647061:
                                if x[348] <= 0.2372549027:
                                    if x[292] <= 0.4980392307:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(6)
                            else:
                                if x[464] <= 0.9098039269:
                                    results.append(4)
                                else:
                                    results.append(0)
                        else:
                            if x[213] <= 0.9901960790:
                                results.append(5)
                            else:
                                if x[295] <= 0.4784313887:
                                    results.append(2)
                                else:
                                    results.append(2)
                else:
                    if x[377] <= 0.3666666746:
                        if x[627] <= 0.9431372583:
                            if x[464] <= 0.7862745225:
                                results.append(8)
                            else:
                                results.append(7)
                        else:
                            if x[404] <= 0.0058823531:
                                results.append(2)
                            else:
                                results.append(0)
                    else:
                        if x[215] <= 0.0686274543:
                            if x[462] <= 0.9647058845:
                                if x[439] <= 0.1941176504:
                                    results.append(8)
                                else:
                                    results.append(3)
                            else:
                                if x[184] <= 0.8352941275:
                                    results.append(8)
                                else:
                                    results.append(1)
                        else:
                            if x[580] <= 0.6862745136:
                                if x[375] <= 0.0098039219:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(2)
        else:
            if x[406] <= 0.0019607844:
                if x[461] <= 0.0196078438:
                    if x[385] <= 0.0352941193:
                        if x[183] <= 0.0117647061:
                            results.append(7)
                        else:
                            if x[242] <= 0.2509804070:
                                results.append(5)
                            else:
                                if x[293] <= 0.8450980484:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[435] <= 0.0058823531:
                            if x[599] <= 0.0176470596:
                                results.append(0)
                            else:
                                if x[685] <= 0.7568627596:
                                    results.append(0)
                                else:
                                    results.append(0)
                        else:
                            results.append(6)
                else:
                    if x[539] <= 0.0078431377:
                        if x[354] <= 0.0490196086:
                            results.append(6)
                        else:
                            if x[240] <= 0.1058823559:
                                results.append(4)
                            else:
                                if x[157] <= 0.2196078449:
                                    results.append(9)
                                else:
                                    results.append(4)
                    else:
                        if x[578] <= 0.2784313876:
                            results.append(2)
                        else:
                            results.append(6)
            else:
                if x[496] <= 0.0725490227:
                    if x[597] <= 0.0588235315:
                        if x[426] <= 0.0392156877:
                            if x[487] <= 0.6509804130:
                                if x[716] <= 0.0117647061:
                                    if x[237] <= 0.1411764771:
                                        results.append(4)
                                    else:
                                        if x[602] <= 0.1019607857:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                else:
                                    results.append(9)
                            else:
                                if x[266] <= 0.7431372702:
                                    if x[351] <= 0.3568627611:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(9)
                        else:
                            if x[454] <= 0.5666666925:
                                if x[409] <= 0.9941176474:
                                    results.append(9)
                                else:
                                    results.append(4)
                            else:
                                if x[342] <= 0.2019607946:
                                    results.append(4)
                                else:
                                    results.append(9)
                    else:
                        if x[493] <= 0.2313725576:
                            if x[573] <= 0.7843137383:
                                results.append(8)
                            else:
                                results.append(4)
                        else:
                            if x[491] <= 0.6156862974:
                                results.append(5)
                            else:
                                results.append(2)
                else:
                    if x[514] <= 0.2529411837:
                        if x[174] <= 0.0647058859:
                            if x[539] <= 0.0333333351:
                                if x[297] <= 0.0196078438:
                                    results.append(5)
                                else:
                                    if x[434] <= 0.9686274529:
                                        results.append(3)
                                    else:
                                        results.append(4)
                            else:
                                if x[466] <= 0.2686274648:
                                    results.append(6)
                                else:
                                    results.append(2)
                        else:
                            results.append(3)
                    else:
                        if x[271] <= 0.0078431377:
                            if x[604] <= 0.0352941193:
                                results.append(6)
                            else:
                                if x[356] <= 0.8411764801:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[403] <= 0.1941176504:
                                results.append(6)
                            else:
                                if x[371] <= 0.5784313828:
                                    results.append(2)
                                else:
                                    results.append(4)
    
    else:
      return vote_logic(results)
    
    # Tree 43
    if time.time() < deadline or interrupt_flag.is_set():
        if x[378] <= 0.5098039508:
            if x[462] <= 0.0176470596:
                if x[570] <= 0.0352941193:
                    if x[186] <= 0.0294117648:
                        if x[378] <= 0.0117647063:
                            if x[625] <= 0.0843137279:
                                if x[270] <= 0.0725490227:
                                    results.append(7)
                                else:
                                    if x[437] <= 0.9941176474:
                                        if x[313] <= 0.8745098114:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                results.append(3)
                        else:
                            results.append(9)
                    else:
                        if x[469] <= 0.9215686321:
                            if x[244] <= 0.0627451017:
                                if x[182] <= 0.2019607946:
                                    results.append(9)
                                else:
                                    results.append(5)
                            else:
                                if x[215] <= 0.9843137264:
                                    results.append(0)
                                else:
                                    results.append(2)
                        else:
                            results.append(0)
                else:
                    if x[510] <= 0.4313725531:
                        if x[412] <= 0.2470588312:
                            if x[298] <= 0.0137254905:
                                if x[155] <= 0.6411764920:
                                    results.append(6)
                                else:
                                    results.append(5)
                            else:
                                results.append(0)
                        else:
                            if x[456] <= 0.0372549035:
                                results.append(3)
                            else:
                                if x[208] <= 0.9901960790:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[345] <= 0.0352941193:
                            results.append(0)
                        else:
                            results.append(0)
            else:
                if x[126] <= 0.0509803938:
                    if x[569] <= 0.3450980484:
                        if x[486] <= 0.0019607844:
                            if x[403] <= 0.0098039219:
                                if x[459] <= 0.3490196168:
                                    results.append(7)
                                else:
                                    results.append(9)
                            else:
                                if x[186] <= 0.9529411793:
                                    if x[489] <= 0.9941176474:
                                        if x[211] <= 0.0882352963:
                                            if x[271] <= 0.1058823541:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            if x[375] <= 0.9901960790:
                                                results.append(9)
                                            else:
                                                results.append(3)
                                    else:
                                        results.append(8)
                                else:
                                    if x[603] <= 0.9901960790:
                                        results.append(3)
                                    else:
                                        results.append(5)
                        else:
                            if x[717] <= 0.0470588244:
                                if x[68] <= 0.0215686280:
                                    if x[601] <= 0.9941176474:
                                        if x[411] <= 0.3196078539:
                                            if x[204] <= 0.0254901964:
                                                results.append(4)
                                            else:
                                                results.append(3)
                                        else:
                                            if x[656] <= 0.2039215788:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(6)
                            else:
                                if x[433] <= 0.4549019784:
                                    results.append(9)
                                else:
                                    results.append(9)
                    else:
                        if x[328] <= 0.0803921595:
                            if x[429] <= 0.2215686329:
                                results.append(2)
                            else:
                                if x[381] <= 0.0235294122:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[262] <= 0.9607843161:
                                if x[329] <= 0.8254902065:
                                    if x[594] <= 0.3470588326:
                                        results.append(4)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(0)
                            else:
                                results.append(8)
                else:
                    if x[599] <= 0.7196078598:
                        if x[468] <= 0.5039215982:
                            if x[624] <= 0.0607843138:
                                results.append(2)
                            else:
                                results.append(2)
                        else:
                            if x[263] <= 0.2588235363:
                                results.append(2)
                            else:
                                results.append(6)
                    else:
                        if x[626] <= 0.0372549025:
                            results.append(6)
                        else:
                            if x[625] <= 0.4156862795:
                                results.append(2)
                            else:
                                if x[575] <= 0.9941176474:
                                    results.append(2)
                                else:
                                    results.append(2)
        else:
            if x[461] <= 0.1058823541:
                if x[317] <= 0.0352941183:
                    if x[291] <= 0.2686274648:
                        if x[325] <= 0.4215686321:
                            if x[431] <= 0.1490196139:
                                if x[578] <= 0.6274510026:
                                    results.append(2)
                                else:
                                    results.append(3)
                            else:
                                if x[272] <= 0.3764705956:
                                    results.append(2)
                                else:
                                    results.append(5)
                        else:
                            if x[625] <= 0.0352941193:
                                results.append(3)
                            else:
                                results.append(3)
                    else:
                        if x[602] <= 0.0549019612:
                            results.append(8)
                        else:
                            if x[572] <= 0.4568627626:
                                results.append(3)
                            else:
                                results.append(5)
                else:
                    if x[158] <= 0.3470588326:
                        if x[464] <= 0.6862745285:
                            if x[341] <= 0.0725490227:
                                if x[626] <= 0.8882353008:
                                    if x[259] <= 0.3352941312:
                                        if x[237] <= 0.4392156899:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(8)
                                else:
                                    if x[523] <= 0.3274509832:
                                        results.append(8)
                                    else:
                                        results.append(3)
                            else:
                                results.append(9)
                        else:
                            if x[409] <= 0.3568627536:
                                results.append(5)
                            else:
                                if x[178] <= 0.0098039219:
                                    if x[459] <= 0.0333333351:
                                        if x[683] <= 0.5313725546:
                                            results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(4)
                    else:
                        if x[634] <= 0.0372549025:
                            results.append(5)
                        else:
                            if x[238] <= 0.0882352963:
                                results.append(5)
                            else:
                                results.append(5)
            else:
                if x[521] <= 0.0058823531:
                    if x[403] <= 0.1176470630:
                        if x[634] <= 0.0568627454:
                            if x[273] <= 0.1215686295:
                                if x[380] <= 0.9901960790:
                                    if x[207] <= 0.5784313828:
                                        results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(8)
                        else:
                            if x[407] <= 0.7313725650:
                                results.append(1)
                            else:
                                results.append(2)
                    else:
                        if x[236] <= 0.0137254903:
                            if x[599] <= 0.9470588267:
                                if x[318] <= 0.1176470593:
                                    results.append(3)
                                else:
                                    results.append(8)
                            else:
                                results.append(1)
                        else:
                            if x[631] <= 0.1411764733:
                                if x[542] <= 0.0921568647:
                                    if x[434] <= 0.9803921580:
                                        results.append(4)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(2)
                            else:
                                if x[374] <= 0.8803921640:
                                    results.append(8)
                                else:
                                    results.append(8)
                else:
                    if x[542] <= 0.0137254903:
                        if x[346] <= 0.0470588254:
                            if x[299] <= 0.2254901975:
                                if x[292] <= 0.4647058994:
                                    results.append(3)
                                else:
                                    results.append(1)
                            else:
                                if x[459] <= 0.2666666731:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[410] <= 0.5215686560:
                                if x[260] <= 0.0117647061:
                                    results.append(9)
                                else:
                                    results.append(8)
                            else:
                                if x[298] <= 0.7705882490:
                                    results.append(4)
                                else:
                                    results.append(9)
                    else:
                        if x[654] <= 0.0078431377:
                            if x[687] <= 0.0529411770:
                                if x[565] <= 0.3333333358:
                                    if x[239] <= 0.9901960790:
                                        if x[214] <= 0.3764705956:
                                            results.append(6)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(8)
                        else:
                            if x[566] <= 0.2156862840:
                                if x[605] <= 0.0137254905:
                                    results.append(8)
                                else:
                                    if x[515] <= 0.6862745285:
                                        results.append(8)
                                    else:
                                        results.append(8)
                            else:
                                results.append(3)
    
    else:
      return vote_logic(results)
    
    # Tree 44
    if time.time() < deadline or interrupt_flag.is_set():
        if x[378] <= 0.4450980425:
            if x[566] <= 0.0039215689:
                if x[457] <= 0.0039215689:
                    if x[462] <= 0.9666666687:
                        if x[270] <= 0.0039215689:
                            if x[202] <= 0.0941176489:
                                if x[181] <= 0.7431372702:
                                    if x[295] <= 0.1764705926:
                                        if x[431] <= 0.8000000119:
                                            if x[213] <= 0.5509804040:
                                                results.append(4)
                                            else:
                                                results.append(7)
                                        else:
                                            results.append(6)
                                    else:
                                        if x[602] <= 0.7921568751:
                                            results.append(9)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(5)
                            else:
                                results.append(7)
                        else:
                            if x[465] <= 0.4117647111:
                                if x[265] <= 0.6921568811:
                                    if x[462] <= 0.0196078438:
                                        results.append(0)
                                    else:
                                        if x[543] <= 0.2196078487:
                                            results.append(7)
                                        else:
                                            results.append(2)
                                else:
                                    if x[326] <= 0.7215686440:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[182] <= 0.8117647171:
                                    if x[688] <= 0.6254902184:
                                        if x[547] <= 0.9901960790:
                                            results.append(7)
                                        else:
                                            if x[600] <= 0.0980392173:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    results.append(2)
                    else:
                        if x[347] <= 0.5490196347:
                            if x[401] <= 0.0019607844:
                                if x[627] <= 0.2647058852:
                                    results.append(3)
                                else:
                                    if x[296] <= 0.5333333462:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                results.append(8)
                        else:
                            if x[601] <= 0.5333333611:
                                if x[654] <= 0.8431372643:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                if x[431] <= 0.7098039389:
                                    results.append(8)
                                else:
                                    results.append(9)
                else:
                    if x[156] <= 0.1745098084:
                        if x[183] <= 0.4352941215:
                            if x[239] <= 0.2117647082:
                                if x[70] <= 0.0019607844:
                                    if x[572] <= 0.9254902005:
                                        if x[380] <= 0.0019607844:
                                            if x[516] <= 0.1392156892:
                                                results.append(4)
                                            else:
                                                results.append(2)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[544] <= 0.9352941215:
                                            results.append(4)
                                        else:
                                            results.append(6)
                                else:
                                    results.append(6)
                            else:
                                if x[407] <= 0.3784313798:
                                    if x[550] <= 0.4529411942:
                                        if x[492] <= 0.9941176474:
                                            results.append(7)
                                        else:
                                            results.append(6)
                                    else:
                                        if x[301] <= 0.0294117648:
                                            results.append(5)
                                        else:
                                            results.append(0)
                                else:
                                    if x[515] <= 0.2078431435:
                                        if x[374] <= 0.3549019620:
                                            if x[549] <= 0.9725490212:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(4)
                        else:
                            if x[460] <= 0.3313725591:
                                results.append(0)
                            else:
                                if x[381] <= 0.8254902065:
                                    results.append(5)
                                else:
                                    if x[235] <= 0.5725490302:
                                        results.append(9)
                                    else:
                                        results.append(9)
                    else:
                        if x[300] <= 0.4078431576:
                            if x[297] <= 0.0117647061:
                                if x[656] <= 0.0058823531:
                                    if x[402] <= 0.4607843310:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(5)
                            else:
                                if x[126] <= 0.5588235408:
                                    if x[658] <= 0.5058823675:
                                        results.append(4)
                                    else:
                                        results.append(3)
                                else:
                                    if x[554] <= 0.3490196168:
                                        results.append(2)
                                    else:
                                        results.append(2)
                        else:
                            if x[490] <= 0.0843137279:
                                results.append(0)
                            else:
                                results.append(8)
            else:
                if x[381] <= 0.4333333522:
                    if x[413] <= 0.0176470596:
                        if x[183] <= 0.0117647061:
                            results.append(5)
                        else:
                            if x[373] <= 0.4627451152:
                                if x[459] <= 0.6764706075:
                                    results.append(5)
                                else:
                                    results.append(2)
                            else:
                                results.append(0)
                    else:
                        if x[301] <= 0.0490196096:
                            if x[212] <= 0.7960784435:
                                results.append(0)
                            else:
                                results.append(2)
                        else:
                            if x[238] <= 0.2686274648:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[294] <= 0.7960784435:
                        if x[413] <= 0.0980392173:
                            if x[601] <= 0.7725490332:
                                results.append(2)
                            else:
                                results.append(2)
                        else:
                            results.append(8)
                    else:
                        results.append(3)
        else:
            if x[467] <= 0.0137254903:
                if x[319] <= 0.0470588244:
                    if x[381] <= 0.6039215922:
                        if x[152] <= 0.8450980484:
                            if x[514] <= 0.8411764801:
                                if x[462] <= 0.0843137279:
                                    results.append(3)
                                else:
                                    if x[492] <= 0.8098039329:
                                        if x[569] <= 0.5000000149:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(3)
                            else:
                                if x[408] <= 0.0156862754:
                                    results.append(8)
                                else:
                                    results.append(1)
                        else:
                            if x[608] <= 0.0882352963:
                                results.append(1)
                            else:
                                results.append(2)
                    else:
                        if x[460] <= 0.5450980663:
                            if x[403] <= 0.6215686351:
                                results.append(3)
                            else:
                                if x[627] <= 0.2000000030:
                                    results.append(4)
                                else:
                                    results.append(9)
                        else:
                            if x[605] <= 0.0078431377:
                                if x[327] <= 0.6215686500:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(2)
                else:
                    if x[400] <= 0.0019607844:
                        if x[266] <= 0.8196078539:
                            if x[214] <= 0.1862745136:
                                if x[515] <= 0.0568627454:
                                    if x[319] <= 0.6176470816:
                                        results.append(9)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(8)
                            else:
                                if x[462] <= 0.5019607991:
                                    if x[188] <= 0.2725490201:
                                        results.append(8)
                                    else:
                                        results.append(5)
                                else:
                                    if x[545] <= 0.8588235378:
                                        results.append(8)
                                    else:
                                        results.append(8)
                        else:
                            if x[239] <= 0.9941176474:
                                if x[433] <= 0.8568627536:
                                    results.append(5)
                                else:
                                    results.append(1)
                            else:
                                results.append(9)
                    else:
                        if x[409] <= 0.4745098203:
                            if x[272] <= 0.0725490227:
                                results.append(6)
                            else:
                                results.append(5)
                        else:
                            if x[544] <= 0.8843137324:
                                if x[239] <= 0.5333333611:
                                    results.append(4)
                                else:
                                    if x[457] <= 0.7196078598:
                                        results.append(9)
                                    else:
                                        results.append(9)
                            else:
                                results.append(4)
            else:
                if x[658] <= 0.4274509847:
                    if x[571] <= 0.9862745106:
                        if x[540] <= 0.0039215689:
                            if x[185] <= 0.1941176504:
                                if x[266] <= 0.0705882385:
                                    results.append(4)
                                else:
                                    if x[545] <= 0.0490196086:
                                        results.append(9)
                                    else:
                                        results.append(3)
                            else:
                                if x[578] <= 0.6627451181:
                                    results.append(3)
                                else:
                                    results.append(5)
                        else:
                            if x[431] <= 0.1431372622:
                                results.append(5)
                            else:
                                if x[629] <= 0.9529411793:
                                    results.append(2)
                                else:
                                    results.append(0)
                    else:
                        if x[213] <= 0.9196078479:
                            if x[384] <= 0.2627451122:
                                results.append(6)
                            else:
                                results.append(6)
                        else:
                            results.append(2)
                else:
                    if x[149] <= 0.6784313917:
                        if x[268] <= 0.0529411770:
                            if x[272] <= 0.0431372561:
                                if x[431] <= 0.3156862780:
                                    if x[291] <= 0.4509803951:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    results.append(8)
                            else:
                                if x[382] <= 0.4686274547:
                                    results.append(8)
                                else:
                                    results.append(3)
                        else:
                            if x[186] <= 0.9901960790:
                                if x[542] <= 0.0803921577:
                                    if x[466] <= 0.6019607931:
                                        results.append(5)
                                    else:
                                        if x[345] <= 0.3549019694:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    if x[235] <= 0.9568627477:
                                        results.append(8)
                                    else:
                                        results.append(8)
                            else:
                                results.append(5)
                    else:
                        if x[665] <= 0.0098039221:
                            if x[294] <= 0.0196078438:
                                results.append(3)
                            else:
                                results.append(3)
                        else:
                            results.append(5)
    
    else:
      return vote_logic(results)
    
    # Tree 45
    if time.time() < deadline or interrupt_flag.is_set():
        if x[346] <= 0.0058823533:
            if x[377] <= 0.0117647066:
                if x[266] <= 0.7294117808:
                    if x[344] <= 0.0254901964:
                        if x[126] <= 0.0117647061:
                            if x[153] <= 0.0313725509:
                                if x[208] <= 0.0470588244:
                                    results.append(1)
                                else:
                                    if x[411] <= 0.1666666735:
                                        if x[435] <= 0.8764705956:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[436] <= 0.3274509944:
                                    results.append(0)
                                else:
                                    results.append(2)
                        else:
                            if x[518] <= 0.0176470596:
                                results.append(3)
                            else:
                                if x[544] <= 0.0039215689:
                                    results.append(2)
                                else:
                                    if x[575] <= 0.9901960790:
                                        results.append(2)
                                    else:
                                        results.append(2)
                    else:
                        if x[470] <= 0.6960784495:
                            if x[602] <= 0.7333333492:
                                if x[181] <= 0.5568627715:
                                    if x[261] <= 0.5607843399:
                                        if x[176] <= 0.1588235367:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(9)
                            else:
                                if x[497] <= 0.2745098043:
                                    results.append(0)
                                else:
                                    results.append(6)
                        else:
                            if x[629] <= 0.5274510086:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[551] <= 0.5098039508:
                        if x[300] <= 0.9941176474:
                            if x[742] <= 0.4901960939:
                                results.append(7)
                            else:
                                results.append(7)
                        else:
                            results.append(7)
                    else:
                        if x[719] <= 0.6588235497:
                            results.append(3)
                        else:
                            results.append(7)
            else:
                if x[495] <= 0.0137254908:
                    if x[465] <= 0.0392156877:
                        if x[636] <= 0.0215686280:
                            if x[329] <= 0.2019607881:
                                if x[207] <= 0.0823529446:
                                    if x[406] <= 0.9490196109:
                                        results.append(1)
                                    else:
                                        if x[295] <= 0.0294117648:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[299] <= 0.2647058964:
                                        if x[294] <= 0.3000000119:
                                            results.append(3)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(8)
                            else:
                                if x[183] <= 0.9235294163:
                                    results.append(8)
                                else:
                                    results.append(8)
                        else:
                            results.append(2)
                    else:
                        if x[382] <= 0.0078431377:
                            if x[602] <= 0.9411764741:
                                if x[291] <= 0.0254901964:
                                    if x[549] <= 0.9411764741:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(1)
                            else:
                                results.append(6)
                        else:
                            if x[130] <= 0.0117647061:
                                if x[658] <= 0.7078431547:
                                    results.append(9)
                                else:
                                    results.append(8)
                            else:
                                results.append(2)
                else:
                    if x[541] <= 0.1764705926:
                        if x[516] <= 0.5333333611:
                            if x[623] <= 0.0254901964:
                                if x[684] <= 0.2862745225:
                                    if x[601] <= 0.0745098069:
                                        results.append(9)
                                    else:
                                        results.append(3)
                                else:
                                    if x[661] <= 0.3607843220:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[497] <= 0.2568627596:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            results.append(6)
                    else:
                        if x[321] <= 0.4196078517:
                            if x[472] <= 0.0098039219:
                                if x[520] <= 0.7235294282:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(2)
                        else:
                            results.append(6)
        else:
            if x[156] <= 0.0019607844:
                if x[380] <= 0.6117647290:
                    if x[241] <= 0.1960784346:
                        if x[273] <= 0.0098039219:
                            if x[327] <= 0.8823529482:
                                if x[124] <= 0.0274509806:
                                    if x[657] <= 0.0372549035:
                                        results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(6)
                            else:
                                results.append(7)
                        else:
                            if x[356] <= 0.0137254903:
                                results.append(5)
                            else:
                                if x[461] <= 0.0235294122:
                                    results.append(7)
                                else:
                                    results.append(4)
                    else:
                        if x[410] <= 0.4647058845:
                            if x[384] <= 0.0313725509:
                                if x[207] <= 0.1470588315:
                                    if x[188] <= 0.7803921700:
                                        results.append(5)
                                    else:
                                        results.append(5)
                                else:
                                    if x[491] <= 0.5274509937:
                                        results.append(5)
                                    else:
                                        results.append(8)
                            else:
                                results.append(0)
                        else:
                            if x[463] <= 0.2941176593:
                                results.append(7)
                            else:
                                if x[299] <= 0.7921568751:
                                    results.append(9)
                                else:
                                    if x[348] <= 0.0294117648:
                                        results.append(7)
                                    else:
                                        results.append(7)
                else:
                    if x[265] <= 0.0235294127:
                        if x[434] <= 0.6352941394:
                            results.append(9)
                        else:
                            if x[210] <= 0.0313725509:
                                if x[489] <= 0.9372549057:
                                    if x[206] <= 0.5078431517:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(6)
                            else:
                                results.append(9)
                    else:
                        if x[246] <= 0.0235294122:
                            if x[412] <= 0.1098039262:
                                if x[601] <= 0.9705882370:
                                    if x[495] <= 0.7490196228:
                                        if x[598] <= 0.3431372643:
                                            if x[438] <= 0.7823529541:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(3)
                                else:
                                    if x[316] <= 0.0313725495:
                                        results.append(9)
                                    else:
                                        results.append(7)
                            else:
                                if x[464] <= 0.5941176713:
                                    results.append(3)
                                else:
                                    if x[183] <= 0.3098039255:
                                        results.append(4)
                                    else:
                                        results.append(9)
                        else:
                            if x[542] <= 0.4803921729:
                                if x[490] <= 0.9333333373:
                                    results.append(5)
                                else:
                                    if x[403] <= 0.5607843399:
                                        results.append(7)
                                    else:
                                        results.append(4)
                            else:
                                results.append(8)
            else:
                if x[654] <= 0.0039215689:
                    if x[571] <= 0.0117647061:
                        if x[456] <= 0.9901960790:
                            if x[686] <= 0.0843137279:
                                results.append(4)
                            else:
                                results.append(9)
                        else:
                            results.append(4)
                    else:
                        if x[576] <= 0.7333333492:
                            if x[428] <= 0.1000000015:
                                if x[235] <= 0.3764705956:
                                    if x[490] <= 0.0843137279:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(8)
                            else:
                                if x[433] <= 0.0313725509:
                                    results.append(0)
                                else:
                                    results.append(6)
                        else:
                            if x[269] <= 0.7372549176:
                                if x[270] <= 0.0156862754:
                                    if x[127] <= 0.9941176474:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(8)
                            else:
                                results.append(3)
                else:
                    if x[350] <= 0.8411764801:
                        if x[426] <= 0.0039215689:
                            if x[460] <= 0.0117647063:
                                if x[458] <= 0.0568627454:
                                    if x[125] <= 0.6901960969:
                                        if x[576] <= 0.0215686280:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        results.append(3)
                                else:
                                    if x[483] <= 0.0666666701:
                                        results.append(0)
                                    else:
                                        results.append(0)
                            else:
                                if x[272] <= 0.0039215689:
                                    if x[261] <= 0.7450980544:
                                        if x[297] <= 0.0941176489:
                                            results.append(5)
                                        else:
                                            results.append(3)
                                    else:
                                        results.append(8)
                                else:
                                    if x[573] <= 0.5686274767:
                                        if x[632] <= 0.0411764719:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                    else:
                                        if x[154] <= 0.3882353008:
                                            results.append(9)
                                        else:
                                            results.append(8)
                        else:
                            if x[263] <= 0.0392156886:
                                results.append(0)
                            else:
                                if x[512] <= 0.0960784331:
                                    results.append(0)
                                else:
                                    results.append(0)
                    else:
                        if x[594] <= 0.0882352963:
                            if x[270] <= 0.8647058904:
                                if x[596] <= 0.6450980604:
                                    results.append(3)
                                else:
                                    results.append(5)
                            else:
                                if x[150] <= 0.2058823593:
                                    results.append(8)
                                else:
                                    results.append(8)
                        else:
                            if x[269] <= 0.0117647061:
                                results.append(5)
                            else:
                                if x[412] <= 0.8980392218:
                                    results.append(3)
                                else:
                                    results.append(3)
    
    else:
      return vote_logic(results)
    
    # Tree 46
    if time.time() < deadline or interrupt_flag.is_set():
        if x[489] <= 0.0019607844:
            if x[482] <= 0.0392156877:
                if x[182] <= 0.0431372561:
                    if x[598] <= 0.0862745102:
                        if x[432] <= 0.0411764719:
                            if x[465] <= 0.7019608021:
                                if x[377] <= 0.0294117648:
                                    if x[234] <= 0.1843137331:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    if x[438] <= 0.2333333343:
                                        results.append(9)
                                    else:
                                        results.append(5)
                            else:
                                if x[299] <= 0.0607843138:
                                    results.append(7)
                                else:
                                    results.append(7)
                        else:
                            if x[236] <= 0.5745098293:
                                if x[236] <= 0.0235294122:
                                    if x[215] <= 0.3980392292:
                                        results.append(4)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[319] <= 0.8176470697:
                                    if x[375] <= 0.0333333341:
                                        results.append(9)
                                    else:
                                        results.append(9)
                                else:
                                    results.append(9)
                    else:
                        if x[126] <= 0.8196078539:
                            if x[298] <= 0.3901960850:
                                if x[241] <= 0.7215686440:
                                    results.append(5)
                                else:
                                    results.append(5)
                            else:
                                results.append(5)
                        else:
                            results.append(2)
                else:
                    if x[456] <= 0.3705882430:
                        if x[263] <= 0.0294117657:
                            if x[270] <= 0.0196078438:
                                if x[350] <= 0.0117647061:
                                    results.append(5)
                                else:
                                    if x[125] <= 0.2274509817:
                                        if x[570] <= 0.0156862754:
                                            results.append(3)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(3)
                            else:
                                if x[545] <= 0.4862745255:
                                    if x[466] <= 0.1941176504:
                                        if x[349] <= 0.5294117704:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                    else:
                                        if x[687] <= 0.8647058904:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(2)
                        else:
                            if x[629] <= 0.2647058964:
                                if x[373] <= 0.0235294125:
                                    results.append(0)
                                else:
                                    if x[345] <= 0.8431372643:
                                        results.append(9)
                                    else:
                                        results.append(9)
                            else:
                                if x[466] <= 0.9000000060:
                                    if x[541] <= 0.0862745121:
                                        if x[632] <= 0.0254901964:
                                            results.append(9)
                                        else:
                                            if x[601] <= 0.9392156899:
                                                results.append(5)
                                            else:
                                                results.append(3)
                                    else:
                                        if x[596] <= 0.6529411972:
                                            if x[572] <= 0.5686274767:
                                                results.append(8)
                                            else:
                                                results.append(6)
                                        else:
                                            results.append(0)
                                else:
                                    if x[325] <= 0.8607843220:
                                        if x[237] <= 0.9725490212:
                                            results.append(5)
                                        else:
                                            results.append(5)
                                    else:
                                        if x[354] <= 0.9901960790:
                                            results.append(3)
                                        else:
                                            results.append(3)
                    else:
                        if x[405] <= 0.0901960805:
                            if x[241] <= 0.0372549035:
                                results.append(5)
                            else:
                                results.append(0)
                        else:
                            if x[404] <= 0.9764705896:
                                results.append(9)
                            else:
                                results.append(5)
            else:
                if x[323] <= 0.1568627506:
                    if x[432] <= 0.0313725509:
                        if x[272] <= 0.3529411852:
                            if x[633] <= 0.0117647061:
                                if x[218] <= 0.1843137257:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(3)
                        else:
                            if x[297] <= 0.5176470876:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[375] <= 0.3823529482:
                            results.append(4)
                        else:
                            results.append(5)
                else:
                    if x[156] <= 0.0764705921:
                        results.append(5)
                    else:
                        if x[455] <= 0.6333333403:
                            results.append(3)
                        else:
                            results.append(8)
        else:
            if x[430] <= 0.0019607844:
                if x[409] <= 0.0019607844:
                    if x[236] <= 0.7568627596:
                        if x[231] <= 0.0196078438:
                            if x[354] <= 0.0156862754:
                                if x[575] <= 0.9901960790:
                                    if x[626] <= 0.9901960790:
                                        if x[575] <= 0.7627451122:
                                            if x[431] <= 0.1215686314:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[517] <= 0.9901960790:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                else:
                                    if x[435] <= 0.9176470637:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                results.append(8)
                        else:
                            results.append(2)
                    else:
                        if x[245] <= 0.1803921573:
                            if x[405] <= 0.9215686321:
                                results.append(2)
                            else:
                                if x[242] <= 0.5019607916:
                                    results.append(1)
                                else:
                                    results.append(8)
                        else:
                            results.append(3)
                else:
                    if x[456] <= 0.1117647104:
                        if x[288] <= 0.6843137443:
                            if x[375] <= 0.1705882438:
                                if x[127] <= 0.0098039219:
                                    if x[237] <= 0.0627450983:
                                        if x[543] <= 0.9588235319:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        if x[578] <= 0.3333333358:
                                            if x[542] <= 0.3117647097:
                                                results.append(7)
                                            else:
                                                results.append(7)
                                        else:
                                            results.append(2)
                                else:
                                    if x[324] <= 0.8392156959:
                                        results.append(2)
                                    else:
                                        results.append(2)
                            else:
                                if x[515] <= 0.2745098099:
                                    results.append(9)
                                else:
                                    if x[154] <= 0.1058823559:
                                        results.append(8)
                                    else:
                                        results.append(8)
                        else:
                            if x[542] <= 0.1647058874:
                                if x[206] <= 0.4921568781:
                                    results.append(7)
                                else:
                                    results.append(7)
                            else:
                                results.append(2)
                    else:
                        if x[469] <= 0.0019607844:
                            if x[600] <= 0.4352941215:
                                if x[551] <= 0.1156862751:
                                    results.append(9)
                                else:
                                    results.append(9)
                            else:
                                results.append(9)
                        else:
                            if x[571] <= 0.6411764771:
                                results.append(4)
                            else:
                                results.append(6)
            else:
                if x[567] <= 0.0156862750:
                    if x[497] <= 0.0372549025:
                        if x[571] <= 0.3941176534:
                            if x[209] <= 0.1647058874:
                                if x[429] <= 0.6980392337:
                                    if x[244] <= 0.1176470593:
                                        results.append(7)
                                    else:
                                        results.append(4)
                                else:
                                    if x[437] <= 0.2823529467:
                                        results.append(4)
                                    else:
                                        if x[372] <= 0.2254901975:
                                            results.append(4)
                                        else:
                                            results.append(4)
                            else:
                                if x[453] <= 0.0156862754:
                                    if x[400] <= 0.7882353067:
                                        if x[436] <= 0.0705882367:
                                            if x[183] <= 0.3921568692:
                                                results.append(5)
                                            else:
                                                results.append(8)
                                        else:
                                            if x[241] <= 0.0901960814:
                                                results.append(4)
                                            else:
                                                results.append(9)
                                    else:
                                        if x[522] <= 0.1431372575:
                                            if x[245] <= 0.5666666925:
                                                results.append(9)
                                            else:
                                                results.append(5)
                                        else:
                                            results.append(9)
                                else:
                                    if x[520] <= 0.9764705896:
                                        results.append(4)
                                    else:
                                        results.append(4)
                        else:
                            if x[495] <= 0.0666666673:
                                if x[658] <= 0.4333333373:
                                    if x[429] <= 0.0333333341:
                                        if x[548] <= 0.0294117648:
                                            results.append(9)
                                        else:
                                            results.append(2)
                                    else:
                                        if x[185] <= 0.0196078438:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                else:
                                    if x[633] <= 0.2176470682:
                                        results.append(8)
                                    else:
                                        results.append(8)
                            else:
                                if x[440] <= 0.4156862795:
                                    results.append(6)
                                else:
                                    results.append(6)
                    else:
                        if x[325] <= 0.0784313753:
                            if x[438] <= 0.0137254903:
                                results.append(6)
                            else:
                                results.append(6)
                        else:
                            if x[186] <= 0.0843137279:
                                results.append(6)
                            else:
                                results.append(8)
                else:
                    if x[103] <= 0.9470588267:
                        if x[317] <= 0.0058823531:
                            if x[552] <= 0.0098039219:
                                if x[374] <= 0.7490196228:
                                    if x[543] <= 0.8470588326:
                                        if x[537] <= 0.1568627506:
                                            if x[434] <= 0.9490196109:
                                                results.append(8)
                                            else:
                                                results.append(8)
                                        else:
                                            results.append(2)
                                    else:
                                        if x[543] <= 0.9803921580:
                                            results.append(2)
                                        else:
                                            results.append(2)
                                else:
                                    results.append(5)
                            else:
                                if x[274] <= 0.0549019612:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            if x[155] <= 0.7529411912:
                                if x[515] <= 0.0921568647:
                                    results.append(5)
                                else:
                                    results.append(6)
                            else:
                                results.append(8)
                    else:
                        results.append(6)
    
    else:
      return vote_logic(results)
    
    # Tree 47
    if time.time() < deadline or interrupt_flag.is_set():
        if x[433] <= 0.0176470596:
            if x[595] <= 0.0058823533:
                if x[153] <= 0.0098039219:
                    if x[378] <= 0.0156862754:
                        if x[486] <= 0.0235294122:
                            if x[469] <= 0.0137254903:
                                if x[267] <= 0.3941176534:
                                    if x[655] <= 0.1705882400:
                                        results.append(7)
                                    else:
                                        results.append(7)
                                else:
                                    if x[297] <= 0.0176470596:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[264] <= 0.0627450999:
                                    results.append(6)
                                else:
                                    results.append(7)
                        else:
                            if x[523] <= 0.0960784331:
                                if x[655] <= 0.0725490209:
                                    results.append(4)
                                else:
                                    results.append(5)
                            else:
                                if x[234] <= 0.0784313753:
                                    results.append(6)
                                else:
                                    results.append(6)
                    else:
                        if x[630] <= 0.8509804010:
                            if x[238] <= 0.1235294156:
                                results.append(6)
                            else:
                                if x[376] <= 0.7137255073:
                                    results.append(7)
                                else:
                                    if x[352] <= 0.6470588446:
                                        results.append(9)
                                    else:
                                        results.append(9)
                        else:
                            results.append(1)
                else:
                    if x[324] <= 0.0215686280:
                        if x[465] <= 0.3901960850:
                            if x[491] <= 0.0039215689:
                                if x[512] <= 0.1725490242:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(4)
                        else:
                            if x[601] <= 0.3568627611:
                                results.append(2)
                            else:
                                results.append(6)
                    else:
                        if x[264] <= 0.1607843190:
                            if x[295] <= 0.1156862751:
                                results.append(5)
                            else:
                                if x[627] <= 0.8352941275:
                                    results.append(3)
                                else:
                                    results.append(3)
                        else:
                            if x[186] <= 0.0058823531:
                                results.append(0)
                            else:
                                results.append(5)
            else:
                if x[351] <= 0.0098039219:
                    if x[441] <= 0.0117647061:
                        if x[319] <= 0.8058823645:
                            if x[462] <= 0.1745098121:
                                results.append(5)
                            else:
                                if x[380] <= 0.0745098069:
                                    results.append(2)
                                else:
                                    results.append(2)
                        else:
                            results.append(0)
                    else:
                        if x[482] <= 0.0392156877:
                            results.append(0)
                        else:
                            if x[463] <= 0.1745098121:
                                results.append(0)
                            else:
                                results.append(0)
                else:
                    if x[153] <= 0.0196078438:
                        if x[431] <= 0.0019607844:
                            if x[569] <= 0.8745098114:
                                results.append(5)
                            else:
                                results.append(5)
                        else:
                            results.append(3)
                    else:
                        if x[176] <= 0.6254902035:
                            if x[605] <= 0.9352941215:
                                if x[624] <= 0.7372549176:
                                    results.append(3)
                                else:
                                    results.append(3)
                            else:
                                results.append(3)
                        else:
                            if x[176] <= 0.9392156899:
                                results.append(5)
                            else:
                                results.append(3)
        else:
            if x[542] <= 0.0058823531:
                if x[427] <= 0.0568627473:
                    if x[205] <= 0.0058823531:
                        if x[520] <= 0.2921568751:
                            if x[346] <= 0.0372549035:
                                if x[298] <= 0.0411764719:
                                    if x[292] <= 0.5803921670:
                                        if x[378] <= 0.8235294223:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(8)
                            else:
                                if x[239] <= 0.4941176623:
                                    if x[490] <= 0.5294117779:
                                        results.append(3)
                                    else:
                                        results.append(4)
                                else:
                                    if x[684] <= 0.0294117657:
                                        results.append(5)
                                    else:
                                        results.append(9)
                        else:
                            if x[321] <= 0.8098039329:
                                if x[462] <= 0.9215686321:
                                    if x[626] <= 0.5980392247:
                                        if x[491] <= 0.5764706135:
                                            if x[630] <= 0.3431372643:
                                                results.append(9)
                                            else:
                                                results.append(9)
                                        else:
                                            if x[629] <= 0.3137255013:
                                                results.append(4)
                                            else:
                                                results.append(9)
                                    else:
                                        if x[652] <= 0.0941176489:
                                            results.append(5)
                                        else:
                                            results.append(3)
                                else:
                                    if x[293] <= 0.0254901964:
                                        if x[430] <= 0.9549019635:
                                            if x[234] <= 0.2784313858:
                                                results.append(2)
                                            else:
                                                results.append(5)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[155] <= 0.0254901964:
                                            results.append(7)
                                        else:
                                            results.append(5)
                            else:
                                if x[236] <= 0.1235294123:
                                    results.append(6)
                                else:
                                    if x[322] <= 0.9470588267:
                                        results.append(1)
                                    else:
                                        results.append(1)
                    else:
                        if x[484] <= 0.5764705986:
                            if x[288] <= 0.1588235348:
                                if x[574] <= 0.4725490361:
                                    if x[319] <= 0.4254902005:
                                        results.append(3)
                                    else:
                                        results.append(3)
                                else:
                                    results.append(3)
                            else:
                                if x[428] <= 0.0254901964:
                                    if x[374] <= 0.8627451062:
                                        results.append(3)
                                    else:
                                        results.append(8)
                                else:
                                    if x[486] <= 0.1627451032:
                                        results.append(9)
                                    else:
                                        results.append(4)
                        else:
                            results.append(2)
                else:
                    if x[598] <= 0.8705882430:
                        if x[402] <= 0.2294117659:
                            if x[238] <= 0.0509803928:
                                results.append(4)
                            else:
                                if x[631] <= 0.0470588244:
                                    results.append(9)
                                else:
                                    results.append(9)
                        else:
                            if x[464] <= 0.0019607844:
                                results.append(5)
                            else:
                                if x[492] <= 0.1098039243:
                                    if x[634] <= 0.6882352978:
                                        results.append(4)
                                    else:
                                        results.append(5)
                                else:
                                    if x[241] <= 0.0823529456:
                                        results.append(4)
                                    else:
                                        if x[209] <= 0.0745098069:
                                            results.append(4)
                                        else:
                                            results.append(9)
                    else:
                        if x[510] <= 0.3980392367:
                            results.append(5)
                        else:
                            results.append(0)
            else:
                if x[655] <= 0.1333333403:
                    if x[519] <= 0.8352941275:
                        if x[296] <= 0.0549019631:
                            if x[235] <= 0.0274509806:
                                if x[549] <= 0.1176470593:
                                    results.append(4)
                                else:
                                    if x[210] <= 0.6941176653:
                                        results.append(6)
                                    else:
                                        results.append(6)
                            else:
                                if x[300] <= 0.1568627506:
                                    if x[604] <= 0.0392156877:
                                        results.append(6)
                                    else:
                                        results.append(6)
                                else:
                                    results.append(7)
                        else:
                            if x[651] <= 0.0039215689:
                                if x[179] <= 0.0862745121:
                                    if x[625] <= 0.5470588356:
                                        if x[602] <= 0.6960784495:
                                            if x[246] <= 0.3823529482:
                                                results.append(3)
                                            else:
                                                results.append(5)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(1)
                                else:
                                    if x[343] <= 0.1058823541:
                                        if x[598] <= 0.9725490212:
                                            results.append(2)
                                        else:
                                            results.append(2)
                                    else:
                                        results.append(6)
                            else:
                                if x[378] <= 0.8980392218:
                                    results.append(1)
                                else:
                                    results.append(1)
                    else:
                        if x[346] <= 0.2549019679:
                            if x[516] <= 0.1960784346:
                                results.append(6)
                            else:
                                if x[386] <= 0.0784313753:
                                    results.append(2)
                                else:
                                    results.append(6)
                        else:
                            if x[292] <= 0.6960784495:
                                results.append(6)
                            else:
                                results.append(5)
                else:
                    if x[319] <= 0.0078431375:
                        if x[210] <= 0.0019607844:
                            if x[572] <= 0.4960784465:
                                results.append(2)
                            else:
                                if x[683] <= 0.0372549035:
                                    results.append(1)
                                else:
                                    results.append(1)
                        else:
                            if x[599] <= 0.9058823586:
                                if x[181] <= 0.5705882385:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                if x[409] <= 0.8647058904:
                                    if x[212] <= 0.8529411852:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(3)
                    else:
                        if x[515] <= 0.4196078479:
                            if x[401] <= 0.4941176623:
                                if x[633] <= 0.1843137294:
                                    results.append(0)
                                else:
                                    results.append(8)
                            else:
                                results.append(4)
                        else:
                            if x[266] <= 0.9862745106:
                                if x[401] <= 0.9117647111:
                                    if x[243] <= 0.9941176474:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
    
    else:
      return vote_logic(results)
    
    # Tree 48
    if time.time() < deadline or interrupt_flag.is_set():
        if x[515] <= 0.0568627454:
            if x[596] <= 0.0039215689:
                if x[460] <= 0.0686274525:
                    if x[153] <= 0.0274509806:
                        if x[434] <= 0.8137255013:
                            if x[211] <= 0.8725490272:
                                if x[379] <= 0.7274509966:
                                    if x[265] <= 0.1117647104:
                                        if x[511] <= 0.1666666716:
                                            results.append(7)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(7)
                                else:
                                    if x[323] <= 0.1313725505:
                                        results.append(5)
                                    else:
                                        results.append(7)
                            else:
                                if x[372] <= 0.0313725509:
                                    if x[465] <= 0.2568627596:
                                        if x[434] <= 0.1294117682:
                                            results.append(9)
                                        else:
                                            results.append(7)
                                    else:
                                        if x[292] <= 0.0960784340:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                else:
                                    if x[354] <= 0.2803921625:
                                        results.append(5)
                                    else:
                                        if x[314] <= 0.0686274543:
                                            results.append(9)
                                        else:
                                            results.append(9)
                        else:
                            if x[464] <= 0.0019607844:
                                if x[183] <= 0.8588235378:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                if x[381] <= 0.0411764719:
                                    results.append(3)
                                else:
                                    if x[405] <= 0.3431372680:
                                        results.append(7)
                                    else:
                                        if x[408] <= 0.9901960790:
                                            results.append(4)
                                        else:
                                            results.append(4)
                    else:
                        if x[324] <= 0.7705882490:
                            if x[598] <= 0.4647058994:
                                if x[375] <= 0.1176470593:
                                    if x[433] <= 0.3196078539:
                                        results.append(0)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(3)
                            else:
                                results.append(0)
                        else:
                            if x[318] <= 0.0882352963:
                                results.append(3)
                            else:
                                results.append(3)
                else:
                    if x[492] <= 0.0725490227:
                        if x[545] <= 0.1745098084:
                            if x[346] <= 0.4274509996:
                                if x[211] <= 0.8294117749:
                                    results.append(4)
                                else:
                                    results.append(3)
                            else:
                                results.append(5)
                        else:
                            if x[375] <= 0.0313725509:
                                if x[658] <= 0.9490196109:
                                    results.append(1)
                                else:
                                    results.append(1)
                            else:
                                results.append(8)
                    else:
                        if x[208] <= 0.1078431383:
                            if x[291] <= 0.4941176623:
                                if x[325] <= 0.0196078438:
                                    results.append(4)
                                else:
                                    results.append(4)
                            else:
                                if x[212] <= 0.1843137294:
                                    results.append(4)
                                else:
                                    if x[272] <= 0.3980392218:
                                        results.append(9)
                                    else:
                                        results.append(9)
                        else:
                            if x[326] <= 0.1960784346:
                                if x[184] <= 0.3333333433:
                                    if x[524] <= 0.0568627454:
                                        results.append(4)
                                    else:
                                        results.append(3)
                                else:
                                    if x[576] <= 0.3431372643:
                                        results.append(7)
                                    else:
                                        results.append(5)
                            else:
                                if x[241] <= 0.4411764741:
                                    if x[211] <= 0.2294117734:
                                        results.append(4)
                                    else:
                                        results.append(9)
                                else:
                                    if x[380] <= 0.3392156959:
                                        results.append(9)
                                    else:
                                        results.append(9)
            else:
                if x[262] <= 0.4862745255:
                    if x[290] <= 0.0980392173:
                        if x[264] <= 0.1372549087:
                            if x[321] <= 0.0392156877:
                                if x[323] <= 0.0254901974:
                                    if x[632] <= 0.0647058832:
                                        results.append(2)
                                    else:
                                        results.append(2)
                                else:
                                    results.append(3)
                            else:
                                if x[483] <= 0.1470588297:
                                    if x[156] <= 0.0254901964:
                                        results.append(5)
                                    else:
                                        if x[152] <= 0.3039215803:
                                            results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    results.append(8)
                        else:
                            if x[180] <= 0.2274509892:
                                if x[541] <= 0.0176470596:
                                    results.append(5)
                                else:
                                    if x[655] <= 0.0176470596:
                                        results.append(6)
                                    else:
                                        results.append(0)
                            else:
                                if x[652] <= 0.2509803958:
                                    results.append(3)
                                else:
                                    results.append(3)
                    else:
                        if x[413] <= 0.0254901964:
                            if x[574] <= 0.2627451010:
                                results.append(8)
                            else:
                                if x[566] <= 0.7588235438:
                                    results.append(5)
                                else:
                                    results.append(5)
                        else:
                            if x[266] <= 0.4549019635:
                                if x[129] <= 0.6627451181:
                                    results.append(5)
                                else:
                                    results.append(0)
                            else:
                                if x[596] <= 0.5980392173:
                                    results.append(0)
                                else:
                                    results.append(0)
                else:
                    if x[352] <= 0.0019607844:
                        if x[358] <= 0.0039215689:
                            if x[436] <= 0.0313725509:
                                results.append(0)
                            else:
                                results.append(5)
                        else:
                            if x[295] <= 0.2352941260:
                                results.append(0)
                            else:
                                results.append(0)
                    else:
                        if x[435] <= 0.5529412031:
                            if x[347] <= 0.3509804010:
                                results.append(8)
                            else:
                                if x[661] <= 0.0019607844:
                                    results.append(5)
                                else:
                                    results.append(5)
                        else:
                            if x[351] <= 0.4000000060:
                                results.append(8)
                            else:
                                results.append(3)
        else:
            if x[373] <= 0.2000000104:
                if x[126] <= 0.3352941275:
                    if x[291] <= 0.0078431377:
                        if x[465] <= 0.0313725509:
                            if x[574] <= 0.0882352963:
                                if x[633] <= 0.0529411770:
                                    if x[354] <= 0.7392157018:
                                        if x[241] <= 0.3980392218:
                                            results.append(1)
                                        else:
                                            if x[515] <= 0.4235294312:
                                                results.append(1)
                                            else:
                                                results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(3)
                            else:
                                if x[548] <= 0.6784313917:
                                    if x[545] <= 0.9137254953:
                                        results.append(8)
                                    else:
                                        if x[210] <= 0.8980392218:
                                            results.append(1)
                                        else:
                                            results.append(8)
                                else:
                                    results.append(2)
                        else:
                            if x[242] <= 0.6823529601:
                                if x[350] <= 0.4137254953:
                                    if x[342] <= 0.2823529541:
                                        if x[515] <= 0.9509803951:
                                            if x[466] <= 0.3294117674:
                                                results.append(2)
                                            else:
                                                results.append(2)
                                        else:
                                            results.append(6)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(6)
                            else:
                                results.append(7)
                    else:
                        if x[657] <= 0.0058823531:
                            if x[102] <= 0.1470588297:
                                if x[241] <= 0.9392156899:
                                    if x[184] <= 0.9901960790:
                                        if x[513] <= 0.5607843250:
                                            results.append(3)
                                        else:
                                            results.append(8)
                                    else:
                                        results.append(2)
                                else:
                                    if x[210] <= 0.7725490332:
                                        results.append(7)
                                    else:
                                        results.append(2)
                            else:
                                results.append(6)
                        else:
                            if x[294] <= 0.9019607902:
                                if x[551] <= 0.6588235497:
                                    if x[438] <= 0.4745098203:
                                        if x[178] <= 0.8686274588:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                    else:
                                        if x[262] <= 0.7921568751:
                                            results.append(8)
                                        else:
                                            results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(7)
                else:
                    if x[346] <= 0.0509803928:
                        if x[152] <= 0.0392156877:
                            if x[464] <= 0.0058823531:
                                results.append(1)
                            else:
                                results.append(3)
                        else:
                            if x[605] <= 0.9901960790:
                                results.append(2)
                            else:
                                if x[434] <= 0.9568627477:
                                    results.append(2)
                                else:
                                    results.append(2)
                    else:
                        if x[185] <= 0.0274509806:
                            results.append(6)
                        else:
                            results.append(8)
            else:
                if x[657] <= 0.0215686280:
                    if x[271] <= 0.0254901964:
                        if x[594] <= 0.1686274521:
                            if x[543] <= 0.8568627536:
                                if x[100] <= 0.0039215689:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(6)
                        else:
                            results.append(5)
                    else:
                        if x[382] <= 0.7705882490:
                            if x[375] <= 0.3784313798:
                                results.append(0)
                            else:
                                results.append(5)
                        else:
                            if x[488] <= 0.9901960790:
                                results.append(4)
                            else:
                                results.append(4)
                else:
                    if x[407] <= 0.0490196086:
                        if x[270] <= 0.8235294223:
                            results.append(5)
                        else:
                            results.append(0)
                    else:
                        if x[467] <= 0.1647058874:
                            if x[238] <= 0.8921568692:
                                if x[372] <= 0.9843137264:
                                    results.append(8)
                                else:
                                    results.append(8)
                            else:
                                results.append(8)
                        else:
                            if x[291] <= 0.3019607849:
                                results.append(8)
                            else:
                                results.append(4)
    
    else:
      return vote_logic(results)
    
    # Tree 49
    if time.time() < deadline or interrupt_flag.is_set():
        if x[455] <= 0.0176470596:
            if x[376] <= 0.0098039219:
                if x[405] <= 0.0039215689:
                    if x[430] <= 0.0019607844:
                        if x[569] <= 0.3392156959:
                            if x[182] <= 0.8607843220:
                                if x[465] <= 0.3431372643:
                                    if x[600] <= 0.1568627525:
                                        results.append(7)
                                    else:
                                        if x[205] <= 0.4176470786:
                                            results.append(7)
                                        else:
                                            results.append(7)
                                else:
                                    if x[597] <= 0.1235294137:
                                        results.append(7)
                                    else:
                                        results.append(7)
                            else:
                                if x[154] <= 0.8509804010:
                                    results.append(0)
                                else:
                                    results.append(3)
                        else:
                            if x[655] <= 0.1274509840:
                                if x[380] <= 0.6529411972:
                                    results.append(2)
                                else:
                                    results.append(2)
                            else:
                                results.append(5)
                    else:
                        if x[436] <= 0.0117647061:
                            results.append(5)
                        else:
                            if x[543] <= 0.0078431377:
                                if x[325] <= 0.1686274596:
                                    results.append(9)
                                else:
                                    if x[429] <= 0.9941176474:
                                        if x[488] <= 0.2254901975:
                                            results.append(4)
                                        else:
                                            results.append(9)
                                    else:
                                        results.append(4)
                            else:
                                if x[187] <= 0.0137254903:
                                    results.append(6)
                                else:
                                    results.append(2)
                else:
                    if x[271] <= 0.0039215689:
                        if x[206] <= 0.0039215689:
                            if x[634] <= 0.5137255043:
                                if x[318] <= 0.0058823531:
                                    if x[601] <= 0.0098039219:
                                        if x[212] <= 0.1000000015:
                                            results.append(1)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                                else:
                                    results.append(9)
                            else:
                                results.append(2)
                        else:
                            if x[297] <= 0.1392156929:
                                results.append(6)
                            else:
                                if x[488] <= 0.1294117654:
                                    results.append(4)
                                else:
                                    results.append(2)
                    else:
                        if x[625] <= 0.3078431487:
                            if x[345] <= 0.0137254903:
                                results.append(7)
                            else:
                                if x[263] <= 0.7588235438:
                                    results.append(9)
                                else:
                                    if x[409] <= 0.9372549057:
                                        results.append(9)
                                    else:
                                        results.append(9)
                        else:
                            if x[211] <= 0.0078431377:
                                if x[571] <= 0.7960784435:
                                    results.append(2)
                                else:
                                    if x[436] <= 0.4607843235:
                                        results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[459] <= 0.0274509806:
                                    results.append(3)
                                else:
                                    results.append(2)
            else:
                if x[516] <= 0.0019607844:
                    if x[623] <= 0.2313725576:
                        if x[464] <= 0.6862745285:
                            if x[159] <= 0.2392156869:
                                if x[635] <= 0.6607843339:
                                    if x[347] <= 0.0137254903:
                                        if x[403] <= 0.0254901964:
                                            results.append(1)
                                        else:
                                            results.append(9)
                                    else:
                                        if x[123] <= 0.0392156867:
                                            if x[353] <= 0.3254902065:
                                                results.append(5)
                                            else:
                                                results.append(3)
                                        else:
                                            results.append(3)
                                else:
                                    if x[202] <= 0.2823529467:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                if x[209] <= 0.1666666716:
                                    results.append(6)
                                else:
                                    if x[325] <= 0.4901960939:
                                        results.append(5)
                                    else:
                                        results.append(5)
                        else:
                            if x[625] <= 0.1000000052:
                                if x[211] <= 0.3058823571:
                                    if x[237] <= 0.6392157078:
                                        if x[548] <= 0.8333333433:
                                            results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        results.append(1)
                                else:
                                    if x[264] <= 0.0196078438:
                                        results.append(4)
                                    else:
                                        if x[627] <= 0.3529411778:
                                            results.append(9)
                                        else:
                                            results.append(9)
                            else:
                                if x[241] <= 0.9647058845:
                                    if x[521] <= 0.9156862795:
                                        results.append(2)
                                    else:
                                        results.append(8)
                                else:
                                    if x[464] <= 0.9901960790:
                                        results.append(3)
                                    else:
                                        results.append(3)
                    else:
                        if x[298] <= 0.0058823531:
                            if x[188] <= 0.1137254909:
                                results.append(3)
                            else:
                                if x[436] <= 0.5803921819:
                                    results.append(5)
                                else:
                                    results.append(5)
                        else:
                            if x[291] <= 0.3862745166:
                                if x[181] <= 0.0490196086:
                                    results.append(3)
                                else:
                                    if x[457] <= 0.3137255013:
                                        results.append(3)
                                    else:
                                        results.append(3)
                            else:
                                results.append(3)
                else:
                    if x[298] <= 0.0549019612:
                        if x[439] <= 0.0274509815:
                            if x[437] <= 0.0313725499:
                                if x[266] <= 0.5039215833:
                                    if x[291] <= 0.0254901964:
                                        results.append(2)
                                    else:
                                        results.append(4)
                                else:
                                    if x[236] <= 0.0078431377:
                                        if x[156] <= 0.7509804070:
                                            results.append(2)
                                        else:
                                            results.append(1)
                                    else:
                                        results.append(1)
                            else:
                                if x[486] <= 0.0862745123:
                                    results.append(8)
                                else:
                                    results.append(6)
                        else:
                            if x[179] <= 0.0196078441:
                                if x[518] <= 0.8058823645:
                                    results.append(6)
                                else:
                                    results.append(6)
                            else:
                                results.append(3)
                    else:
                        if x[377] <= 0.9156862795:
                            if x[685] <= 0.2196078449:
                                if x[459] <= 0.4607843310:
                                    if x[211] <= 0.8352941275:
                                        if x[354] <= 0.7490196228:
                                            results.append(5)
                                        else:
                                            results.append(7)
                                    else:
                                        results.append(9)
                                else:
                                    if x[161] <= 0.0705882385:
                                        results.append(2)
                                    else:
                                        results.append(1)
                            else:
                                if x[204] <= 0.1431372613:
                                    if x[601] <= 0.5392157137:
                                        results.append(8)
                                    else:
                                        results.append(4)
                                else:
                                    results.append(3)
                        else:
                            if x[660] <= 0.0392156877:
                                if x[430] <= 0.4117647111:
                                    if x[517] <= 0.7470588386:
                                        results.append(8)
                                    else:
                                        results.append(8)
                                else:
                                    results.append(1)
                            else:
                                results.append(8)
        else:
            if x[433] <= 0.0117647061:
                if x[386] <= 0.0941176489:
                    if x[328] <= 0.7215686440:
                        if x[275] <= 0.1098039225:
                            if x[545] <= 0.4627451003:
                                if x[467] <= 0.4333333522:
                                    results.append(9)
                                else:
                                    results.append(0)
                            else:
                                if x[238] <= 0.3470588336:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            results.append(5)
                    else:
                        if x[595] <= 0.0019607844:
                            if x[570] <= 0.5803921670:
                                if x[262] <= 0.6509804130:
                                    results.append(4)
                                else:
                                    results.append(7)
                            else:
                                results.append(0)
                        else:
                            if x[497] <= 0.4450980425:
                                if x[189] <= 0.1058823578:
                                    results.append(0)
                                else:
                                    results.append(0)
                            else:
                                results.append(3)
                else:
                    if x[266] <= 0.0490196086:
                        if x[325] <= 0.0078431377:
                            if x[214] <= 0.1686274558:
                                results.append(0)
                            else:
                                results.append(0)
                        else:
                            results.append(0)
                    else:
                        if x[209] <= 0.0607843138:
                            results.append(0)
                        else:
                            results.append(0)
            else:
                if x[538] <= 0.1254901998:
                    if x[516] <= 0.9568627477:
                        if x[370] <= 0.7176470757:
                            if x[570] <= 0.9156862795:
                                if x[553] <= 0.1098039225:
                                    if x[714] <= 0.0882352963:
                                        if x[710] <= 0.0745098069:
                                            if x[569] <= 0.0235294122:
                                                results.append(4)
                                            else:
                                                results.append(4)
                                        else:
                                            results.append(4)
                                    else:
                                        if x[242] <= 0.8960784376:
                                            results.append(9)
                                        else:
                                            results.append(4)
                                else:
                                    results.append(3)
                            else:
                                if x[208] <= 0.1549019667:
                                    results.append(6)
                                else:
                                    results.append(6)
                        else:
                            if x[262] <= 0.4039215744:
                                results.append(4)
                            else:
                                if x[369] <= 0.3490196168:
                                    results.append(9)
                                else:
                                    results.append(5)
                    else:
                        if x[497] <= 0.0058823531:
                            results.append(2)
                        else:
                            if x[463] <= 0.9901960790:
                                results.append(6)
                            else:
                                results.append(6)
                else:
                    if x[346] <= 0.1313725524:
                        if x[521] <= 0.1352941245:
                            results.append(8)
                        else:
                            if x[243] <= 0.3274509907:
                                results.append(2)
                            else:
                                results.append(2)
                    else:
                        if x[485] <= 0.9901960790:
                            if x[379] <= 0.6254902184:
                                results.append(5)
                            else:
                                if x[601] <= 0.7117647231:
                                    results.append(2)
                                else:
                                    results.append(3)
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
