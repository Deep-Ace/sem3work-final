from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pythonBDD.Pages.HomePage import HomePage
from pythonBDD.Pages.LoginPage import LoginPage
from pythonBDD.Pages.LogoutPage import LogoutPage
from pythonBDD.Pages.RegisterPage import RegisterPage
from pythonBDD.Utilities.customlogger import LogGen
from pythonBDD.Utilities.readproperty import ReadConfig
import time

baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()

@given(u'Open the App')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("*****Driver Initialised*****")
    context.driver.get(baseURL)
    mylogger.info("*****Browser Launched*****")

@when(u'enter the login data')
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

@then(u'click signin')
def step_impl(context):
    loginpage.clickOnLogin()
    mylogger.info("*****Login Button Clicked*****")

@then(u'verify the lpage title')
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


@then(u'click the profile icon')
def step_impl(context):
    mylogger.info("*****Clicking Profile Icon*****")
    global logoutpage
    logoutpage = LogoutPage(context.driver)

    logoutpage.clickOnProfile()
    mylogger.info("*****Profile Button Clicked*****")


@then(u'click logout')
def step_impl(context):
    mylogger.info("*****Clicking Logout Button*****")
    time.sleep(3)
    logoutpage.clickOnLogout()
    mylogger.info("*****Logout Button Clicked*****")
    time.sleep(3)

@then(u'close the log app')
def step_impl(context):
    context.driver.close()
    mylogger.info("*****Browser Closed*****")