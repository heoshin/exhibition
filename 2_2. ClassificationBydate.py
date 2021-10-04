from os import write
import pandas as pd
import json
import numpy as np
import datetime as dt

path = "./물금고등학교-익명의-숲_생활편/"


def seperateBydate(date, isBefore):
    df = pd.read_json(path + "contents.json")
    df = df.sort_values(by=["writer", "date"])

    if isBefore:
        df = df[df["date"] <= date]
    else:
        df = df[df["date"] > date]
        
    cnt = df["writer"].value_counts()

    datas = dict()
    for writer, cnt in cnt.items():
        for idx in range(cnt):
            if writer in datas:
                datas[writer] += df[df["writer"] == writer].iloc[idx]["content"]
            else:
                datas[writer] = df[df["writer"] == writer].iloc[idx]["content"]

    return datas
    

datasBefore = seperateBydate(pd.Timestamp(2021, 6, 18), True)
datasAfter = seperateBydate(pd.Timestamp(2021, 6, 18), False)
    
with open(path + "Classification_before.json", "w", encoding="UTF-8") as j:
    json.dump(datasBefore, j, ensure_ascii=False, indent=4)
with open(path + "Classification_after.json", "w", encoding="UTF-8") as j:
    json.dump(datasAfter, j, ensure_ascii=False, indent=4)