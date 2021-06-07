import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def openYT():
    driver = webdriver.Firefox(executable_path = '/Applications/Python 3.9/bin/geckodriver')
    driver.get('https://www.youtube.com/watch?v=cmsTvlFv0ug')
    driver.fullscreen_window()
    playButton = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/button")
    playButton.click()
    fsButton = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[31]/div[2]/div[2]/button[10]')
    fsButton.click()

    try:
        element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    finally:
        driver.quit()    
