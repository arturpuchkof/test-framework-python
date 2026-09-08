from playwright.sync_api import Page

from src.variables import UI_BASE_URL


class BasePage:
    def __init__(self, page: Page):
        self.page = page


    def goto(self, path: str = '') -> None:
        return self.page.goto(f'{UI_BASE_URL}{path}')