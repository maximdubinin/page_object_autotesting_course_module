from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty, but should be"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is empty, but should not be"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK), \
            "Continue shopping link is not present, but should be"

    def should_not_be_empty_basket_text(self):
        assert self.is_not_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK), \
            "Continue shopping link is present, but should not be"
