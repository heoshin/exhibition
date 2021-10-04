from os import sep, write
from konlpy.tag import Okt
from collections import Counter
from PIL import Image
from wordcloud import WordCloud
import numpy as np
import json
ok_twitter = Okt()

def createWordCloud(json_file, fileName):
    text = ""
    words_cnt = 0
    for writer, dic in json_file.items():
        words = dic["morph"]
        if len(words) > 0:
            count = np.array(list(Counter(words).items()))
            count_value = np.array(count[:, 1], dtype=np.int32)
            word_cnt = len(count_value[count_value > 1])
            print(word_cnt, end="  ")
            words_cnt += word_cnt
            if word_cnt > 0:
                for word in words:
                    text += word + " "
    print(words_cnt, text)
    #워드 클라우드 생성
    mask_image = np.array(Image.open(path + 'data/mask.png'))
    wc = WordCloud(
        font_path='C:/Windows/Fonts/NanumGothic.ttf', # 사용할 폰트
        background_color='white', # 배경색
        max_words=250, # 최대 빈도수를 기준으로 출력할 단어 수
        mask=mask_image, # 마스크 이미지
        max_font_size=100, # 최대 폰트 크기
        colormap='hsv' # 컬러 스타일 ex)'Accent', 'Accent_r', 'Blues', 'Blues_r' 등등
    ).generate(text)
    wc.to_file(path + fileName + '.png')

path = "./물금고등학교-익명의-숲_생활편/"

with open(path + "morphs_before.json", "r", encoding='UTF-8') as j:
    json_file = json.load(j)

createWordCloud(json_file, "before")

with open(path + "morphs_before.json", "r", encoding='UTF-8') as j:
    json_file = json.load(j)
    
createWordCloud(json_file, "after")