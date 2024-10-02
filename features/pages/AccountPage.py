from selenium.webdriver.common.by import By

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    edit_account_info_xpath = "//a[text()='Edit your account information']"

    def verify_edit_account_info(self, expected_msg):
        return self.driver.find_element(By.XPATH, self.edit_account_info_xpath).text.__contains__(expected_msg)