from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  #Explicit_Wait class
from selenium.webdriver.support import expected_conditions
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path)
driver.get('file:///C:/Users/admin/OneDrive/Desktop/Selenium/progressbar%20(1).html')
driver.maximize_window()
driver.find_element_by_xpath("//button[text()='Click Me']").click()
wait_obj= WebDriverWait(driver,100)
wait_obj.until(expected_conditions.presence_of_element_located(("xpath","//div[text()='100%']")))
driver.find_element_by_xpath("//button[text()='Click Me']").click()
