import pytest
from playwright.sync_api import sync_playwright

from src.clients.mqtt_client import MqttClient


@pytest.fixture()
def chrome_browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(locale='en-PL')
        page = context.new_page()
        yield page
        page.close()
        browser.close()


@pytest.fixture()
def mqtt_client():
    mqttc = MqttClient()
    mqttc.on_subscribe()
    yield mqttc