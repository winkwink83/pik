from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from functools import partial
from tkinter import *



def techang(cos):
    driver = webdriver.Chrome('/chromedriver.exe')
    driver.get('https://www.google.pl/')
    time.sleep(1)
    element = driver.find_element(By.XPATH, '//*[@id="W0wltc"]/div')
    element.click()

    search = driver.find_element(By.NAME, 'q')
    search.send_keys(str(cos))
    time.sleep(1)
    search.send_keys(Keys.RETURN)

    news = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[3]/a')
    news.click()
    time.sleep(1)
    articles =driver.find_elements(By.CLASS_NAME, 'WlydOe')
    titles = []
    for article in articles:
        if len(article.text) > 1:
            titles.append(article)
            print(article.text)
    print(len(titles))
