from playwright.sync_api import Page

from src.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.order_now_unitree_g1_button = page.locator('a.text-column__button[href="/products/unitree-g1"]')
        self.order_now_unitree_r1_button = page.locator('a.text-column__button[href="/products/unitree-r1"]')
        self.order_now_unitree_go2_button = page.locator('a.text-column__button[href="/products/unitree-go2"]')