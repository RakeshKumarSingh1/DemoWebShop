

from selenium import webdriver
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path)
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("8873727774")
time.sleep(3)
driver.find_element_by_id("pass").send_keys("Indudevi@123")
time.sleep(3)
driver.find_element_by_xpath("//button[@name='login']").click()
