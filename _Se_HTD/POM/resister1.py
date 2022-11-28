from selenium import webdriver
import time
from Data_package import reading_object
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path)
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
driver.implicitly_wait(30)

login_objects = reading_object.read_locators()

class Resister:

    def __init__(self,driver):
        self.driver=driver

    def gender(self):
        driver.find_element_by_xpath("//label[@class='forcheckbox']/../..//input[@id='gender-male']").click()

    def first_name(self):
        driver.find_element_by_id("FirstName").send_keys("Rakesh")

    def last_name(self):
        driver.find_element_by_id("LastName").send_keys("Singh")

    def email(self):
        driver.find_element_by_id("Email").send_keys("rkscpr9934@gmail.com")

    def password(self):
        driver.find_element_by_xpath("//input[@id='Password']").send_keys("rakesh@123")

    def confirm_password(self):
        driver.find_element_by_xpath("//input[@id='ConfirmPassword']").send_keys("rakesh@123")

    def click_resister_button(self):
        driver.find_element_by_id("register-button").click()

    def click_login_button(self):
        driver.find_element_by_xpath("//a[text()='Log in']").click()


    def enter_username(self):
        self.driver.find_element_by_id(*login_objects["username"]).send_keys("admin")
    def enter_pwd(self):
        self.driver.find_element_by_name(*login_objects["pwd"]).send_keys("manager")
    def click_login(self):
        self.driver.find_element_by_xpath(*login_objects["//div[text()='Login ']"]).click()

lp=Resister()
lp.enter_username()
lp.enter_pwd()
lp.click_login()