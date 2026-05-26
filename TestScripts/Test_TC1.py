from POM.loginpage import LoginPage
import pytest

@pytest.mark.order(2)
def test_Test_TC1(setup):
    driver = setup
    login =  LoginPage(driver)
    login.email_text_field("sujal@gmail.com")
    login.password_text_field("Sujal@123")
    login.login_btn()
