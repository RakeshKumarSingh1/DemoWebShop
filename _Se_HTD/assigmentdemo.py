from selenium import webdriver
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver1=webdriver.Chrome(path)
driver1.get('https://demowebshop.tricentis.com/books')
time.sleep(1)
driver1.maximize_window()
list1=['Health Book', 'Fiction','Computing and Internet']
for item in list1:
    #driver1.find_element_by_xpath("//a[text()='Computing and Internet']/../..//input[@class='button-2 product-box-add-to-cart-button']").click()
    driver1.find_element_by_xpath(f"//a[text()='{item}']/../..//input[@class='button-2 product-box-add-to-cart-button']").click()
    time.sleep(3)

