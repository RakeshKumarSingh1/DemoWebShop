from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
driver.implicitly_wait(20)
ac_obj = ActionChains(driver)

driver.find_element_by_xpath("//input[@value='Search']").click()
# aler_obj=driver.switch_to.alert
# aler_obj.accept()
driver.find_element_by_link_text("Log in").click()
