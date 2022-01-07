import os
import random  # define the random module
import string
import sys
import threading
import time

import requests
import selenium.common.exceptions
import selenium
from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
if len(sys.argv) < 2:
    print("make sure to start from main.py or same arguments as that: python remixer.py *file*")
    print(sys.argv)
    exit()
#
CAPTCHA_BYPASS_WITH_BUSTER = True
#

options = Options()
options.add_argument("--enable-javascript")
#options.add_argument("--headless")
options.set_preference("profile" ,"C:/Users/pc/AppData/Roaming/Mozilla/Firefox/Profiles/scraper")
browser = webdriver.Firefox(options=options)
browser.implicitly_wait(20)
if CAPTCHA_BYPASS_WITH_BUSTER is True:
    browser.install_addon(os.path.join(os.getcwd(),"buster.xpi"), temporary=False)
file = sys.argv[1]
f = open(file, "r")
filecontents = []
readfile = f.read().split("\n")
del readfile[-1]
for filecontent in readfile:
    filecontent = filecontent.split("~")#.replace("https://glitch.com/","")
    filecontent = filecontent[1].split(":")[0]
    filecontents.append(filecontent)
for filecontent in filecontents:
    try:
        browser.get(f"https://glitch.com/edit/#!/remix/{filecontent}")
    except selenium.common.exceptions.UnexpectedAlertPresentException:
        e = browser.find_element(By.ID, "rc-control")
        if e:
            if CAPTCHA_BYPASS_WITH_BUSTER is True:
                browser.find_element(By.ID, "solver-button").click()
                time.sleep(1)
            else:
                browser.refresh() # tries to bypass anyway?
    time.sleep(1)
    while True:
        try:
            WebDriverWait(browser, 120).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/button[4]/div'))
                    )
            browser.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[1]/button[4]/div').click()
            browser.find_element(By.XPATH,("/html/body/div[6]/div/div/div/div[1]")).click()
            to_download = browser.find_element(By.XPATH, ('//*[@id="download-project"]')).get_attribute('href')#"""https://glitch.com/edit/#!/remix/spurious-held-law"""
            content = requests.get(to_download)
            open(f"{filecontent}.tgz", 'wb').write(content.content)
            break
        except (selenium.common.exceptions.NoSuchElementException,selenium.common.exceptions.ElementNotInteractableException,selenium.common.exceptions.ElementClickInterceptedException
                ,selenium.common.exceptions.StaleElementReferenceException):
            break
    while True:
        try:
            browser.find_element(By.XPATH,"/html/body/div[3]/div/header/nav/button/div/span").click()
            browser.find_element(By.XPATH,'//*[@id="delete-project"]').click()
            ale = browser.switch_to.alert
            ale.accept()
            break
        except (selenium.common.exceptions.NoSuchElementException,selenium.common.exceptions.ElementNotInteractableException,selenium.common.exceptions.ElementClickInterceptedException
                ,selenium.common.exceptions.StaleElementReferenceException):
            break
