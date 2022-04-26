from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pythonBDD.Pages.HomePage import HomePage
from pythonBDD.Pages.LoginPage import LoginPage
from pythonBDD.Utilities.customlogger import LogGen
from pythonBDD.Utilities.readproperty import ReadConfig
import time

baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()


@given(u'Launch the App')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("*****Driver Initialised*****")
    context.driver.get(baseURL)
    mylogger.info("*****Browser Launched*****")


@when(u'enter the login credentials')
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



@then(u'click login')
def step_impl(context):
    loginpage.clickOnLogin()
    mylogger.info("*****Login Button Clicked*****")



@then(u'close the App')
def step_impl(context):
    context.driver.close()
    mylogger.info("*****Browser Closed*****")