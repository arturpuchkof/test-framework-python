import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture()
def chrome_browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()