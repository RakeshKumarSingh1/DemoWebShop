import time
import pytest
from selenium import webdriver
from Library.config import Config
from selenium.webdriver.firefox.options import Options


@pytest.fixture(params=["Chrome","Edge","Firefox",])
def init_driver(request):
    global driver
    browser=request.param

    if browser.lower() == "chrome":
        driver= webdriver.Chrome(executable_path=Config.Chrome_Driver_Path)

    elif request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_Driver_Path)

    elif request.param == "Firefox":

        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver = webdriver.Firefox(executable_path=Config.Firefox_Driver_Path, options=options)



    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    time.sleep(2)
    yield driver
    print(driver.title)
    driver.close()
