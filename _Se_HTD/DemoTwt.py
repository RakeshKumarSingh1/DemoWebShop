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
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

driver.find_element_by_xpath("//a[@href='https://twitter.com/nopCommerce']").click()
time.sleep(2)

handles=driver.window_handles
print(handles)
driver.switch_to.window(handles[1])
time.sleep(2)
driver.find_element_by_xpath("//span[text()='Follow']").click()
