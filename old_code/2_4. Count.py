import json
import pandas as pd
import numpy as np
from collections import Counter

def count(morphs):
    ratio_json = dict()
    morphs_only = dict()
    for writer, dic in morphs.items():
        count = Counter(dic["morph"])
        cnt_cat_dict = dict()
        for type in category.columns:
            cnt_cat_dict[type] = 0
            #유형별 주요 단어
            for word in category[type]:
                if word in count.keys():
                    cnt_cat_dict[type] += 1

        cnt_cat = list(cnt_cat_dict.items())
        cnt_cat_sorted = sorted(cnt_cat, reverse=True, key=lambda item: item[1])
        
        morphs[writer]["count"] = cnt_cat_dict
        morphs_only[writer] = dict()
        morphs_only[writer]["count"] = cnt_cat_dict
        print(cnt_cat_dict)
    return morphs, morphs_only

path = "./물금고등학교-익명의-숲_생활편/"

category = pd.read_excel(path + "data/word.xlsx")

with open(path + "morphs_before.json", "r", encoding='UTF-8') as j:
    morphs = json.load(j)

morphs, morphs_only = count(morphs)

with open(path + "count_before.json", "w", encoding="UTF-8") as j:
    json.dump(morphs, j, ensure_ascii=False, indent=4)
with open(path + "count_before_only.json", "w", encoding="UTF-8") as j:
    json.dump(morphs_only, j, ensure_ascii=False, indent=4)


with open(path + "morphs_after.json", "r", encoding='UTF-8') as j:
    morphs = json.load(j)

morphs, morphs_only = count(morphs)

with open(path + "count_after.json", "w", encoding="UTF-8") as j:
    json.dump(morphs, j, ensure_ascii=False, indent=4)
with open(path + "count_after_only.json", "w", encoding="UTF-8") as j:
    json.dump(morphs_only, j, ensure_ascii=False, indent=4)