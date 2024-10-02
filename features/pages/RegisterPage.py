from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    my_account_xpath="//span[text()='My Account']"
    register_option_xpath="//li/ul//li/a[text()='Register']"
    first_name_xpath = "//input[@name='firstname']"
    last_name_xpath = "//input[@name='lastname']"
    confirm_pass_xpath = "//input[@name='confirm']"
    telephone_xpath = "//input[@name='telephone']"
    terms_conditions_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"
    account_created_xpath = "//div[@id='content']//following-sibling::h1"
    warning_msg_xpath = "//div[@class='text-danger']"
    warning_msg_mandatory_fields_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_xpath).click()

    def register_option(self):
        self.driver.find_element(By.XPATH, self.register_option_xpath).click()

    def first_name(self,name):
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(name)

    def last_name(self,surname):
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(surname)

    def confirm_password(self, confirm_pass):
        self.driver.find_element(By.XPATH, self.confirm_pass_xpath).send_keys(confirm_pass)

    def enter_telephone(self,telephone):
        self.driver.find_element(By.XPATH, self.telephone_xpath).send_keys(telephone)

    def terms_and_conditions(self):
        self.driver.find_element(By.XPATH, self.terms_conditions_xpath).click()

    def continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def account_created(self, expected_msg):
        return self.driver.find_element(By.XPATH, self.account_created_xpath).text.__contains__(expected_msg)

    def warning_message(self,warning_msg):
        return self.driver.find_element(By.XPATH, self.warning_msg_xpath).text.__contains__(warning_msg)

    def warning_msg_mandatory_fields(self, warn_msg):
        return self.driver.find_element(By.XPATH, self.warning_msg_mandatory_fields_xpath).text.__contains__(warn_msg)