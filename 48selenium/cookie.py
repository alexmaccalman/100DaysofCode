from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys # needed for things like ENTER, TAB, SHITFT etc.
import time

s=Service('C:\Development\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element(By.ID, "bigCookie")
# print(cookie.size)
# get upgrade item ids
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

print(item_ids)
timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

# while True:
#     cookie.click()

#     #Every 5 seconds:
#     if time.time() > timeout:

#         #Get all upgrade <b> tags
#         all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
#         item_prices = []
        
#         for price in all_prices:
#             print(price.text)

# 

# driver.quit() # quits the entire browser