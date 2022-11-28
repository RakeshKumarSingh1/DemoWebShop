from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('https://www.monsterindia.com/')
driver.maximize_window()
ac_obj = ActionChains(driver)

job = driver.find_element_by_xpath("//a[@data-check='menutab']")
ac_obj.move_to_element(job).perform()
time.sleep(2)

skill = driver.find_element_by_xpath("//a[text()='Jobs by Skills']")
ac_obj.move_to_element(skill).perform()
time.sleep(2)

py = driver.find_element_by_xpath("//a[@href='https://www.monsterindia.com/search/python-jobs']")
ac_obj.click(py).perform()
time.sleep(2)

# driver.get('https://crossbrowsertesting.github.io/drag-and-drop.html')
# driver.maximize_window()
# time.sleep(2)
# source=driver.find_element_by_id("draggable")
# target=driver.find_element_by_id("droppable")
# ac_obj=ActionChains(driver)
# ac_obj.drag_and_drop(source,target).perform()
