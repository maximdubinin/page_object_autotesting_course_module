from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "2login_form")
    REGISTER_FORM = (By.ID, "2register_form")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/accounts/login/a"
