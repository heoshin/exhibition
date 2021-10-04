# from konlpy.tag import Okt
from konlpy.tag import Mecab
from collections import Counter
import numpy as np
import json
import pandas as pd

# ok_twitter = Okt()
mec = Mecab("C:/mecab/mecab-ko-dic")

#형태소 별로 분리
def get_morph(sentence):
    # morph = np.array(np.empty((0, 2)))
    morph = mec.pos(sentence)
    # part_of_speech = ok_twitter.pos(sentence)
    # for wordPart in part_of_speech:
    #     morph = np.append(morph, [wordPart], axis=0)
    morph = pd.DataFrame(morph, columns=['word', 'part'])
    return morph

#학생별 형태소 딕셔너리 생성
def get_dict_morph(classification):
    df_morphs = pd.DataFrame(columns=['writer', 'morph'])

    for idx, (writer, sentence) in classification.iterrows():
        print(idx + 1, "/", len(classification), sep="")
        morph_all = get_morph(sentence)
        morph = morph_all[(morph_all['part'] == 'NNG') | (morph_all['part'] == 'NNG')]['word'].to_list()
        # morph = list(morph[(morph[:, 1] == "Noun") | (morph[:, 1] == "Adjective"), 0])
        # morph = morph_all[:, 0]
        # morph = morph_all
        words = {'writer': writer, "morph" : morph}
        df_morphs = df_morphs.append(words, ignore_index=True)

    return df_morphs

path = "./물금고등학교-익명의-숲_진로편/"
#불러오기

df = pd.read_csv(path + 'classification.csv')

df_morphs = get_dict_morph(df)
df_morphs.drop(df_morphs[df_morphs['morph'].apply(len) == 0].index, inplace=True)

# morphs = dict(sorted(morphs.items(), key=lambda x : x[0]))

df_morphs.to_csv(path + 'morphs.csv', header=True, index=False)
