from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def messages_should_be_after_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MASSAGES), "No messages are appeared"

    def correct_product_should_be_added_to_basket(self):
        correct_product_name = self.browser.find_element(*ProductPageLocators.CORRECT_PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert correct_product_name == added_product_name, "incorrect product name added to basket"

    def correct_product_prise_should_be_added_to_basket(self):
        correct_product_price = self.browser.find_element(*ProductPageLocators.CORRECT_PRODUCT_PRICE).text
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        assert correct_product_price == added_product_price, "incorrect product price added to basket"
