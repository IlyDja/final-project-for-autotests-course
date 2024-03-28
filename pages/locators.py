from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BUSKET_LINK = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_PARAGRAPH = (By.XPATH, '//*[@id="content_inner"]/p')
    BASKET_IS_EMPTY_STATUS = ("tag name", 'h2')
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
