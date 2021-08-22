from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.firefox.options import Options
import time
import string
import threading
import random # define the random module
import os
import requests
import sys
options = Options()
options.add_argument("--enable-javascript")
options.add_argument("--headless")
fp = webdriver.FirefoxProfile("C:/Users/pc/AppData/Roaming/Mozilla/Firefox/Profiles/scraper")
browser = webdriver.Firefox(firefox_profile=fp)
browser.implicitly_wait(20)
if len(sys.argv) < 2:
    print("make sure to start from main.py or same arguments as that: python remixer.py *file*")
    print(sys.argv)
    exit()

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
    browser.get(f"https://glitch.com/edit/#!/remix/{filecontent}")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="tools-pop-button"]').click() #"""https://glitch.com/edit/#!/remix/spurious-held-law"""
    browser.find_element_by_xpath("/html/body/div[3]/div/main/div[1]/section[1]/footer/section/div[2]/dialog/section[3]/div[1]/button").click()
    to_download = browser.find_element_by_xpath('//*[@id="download-project"]').get_attribute('href')
    content = requests.get(to_download)
    open(f"{filecontent}.tgz", 'wb').write(content.content)
    browser.find_element_by_xpath("/html/body/div[3]/div/header/nav/button/div/span").click()
    browser.find_element_by_xpath('//*[@id="delete-project"]').click()
    ale = browser.switch_to.alert
    ale.accept()