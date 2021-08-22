from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.firefox.options import Options
import time
import string
import threading
import os
import sys
import random
options = Options()
options.add_argument("--enable-javascript")
options.add_argument("--headless")
print("initalizing")
fp = webdriver.FirefoxProfile("C:/Users/pc/AppData/Roaming/Mozilla/Firefox/Profiles/scraper")
fp.set_preference("permissions.default.image", 2)
browser = webdriver.Firefox(options=options,firefox_profile=fp)
browser.get("https://glitch.com/edit/#!/hello-express")
def randomtext():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10 )) 
#
remix = False
#

rantext = randomtext()

file = f"glitch.{rantext}.txt"
file2 = f"glitch.desc.{rantext}.txt"
f = open(file, "a+",encoding="utf-16")
f2 = open(file2, "a+",encoding="utf-16")

print(file)

print("init finished")

def scrap(url):
    f = open(file, "a+",encoding="utf-16")
    f2 = open(file2, "a+",encoding="utf-16")
    browser.get(f'https://glitch.com/search?q={url}&activeFilter=project')
    print(f"scraping {url}")
    for i in range(100):
        e = browser.find_elements_by_xpath(f"/html/body/div/div/div[2]/main/article/ul/li[{i}]/div/div/div/div/div/a")
        e2 = browser.find_elements_by_xpath(f"/html/body/div/div/div[2]/main/article/ul/li[{i}]/div/div/div/div/div/a/div[2]/div/p")
        for elem in e:
            threading.Thread(target=f.write(f'{elem.get_attribute("href")}:{url}\n'))
        for elem in e2:
            threading.Thread(target=f2.write(f'{elem.text}\n'))
    f.close()
    f2.close()
    print(f"finished scraping {url}")
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