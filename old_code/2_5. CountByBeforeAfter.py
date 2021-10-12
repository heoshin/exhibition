import json
import numpy as np

def count(json_file):
    pos = []
    neg = []
    for k in list(json_file.values()):
        pos.append(k["count"]["긍정"])
        neg.append(k["count"]["부정"])
    posCnt = sum(pos)
    negCnt = sum(neg)

    return posCnt, negCnt

path = "./물금고등학교-익명의-숲_생활편/"

with open(path + "count_before_only.json", "r", encoding='UTF-8') as j:
    json_file = json.load(j)

cnt = count(json_file)
print("6/18 이전 긍정적인 단어 수:", cnt[0])
print("6/18 이전 부정적인 단어 수:", cnt[1])

with open(path + "count_after_only.json", "r", encoding='UTF-8') as j:
    json_file = json.load(j)

cnt = count(json_file)
print("6/18 이후 긍정적인 단어 수:", cnt[0])
print("6/18 이후 부정적인 단어 수:", cnt[1])