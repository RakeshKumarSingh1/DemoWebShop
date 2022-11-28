from selenium import webdriver
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath("//label[text()='Excellent']/..//input[@id='pollanswers-1']").click()
time.sleep(2)
driver.find_element_by_xpath("//label[text()='Good']/..//input[@id='pollanswers-1']").click()
time.sleep(2)