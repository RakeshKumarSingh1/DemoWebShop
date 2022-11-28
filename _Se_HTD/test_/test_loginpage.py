from POM.loginpage import Loginpage

class TestLoginpage:
    def test_login(self,_driver):
        lp=lp=Loginpage()
        lp.enter_username()
        lp.enter_pwd()
        lp.click_login()