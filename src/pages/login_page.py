from playwright.sync_api import Page

from src.pages.base_page import BasePage
from src.variables import UI_USER_EMAIL, UI_USER_PASSWORD


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_field = page.locator('#customer_email')
        self.password_field = page.locator('#customer_password')
        self.sign_in_button = page.get_by_text('Sign In')


    def log_in_user(self, email: str = UI_USER_EMAIL, password: str = UI_USER_PASSWORD):
        self.goto('/account/login')
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.sign_in_button.click()