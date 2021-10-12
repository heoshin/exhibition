from konlpy.tag import Okt
from collections import Counter
import numpy as np
import json

ok_twitter = Okt()

#형태소 별로 분리
def get_morph(sentence):
    morph = np.array(np.empty((0, 2)))
    part_of_speech = ok_twitter.pos(sentence)
    for wordPart in part_of_speech:
        morph = np.append(morph, [wordPart], axis=0)
    return morph

#학생별 형태소 딕셔너리
def get_dict_morph(classification):
    morphs = dict()
    i = 0
    for writer, sentence in classification.items():
        print(i + 1, "/", len(classification), sep="")
        morph = get_morph(sentence)
        morphs[writer] = {"morph" : list(morph[(morph[:, 1] == "Noun") | (morph[:, 1] == "Adjective"), 0])}
        i += 1
    return morphs

path = "./물금고등학교-익명의-숲_생활편/"
#불러오기
with open(path + "classification_before.json", "r", encoding='UTF-8') as j:
    classification = json.load(j)

morphs = get_dict_morph(classification)
morphs = dict(sorted(morphs.items(), key=lambda x : x[0]))

with open(path + "morphs_before.json", "w", encoding="UTF-8") as j:
    json.dump(morphs, j, ensure_ascii=False, indent=4)

with open(path + "classification_after.json", "r", encoding='UTF-8') as j:
    classification = json.load(j)

morphs = get_dict_morph(classification)
morphs = dict(sorted(morphs.items(), key=lambda x : x[0]))

with open(path + "morphs_after.json", "w", encoding="UTF-8") as j:
    json.dump(morphs, j, ensure_ascii=False, indent=4)