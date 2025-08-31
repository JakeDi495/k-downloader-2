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







#get list post

#create list post's links outside cycles
link_list = []


for an in range(0, post_count*50+1, 50):

    if an == 0:
        a_mod = ""
    else:
        a_mod = f"?o={an}"

    print(f"{link}{a_mod}")

    #open link
    browser.get(f"{link}{a_mod}")
    time.sleep(2)

   
    #find block
    link_list_sel = browser.find_element(By.CLASS_NAME, "card-list__items")
    #find list post's links on page
    links_post = link_list_sel.find_elements(By.CLASS_NAME, "fancy-link--kemono")

    for a in range(len(links_post)):
        href = links_post[a].get_attribute('href')
        link_list.append(href)
        print(len(link_list), href)

    

#create list file's links outside cycles
file_link_list = []



for b in range(len(link_list)):
    browser.get(link_list[b])
    time.sleep(2)

    #find file's links
    file_link = browser.find_elements(By.CLASS_NAME, "fileThumb")
    for c in range(len(file_link)):
        file_href = file_link[c].get_attribute('href')

        #eliminate duplicates
        if file_link_list.count(file_href) > 0:
            continue

        file_link_list.append(file_href)

        file_link_list_file = open("file_link_list.txt", "w")
        file_link_list_file.write(",".join(file_link_list))
        file_link_list_file.close

        print(len(file_link_list), file_href)


    time.sleep(2)




# pic_bytes = requests.get(link).content

# with open("download/name", 'wb') as file:
#     file.write(pic_bytes)

#     print("ok")

