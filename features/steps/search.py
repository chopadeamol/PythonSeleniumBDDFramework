from behave import *
from selenium.webdriver.common.by import By

@given('I am navigated to home page')
def open_browser(context):
    expected_title = "Your Store"
    assert context.driver.title.__eq__(expected_title)

@when('I entered valid product say "HP" into the search box field')
def enter_product(context):
    context.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("HP")

@when('I click on search button')
def click_button(context):
    context.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()

@then('Valid product should get displayed in search result')
def display_product(context):
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

@when('I entered Invalid product say "Hero" into the search field')
def enter_invalid_product(context):
    context.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("Hero")

@then('Proper message should displayed in search results')
def proper_message(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    context.driver.quit()

@when('I did not enter anything in text box')
def enter_nothing(context):
    context.driver.find_element(By.XPATH,"//input[@name='search']").send_keys("")

@then('Proper message should displayed in search result')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(
        expected_text)
    context.driver.quit()