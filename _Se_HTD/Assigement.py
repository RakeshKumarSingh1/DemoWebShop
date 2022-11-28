from selenium import webdriver
import time

path = r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
object1=webdriver.Chrome(path)
object1.get("https://demo.actitime.com/login.do")
object1.find_element_by_class_name('textField').send_keys('admin')
object1.find_element_by_class_name('textField.pwdfield').send_keys('manager')
object1.find_element_by_xpath("//div[text()='Login ']").click()
time.sleep(10)
object1.find_element_by_xpath("//a[@class='logout']").click()

###############contains
'''syntax: (//tagname[contains(@attribute, 'attribute value')])[1]'''
