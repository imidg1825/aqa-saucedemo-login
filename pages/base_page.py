import re
from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, url: str) -> None:
        # Более стабильная загрузка + увеличенный таймаут
        self.page.goto(url, wait_until="load", timeout=60000)

    def expect_visible(self, locator: Locator, timeout: int = 5000) -> None:
        expect(locator).to_be_visible(timeout=timeout)

    def expect_url_contains(self, part: str, timeout: int = 5000) -> None:
        # to_have_url принимает строку или regex (lambda нельзя)
        pattern = re.compile(rf".*{re.escape(part)}.*")
        expect(self.page).to_have_url(pattern, timeout=timeout)
