import pytest
from selenium import webdriver
path=r'C:\Users\admin\Downloads\chromedriver_win32 (1)\chromedriver.exe'
from Library.config import Config


@pytest.fixture
def _driver():
    driver= webdriver.Chrome(executable_path=Config.Chrome_Driver_Path)
    #driver.get("https://demo.actitime.com/login.do")
    driver.maximize_window()
    yield driver
    print(driver.title)
    driver.close()
