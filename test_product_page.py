import time
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    book_name = browser.find_element(By.TAG_NAME, 'h1').text
    book_price = browser.find_element(By.CSS_SELECTOR, 'h1 + p').text
    page.add_to_basket()
    WebDriverWait(browser, 5).until(EC.alert_is_present())
    page.solve_quiz_and_get_code()
    assert book_name == browser.find_element(By.CSS_SELECTOR, '#messages strong').text
    assert book_price == browser.find_element(By.CSS_SELECTOR, '#messages p strong').text
