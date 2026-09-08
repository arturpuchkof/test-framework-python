from playwright.sync_api import Page

from src.pages.base_page import BasePage


class CheckOutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.total_price = page.locator('._19gi7yt0._19gi7yt18._19gi7yt1g._19gi7yt1n._1fragem69.notranslate').first
        self.quantity = page.locator('._1m6j2n31b._1fragem120')