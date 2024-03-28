from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def basket_is_empty(self):
        try:
            self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_STATUS)
            return False
        except:
            return True
