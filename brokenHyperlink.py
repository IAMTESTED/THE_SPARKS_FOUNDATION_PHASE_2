import request
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
driver.maximize_window()
driver.get('http://www.irctc.com/')


links = driver.find_element_by_css_selector("a")
print("Total number of links present on the websites = ", len(links))

print("Broken Links are Listed Below")

for link in links:
    linkReq = requests.head(link.get_attribute('href'))
    if(linkReq.status_code >=400):
        print(link.get_attribute('href'),linkReq.status_code)
time.sleep(2)
driver.quit()
print("The test is complete")
