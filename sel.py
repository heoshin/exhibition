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
import pyautogui

driver = webdriver.Chrome('./chromedriver.exe')

# driver.get('http://gaz1979.dothome.co.kr/login/?redirect_to=%2F')
# time.sleep(0.5)
# driver.find_element_by_xpath('//*[@id="post-1463"]/div/div/form/fieldset/div[4]/a[1]').click()
# time.sleep(0.5)
# driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('1guestyeongbeul')
# time.sleep(0.5)
# driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
# time.sleep(0.5)
# driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('rnrmf0713')
# time.sleep(0.5)
# driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

driver.get('http://gaz1979.dothome.co.kr/login')
driver.find_element_by_xpath('//*[@id="post-1463"]/div/div/form/fieldset/div[4]/a[1]').click()
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
element.send_keys('ghtls050')
element.send_keys(Keys.RETURN)
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
element.send_keys('rnrmf030810')
element.send_keys(Keys.RETURN)
# time.sleep(3)
# pyautogui.write('ghtls050')
# time.sleep(1)
# pyautogui.press('enter')
# time.sleep(3)
# pyautogui.write('rnrmf030810')
# pyautogui.press('enter')

input()

driver.get('http://gaz1979.dothome.co.kr/물금고등학교-진로-관련-자료/')
driver.find_element_by_css_selector('#kboard-avatar-list > div.kboard-list > table > tbody > tr:nth-child(1) > td.kboard-list-title > a').click()
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

content = soup.select_one('#kboard-avatar-document > div.kboard-document-wrap > div.kboard-content > div')
print(content.text)