class Registration:

    def __init__(self, driver):
        self.driver = driver

    def registration_link(self):
        self.driver.find_element('xpath', "//a[text()='Register']").click()

    def gender_radio(self):
        return self.driver.find_element('id', 'gender-male')

    def firstname_text_field(self, firstname):
        self.driver.find_element('id', "FirstName").send_keys(firstname)

    def lastname_text_field(self, lastname):
        self.driver.find_element('id', "LastName").send_keys(lastname)

    def email_text_field(self, email):
        self.driver.find_element('id', "Email").send_keys(email)

    def password_text_field(self, password):
        self.driver.find_element('id', "Password").send_keys(password)

    def confirm_password_text_field(self, confirm_password):
        self.driver.find_element('id', "ConfirmPassword").send_keys(confirm_password)

    def registration_btn(self):
        self.driver.find_element('id', "register-button").click()
