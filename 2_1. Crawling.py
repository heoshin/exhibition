from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from soupsieve.util import get_pattern_context
import time
import numpy as np
import json

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

def getPostUrlByBulletin2(url):
    driver.get(url)
    posts = np.array([])
    while True:
        posts = np.append(posts, getPostUrlByPage())
        print(len(posts))
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#kboard-avatar-list > div.kboard-pagination > ul > li.next-page > a')))
            element.click()
        except:
            break
    print("Complate Posts")
    return posts

def getPostUrlByBulletin(url):
    driver.get(url)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#kboard-avatar-list > div.kboard-pagination > ul > li.last-page > a'))).click()
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#kboard-avatar-list > div.kboard-pagination > ul > li.active > a')))
        print("lastNum: " + element.text)
        lastNum = int(element.text)
    except:
        lastNum = 1

    posts = np.array([])
    for i in range(1, lastNum + 1):
        driver.get(url + "/?pageid=" + str(i))
        posts = np.append(posts, getPostUrlByPage())
        print(len(posts), "  ", i, "/", lastNum, sep="")

    print("Complate Get Post Url")
    return posts

def getPostUrlByPage():
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select("#kboard-avatar-list > div.kboard-list > table > tbody > tr > td.kboard-list-title > a")
    posts = []
    for link in links:
        post_link = link.get("href")
        posts.append(main_url + post_link)

    return posts

def CrawlFromPosts(posts):
    contents = np.array([])
    for i, post in enumerate(posts):
        contents = np.append(contents, get_content(post))
        print("Get Contents: ", i + 1, "/", len(posts), sep="")
    print("Complate Get Post Contents")
    return contents

def get_content(path):
    req_url = main_url + path
    driver.get(req_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.select_one('#kboard-avatar-document > div.kboard-document-wrap > div.kboard-title > h1').text.strip()
    writer = soup.select_one('#kboard-avatar-document > div.kboard-document-wrap > div.kboard-detail > div.detail-attr.detail-writer > div.detail-value').text.strip()
    writer = writer.lstrip("학생")
    content = soup.select_one('#kboard-avatar-document > div.kboard-document-wrap > div.kboard-content > div').text.strip()
    date = soup.select_one('#kboard-avatar-document > div.kboard-document-wrap > div.kboard-detail > div.detail-attr.detail-date > div.detail-value').text.strip()
    print("writer: " + writer + "  title: " + title)
    return {"writer" : writer, "date" : date, "title": title, "content": content}

login()

path = "./물금고등학교-익명의-숲_생활편/"
target = "물금고등학교-익명의-숲"
posts = getPostUrlByBulletin(main_url + target)

contents = CrawlFromPosts(posts)

with open(path + "contents.json", "w", encoding='UTF-8') as f:
    json.dump(list(contents), f, ensure_ascii=False, indent=4)
print("save txt!")