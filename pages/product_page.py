from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import pytest

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), f"No Add to basket button"
    
    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def the_same_names_of_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        assert product_name == basket_product_name, f"Product {product_name} is different from basket product {basket_product_name}"

    def the_same_prices_of_product(self):    
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text
        assert product_price == basket_product_price, f"Product price {product_price} is different from basket product price {basket_product_price}"


    


