import time
import re
from Library.config import Config
from Library.reading_object import ReadExcel

class Register:

    r_Excel = ReadExcel()
    demo_loc = r_Excel.read_locators(Config.Locator_Sheet)


    def __init__(self,driver):
        self.driver = driver


    def register(self):
        locators = self.demo_loc["reg_button"]
        self.driver.find_element(*locators).click()
        # self.driver.find_element("xpath",'//a[text()="Register"]').click()
        time.sleep(2)

    def gender(self):
        locators = self.demo_loc["gender_radio"]
        self.driver.find_element(*locators).click()
        # self.driver.find_element("xpath",'//input[@id="gender-male"]').click()
        time.sleep(2)

    def first_name(self,FirstName):
        locator = self.demo_loc["enter_FN"]
        self.driver.find_element(*locator).send_keys(FirstName)
        #self.driver.find_element_by_id("FirstName").send_keys("Rakesh")
        time.sleep(2)


    def last_name(self,LastName):
        locator = self.demo_loc["enter_LN"]
        self.driver.find_element(*locator).send_keys(LastName)
        #self.driver.find_element_by_id("LastName").send_keys("Singh")
        time.sleep(2)

    def email(self,R_Email):
        locator = self.demo_loc["enter_email"]
        self.driver.find_element(*locator).send_keys(R_Email)
        #self.driver.find_element_by_id("Email").send_keys("rkscpr9934@gmail.com")
        time.sleep(2)

    def password(self,Password):
        locator = self.demo_loc["enter_pwd"]
        self.driver.find_element(*locator).send_keys(Password)
        #self.driver.find_element_by_xpath("//input[@id='Password']").send_keys("rakesh@123")
        time.sleep(2)

    def confirm_password(self,confirm_pwd):
        loator = self.demo_loc["enter-con_pwd"]
        self.driver.find_element(*loator).send_keys(confirm_pwd)
        #self.driver.find_element_by_xpath("//input[@id='ConfirmPassword']").send_keys("rakesh@123")
        time.sleep(2)

    def click_resister_button(self):
        locator = self.demo_loc["click_reg"]
        self.driver.find_element(*locator).click()
        #self.driver.find_element_by_id("register-button").click()
        time.sleep(2)

    def click_login_button(self):
        locator = self.demo_loc["click_login"]
        self.driver.find_element(*locator).click()
        #self.driver.find_element_by_xpath("//a[text()='Log in']").click()
        time.sleep(2)


    def enter_username(self,L_Email):
        locator = self.demo_loc["enter_L_email"]
        self.driver.find_element(*locator).send_keys(L_Email)
        #self.driver.find_element_by_id("Email").send_keys("rkscpr9934@gmail.com")
        time.sleep(2)

    def enter_pwd(self,L_pwd):
        locator = self.demo_loc["enter_L_pwd"]
        self.driver.find_element(*locator).send_keys(L_pwd)
        #self.driver.find_element_by_name("Password").send_keys("rakesh@123")
        time.sleep(2)

    def remember_pwd(self):
        locator = self.demo_loc["click_on_rem"]
        self.driver.find_element(*locator).click()
        #self.driver.find_element_by_id("RememberMe").click()
        time.sleep(2)

    def forgot_pwd(self):
        locator = self.demo_loc["forgot_pwd_btn"]
        self.driver.find_element(*locator).click()
        #self.driver.find_element_by_xpath("//a[text()='Forgot password?']").click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    def click_login(self):
        locator = self.demo_loc["click_on_login"]
        self.driver.find_element(*locator).click()
        #self.driver.find_element_by_xpath("//input[@class='button-1 login-button']").click()
        time.sleep(2)

    def click_logout(self):
        locator = self.demo_loc["click_on_logout"]
        self.driver.find_element(*locator).click()
        #self.driver.find_element_by_xpath("//a[text()='Log out']").click()




