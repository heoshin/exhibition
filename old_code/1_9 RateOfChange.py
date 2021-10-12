from os import sep
import pandas as pd
import numpy as np
import json

def RateOfChange(person):
    print(person['persent'], person['merge'])
    for i in range(6):
        src, dst = person['persent'][i], person['merge'][i]
        print(round((dst - src) / src  * 100, 2), end=" ")
    print()


path = "./물금고등학교-익명의-숲_진로편/"

type_name = ["현실형", "탐구형", "예술형", "사회형", "진취형", "관습형"]

with open(path + "organize.json", "r", encoding='UTF-8') as j:
    organizes = json.load(j)

rateOfChanges = organizes

for writer, person in organizes.items(): #organizes json 파일
    organizes[writer]['rateOfChange'] = RateOfChange(person)

with open(path + "rateOfChange.json", "w", encoding="UTF-8") as j:
    json.dump(rateOfChanges, j, ensure_ascii=False, indent=4)
