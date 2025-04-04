from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Registration, Login
from login_and_password_generators import generate_login, generate_password


def test_successful_registration(chrome, main_page, login_page):
    login_test_email = generate_login()
    login_test_password = generate_password()
    element_visible = expected_conditions.visibility_of_element_located
    element_no_longer_visible = expected_conditions.invisibility_of_element_located
    wait = WebDriverWait(chrome, 4)
    chrome.get(main_page)
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

    assert chrome.current_url == login_page
