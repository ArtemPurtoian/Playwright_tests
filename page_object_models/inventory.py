from page_object_models.base import Base
from playwright.sync_api import expect


class Inventory(Base):

    SHOPPING_CART_LOCATOR = "[data-test=\"shopping-cart-link\"]"
    INVENTORY_LOCATOR = "[data-test=\"inventory-list\"]"
    INVENTORY_SNAPSHOT = ("- link /.+/:\n  - /url: \"#\"\n"
                            "  - img /.+/\n- link /.+/:\n"
                            "  - /url: \"#\"\n- text: /.+\$\d+\.\d+/\n"
                            "- button \"Add to cart\"\n"
                            "- link /.+/:\n  - /url: \"#\"\n"
                            "  - img /.+/\n- link /.+/:\n"
                            "  - /url: \"#\"\n- text: /.+\$\d+\.\d+/\n"
                            "- button \"Add to cart\"\n"
                            "- link /.+/:\n  - /url: \"#\"\n"
                            "  - img /.+/\n- link /.+/:\n"
                            "  - /url: \"#\"\n- text: /.+\$\d+\.\d+/\n"
                            "- button \"Add to cart\"\n"
                            "- link /.+/:\n  - /url: \"#\"\n"
                            "  - img /.+/\n- link /.+/:\n"
                            "  - /url: \"#\"\n- text: /.+\$\d+\.\d+/\n"
                            "- button \"Add to cart\"\n"
                            "- link /.+/:\n  - /url: \"#\"\n"
                            "  - img /.+/\n- link /.+/:\n"
                            "  - /url: \"#\"\n- text: /.+\$\d+\.\d+/\n"
                            "- button \"Add to cart\"\n"
                            "- link /.+/:\n  - /url: \"#\"\n"
                            "  - img /.+/\n- link /.+/:\n"
                            "  - /url: \"#\"\n- text: /.+\$\d+\.\d+/\n"
                            "- button \"Add to cart\"")

    def __init__(self, page):
        super().__init__(page)

    def check_inventory_elements(self):
        self.is_enabled(self.SHOPPING_CART_LOCATOR)
        self.is_match_snapshot(self.INVENTORY_LOCATOR, self.INVENTORY_SNAPSHOT)
        return self
