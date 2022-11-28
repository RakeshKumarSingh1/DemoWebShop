#1  Switching by id/name attribute
''' 1.  driver.switch_to.frame("fr1)-- id value
    2. driver.switch_to.frame(frame)--name value'''

#  Switching by index
'''1.driver.switch_to.frame(index)'''

#  Switching by webelement
''' 1.web_frame1=driver.find_element_By_id(fr1)
    2.driver.Switch_to.frame(Web_frame1)'''

#   to switch back to parent frame
''' 1.driver_Switch_to.default_Content()'''

from selenium import webdriver
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path)
driver.get("file:///C:/Users/admin/OneDrive/Desktop/Selenium/iframe%20(1).html")
driver.maximize_window()
driver.implicitly_wait(20)

frame1=driver.find_element_by_id("FR1")
driver.switch_to.frame("frame1")
driver.find_element_by_id("small-searchterms").send_keys("pen")
driver.switch_to.default_content()

frame2=driver.find_element_by_id("FR2")
driver.switch_to.frame(frame2)
driver.find_element_by_id("search_form").send_keys("heyyy")
driver.switch_to.default_content()

#Switching using Webelement

ele=driver.find_element_by_xpath("//input[@type='text']")
