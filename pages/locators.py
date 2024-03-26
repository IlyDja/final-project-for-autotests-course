from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators:
    ADD_TO_BUSKET_LINK = (By.CLASS_NAME, 'btn-add-to-basket')
    #SUCCESSFULL_ADDED_MESSAGE = (By.)
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
