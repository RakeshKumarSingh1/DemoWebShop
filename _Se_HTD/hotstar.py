from selenium import webdriver
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path)
driver.get("https://www.hotstar.com/in")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//button[@class='subscribe-btn right-element']").click()