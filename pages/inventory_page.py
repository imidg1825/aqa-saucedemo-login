from playwright.sync_api import Locator
from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_list: Locator = page.locator(".inventory_list")

    def assert_opened(self, timeout: int = 5000) -> None:
        self.expect_url_contains("/inventory.html", timeout=timeout)
        self.expect_visible(self.inventory_list, timeout=timeout)
