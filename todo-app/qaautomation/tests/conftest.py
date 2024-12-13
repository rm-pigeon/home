import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://localhost:3000")

        yield page
        page.close()