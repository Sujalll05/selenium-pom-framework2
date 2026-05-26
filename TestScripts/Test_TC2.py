from POM.registration import Registration
import pytest


@pytest.mark.order(1)
def test_registration(setup):

    driver = setup

    registration = Registration(driver)

    registration.registration_link()
    registration.gender_radio().click()
    registration.firstname_text_field("Sujal")
    registration.lastname_text_field("Virdande")
    registration.email_text_field("sujal@gmail.com")
    registration.password_text_field("Sujal@123")
    registration.registration_btn()


