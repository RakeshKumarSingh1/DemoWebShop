from selenium import
import time
from selenium.webdriver.support.select import Select
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
time.sleep(2)
driver.find_element_by_link_text('Register').click()
time.sleep(1)
#driver.find_element_by_xpath("//input[@id='gender-male']").click()

# radio button
driver.find_element_by_xpath("//label[@class='forcheckbox']/../..//input[@id='gender-male']").click()
time.sleep(1)

#first name
driver.find_element_by_id("FirstName").send_keys("Rakesh")
time.sleep(1)

#last name
driver.find_element_by_id("LastName").send_keys("Singh")
time.sleep(1)

#email
driver.find_element_by_id("Email").send_keys("rkscpr9934@gmail.com")
time.sleep(1)

#Password
driver.find_element_by_xpath("//input[@id='Password']").send_keys("rakesh@123")
time.sleep(1)

#Confirm Password
driver.find_element_by_xpath("//input[@id='ConfirmPassword']").send_keys("rakesh@123")
time.sleep(1)

#click Resister
driver.find_element_by_id("register-button").click()
time.sleep(1)

#Click Login
driver.find_element_by_xpath("//a[text()='Log in']").click()
time.sleep(1)

#Click email
driver.find_element_by_id("Email").click()
time.sleep(1)

#Provide email
driver.find_element_by_id("Email").send_keys("rkscpr9934@gmail.com")
time.sleep(1)

#Provide Paasword
driver.find_element_by_id("Password").send_keys("rakesh@123")
time.sleep(1)

#Remember Password
driver.find_element_by_id("RememberMe").click()

# Click Login
driver.find_element_by_xpath("//input[@value='Log in']").click()

#Click Logout
driver.find_element_by_xpath("//a[text()='Log out']").click()
