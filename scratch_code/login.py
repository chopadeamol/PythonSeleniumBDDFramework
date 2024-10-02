from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigated to login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    context.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    context.driver.find_element(By.XPATH,"//a[text()='Login']").click()


@when(u'I entered valid email and password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("amol@gmail.com")
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("abc123")


@when(u'I click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@value='Login']").click()


@then(u'I should get login')
def step_impl(context):
    expected_text = "Edit your account information"
    assert context.driver.find_element(By.XPATH,"//a[text()='Edit your account information']").text.__contains__(expected_text)


@when(u'I entered invalid email and valid password')
def step_impl(context):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    email_text = "amol" + timestamp + "@gmail.com"
    context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email_text)
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("abc123")


@then(u'I should get proper warning message')
def step_impl(context):
    warn_msg = "Warning: No match for E-Mail Address and/or Password."
    assert context.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text.__contains__(warn_msg)


@when(u'I entered valid email and invalid password')
def step_impl(context):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    email_text = "amol@gmail.com"
    context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email_text)
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(timestamp)


@when(u'I entered invalid email and invalid password')
def step_impl(context):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    email_text = "amol" + timestamp + "@gmail.com"
    context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email_text)
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(timestamp)


@when(u'I do not enter anything in the email and password fields')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("")
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")

