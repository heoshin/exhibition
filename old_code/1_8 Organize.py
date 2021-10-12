from os import sep
import pandas as pd
import numpy as np
import json

def Organize(merge):
    #dict 생성, value 기준으로 정렬
    ratio_type = dict()
    for i, ratio in enumerate(merge):
        ratio_type[type_name[i]] = ratio
    ratio_type_sorted = sorted(ratio_type.items(), reverse=True, key=lambda item: item[1])

    #상위 3개, 15% 이하 버림
    organize = dict()
    for type, ratio in ratio_type_sorted[0:3]:
        if np.all(ratio >= 15):
            print(type, ratio, end="  ")
            organize[type] = ratio
    print()
    
    return organize


path = "./물금고등학교-익명의-숲_진로편/"

type_name = ["현실형", "탐구형", "예술형", "사회형", "진취형", "관습형"]

with open(path + "merge.json", "r", encoding='UTF-8') as j:
    merges = json.load(j)

organizes = merges

for writer, dic in merges.items(): #merges json 파일
    if not 'merge' in dic.keys():
        continue
    organizes[writer]['organize'] = Organize(dic['merge'])

with open(path + "organize.json", "w", encoding="UTF-8") as j:
    json.dump(merges, j, ensure_ascii=False, indent=4)
