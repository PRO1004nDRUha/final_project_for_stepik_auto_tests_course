from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "element present, when shouldn't"

    def should_be_written_that_empty(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.INSCRIPTION_BASKET_EMPTY).text,\
            "Basket is not empty"
