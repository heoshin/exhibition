import json
import pandas as pd
import numpy as np
from collections import Counter

def Percent(df_count):
    list_persent = []
    for idx, (writer, count) in df_count[['writer', 'count']].iterrows():
        cntFromCat = count
        # cnt_cat_sorted = sorted(cnt_cat, reverse=True, key=lambda item: item[1])
        cntSum = sum(cntFromCat)

        persent = []
        print(writer, end=": ")
        for i in cntFromCat:
            persent.append(round(i / cntSum * 100, 2))
        
        print(persent)

        list_persent.append(persent)
    return list_persent

path = "./물금고등학교-익명의-숲_진로편/"

df_count = pd.read_csv(path + 'count.csv', converters={'count': eval})

list_persent = Percent(df_count)
df_persent = df_count
df_persent['persent'] = list_persent

df_persent.to_csv(path + 'persent.csv', index=False)
