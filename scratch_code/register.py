from _datetime import datetime
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I navigated to register page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    context.driver.implicitly_wait(2)
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.XPATH, "//li/ul//li/a[text()='Register']").click()

@when(u'I enter mandatory fields')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Amol")
    context.driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("Chopade")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    email_text = "amol"+timestamp+"@gmail.com"
    context.driver.find_element(By.XPATH,"//input[@name='email']").send_keys(email_text)
    context.driver.find_element(By.XPATH,"//input[@name='telephone']").send_keys("1234567890")
    context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("abc123")
    context.driver.find_element(By.XPATH,"//input[@name='confirm']").send_keys("abc123")
    context.driver.find_element(By.XPATH, "//input[@name='agree']").click()


@when(u'I click on Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@value='Continue']").click()


@then(u'Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH,"//div[@id='content']//following-sibling::h1").text.__eq__(expected_text)

@when(u'I enter all fields')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Amol")
    context.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Chopade")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    email_text = "amol" + timestamp + "@gmail.com"
    context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email_text)
    context.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("1234567890")
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("abc123")
    context.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("abc123")
    context.driver.find_element(By.XPATH, "//input[@name='agree']").click()


@when(u'I enter all details except email')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Amol")
    context.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Chopade")
    context.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("1234567890")
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("abc123")
    context.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("abc123")
    context.driver.find_element(By.XPATH, "//input[@name='agree']").click()


@then(u'Proper warning message about duplicate account should display')
def step_impl(context):
    warning_msg = "E-Mail Address does not appear to be valid!"
    assert context.driver.find_element(By.XPATH,"//div[@class='text-danger']").text.__contains__(warning_msg)


@when(u'I do not enter any details')
def step_impl(context):
    print(".....Not entering any details inside any field.......")


@then(u'Proper warning message for all mandatory fields should display')
def step_impl(context):
    warn_msg = "Warning: You must agree to the Privacy Policy!"
    assert context.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text.__contains__(warn_msg)
