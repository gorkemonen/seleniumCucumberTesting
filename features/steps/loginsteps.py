from behave import *
from selenium import webdriver

@given('I launch Chrome Browser')
def step_impl(context):
    context.driver =webdriver.Chrome(executable_path="C:\\Users\\PC\\Desktop\\chromedriver.exe")


@when('I open orange hrm homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)



@when('Click on login button')
def step_impl(context):
    context.driver.find_element_by_id("btnLogin").click()



@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text=context.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/h1").text
    except :
        context.driver.close()
        assert False,"Test failed"
    if text =="Dashboard":
       context.driver.close()
       assert True,"Test Passed"
