from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email_xpath = "//input[@name='email']"
    password_xpath = "//input[@name='password']"
    login_button_xpath = "//input[@value='Login']"
    warning_msg_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email(self,email_text):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email_text)

    def enter_password(self,pass_email):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(pass_email)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def display_warning_msg(self,warn_msg):
        return self.driver.find_element(By.XPATH,self.warning_msg_xpath).text.__contains__(warn_msg)