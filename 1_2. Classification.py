import pandas as pd
import json
import numpy as np
import re

path = "./물금고등학교-익명의-숲_진로편/"
        
df = pd.read_csv(path + 'contents.csv')

# df = df.sort_values(by=["writer", "date"])
# cnt = df["writer"].value_counts()

# df = df.drop(['date', 'title'], axis=1)
df = df.dropna()

df_class = df.groupby('writer').agg({'content': ''.join}).reset_index()
clean = re.compile(r'[^가-힣ㄱ-ㅎㅏ-ㅣ ]')
df_class['content'] = df_class['content'].apply(lambda x: clean.sub('', x))

df_class.to_csv(path + 'classification.csv', index=False)
