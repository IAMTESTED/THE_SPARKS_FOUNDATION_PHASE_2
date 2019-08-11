from selenium import webdriver
import time

email = "akashkumarguptaisc1997"
pwd = "AKG070797@"
rec = "raka123"
subj = "Automation Test"
txt = "This is how automation is performed with the combination of Python and Selenium Webdriver. "

driver = webdriver. Chrome(executable_path="../driver/chromedriver.exe")
driver.maximize_window()
driver.get("http://www.gmail.com/")
time.sleep(1)
driver.find_element_by_name("identifier").send_keys(email)
driver.find_element_by_id("identifierNext").click()
driver.implicitly_wait(5)
driver.find_element_by_name("password").send_keys(pwd)
driver.find_element_by_id("passwordNext").click()
driver.find_element_by_css_selector('.aic .z0.div').click()
driver.find_element_by_id(":96").send_keys(rec)
driver.find_element_by_id(":80").send_keys(subj)
driver.find_element_by_id(":96").send_keys(txt)
driver.find_element_by_id(":8e").click()
time.sleep(1)
driver.close()