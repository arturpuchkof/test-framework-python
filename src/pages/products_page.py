from playwright.sync_api import Page

from src.pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.current_price = page.locator('.current-price.theme-money')
        self.quantity = page.locator('#quantity')
        self.add_to_cart_button = page.locator('.button.button--large')
        self.cart_button = page.locator('.button.to-cart')