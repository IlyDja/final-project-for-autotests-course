from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from pages.locators import ProductPageLocators, BasketPageLocators
from selenium import webdriver
import time


@pytest.mark.basket_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.browser = browser
        page = LoginPage(browser)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = 'lkjjjjjjj'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser)
        page.open()
        book_name = self.browser.find_element(By.TAG_NAME, 'h1').text
        book_price = self.browser.find_element(By.CSS_SELECTOR, 'h1 + p').text
        page.add_to_basket()
        assert book_name == self.browser.find_element(By.CSS_SELECTOR, '#messages strong').text
        assert book_price == self.browser.find_element(By.CSS_SELECTOR, '#messages p strong').text


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    book_name = browser.find_element(By.TAG_NAME, 'h1').text
    book_price = browser.find_element(By.CSS_SELECTOR, 'h1 + p').text
    page.add_to_basket()
    assert book_name == browser.find_element(By.CSS_SELECTOR, '#messages strong').text
    assert book_price == browser.find_element(By.CSS_SELECTOR, '#messages p strong').text


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_to_basket()
    WebDriverWait(browser, 9).until(EC.alert_is_present())
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_to_basket()
    WebDriverWait(browser, 9).until(EC.alert_is_present())
    page.solve_quiz_and_get_code()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'message not disappeared after adding product to basket'


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_basket()
    assert BasketPage.basket_is_empty(browser)
    assert browser.find_element(*BasketPageLocators.EMPTY_BASKET_PARAGRAPH)
