import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Login")
@allure.story("Successful login: standard_user")
def test_login_success_standard_user(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.open_login()
        login.assert_form_visible()

    with allure.step("Login with valid credentials"):
        login.login("standard_user", "secret_sauce")

    with allure.step("Verify inventory page opened"):
        inventory = InventoryPage(page)
        inventory.assert_opened(timeout=7000)


@allure.feature("Login")
@allure.story("Invalid password: standard_user")
def test_login_invalid_password(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.open_login()
        login.assert_form_visible()

    with allure.step("Login with wrong password"):
        login.login("standard_user", "wrong_pass")

    with allure.step("Verify error and stay on login page"):
        assert "/inventory.html" not in page.url
        error_text = login.get_error_text()
        assert "Username and password do not match" in error_text


@allure.feature("Login")
@allure.story("Locked out user: locked_out_user")
def test_login_locked_out_user(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.open_login()

    with allure.step("Login as locked_out_user"):
        login.login("locked_out_user", "secret_sauce")

    with allure.step("Verify locked out error message"):
        assert "/inventory.html" not in page.url
        error_text = login.get_error_text()
        assert "locked out" in error_text.lower()


@allure.feature("Login")
@allure.story("Empty fields")
def test_login_empty_fields(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.open_login()

    with allure.step("Click login with empty fields"):
        login.click_login()

    with allure.step("Verify 'Username is required'"):
        error_text = login.get_error_text()
        assert "Username is required" in error_text


@allure.feature("Login")
@allure.story("Performance glitch user: performance_glitch_user")
def test_login_performance_glitch_user(page):
    login = LoginPage(page)

    with allure.step("Open login page"):
        login.open_login()

    with allure.step("Login as performance_glitch_user"):
        login.login("performance_glitch_user", "secret_sauce")

    with allure.step("Verify inventory page opened with extra timeout"):
        inventory = InventoryPage(page)
        inventory.assert_opened(timeout=20000)
