                               # Action Chain
#Keys
#. from selenium.webdriver.common.action_chains import Actionchains
#'''to perform lower level operations we use action chain function.
#ex= clicking, dragging,dropping ,double click ,overing around'''

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
# driver1=webdriver.Chrome(executable_path=path)
# driver1.get('https://www.meesho.com/')
# driver1.maximize_window()
# women_ethnic=driver1.find_element_by_xpath("//span[text()='Women Ethnic']")
# ac_obj=ActionChains(driver1)
# ac_obj.move_to_element(women_ethnic).perform()

##########################################################################################

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver1=webdriver.Chrome(path)
driver1.get('file:///C:/Users/admin/OneDrive/Desktop/Selenium/demo%20(1).html')
time.sleep(3)
driver1.maximize_window()
ele_add=driver1.find_element_by_id('double-click')
ac_obj=ActionChains(driver1)
ac_obj.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(2)
ac_obj.double_click(ele_add).perform()
time.sleep(2)
ac_obj.send_keys(Keys.PAGE_UP)

###Simulating Keys

ac_obj.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()