from behave import *
from selenium import webdriver
@given('launch Chrome Browser')
def launch_browser(context):
    context.driver =webdriver.Chrome(executable_path="C:\\Users\\PC\\Desktop\\chromedriver.exe")

@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
    assert status is True

@then('close browser')
def closeBrowser(context):
    context.driver.close()

