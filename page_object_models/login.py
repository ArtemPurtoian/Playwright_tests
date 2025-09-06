from page_object_models.base import Base
from playwright.sync_api import expect
from utils.env_reader import get_user_credentials
import allure


"""
Creating the Login class that implements actions on the login page,
which will be used in the tests.
"""
class Login(Base):

    USERNAME_LOCATOR = '[data-test="username"]'
    PASSWORD_LOCATOR = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    HEADER_LOCATOR = '[data-test="primary-header"] div'
    HEADER_TEXT = "Swag Labs"

    def __init__(self, page):
        super().__init__(page)

    def check_page_elements(self):
        self.is_visible(self.USERNAME_LOCATOR)
        self.is_visible(self.PASSWORD_LOCATOR)
        self.is_visible(self.LOGIN_BUTTON)

    def login(self):
        username, password = get_user_credentials()
        self.fill_input(self.USERNAME_LOCATOR, username)
        self.fill_input(self.PASSWORD_LOCATOR, password)
        self.click_element(self.LOGIN_BUTTON)
        return self

    def check_login_success(self, text=HEADER_TEXT):
        with allure.step("Check login success"):
            expect(self.page.locator(self.HEADER_LOCATOR).filter(
                has_text=text).first).to_be_visible()
