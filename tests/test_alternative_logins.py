import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import STELLAR_BURGERS_FORGOT_PASSWORD_PAGE, STELLAR_BURGERS_FORGOT_REGISTER_PAGE
from locators import Login
from login_and_password_generators import CustomLogin


@pytest.mark.parametrize('login_pages', [STELLAR_BURGERS_FORGOT_PASSWORD_PAGE, STELLAR_BURGERS_FORGOT_REGISTER_PAGE])
def test_login_through_enter_account_button_on_main_page(chrome, login_pages, main_page):
    element_visible = expected_conditions.visibility_of_element_located
    element_no_longer_visible = expected_conditions.invisibility_of_element_located
    wait = WebDriverWait(chrome, 4)
    chrome.get(login_pages)   # parametrized logins
    wait.until(element_visible(Login.LOGIN_LINK)).click()
    wait.until(element_visible(Login.LOGIN_BUTTON))
    wait.until(element_visible(Login.LOGIN_EMAIL)).click()
    wait.until(element_visible(Login.LOGIN_EMAIL)).send_keys(CustomLogin.EMAIL)
    wait.until(element_visible(Login.LOGIN_PASSWORD)).send_keys(CustomLogin.PASSWORD)
    wait.until(element_visible(Login.LOGIN_BUTTON)).click()
    wait.until(element_no_longer_visible(Login.LOGIN_BUTTON))
    wait.until(element_visible(Login.PERSONAL_ACCOUNT)).click()
    wait.until(element_no_longer_visible(Login.WHEN_LOGGED_IN_PUT_ORDER_BUTTON))

    assert wait.until(element_visible(Login.WHEN_LOGGED_IN_PERSONAL_ACCOUNT_PAGE_SETTINGS)).is_displayed()
