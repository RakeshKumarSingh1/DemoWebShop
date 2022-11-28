from selenium import webdriver
import pytest
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path)
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
driver.implicitly_wait(30)


@pytest.mark.parametrize("user_,pwd_",[("admin","manager"), ("trainee", "trainee")])
def test_login(user_,pwd_):
    driver.find_element_by_id("username").send_keys(user_)
    time.sleep(2)
    driver.find_element_by_xpath("//input[@class='textField pwdfield']").send_keys(pwd_)
    time.sleep(2)
    driver.find_element_by_xpath("//div[text()='Login ']").click()
    print(driver.title)
    time.sleep(2)
    driver.find_element_by_xpath("//a[text()='Logout']").click()
