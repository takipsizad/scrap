import os
import random
import string
import sys
import threading
import time

import selenium
from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--enable-javascript")
options.add_argument("--headless")
print("initalizing")
options.set_preference("profile" ,"C:/Users/pc/AppData/Roaming/Mozilla/Firefox/Profiles/scraper")
options.set_preference("permissions.default.image", 2)
browser = webdriver.Firefox(options=options)
browser.get("https://glitch.com/edit/#!/hello-express")
def randomtext():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10 )) 
#
remix = False
#

rantext = randomtext()

file = f"glitch.{rantext}.txt"
file2 = f"glitch.desc.{rantext}.txt"
f = open(file, "a+",encoding="utf-8")
f2 = open(file2, "a+",encoding="utf-16")

print(file)

print("init finished")

def scrap(url):
    try:
        browser.get(f'https://glitch.com/search?q={url}&activeFilter=project')
    except selenium.common.exceptions.UnexpectedAlertPresentException:
        print("alert")
        browser.refresh();
    print(f"scraping {url}")
    f = open(file, "a+",encoding="utf-8")
    f2 = open(file2, "a+",encoding="utf-16")
    for i in range(100):
        try:
            WebDriverWait(browser, 120).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/main/article/ul/li[1]/div/div/div/div/div/a"))
                    )
            e = browser.find_elements(By.XPATH,f"/html/body/div/div/div[2]/main/article/ul/li[{i}]/div/div/div/div/div/a")
            e2 = browser.find_elements(By.XPATH,f"/html/body/div/div/div[2]/main/article/ul/li[{1}]/div/div/div[1]/p")
        except selenium.common.exceptions.TimeoutException:
            break
        for elem in e:
            f.write(f'{elem.get_attribute("href")}:{url}\n')
        for elem in e2:
            f2.write(f'{elem.text}\n')
    print(f"finished scraping {url}")
    f.close()
    f2.close()
keywords = [
"j4j",
"bot",
"dm",
"matador dm",
"altyapı",
"v12 altyapı",
"en iyi altyapı",
"dizzy",
"botclub",
"asreaper",
"dumps",
"gamerwolf",
"lrows",
"hypnos",
"Lord Creative",
"Muhammed Demirel",
"maximus boys",
"enes ancar",
"nitro gen",
"gif",
"gizli",
"uptime",
"v13",
"v12",
"v11",
"discord.gg",
"discord bot altyapı",
"lynx",
"dm duyuru",
"raid",
"Aethra",
"Charles",
"Jumbo codding",
"Uptime",
"vension",
"disboard",
"ses",
"redania",
"MustiDvclr",
"salvo",
"ATHERİUS",
"synx",
"powercode",
"CodeMareFi",
"bybiggz",
"jkood",
"nordx",
"Present Code",
"CodeWork",
"Bedels",
"acar",
"ban bot",
"nitro gen",
"synem",
"Creative Developers",
"Codinator",
"Aoi.js",
"Tokyo development",
"iAyAspth",
"saturn",
"BlackBlvee ",
"cloudup",
"codare",
"rasex",
"Koala Youtube",
"deu",
"ryhson",
"Code Shâre",
"SPLASHEN",
"Xentrias",
"Valiant Developers",
"Kinger",
"FrenzyCODE",
]
for keyword in keywords:
    scrap(keyword)
if remix == True:
    os.system(f"{sys.executable} remixer.py {file}")
