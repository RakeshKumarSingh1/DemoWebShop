from selenium import webdriver
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
time.sleep(3)

driver.get("https://www.python.org/")
driver.maximize_window()
time.sleep(2)
links=driver.find_elements_by_xpath("xpath","//a")
link_text=[]
for link in links:
    text=link_text
    print(link.get_attribute("href"))

    if text:
        link_text.append(text)

print(link_text)