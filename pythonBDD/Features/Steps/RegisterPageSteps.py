from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pythonBDD.Pages.HomePage import HomePage
from pythonBDD.Pages.LoginPage import LoginPage
from pythonBDD.Pages.RegisterPage import RegisterPage
from pythonBDD.Utilities.customlogger import LogGen
from pythonBDD.Utilities.readproperty import ReadConfig
import time

baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()

@given(u'Launch the Register App')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("*****Driver Initialised*****")
    context.driver.get(baseURL)
    mylogger.info("*****Browser Launched*****")

@when(u'enter the register credentials')
def step_impl(context):
    mylogger.info("*****Passing Credentials*****")
    global homepage
    global loginpage
    global registerpage

    homepage = HomePage(context.driver)
    homepage.clickOnLogin()
    loginpage = LoginPage(context.driver)
    loginpage.clickOnCreate()
    registerpage = RegisterPage(context.driver)
    user = ReadConfig.getUserName()
    first = ReadConfig.getFirstName()
    last = ReadConfig.getLastName()
    emai = ReadConfig.getEmail()
    pwd = ReadConfig.getPassword()
    conpwd = ReadConfig.getConPassword()
    time.sleep(3)
    registerpage.setusername(user)
    registerpage.setfirstname(first)
    registerpage.setlastname(last)
    registerpage.setemail(emai)
    registerpage.setpassword(pwd)
    registerpage.setconpassword(conpwd)
    mylogger.info("*****Credentials Entered Successfully*****")

@then(u'click terms')
def step_impl(context):
    registerpage.setagree()
    # time.sleep(5)
    mylogger.info("*****Terms Accepted*****")


@then(u'click register')
def step_impl(context):
    registerpage.clickOnRegister()
    mylogger.info("*****Register Button Clicked*****")

@then(u'verify the rpage title')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = "BookMart | User Register"
    if actual_title == expected_title:
        assert True
        mylogger.info("*****Title Matched*****")
    else:
        mylogger.info("*****Title Not Matched*****")
        assert False

@then(u'close the Register App')
def step_impl(context):
    context.driver.close()
    mylogger.info("*****Browser Closed*****")
