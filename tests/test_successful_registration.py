from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import constants
from locators import Registration, Login
from login_and_password_generators import generate_login, generate_password, generate_invalid_password


class TestRegistrations:
    def test_successful_registration(self, chrome):
        login_test_email = generate_login()
        login_test_password = generate_password()
        element_visible = expected_conditions.visibility_of_element_located
        element_no_longer_visible = expected_conditions.invisibility_of_element_located
        wait = WebDriverWait(chrome, 4)
        chrome.get(constants.STELLAR_BURGERS_MAIN_PAGE)
        wait.until(element_visible(Login.PERSONAL_ACCOUNT)).click()
        wait.until(element_visible(Registration.REGISTER)).click()
        wait.until(element_visible(Registration.REGISTRATION_PAGE_NAME)).send_keys(
            login_test_email)
        wait.until(element_visible(Registration.REGISTRATION_PAGE_EMAIL)).send_keys(
            login_test_email)
        wait.until(element_visible(Registration.REGISTRATION_PAGE_PASSWORD)).send_keys(
            login_test_password)
        wait.until(element_visible(Registration.REGISTRATION_PAGE_REGISTER_BUTTON)).click()
        wait.until(element_no_longer_visible(Registration.REGISTRATION_PAGE_REGISTER_BUTTON))

        assert chrome.current_url == constants.STELLAR_BURGERS_LOGIN_PAGE


    def test_registration_with_incorrect_password(self, chrome):
        login_test_email = generate_login()
        login_invalid_password = generate_invalid_password()
        element_visible = expected_conditions.visibility_of_element_located
        wait = WebDriverWait(chrome, 4)
        chrome.get(constants.STELLAR_BURGERS_MAIN_PAGE)
        wait.until(
            element_visible(Login.PERSONAL_ACCOUNT)).click()
        wait.until(element_visible(Registration.REGISTER)).click()
        wait.until(element_visible(Registration.REGISTRATION_PAGE_NAME)).send_keys(
            login_test_email)
        wait.until(element_visible(Registration.REGISTRATION_PAGE_EMAIL)).send_keys(
            login_test_email)
        wait.until(element_visible(Registration.REGISTRATION_PAGE_PASSWORD)).send_keys(
            login_invalid_password)
        wait.until(element_visible(Registration.REGISTRATION_PAGE_REGISTER_BUTTON)).click()

        assert wait.until(element_visible(Registration.REGISTRATION_PAGE_INCORRECT_PASSWORD_ERROR)).is_displayed()