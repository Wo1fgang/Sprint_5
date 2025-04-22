from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import constants
from tests.locators import Constructor, Login


class TestButtonsInHeaders:
    def test_click_constructor_button_in_header(self, chrome):
        chrome.get(constants.STELLAR_BURGERS_LOGIN_PAGE)
        element_visible = expected_conditions.visibility_of_element_located
        wait = WebDriverWait(chrome, 4)
        wait.until(element_visible(Constructor.MAIN_PAGE_CONSTRUCTOR_LINK)).click()

        assert chrome.current_url == constants.STELLAR_BURGERS_MAIN_PAGE

    def test_click_personal_account_in_header(self, chrome):
        element_visible = expected_conditions.visibility_of_element_located
        wait = WebDriverWait(chrome, 4)
        chrome.get(constants.STELLAR_BURGERS_MAIN_PAGE)
        wait.until(element_visible(Login.PERSONAL_ACCOUNT)).click()

        assert wait.until(element_visible(Login.PURPLE_LOGIN_BUTTON_ON_LOGIN_PAGE)).is_displayed()

    def test_click_stellar_burgers_logo_in_header(self, chrome):
        chrome.get(constants.STELLAR_BURGERS_LOGIN_PAGE)
        element_visible = expected_conditions.visibility_of_element_located
        wait = WebDriverWait(chrome, 4)
        wait.until(element_visible(Constructor.MAIN_PAGE_STELLAR_BURGERS_LOGO)).click()

        assert chrome.current_url == constants.STELLAR_BURGERS_MAIN_PAGE