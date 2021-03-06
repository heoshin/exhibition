from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
# from soupsieve.util import get_pattern_context
import time
import numpy as np
import json
import pandas as pd

driver = webdriver.Chrome('./chromedriver.exe')

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
    df = pd.DataFrame(columns=['writer', 'date', 'title', 'content'])

    contents = np.array([])
    for i, post in enumerate(posts):
        content = get_content(post)
        contents = np.append(contents, content)
        df = df.append(content, ignore_index=True)
        print(content)
        print("Get Contents: ", i + 1, "/", len(posts), sep="")
    print("Complate Get Post Contents")

    return df

def get_content(path):
    req_url = main_url + path
    driver.get(req_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.select_one('#kboard-avatar-document > div.kboard-document-wrap > div.kboard-title > h1').text.strip()
    writer = soup.select_one('#kboard-avatar-document > div.kboard-document-wrap > div.kboard-detail > div.detail-attr.detail-writer > div.detail-value').text.strip()
    writer = writer.lstrip("??????")
    content = soup.select_one('#kboard-avatar-document > div.kboard-document-wrap > div.kboard-content > div').text.strip()
    date = soup.select_one('#kboard-avatar-document > div.kboard-document-wrap > div.kboard-detail > div.detail-attr.detail-date > div.detail-value').text.strip()
    # print("writer: " + writer + "  title: " + title)
    return {"writer" : str(writer), "date" : str(date), "title": str(title), "content": str(content)}

login()

main_url = "http://gaz1979.dothome.co.kr/"

path = "./??????????????????-?????????-???_?????????/"
target = "??????????????????-?????????-???-2"
posts = getPostUrlByBulletin(main_url + target)

contents_df = CrawlFromPosts(posts)

contents_df.to_csv(path + 'contents.csv', header=True, index=False)

# with open(path + "contents.json", "w", encoding='UTF-8') as f:
#     json.dump(list(contents), f, ensure_ascii=False, indent=4)
print("save txt!")