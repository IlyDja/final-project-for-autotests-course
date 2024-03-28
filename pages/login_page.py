from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'URL is not correct'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'login form is not present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'register form is not present'

    def register_new_user(self, email, password):
        self.browser.find_element(By.ID, 'id_registration-email').send_keys(email)
        self.browser.find_element(By.ID, 'id_registration-password1').send_keys(password)
        self.browser.find_element(By.ID, 'id_registration-password2').send_keys(password)
        self.browser.find_element(By.XPATH, '//*[@id="register_form"]/button').click()
