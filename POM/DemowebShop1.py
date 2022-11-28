from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
time.sleep(2)
driver.find_element("xpath",'//a[text()="Register"]').click()
time.sleep(1)

# radio button
driver.find_element("xpath",'//input[@id="gender-male"]').click()
time.sleep(1)

#first name
driver.find_element("id","FirstName").send_keys("Rakesh")
time.sleep(1)

#last name
driver.find_element("id","LastName").send_keys("Singh")
time.sleep(1)

#email
driver.find_element("id","Email").send_keys("rkscpr9934@gmail.com")
time.sleep(1)

#Password
driver.find_element("xpath","//input[@id='Password']").send_keys("rakesh@123")
time.sleep(1)

#Confirm Password
driver.find_element("xpath","//input[@id='ConfirmPassword']").send_keys("rakesh@123")
time.sleep(1)

#click Resister
driver.find_element("id","register-button").click()
time.sleep(1)

#Click Login
driver.find_element("xpath","//a[text()='Log in']").click()
time.sleep(1)

#Provide email
driver.find_element("id","Email").send_keys("rkscpr9934@gmail.com")
time.sleep(1)

#Provide Paasword
driver.find_element("id","Password").send_keys("rakesh@123")
time.sleep(1)

#Remember Password
driver.find_element("id","RememberMe").click()
time.sleep(2)

#Forgot Password
driver.find_element("xpath","//a[text()='Forgot password?']").click()
time.sleep(2)
driver.back()

# Click Login
driver.find_element("xpath","//input[@value='Log in']").click()
time.sleep(1)

#Click Logout
driver.find_element("xpath","//a[text()='Log out']").click()
