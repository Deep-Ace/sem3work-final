class RegisterPage:
    txt_username_id = "username"
    txt_firstname_id = "name"
    txt_lastname_id = "lastname"
    txt_email_id = "email"
    txt_password_id = "password"
    txt_conpassword_id = "cpassword"
    txt_terms_id = "agree"
    txt_terms_xpath = '//*[@id="agree"]'

    # btn_register_id = "registerButton"
    btn_register_xpath = "/html/body/section/div/div/div/div[1]/div/form/div[8]/button"



    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)

    def setfirstname(self, name):
        self.driver.find_element_by_id(self.txt_firstname_id).send_keys(name)

    def setlastname(self, lastname):
        self.driver.find_element_by_id(self.txt_lastname_id).send_keys(lastname)

    def setemail(self, email):
        self.driver.find_element_by_id(self.txt_email_id).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)

    def setconpassword(self, cpassword):
        self.driver.find_element_by_id(self.txt_conpassword_id).send_keys(cpassword)

    # def setagree(self):
    #     self.driver.find_element_by_xpath(self.txt_terms_xpath).click()

    def setagree(self):
        self.driver.find_element_by_id(self.txt_terms_id).click()

    # def clickOnRegister(self):
    #     self.driver.find_element_by_id(self.btn_register_id).click()

    def clickOnRegister(self):
        self.driver.find_element_by_xpath(self.btn_register_xpath).click()