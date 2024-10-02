from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    my_account_xpath = "//span[text()='My Account']"
    login_xpath = "//a[text()='Login']"

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH,self.my_account_xpath).click()

    def click_on_login_option(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()
