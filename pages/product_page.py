from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        current_url = self.url
        if "?promo=" in current_url:
            self.solve_quiz_and_get_code()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasePageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*BasePageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def should_be_added_to_basket_with_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_PRODUCT_NAME)
        assert product_name.text == added_product_name.text, \
            f"Added to basket product name is incorrect. Expected: '{product_name.text}'. " \
            f"Current: '{added_product_name.text}'"

    def should_be_added_to_basket_with_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_PRODUCT_PRICE)
        assert product_price.text == added_product_price.text, \
            f"Added to basket product price is incorrect. Expected: '{product_price.text}'. " \
            f"Current: '{added_product_price.text}'"
