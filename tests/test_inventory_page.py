from page_object_models.inventory import Inventory
from page_object_models.login import Login


def test_inventory_page_elements(open_page):
    Login(open_page).login()
    Inventory(open_page).check_inventory_elements()
