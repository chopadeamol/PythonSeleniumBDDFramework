from _datetime import datetime
from behave import *
from features.pages.LoginPage import LoginPage
from features.pages.RegisterPage import RegisterPage


@given(u'I navigated to register page')
def step_impl(context):
    context.driver.implicitly_wait(2)
    context.register_page = RegisterPage(context.driver)
    context.register_page.my_account()
    context.register_page.register_option()
    context.login_page = LoginPage(context.driver)

@when(u'I enter mandatory fields')
def step_impl(context):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    email_text = "amol" + timestamp + "@gmail.com"

    context.register_page.first_name("Amol")
    context.register_page.last_name("Chopade")
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(email_text)
    context.register_page.enter_telephone("1234567890")
    context.login_page.enter_password("abc123")
    context.register_page.confirm_password("abc123")
    context.register_page.terms_and_conditions()

@when(u'I click on Continue button')
def step_impl(context):
    context.register_page.continue_button()

@then(u'Account should get created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    assert context.register_page.account_created(expected_text)

@when(u'I enter all fields')
def step_impl(context):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    email_text = "amol" + timestamp + "@gmail.com"

    context.register_page.first_name("Amol")
    context.register_page.last_name("Chopade")
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email(email_text)
    context.register_page.enter_telephone("1234567890")
    context.login_page.enter_password("abc123")
    context.register_page.confirm_password("abc123")
    context.register_page.terms_and_conditions()

@when(u'I enter all details except email')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.register_page.first_name("Amol")
    context.register_page.last_name("Chopade")
    context.register_page.enter_telephone("1234567890")
    context.login_page.enter_password("abc123")
    context.register_page.confirm_password("abc123")
    context.register_page.terms_and_conditions()

@then(u'Proper warning message about duplicate account should display')
def step_impl(context):
    warning_msg = "E-Mail Address does not appear to be valid!"
    assert context.register_page.warning_message(warning_msg)

@when(u'I do not enter any details')
def step_impl(context):
    print(".....Not entering any details inside any field.......")

@then(u'Proper warning message for all mandatory fields should display')
def step_impl(context):
    warn_msg = "Warning: You must agree to the Privacy Policy!"
    assert context.register_page.warning_msg_mandatory_fields(warn_msg)