import pytest
from playwright.sync_api import sync_playwright
from utils.env_reader import get_browser, get_url


@pytest.fixture
def open_page():
    """
    Creating a context manager to handle Playwright browser instances
    depending on the env configuration, and open the page under test.
    :return:
    """
    with sync_playwright() as playwright:
        if get_browser() == "chromium":
            browser = playwright.chromium.launch(headless=False)
        elif get_browser() == "firefox":
            browser = playwright.firefox.launch(headless=False)
        else:
            browser = playwright.webkit.launch(headless=False)
        page = browser.new_page()
        page.goto(get_url())
        yield page
        browser.close()
