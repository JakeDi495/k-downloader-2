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



# file_link_list_file = open("file_link_list.txt", "r")

# file_list = file_link_list_file.read()
# file_list = file_list.split(",")

# for aa in file_list:
#     print(file_list.index(aa)+1, aa)

# file_link_list_file.close



lane = int(input())
print(lane)
