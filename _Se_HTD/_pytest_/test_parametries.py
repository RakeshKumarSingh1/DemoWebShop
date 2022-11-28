from selenium import webdriver
import pytest
import time
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
driver=webdriver.Chrome(executable_path=path)
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
driver.implicitly_wait(30)


@pytest.mark.parametrize("l",[("admin","manager"), ("trainee", "trainee")])
def test_login(l):
    driver.find_element_by_id("username").send_keys(l[0])
    time.sleep(2)
    driver.find_element_by_xpath("//input[@class='textField pwdfield']").send_keys(l[1])
    time.sleep(2)
    driver.find_element_by_xpath("//div[text()='Login ']").click()
    print(driver.title)
    time.sleep(2)
    driver.find_element_by_xpath("//a[text()='Logout']").click()



@pytest.mark.parametrize("a,b",[(2,3),(4,5),(6,7)])
def test_add(a,b):
    print(a+b)

# test_add(2,3)
# test_add(4,5)
# test_add(6,7)


