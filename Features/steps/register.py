from behave import *
from selenium import webdriver
import time


@given(u'launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe')
    time.sleep(2)
    context.driver.maximize_window()


@given(u'open Demo Web Shop')
def step_impl(context):
    context.driver.get("https://demowebshop.tricentis.com/")


@then(u'Click on Register Button')
def step_impl(context):
    context.driver.find_element("xpath", '//a[text()="Register"]').click()


@then(u'Select radio button for gender')
def step_impl(context):
    context.driver.find_element("xpath", '//input[@id="gender-male"]').click()
    time.sleep(2)


@then(u'enter your first name')
def step_impl(context):
    context.driver.find_element("id", "FirstName").send_keys("Rakesh")
    time.sleep(2)


@then(u'enter your last name')
def step_impl(context):
    context.driver.find_element("id", "LastName").send_keys("Singh")
    time.sleep(2)


@then(u'enter you valid email id')
def step_impl(context):
    context.driver.find_element("id", "Email").send_keys("rkscpr9934@gmail.com")
    time.sleep(2)


@then(u'enter password')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@id='Password']").send_keys("rakesh@123")
    time.sleep(2)


@then(u'Enter confirm password')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@id='ConfirmPassword']").send_keys("rakesh@123")
    time.sleep(2)


@then(u'click the Register Button')
def step_impl(context):
    context.driver.find_element("id", "register-button").click()
    time.sleep(2)


@then(u'Click on Login Button')
def step_impl(context):
    context.driver.find_element("xpath", "//a[text()='Log in']").click()
    time.sleep(2)


@then(u'Enter Valid email id')
def step_impl(context):
    context.driver.find_element("id", "Email").send_keys("rkscpr9934@gmail.com")
    time.sleep(2)


@then(u'Enter Valid Password')
def step_impl(context):
    context.driver.find_element("id", "Password").send_keys("rakesh@123")
    time.sleep(2)


@then(u'Select check box for remeber me')
def step_impl(context):
    context.driver.find_element("id", "RememberMe").click()
    time.sleep(2)


@then(u'Click on Forgot Password')
def step_impl(context):
    context.driver.find_element("xpath", "//a[text()='Forgot password?']").click()
    time.sleep(2)
    context.driver.back()


@then(u'Click the Login Button')
def step_impl(context):
    context.driver.find_element("xpath","//input[@value='Log in']").click()
    time.sleep(2)


@then(u'Click on Logout Button')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@value='Log in']").click()
    context.driver.close()

