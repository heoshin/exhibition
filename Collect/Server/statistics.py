from numpy.core.fromnumeric import shape
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import json

with open("collect.json", "r", encoding='UTF-8') as j:
    json_file = dict(json.load(j))

for mac, datas in json_file.items():
    print(mac)
    np_datas = np.array(np.empty((0, 2)))
    np_date = np.array([])
    values = dict()
    for k in datas[0]["values"]:
        values[k] = np.array(list(), dtype=np.float32)
    
    np_tmp = np.array([])
    for data in datas:
        np_date = np.append(np_date, data["date"])
        for k, v in data["values"].items():
            values[k] = np.append(values[k], float(v))

# fig = plt.figure(figsize=(20, 6))

plt.subplot(1, 5, 1)
plt.ylim([0, 40])
plt.plot(np_date, values["tmp"], color="red", label="tmp")
plt.legend()

plt.subplot(1, 5, 2)
plt.ylim([20, 100])
plt.plot(np_date, values["hum"], color="blue", label="hum")
plt.legend()

plt.subplot(1, 5, 3)
plt.ylim([0, 4000])
plt.plot(np_date, values["co2"], color="black", label="co2")
plt.legend()

plt.subplot(1, 5, 4)
# plt.ylim([0, 2000])
# plt.plot(np_date, values["pm"], color="black", label="pm")
# plt.legend()

plt.subplot(1, 5, 5)
# plt.ylim([0, 1024])
# plt.plot(np_date, values["voc"], color="black", label="voc")
# plt.legend()
plt.show()
