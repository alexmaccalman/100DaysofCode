
# Locating elements: https://selenium-python.readthedocs.io/locating-elements.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s=Service('C:\Development\chromedriver.exe')
driver = webdriver.Chrome(service=s)


driver.get("https://www.python.org/")
# inside of the inspect, right click the element, click copy and choose "copy XPATH"
# price = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]')

# var = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# table = var.text
# list_data = table.split("\n")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time") # use the medium-widget "event-widget" and then the time element
# find_elements returns a list so loop through them to print them
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a") # three layers of CSS selectors
# for event in event_times:
#     print(event.text)

# create a dictionary of dictionary
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

#driver.close() #closes the current browser tab
driver.quit() # quits the entire browser





