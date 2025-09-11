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






def get_file_link(link):

    #main link
    # link = "https://kemono.cr/patreon/user/15773096"


    #count post number
    user = fake_useragent.UserAgent().random

    #options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user}")
    browser = webdriver.Chrome(options=options)

    #open link
    browser.get(link)
    time.sleep(2)


    #page count
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
            file_link_list_file.write("\n".join(file_link_list))
            file_link_list_file.close

            print(len(file_link_list), file_href)


        time.sleep(2)



def download_file():
    file_link_list_file = open("file_link_list.txt", "r")

    file_list = file_link_list_file.read()
    file_list = file_list.split("\n")
    
    min_link_input = input("Введите номер начального файла для скачивания:  ")
    if min_link_input == "":
        min_link = 0
    else: min_link = int(min_link_input)

    max_link_input = input("Введите номер конечного файла для скачивания:  ")
    if max_link_input == "":
        max_link = len(file_list)
    else: max_link = int(max_link_input)

    for aa in range(min_link, max_link):

        file_name = file_list[aa].split("=")
        file_name = file_name[1]
        file_name = file_name.split("+")
        file_name = " ".join(file_name)

        user = fake_useragent.UserAgent().random
        header = {"user-agent": user}
        
        #pic_bytes = requests.get(file_list[aa], headers = header, verify=False).content
        pic_bytes = requests.get(file_list[aa], headers = header).content
        
        with open(f"download/{file_name}", 'wb') as file:
            file.write(pic_bytes)
               
        print(file_list.index(file_list[aa])+1, file_name, file_list[aa])

        time.sleep(random.uniform(0, 3)) 


    file_link_list_file.close




def view_list():
    file_link_list_file = open("file_link_list.txt", "r")

    file_list = file_link_list_file.read()
    file_list = file_list.split("\n")

    for aa in file_list:
        print(file_list.index(aa)+1, aa)





l_or_d = input("введите: l - получить ссылки, d - скачать файлы из списка file_link_list, v - посмотреть список:  ")


if l_or_d == "l":
    link = input("введите ссылку страницы автора:  ")
    get_file_link(link)
    
elif l_or_d == "d":
    download_file()

elif l_or_d == "v":
    view_list()



# pic_bytes = requests.get(link).content

# with open("download/name", 'wb') as file:
#     file.write(pic_bytes)

#     print("ok")

