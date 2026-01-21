from playwright.sync_api import Locator
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        super().__init__(page)
        self.username: Locator = page.locator("#user-name")
        self.password: Locator = page.locator("#password")
        self.login_button: Locator = page.locator("#login-button")
        self.error_container: Locator = page.locator("[data-test='error']")

    def open_login(self) -> None:
        self.open(self.URL)

    def assert_form_visible(self) -> None:
        self.expect_visible(self.username)
        self.expect_visible(self.password)
        self.expect_visible(self.login_button)

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def click_login(self) -> None:
        self.login_button.click()

    def get_error_text(self) -> str:
        self.expect_visible(self.error_container)
        return self.error_container.inner_text()
