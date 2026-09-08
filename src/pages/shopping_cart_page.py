from playwright.sync_api import Page

from src.pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.locator('.majortitle')
        self.subtotal = page.locator('.subtotal.h2-style')
        self.check_out_button = page.get_by_role("button", name="Check out")
        self.increase_quantity_button = page.locator('#updates_inc_1')
        self.empty_cart_message = page.locator('.fully-spaced-row.align-centre.cc-animate-init.-in.cc-animate-complete')
        self.remove_item_button = page.locator('a.remove')