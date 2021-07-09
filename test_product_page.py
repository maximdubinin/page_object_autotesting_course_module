import pytest
import time
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        login_page = LoginPage(browser, login_page_link)
        login_page.open()
        login_page.register_new_user(email, "GPZyLfZVbD7L-3h*QhRN")

    def test_user_cant_see_success_message(self, browser):
        page = MainPage(browser, product_page_link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = MainPage(browser, product_page_link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_product_to_basket()
        product_page.should_be_added_to_basket_with_product_name()
        product_page.should_be_added_to_basket_with_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, product_page_link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, product_page_link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('offer_number', [0,
                                          1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9
                                          ])
def test_guest_can_add_product_to_basket(browser, offer_number):
    promo_link = product_page_link + f"/?promo=offer{offer_number}"
    page = MainPage(browser, promo_link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_product_to_basket()
    product_page.should_be_added_to_basket_with_product_name()
    product_page.should_be_added_to_basket_with_product_price()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = MainPage(browser, product_page_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, product_page_link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_product_to_basket()
    product_page.should_be_disappeared()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = MainPage(browser, product_page_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_text()
