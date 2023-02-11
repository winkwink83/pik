from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def techAn(cos):
    driver = webdriver.Chrome('/chromedriver.exe')
    driver.get('https://www.youtube.com/')
    element = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
    element.click()
    time.sleep(1)
    element = driver.find_element(By.NAME,'search_query')
    element.send_keys(str(cos))
    time.sleep(1)
    element.send_keys(Keys.RETURN)
    time.sleep(1)
    articles = driver.find_elements(By.ID,'video-title')
    titles = []
    for article in articles:
        if len(article.text) > 1:
            titles.append(article)
            print(article.text)
    print(len(titles))
