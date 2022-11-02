from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys # needed for things like ENTER, TAB, SHITFT etc.

s=Service('C:\Development\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://en.wikipedia.org/wiki/Main_Page/")

# count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a") # the # is for the id tag

# to find a link (Contents) and click it, use this
contents = driver.find_element(By.LINK_TEXT, "Contents")
#contents.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python") # types into a field 
search.send_keys(Keys.ENTER) # presses enter

#driver.quit() # quits the entire browser