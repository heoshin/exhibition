import pandas as pd
import numpy as np
import json

path = "./물금고등학교-익명의-숲_진로편/"
data = pd.read_excel(path + "data/data_ratio.xlsx")
data_satis = pd.read_excel(path + "data/satisfaction.xlsx")

type_name = ["현실형", "탐구형", "예술형", "사회형", "진취형", "관습형"]

with open(path + "merge.json", "r", encoding='UTF-8') as j:
    json_file = json.load(j)
with open(path + "merge_only.json", "r", encoding='UTF-8') as j:
    json_file2 = json.load(j)

data.set_index("이름", inplace=True)
dict_satis = dict()
data_satis.set_index("성명", inplace=True)
for writer, dic in json_file.items():
    if writer in list(data.index) and bool(dic["persent"]): #설문지에 데이터 존재하는지 확인 && 타입 존재 확인
        if data.loc[writer, "반영비율"].size > 1: #데이터 여러 개 존재한다면 1번째 선택
            data_ratio = data.loc[writer, "반영비율"].iloc[0]
            data_result = data.loc[writer].iloc[0]
        else:
            data_ratio = data.loc[writer, "반영비율"]
            data_result = data.loc[writer]

        if writer in list(data_satis.index):
            dict_satis[writer] = dict()
            reflect = data_satis.loc[writer, "최종_피드백값"]
            data_ratio += reflect

            data_result = np.round_(np.array(data_result.iloc[1:7]) * data_ratio, 2)

            crawl_ratio = round(1 - data_ratio, 2)
            crawl_result = np.round_(np.array(np.array(list(dic["persent"].items()))[:, 1], dtype=np.float64) * crawl_ratio, 2)
            
            print(writer, data_ratio, reflect, end=": ")
            print(data_result.shape, end=" | ")

            result_merge = np.round_(data_result + crawl_result, 2)

            print(data_result, end=" | ")
            print(crawl_result, end=" | ")
            print(result_merge, end=" | ")
            
            # print(writer, data_ratio, end=": ")
            # print(result_merge)

            #dict 생성, value 기준으로 정렬
            ratio_type = dict()
            for i, ratio in enumerate(result_merge):
                ratio_type[type_name[i]] = ratio
            ratio_type_sorted = sorted(ratio_type.items(), reverse=True, key=lambda item: item[1])

            #상위 3개, 15% 이하 버림
            merge = dict()
            for type, ratio in ratio_type_sorted[0:3]:
                if np.all(ratio >= 15):
                    print(type, ratio, end="  ")
                    merge[type] = ratio
            print()
        
            json_file[writer]["satis"] = merge
            dict_satis[writer]["merge"] = json_file[writer]["merge"]
            dict_satis[writer]["satis"] = merge

with open(path + "satis.json", "w", encoding="UTF-8") as j:
    json.dump(json_file, j, ensure_ascii=False, indent=4)
with open(path + "satis_only.json", "w", encoding="UTF-8") as j:
    json.dump(dict_satis, j, ensure_ascii=False, indent=4)
