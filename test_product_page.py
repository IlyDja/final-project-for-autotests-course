from pages.product_page import ProductPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from pages.locators import ProductPageLocators


# links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"]

# [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}" for n in range(0, 10)]
# @pytest.mark.parametrize('link_', links)
@pytest.mark.parametrize('link_', links)
def test_guest_can_add_product_to_basket(browser, link_):
    link = link_
    page = ProductPage(browser, link)
    page.open()
    book_name = browser.find_element(By.TAG_NAME, 'h1').text
    book_price = browser.find_element(By.CSS_SELECTOR, 'h1 + p').text
    page.add_to_basket()
    WebDriverWait(browser, 9).until(EC.alert_is_present())
    page.solve_quiz_and_get_code()
    assert book_name == browser.find_element(By.CSS_SELECTOR, '#messages strong').text
    assert book_price == browser.find_element(By.CSS_SELECTOR, '#messages p strong').text


@pytest.mark.xfail
@pytest.mark.parametrize('link_', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link_):
    link = link_
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    WebDriverWait(browser, 9).until(EC.alert_is_present())
    page.solve_quiz_and_get_code()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"


@pytest.mark.parametrize('link_', links)
def test_guest_cant_see_success_message(browser, link_):
    link = link_
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link_', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link_):
    link = link_
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    WebDriverWait(browser, 9).until(EC.alert_is_present())
    page.solve_quiz_and_get_code()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'message not disappeared after adding product to basket'


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
