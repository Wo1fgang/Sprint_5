import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import constants
from data import CustomLogin
from locators import Login
from tests import login_action


class TestLogins:
    @pytest.mark.parametrize('login_button', [Login.PERSONAL_ACCOUNT, Login.ENTER_ACCOUNT])
    def test_logins(self, chrome, login_button):
        element_visible = expected_conditions.visibility_of_element_located
        wait = WebDriverWait(chrome, 4)
        chrome.get(constants.STELLAR_BURGERS_MAIN_PAGE)
        wait.until(element_visible(login_button)).click()  # parametrized logins
        login_action.login_on_login_page(chrome)

        assert wait.until(element_visible(Login.WHEN_LOGGED_IN_PERSONAL_ACCOUNT_PAGE_SETTINGS)).is_displayed()

    @pytest.mark.parametrize('login_pages',
                             [constants.STELLAR_BURGERS_FORGOT_PASSWORD_PAGE,
                              constants.STELLAR_BURGERS_FORGOT_REGISTER_PAGE])
    def test_alternative_logins(self, chrome, login_pages):
        element_visible = expected_conditions.visibility_of_element_located
        element_no_longer_visible = expected_conditions.invisibility_of_element_located
        wait = WebDriverWait(chrome, 4)
        chrome.get(login_pages)  # parametrized logins
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
