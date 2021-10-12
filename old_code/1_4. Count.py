import json
import pandas as pd
import numpy as np
from collections import Counter

# def Count(morphs):
#     json_count = dict()
#     for writer, dic in morphs.items():
#         count = Counter(dic["morph"])
#         cntFromCat = []
#         for type in category.columns:
#             cntFromCat.append(0)
#             #유형별 주요 단어
#             for word in category[type]:
#                 if word in count.keys():
#                     cntFromCat[-1] += count[word]

#         json_count[writer] = dict()
#         json_count[writer]["count"] = cntFromCat
#         print(writer, sum(cntFromCat), cntFromCat) 

#         if sum(cntFromCat) == 0:
#             del(json_count[writer])
#             print(writer, 'is zero. remove')
#     return json_count

def Count(df):
    count_list = []
    for idx, (writer, words) in df.iterrows():
        # print(words)
        count = Counter(words) #evel: str->파이썬 코드
        cntByCnt = []
        for type in category.columns:
            cntByCnt.append(0)
            #유형별 주요 단어
            for word in category[type]:
                if word in count.keys():
                    cntByCnt[-1] += count[word]

        count_list.append(cntByCnt)
        # print(writer, sum(cntByCnt), cntByCnt) 
        print(count)

        # if sum(cntFromCat) == 0:
        #     del(count_dict[writer])
        #     print(writer, 'is zero. remove')
    return count_list

path = "./물금고등학교-익명의-숲_진로편/"

category = pd.read_excel(path + "data/category.xlsx")

df = pd.read_csv(path + 'morphs.csv', converters={'morph': eval})

count_list = Count(df)

df['count'] = count_list

df.to_csv(path + 'count.csv', header=True, index=False)
