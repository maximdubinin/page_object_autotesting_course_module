import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('offer_number', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_product_to_basket()
    product_page.should_be_added_to_basket_with_product_name()
    product_page.should_be_added_to_basket_with_product_price()
