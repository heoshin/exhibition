from konlpy.tag import Okt
from collections import Counter
from PIL import Image
from wordcloud import WordCloud
import numpy as np
import json
import os

ok_twitter = Okt()

path = "./물금고등학교-익명의-숲_진로편/"
#불러오기
with open(path + "morphs.json", "r", encoding='UTF-8') as j:
    json_file = json.load(j)

os.makedirs(path + "WordCloud", exist_ok=True)
for writer, dic in json_file.items():
    words = dic["morph"]
    if len(words) > 0:
        count = np.array(list(Counter(words).items()))
        count_value = np.array(count[:, 1], dtype=np.int32)
        max_words = len(count_value[count_value > 1])
        print(max_words, end="  ")
        
        if max_words > 0:
            text = ""
            for word in words:
                text += word + " "

            #워드 클라우드 생성
            mask_image = np.array(Image.open(path + 'data/mask.png'))
            wc = WordCloud(
                font_path='C:/Windows/Fonts/NanumGothic.ttf', # 사용할 폰트
                background_color='white', # 배경색
                max_words=max_words, # 최대 빈도수를 기준으로 출력할 단어 수
                mask=mask_image, # 마스크 이미지
                max_font_size=100, # 최대 폰트 크기
                colormap='hsv' # 컬러 스타일 ex)'Accent', 'Accent_r', 'Blues', 'Blues_r' 등등
            ).generate(text)
            
            wc.to_file(path + 'WordCloud/' + writer + "({})".format(max_words) + '.png')
            print("Create WordCloud: " + writer)