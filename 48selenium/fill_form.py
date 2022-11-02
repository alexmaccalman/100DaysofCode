from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys # needed for things like ENTER, TAB, SHITFT etc.

s=Service('C:\Development\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Alex")
first_name.send_keys(Keys.ENTER) # presses enter
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Mac")
last_name.send_keys(Keys.ENTER) # presses enter
email = driver.find_element(By.NAME, "email")
email.send_keys("mac@mac")
email.send_keys(Keys.ENTER) # presses enter

submit = driver.find_element(By.CSS_SELECTOR, "form button") # finds the "form" tag, then finds the "button" tag
submit.click()