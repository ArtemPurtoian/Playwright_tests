from utils.env_reader import get_url
from page_object_models.login import Login


def test_login_page_elements(open_page):
    Login(open_page).has_url(get_url()).check_page_elements()

def test_login_functionality(open_page):
    Login(open_page).login("standard_user",
                           "secret_sauce").check_login_success()
