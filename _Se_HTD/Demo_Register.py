from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
time.sleep(2)
reg=driver.find_element_by_xpath("//a[text()='Register']")
ac_obj=ActionChains(driver)
time.sleep(2)

ac_obj.context_click(reg).perform()
time.sleep(2)
ac_obj.send_keys(Keys.TAB).perform()
time.sleep(2)
ac_obj.send_keys(Keys.ENTER).perform()