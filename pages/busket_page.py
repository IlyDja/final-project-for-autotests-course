from .locators import BusketPageLocators
from .base_page import BasePage


class BusketPage(BasePage):
    def busket_is_empty(self):
        try:
            self.browser.find_element(*BusketPageLocators.BUSKET_IS_EMPTY_STATUS)
            return False
        except:
            return True
