from selenium import webdriver
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver1=webdriver.Chrome(path)
driver1.get('https://services.smartbear.com/samples/testcomplete14/smartstore/sunglasses')
