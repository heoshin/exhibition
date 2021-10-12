import json
import pandas as pd
import numpy as np
from collections import Counter

path = "./물금고등학교-익명의-숲_진로편/"

category = pd.read_excel(path + "data/category.xlsx")

with open(path + "count.json", "r", encoding='UTF-8') as j:
    json_file = json.load(j)
with open(path + "count_only.json", "r", encoding='UTF-8') as j:
    json_file2 = json.load(j)

ratio_json = dict()
for writer, dic in json_file.items():
    cnt_cat_dict = dic["count"]
    cnt_cat = list(cnt_cat_dict.items())
    # cnt_cat_sorted = sorted(cnt_cat, reverse=True, key=lambda item: item[1])
    
    sum = 0
    for i in cnt_cat:
        sum += i[1]

    persent = dict()
    print(writer, end=": ")
    for i in cnt_cat:
        if sum != 0:
            print(i[0], round(i[1] / sum * 100, 2), end="  ")
            persent[i[0]] = round(i[1] / sum * 100, 2)
    
    json_file[writer]["persent"] = persent
    json_file2[writer]["persent"] = persent
    print()

with open(path + "persent.json", "w", encoding="UTF-8") as j:
    json.dump(json_file, j, ensure_ascii=False, indent=4)
with open(path + "persent_only.json", "w", encoding="UTF-8") as j:
    json.dump(json_file2, j, ensure_ascii=False, indent=4)