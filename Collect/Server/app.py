from re import template
from flask import Flask, request, render_template
import pandas as pd
import datetime as dt
import json
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to heoshin collect server"

@app.route('/sendGET')
def sendGET():
    values = request.args

    pushData(values)
    print(values)

    return f'tmp: {values["tmp"]} hum: {values["hum"]} co2: {values["co2"]} pm1:{values["pm1"]} pm2:{values["pm2"]} pm10:{values["pm10"]} voc: {values["voc"]}'

@app.route('/sendPOST', methods=["GET", "POST"])
def sendPOST():
    if request.method == "GET":
        return render_template("post.html")
        
    elif request.method == "POST":
        values = request.form
        pushData(values)
        return render_template("response.html", mac = request.form["mac"], tmp = request.form["tmp"], hum = request.form["hum"], co2 = request.form["co2"], pm = request.form["pm"], voc = request.form["voc"])

def pushData(values):
    datas = dict()

    mac = values["mac"]
    if not mac in datas.keys():
        datas[mac] = []

    valuesWithOutMac = dict()
    for k, v in values.items():
        if k != "mac":
            valuesWithOutMac[k] = v

    data = {"date" : str(dt.datetime.now()), "values" : valuesWithOutMac}

    datas[mac].append(data)
    
    print(mac, data)

    json_file = dict()
    if os.path.isfile("./collect.json"):
        with open("collect.json", "r", encoding='UTF-8') as j:
            json_file = json.load(j)

    for k, v in datas.items():
        if not mac in json_file.keys():
            json_file[mac] = []
        json_file[k].append(v[0])
    
    with open("collect.json", "w", encoding="UTF-8") as j:
        json.dump(json_file, j, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')

