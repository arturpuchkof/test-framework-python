from playwright.sync_api import Page

from src.pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.account_title = page.get_by_role("heading", name="My Account")
        self.customer_orders = page.locator('#customer_orders')
