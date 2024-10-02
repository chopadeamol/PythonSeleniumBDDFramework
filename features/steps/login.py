from datetime import datetime
from behave import *
from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I navigated to login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.click_on_login_option()


@when(u'I entered valid email and password')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email("amol@gmail.com")
    context.login_page.enter_password("abc123")


@when(u'I click on login button')
def step_impl(context):
    context.login_page.click_on_login_button()


@then(u'I should get login')
def step_impl(context):
    expected_msg = "Edit your account information"
    context.acc_page = AccountPage(context.driver)
    assert context.acc_page.verify_edit_account_info(expected_msg)


@when(u'I entered invalid email and valid password')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    email_text = "amol" + timestamp + "@gmail.com"
    context.login_page.enter_email(email_text)
    context.login_page.enter_password("abc123")


@then(u'I should get proper warning message')
def step_impl(context):
    warn_msg = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.display_warning_msg(warn_msg)


@when(u'I entered valid email and invalid password')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    context.login_page.enter_email("amol@gmail.com")
    context.login_page.enter_password(timestamp)


@when(u'I entered invalid email and invalid password')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    email_text = "amol" + timestamp + "@gmail.com"
    context.login_page.enter_email(email_text)
    context.login_page.enter_password(timestamp)


@when(u'I do not enter anything in the email and password fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email("")
    context.login_page.enter_password("")