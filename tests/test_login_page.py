from playwright.sync_api import expect
from utils.env_reader import get_url


def test_login_page_elements(open_page):
    page = open_page
    expect(page).to_have_url(get_url())
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    expect(page.locator("[data-test=\"password\"]")).to_be_visible()
    expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()

def test_login_functionality(open_page):
    page = open_page
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"primary-header\"] div").filter(
        has_text="Swag Labs").first).to_be_visible()
