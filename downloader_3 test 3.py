# -*- coding: cp1251 -*-

import time
import json
import random
from urllib import response
import requests
from bs4 import BeautifulSoup
import fake_useragent
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By






#main link
link = "https://kemono.cr/patreon/user/14691210/post/313821680"


#count post number
user = fake_useragent.UserAgent().random

#options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user}")
browser = webdriver.Chrome(options=options)

#open link
browser.get(link)
time.sleep(2)



try:
    #error checking
    error_checking = browser.find_element(By.CLASS_NAME, "site-section--")
        
    if error_checking.text.count("Reason: 404") > 0:
        print("Yea"*100)

except selenium.common.exceptions.NoSuchElementException:
    print("ok")
    



# post_count = post_count.text.split(" ")
# post_count = int(post_count[-1])//50

# print(post_count)



