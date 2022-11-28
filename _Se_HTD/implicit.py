##implicit wait- it is applied only to find_element,find_elements
#     you cannot give the condition


import time

from selenium import webdriver
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver1=webdriver.Chrome(path)
driver1.implicitly_wait(10)
# driver1.get('file:///C:/Users/admin/OneDrive/Desktop/Selenium/loading%20(1).html')
# driver1.maximize_window()
# start=time.time()
# driver1.find_element_by_name('fname').send_keys('Rakesh')
# end=time.time()
#print(end-start)

driver1.get('file:///C:/Users/admin/OneDrive/Desktop/Selenium/progressbar%20(1).html')
driver1.maximize_window()
driver1.find_element_by_xpath("//button[text()='Click Me']").click()
driver1.find_element_by_xpath("//div[text()='100%']")
driver1.find_element_by_xpath("//button[text()='Click Me']").click()