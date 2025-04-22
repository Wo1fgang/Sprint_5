from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Login
from data import CustomLogin


def login_on_login_page(chrome):
    element_visible = expected_conditions.visibility_of_element_located
    element_no_longer_visible = expected_conditions.invisibility_of_element_located
    wait = WebDriverWait(chrome, 4)
    wait.until(element_visible(Login.LOGIN_BUTTON)).is_displayed()
    wait.until(element_visible(Login.LOGIN_EMAIL)).click()
    wait.until(element_visible(Login.LOGIN_EMAIL)).send_keys(CustomLogin.EMAIL)
    wait.until(element_visible(Login.LOGIN_PASSWORD)).send_keys(CustomLogin.PASSWORD)
    wait.until(element_visible(Login.LOGIN_BUTTON)).click()
    wait.until(element_no_longer_visible(Login.LOGIN_BUTTON))
    wait.until(element_visible(Login.PERSONAL_ACCOUNT)).click()
    wait.until(element_no_longer_visible(Login.WHEN_LOGGED_IN_PUT_ORDER_BUTTON))
