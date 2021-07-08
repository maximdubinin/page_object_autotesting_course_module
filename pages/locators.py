from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_URL_IDENTIFIER = "accounts/login/"


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADDED_TO_BASKET_PRODUCT_NAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    ADDED_TO_BASKET_PRODUCT_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p/strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
