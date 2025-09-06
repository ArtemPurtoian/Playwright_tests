from playwright.sync_api import expect
import allure


"""
Creating the Base class that implements Playwright actions.
"""
class Base:
    def __init__(self, page):
        self.page = page

    def pause_page(self):
        self.page.pause()
        return self

    def has_url(self, url):
        with allure.step(f"Check the '{url}' url"):
            expect(self.page).to_have_url(url)
            return self

    def is_visible(self, locator):
        with allure.step(f"Check the '{locator}' locator visibility"):
            expect(self.page.locator(locator)).to_be_visible()
            return self

    def fill_input(self, locator, input_value):
        with allure.step(f"Fill '{locator}' locator with '{input_value}' value"):
            self.page.locator(locator).fill(input_value)
            return self

    def click_element(self, locator):
        with allure.step(f"Click on the '{locator}' element"):
            self.page.locator(locator).click()
            return self

    def is_enabled(self, locator):
        with allure.step(f"Check if the '{locator}' element is enabled"):
            expect(self.page.locator(locator)).to_be_enabled()
            return self

    def is_match_snapshot(self, locator, snapshot):
        with allure.step(f"Check if snapshot match at the '{locator}' locator"):
            expect(self.page.locator(locator)).to_match_aria_snapshot(snapshot)
            return self
