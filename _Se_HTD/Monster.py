from selenium import webdriver
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('https://www.monsterindia.com/')
time.sleep(2)
driver.maximize_window()
driver.find_element_by_xpath("//input[@value='Search']").send_keys("Python Jobs")
driver.find_element_by_xpath("//input[@type='submit']").click()

