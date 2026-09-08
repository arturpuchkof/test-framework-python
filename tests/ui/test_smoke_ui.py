import re

import pytest
from playwright.sync_api import expect

from src.pages.account_page import AccountPage
from src.pages.login_page import LoginPage


@pytest.mark.ui
def test_user_login(chrome_browser_fixture):
    login_page = LoginPage(chrome_browser_fixture)
    login_page.log_in_user()
    account_page = AccountPage(chrome_browser_fixture)
    expect(account_page.account_title).to_have_text('My Account')
    expect(account_page.customer_orders).to_have_text("You haven't placed any orders yet.")


@pytest.mark.ui
def test_user_add_items_to_cart(add_unitree_g1_robot_to_cart):
   cart_page, expected_price = add_unitree_g1_robot_to_cart
   expect(cart_page.title).to_have_text('Shopping cart')
   expect(cart_page.subtotal).to_contain_text(expected_price)


@pytest.mark.ui
def test_user_checkout(add_unitree_go2_robot_to_cart):
    checkout_page, price = add_unitree_go2_robot_to_cart
    expect(checkout_page.total_price).to_contain_text(price)
    expect(checkout_page.page).to_have_url(re.compile(r"^https://shop\.unitree\.com/checkouts/"))


@pytest.mark.ui
def test_increase_quantity_in_cart(add_unitree_r1_robot_to_cart):
    cart_page, increased_price = add_unitree_r1_robot_to_cart
    cart_page.increase_quantity_button.click()
    cart_page.increase_quantity_button.click()
    expect(cart_page.subtotal).to_contain_text(increased_price)


@pytest.mark.ui
def test_remove_item_from_cart(add_unitree_g1_robot_to_cart):
    cart_page, _ = add_unitree_g1_robot_to_cart
    cart_page.remove_item_button.click()
    expect(cart_page.empty_cart_message).to_be_visible()