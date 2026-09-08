import time

import pytest

from src.pages.check_out_page import CheckOutPage
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage
from src.pages.shopping_cart_page import ShoppingCartPage


@pytest.fixture()
def add_unitree_g1_robot_to_cart(chrome_browser_fixture):
    login_page = LoginPage(chrome_browser_fixture)
    login_page.log_in_user()
    home_page = HomePage(chrome_browser_fixture)
    home_page.goto()
    home_page.order_now_unitree_g1_button.click()
    products_page = ProductsPage(chrome_browser_fixture)
    price = products_page.current_price.text_content()
    normalized_price = price.replace('USD', '').rstrip()
    products_page.add_to_cart_button.click()
    products_page.cart_button.click()
    cart_page = ShoppingCartPage(chrome_browser_fixture)
    cart_page.goto('/cart')
    yield cart_page, normalized_price


@pytest.fixture()
def add_unitree_go2_robot_to_cart(chrome_browser_fixture):
    login_page = LoginPage(chrome_browser_fixture)
    login_page.log_in_user()
    home_page = HomePage(chrome_browser_fixture)
    home_page.goto()
    home_page.order_now_unitree_go2_button.click()
    products_page = ProductsPage(chrome_browser_fixture)
    price = products_page.current_price.text_content()
    normalized_price = price[:6].replace('$', '').replace('USD', '').rstrip()
    products_page.add_to_cart_button.click()
    products_page.cart_button.click()
    cart_page = ShoppingCartPage(chrome_browser_fixture)
    cart_page.goto('/cart')
    cart_page.check_out_button.click()
    checkout_page = CheckOutPage(chrome_browser_fixture)
    yield checkout_page, normalized_price


@pytest.fixture()
def add_unitree_r1_robot_to_cart(chrome_browser_fixture):
    login_page = LoginPage(chrome_browser_fixture)
    login_page.log_in_user()
    home_page = HomePage(chrome_browser_fixture)
    home_page.goto()
    home_page.order_now_unitree_r1_button.click()
    products_page = ProductsPage(chrome_browser_fixture)
    price = products_page.current_price.text_content()
    normalized_price = price[:6].replace('$', '').replace('USD', '').replace(',', '.').rstrip()
    products_page.add_to_cart_button.click()
    products_page.cart_button.click()
    cart_page = ShoppingCartPage(chrome_browser_fixture)
    cart_page.goto('/cart')
    yield cart_page, str(float(normalized_price)*3)[:6].replace('.', ',')
