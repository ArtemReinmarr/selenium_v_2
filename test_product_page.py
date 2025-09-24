import pytest
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage

link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.the_same_names_of_product()
    page.the_same_prices_of_product()