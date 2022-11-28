# import pytest
#
#
# @pytest.fixture(autouse="True")
# def greet():
#     print("****hi****") #set up module
#     yield
#     print("***Bye***")
#
# def test_spam(greet):
#     print("in test spam")
#
# def test_display(greet):
#     print("in display")


import pytest
from selenium import webdriver
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
@pytest.fixture()
def _driver():
     driver=webdriver.Chrome(path)
     driver.get('https://demowebshop.tricentis.com/')
     driver.maximize_window()
     yield driver
     print(driver.title)
     driver.close()


def test_register(_driver):
    _driver.find_element_by_partial_link_text("Register").click()

def test_login(_driver):
    _driver.find_element_by_partial_link_text("Log in").click()
