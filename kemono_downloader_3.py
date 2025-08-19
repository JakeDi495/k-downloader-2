# -*- coding: cp1251 -*-

import time
import json
import random
from urllib import response
import requests
from bs4 import BeautifulSoup
import fake_useragent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#main link
link = "https://kemono.cr/patreon/user/71053882"


#count post number
user = fake_useragent.UserAgent().random

#options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user}")
browser = webdriver.Chrome(options=options)

#open link
browser.get(link)
time.sleep(2)

post_count = browser.find_element(By.TAG_NAME, "small")
post_count = post_count.text.split(" ")
post_count = int(post_count[-1])//50

print(post_count)

browser.close()






#get list post

#create list post's links outside cycles

link_list = []


for a in range(0, post_count*50+1, 50):

    user = fake_useragent.UserAgent().random

    #options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user}")
    browser = webdriver.Chrome(options=options)

    if a == 0:
        a_mod = ""
    else:
        a_mod = f"?o={a}"

    print(f"{link}{a_mod}")

    #open link
    browser.get(f"{link}{a_mod}")
    time.sleep(2)

   
    #find block
    link_list_sel = browser.find_element(By.CLASS_NAME, "card-list__items")
    #find list post's links on page
    links = link_list_sel.find_elements(By.CLASS_NAME, "fancy-link--kemono")

    for a in range(len(links)):
        href = links[a].get_attribute('href')
        link_list.append(href)
        print(len(link_list), href)

    browser.close()

time.sleep(15)




# pic_bytes = requests.get(link).content

# with open("download/name", 'wb') as file:
#     file.write(pic_bytes)

#     print("ok")

