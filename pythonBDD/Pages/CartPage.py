class CartPage:
    btn_addToCart_xpath = '//*[@id="featured"]/div[2]/div/div/form[1]/div/div[1]/div[2]/button'
    btn_cart_xpath = '//*[@id="navbarSupportedContent"]/ul/li[5]/a/i'
    btn_deleteItem_xpath = '//*[@id="myTable"]/tbody/tr/td[2]/a/i'

    def __init__(self, driver):
        self.driver = driver

    def clickOnAddToCart(self):
        self.driver.find_element_by_xpath(self.btn_addToCart_xpath).click()

    def clickOnCart(self):
        self.driver.find_element_by_xpath(self.btn_cart_xpath).click()

    def clickOnDeleteItem(self):
        self.driver.find_element_by_xpath(self.btn_deleteItem_xpath).click()
    #
    # def clickOnClick(self):
    #     self.driver.find_element_by_xpath('//*[@id="myTable"]/tbody/tr/td[2]/a').click()
