from os import sep
import pandas as pd
import numpy as np
import json

def Merge(writer, persent):
    if data.loc[writer, "반영비율"].size > 1: #같은이름 존재하면 첫 번째 데이터로
        data_ratio = data.loc[writer, "반영비율"].iloc[0]
        data_result = data.loc[writer].iloc[0]
    else:
        data_ratio = data.loc[writer, "반영비율"]
        data_result = data.loc[writer]
    crawl_ratio = round(1 - data_ratio, 2) 

    data_result = np.round_(np.array(data_result.iloc[1:7]) * data_ratio, 2) #검사지 반영 비율 조절
    crawl_result = np.round_(np.array(persent, dtype=np.float64) * crawl_ratio, 2) #크롤링 반영 비율 조절
    
    merge = np.round_(data_result + crawl_result, 2)

    print(writer, data_ratio, end=": ")
    print(data_result, crawl_result, merge)

    return list(merge)

def Labeling(merge_unLabel):
    merge_dict = dict()
    for i, ratio in enumerate(merge_unLabel):
        merge_dict[type_name[i]] = ratio
    return merge_dict

def Loop(percents):
    merges = percents
    data.set_index("이름", inplace=True)
    for writer, dic in percents.items(): #json 파일
        persent = dic["persent"]
        if len(persent) == 0: #json에 데이터 비어있는지 확인
            print(writer, 'is no persent data')
            # del(merges[writer])
            continue
        if not writer in list(data.index): #검사지에 해당 자료 있는지 확인
            print(writer, 'is no test data')
            # del(merges[writer])
            continue
        
        merge_unLabel = Merge(writer, persent)

        # merge_dict = Labeling(merge_unLabel)
        merges[writer]['merge'] = merge_unLabel

    return merges

path = "./물금고등학교-익명의-숲_진로편/"
data = pd.read_excel(path + "data/data_ratio.xlsx")

type_name = ["현실형", "탐구형", "예술형", "사회형", "진취형", "관습형"]

with open(path + "persent.json", "r", encoding='UTF-8') as j:
    json_file = json.load(j)

merges = Loop(json_file)

with open(path + "merge.json", "w", encoding="UTF-8") as j:
    json.dump(merges, j, ensure_ascii=False, indent=4)
