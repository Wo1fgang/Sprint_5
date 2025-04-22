from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import constants
from locators import Constructor


class TestChangeSections:
    def test_change_section_to_buns(self, chrome):
        element_visible = expected_conditions.visibility_of_element_located
        wait = WebDriverWait(chrome, 4)
        chrome.get(constants.STELLAR_BURGERS_MAIN_PAGE)
        wait.until(
            element_visible(Constructor.FILLING_SECTION_CHANGE_BUTTON)).click()
        wait.until(element_visible(Constructor.FILLING_ACTIVE_SECTION)).is_displayed()
        wait.until(
            element_visible(Constructor.INACTIVE_BUNS_SECTION_CHANGE_BUTTON)).click()

        assert wait.until(element_visible(Constructor.BUNS_ACTIVE_SECTION)).is_displayed()

    def test_change_section_to_filling(self, chrome):
        element_visible = expected_conditions.visibility_of_element_located
        wait = WebDriverWait(chrome, 4)
        chrome.get(constants.STELLAR_BURGERS_MAIN_PAGE)
        wait.until(
            element_visible(Constructor.FILLING_SECTION_CHANGE_BUTTON)).click()

        assert wait.until(element_visible(Constructor.FILLING_ACTIVE_SECTION)).is_displayed()

    def test_change_section_to_sauce(self, chrome):
        element_visible = expected_conditions.visibility_of_element_located
        wait = WebDriverWait(chrome, 4)
        chrome.get(constants.STELLAR_BURGERS_MAIN_PAGE)
        wait.until(
            element_visible(Constructor.SAUCE_SECTION_CHANGE_BUTTON)).click()

        assert wait.until(element_visible(Constructor.SAUCE_ACTIVE_SECTION)).is_displayed()

