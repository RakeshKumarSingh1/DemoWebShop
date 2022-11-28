from selenium import webdriver
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get("file:///C:/Users/admin/OneDrive/Desktop/Selenium/demo%20(1).html")
time.sleep(5)
driver.maximize_window()
\
# list2=driver.find_elements_by_xpath("//tbody//input")
# for element in list2:
#     element.click()
#     time.sleep(2)

##X path using dependent and independent element
# list1=['Ruby', 'Java' ,'Perl', 'Python', 'C#', 'JavaScript']
# # for item in list1:
# #     driver.find_element_by_xpath(f"//td[text()='{item}']/..//input[@name='download']").click()
#
# for item in list1[::-2]:
#     driver.find_element_by_xpath(f"//td[text()='{item}']/..//input[@name='download']").click()
# list1=["Ruby","Python","Java","Perl","C#","JavaScript","Php","c"]
# textbox=driver.find_element_by_xpath(//input[contains(@name,'fname')]
# for element,value in zip(list1,textbox):
#     element.send_keys(value)

