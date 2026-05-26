


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def email_text_field(self, email):
        self.driver.find_element('id', 'Email').send_keys(email)

    def password_text_field(self, password):
        self.driver.find_element('id', 'Password').send_keys(password)

    def login_btn(self):
        self.driver.find_element('xpath', '//input[@type="submit"]').click()
