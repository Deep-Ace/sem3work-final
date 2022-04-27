class LogoutPage:
    btn_profile_xpath = '//*[@id="navbarDropdown"]/i'
    btn_logout_xpath = '//*[@id="navbarSupportedContent"]/ul/li[6]/ul/a[3]'

    def __init__(self, driver):
        self.driver = driver

    def clickOnProfile(self):
        self.driver.find_element_by_xpath(self.btn_profile_xpath).click()

    def clickOnLogout(self):
        self.driver.find_element_by_xpath(self.btn_logout_xpath).click()









