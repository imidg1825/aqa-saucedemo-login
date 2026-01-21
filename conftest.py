import pytest
from typing import Generator
from playwright.sync_api import sync_playwright, Browser, Page


@pytest.fixture(scope="session")
def browser() -> Generator[Browser, None, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                "--disable-http2",
                "--disable-features=IsolateOrigins,site-per-process",
                "--disable-web-security",
                "--no-sandbox",
            ],
        )
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser) -> Generator[Page, None, None]:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
