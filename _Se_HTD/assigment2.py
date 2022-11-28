from selenium import webdriver
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get("https://www.python.org/downloads/")
time.sleep(1)
driver.maximize_window()
time.sleep(5)
#driver.find_element_by_xpath("//a[text()='Python 3.10.8']/../..//a[text()='Release Notes']").click()
driver.find_element_by_xpath("//a[text()='Python 3.11.0']/../..//a[text()='Release Notes']").click()