import time
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page()
        LoginPage(browser).should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser)
    page.open()
    page.go_to_basket()
    assert BasketPage.basket_is_empty(browser)
    assert browser.find_element(*BasketPageLocators.EMPTY_BASKET_PARAGRAPH)
