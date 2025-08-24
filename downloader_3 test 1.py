# -*- coding: cp1251 -*-

import time
import json
import random
from urllib import response
import requests
from bs4 import BeautifulSoup
import fake_useragent
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#main link
link_list = ["https://kemono.cr/patreon/user/71053882/post/132354800",
             "https://kemono.cr/patreon/user/71053882/post/132280643",
             "https://kemono.cr/patreon/user/71053882/post/132201109", 
             "https://kemono.cr/patreon/user/71053882/post/131094809",
             "https://kemono.cr/patreon/user/71053882/post/130130110", 
             "https://kemono.cr/patreon/user/71053882/post/130039352", 
             "https://kemono.cr/patreon/user/71053882/post/129801141",
             "https://kemono.cr/patreon/user/71053882/post/128400168",
             "https://kemono.cr/patreon/user/71053882/post/128316268",
             "https://kemono.cr/patreon/user/71053882/post/127927513"]


# link_list = ["https://kemono.cr/patreon/user/71053882/post/132280643", 
#              "https://kemono.cr/patreon/user/71053882/post/132201109", 
#              "https://kemono.cr/patreon/user/71053882/post/132354800"]

#count post number
user = fake_useragent.UserAgent().random

#options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user}")
browser = webdriver.Chrome(options=options)

file_link_list = []

for b in range(len(link_list)):
   
    browser.get(link_list[b])
    time.sleep(2)

    file_link = browser.find_elements(By.CLASS_NAME, "fileThumb")
    for c in range(len(file_link)):

        file_href = file_link[c].get_attribute('href')
        if file_link_list.count(file_href) > 0:
            continue

        file_link_list.append(file_href)
        print("      ", file_href)

    time.sleep(2)

    


for ac in range(len(file_link_list)):
    print(file_link_list[ac])


# pic_bytes = requests.get(link).content

# with open("download/name", 'wb') as file:
#     file.write(pic_bytes)

#     print("ok")

