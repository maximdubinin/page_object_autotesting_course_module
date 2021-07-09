from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_URL_IDENTIFIER = "accounts/login/"
    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASSWORD_INPUT = (By.ID, "id_registration-password1")
    PASSWORD_CONFIRMATION_INPUT = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADDED_TO_BASKET_PRODUCT_NAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    ADDED_TO_BASKET_PRODUCT_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p/strong")


class BasePageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini span > a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "#content_inner > p > a")
