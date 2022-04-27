from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pythonBDD.Pages.CartPage import CartPage
from pythonBDD.Pages.HomePage import HomePage
from pythonBDD.Pages.LoginPage import LoginPage
from pythonBDD.Pages.LogoutPage import LogoutPage
from pythonBDD.Pages.RegisterPage import RegisterPage
from pythonBDD.Utilities.customlogger import LogGen
from pythonBDD.Utilities.readproperty import ReadConfig
import time

baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()

@given(u'Open the app for cart')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("*****Driver Initialised*****")
    context.driver.get(baseURL)
    mylogger.info("*****Browser Launched*****")

@when(u'enter the login data for cart')
def step_impl(context):
    mylogger.info("*****Passing Credentials*****")
    global homepage
    global loginpage

    homepage = HomePage(context.driver)
    homepage.clickOnLogin()
    loginpage = LoginPage(context.driver)
    user = ReadConfig.getUserName()
    pwd = ReadConfig.getPassword()
    time.sleep(3)
    loginpage.setusername(user)
    loginpage.setpassword(pwd)
    mylogger.info("*****Credentials Entered Successfully*****")

@then(u'click signin for cart')
def step_impl(context):
    loginpage.clickOnLogin()
    mylogger.info("*****Login Button Clicked*****")

@then(u'verify the hpage title')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "BookMart | Home"
    if actual_title == expected_title:
        assert True
        mylogger.info("*****Title Matched*****")
    else:
        mylogger.info("*****Title Not Matched*****")
        assert False
    time.sleep(3)

@then(u'click the addtocart button')
def step_impl(context):
    mylogger.info("*****Clicking Add To Cart Button*****")
    global cartpage
    cartpage = CartPage(context.driver)
    cartpage.clickOnAddToCart()
    time.sleep(4)
    mylogger.info("*****Add To Cart Button Clicked*****")

@then(u'click cart buton')
def step_impl(context):
    mylogger.info("*****Clicking Cart Button*****")
    cartpage.clickOnCart()
    time.sleep(4)
    mylogger.info("*****Cart Button Clicked*****")

@then(u'verify the cpage title')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "BookMart | Cart"
    if actual_title == expected_title:
        assert True
        mylogger.info("*****Title Matched*****")
    else:
        mylogger.info("*****Title Not Matched*****")
        assert False

@then(u'delete the item from cart')
def step_impl(context):
    mylogger.info("*****Click the Delete Button*****")
    cartpage.clickOnDeleteItem()
    time.sleep(3)
    mylogger.info("*****Delete Button Clicked*****")

# @then(u'click on onclick')
# def step_impl(context):
#     mylogger.info("*****Clicking OnClick OK Button*****")
#     cartpage.clickOnClick()
#     mylogger.info("*****OnClick OK Button Clicked*****")

@then(u'close the cart app')
def step_impl(context):
    context.driver.close()
    mylogger.info("*****Browser Closed*****")