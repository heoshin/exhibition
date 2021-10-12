from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
from soupsieve.util import get_pattern_context
import time
import numpy as np
from urllib3 import request

driver = webdriver.Chrome('./chromedriver.exe')

main_url = "http://gaz1979.dothome.co.kr/"

def login_google():
    driver.get('http://gaz1979.dothome.co.kr/login')
    driver.find_element_by_xpath('//*[@id="post-1463"]/div/div/form/fieldset/div[4]/a[1]').click()
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
    element.send_keys('ghtls050')
    element.send_keys(Keys.RETURN)
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    time.sleep(0.5)
    element.send_keys('rnrmf030810')
    element.send_keys(Keys.RETURN)

def login():
    driver.get('http://gaz1979.dothome.co.kr/login')
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="log"]')))
    element.send_keys('gaz1979')
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pwd"]')))
    element.send_keys('jeongsiwoo1007!')
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="post-1463"]/div/div/form/fieldset/div[3]/input')))
    element.click()

def get_posts(url):
    posts = np.array([])
    for i in range(1, 10):
        req_url = url + "/?pageid=" + str(i)
        req = requests.get(req_url)
        html = req.text
        time.sleep(1)
        soup = BeautifulSoup(html, 'html.parser')

        hrefs = soup.select("#kboard-avatar-list > div.kboard-list > table > tbody > tr > td.kboard-list-title > a")
        print(hrefs)
        for link in hrefs:
            post_link = link.get("href")
            posts = np.append(posts, main_url + post_link)

    return posts

def get_content(path):
    req_url = main_url + path
    driver.get(req_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.select_one('#kboard-avatar-document > div.kboard-document-wrap > div.kboard-content > div')
    content = content.text.strip() + "\n"
    return content

login()

posts = get_posts(main_url + "물금고등학교-익명의-숲")
print("Complate Posts")

contents = np.array([])
for i, post in enumerate(posts):
    contents = np.append(contents, get_content(post))
    print("Get Contents: ", i + 1, "/", len(posts), sep="")

with open("contents.txt", "w", encoding='UTF-8') as f:
    for text in contents:
        f.write(text)
print("save txt!")