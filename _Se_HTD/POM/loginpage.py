from selenium import webdriver
import time
from
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path)
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
driver.implicitly_wait(30)

login_objects = reading_object.read_locators()

class Loginpage:

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self):
        self.driver.find_element_by_id(*login_objects["username"]).send_keys("admin")
    def enter_pwd(self):
        self.driver.find_element_by_name(*login_objects["pwd"]).send_keys("manager")
    def click_login(self):
        self.driver.find_element_by_xpath(*login_objects["//div[text()='Login ']"]).click()

# lp=Loginpage()
# lp.enter_username()
# lp.enter_pwd()
# lp.click_login()