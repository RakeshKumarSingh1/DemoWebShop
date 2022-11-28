from Library.config import Config
import pytest
from Library.reading_object import ReadExcel
from POM.main_demowebshop import Register


class TestRegister:
    read_xl= ReadExcel()
    data = read_xl.read_test_data()

    @pytest.mark.parametrize("FirstName,LastName,R_Email,Password,confirm_pwd,L_Email,L_pwd",data)
    def test_register(self,init_driver,FirstName,LastName,R_Email,Password,confirm_pwd,L_Email,L_pwd):

        driver = init_driver

        lp = Register(driver)
        lp.register()
        lp.gender()
        lp.first_name(FirstName)
        lp.last_name(LastName)
        lp.email(R_Email)
        lp.password(Password)
        lp.confirm_password(confirm_pwd)
        lp.click_resister_button()
        lp.click_login_button()
        lp.enter_username(L_Email)
        lp.enter_pwd(L_pwd)
        lp.remember_pwd()
        lp.forgot_pwd()
        lp.click_login()
        lp.click_logout()
