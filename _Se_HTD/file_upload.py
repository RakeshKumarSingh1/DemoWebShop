
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('file:///C:/Users/admin/OneDrive/Desktop/Selenium/demo%20(1).html')
driver.find_element_by_xpath()
time.sleep(2)
alert_obj=driver.switch_to.alert
time.sleep()
alert_obj.dismiss()

file_path=''
driver.find_element_by_id()