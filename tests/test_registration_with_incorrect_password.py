from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Registration, Login
from login_and_password_generators import generate_login, generate_invalid_password


def test_registration_with_incorrect_password(chrome, main_page):
    login_test_email = generate_login()
    login_invalid_password = generate_invalid_password()
    element_visible = expected_conditions.visibility_of_element_located
    wait = WebDriverWait(chrome, 4)
    chrome.get(main_page)
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
