from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)
        self.url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_LINK).click()
