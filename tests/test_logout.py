from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import constants
from locators import Login
from tests import login_action


def test_logout(chrome):
    element_visible = expected_conditions.visibility_of_element_located
    element_no_longer_visible = expected_conditions.invisibility_of_element_located
    wait = WebDriverWait(chrome, 4)
    chrome.get(constants.STELLAR_BURGERS_MAIN_PAGE)
    wait.until(element_visible(Login.PERSONAL_ACCOUNT)).click()
    login_action.login_on_login_page(chrome)
    wait.until(element_no_longer_visible(Login.WHEN_LOGGED_IN_PUT_ORDER_BUTTON))
    wait.until(element_visible(Login.LOGOUT_BUTTON)).click()
    assert wait.until(element_visible(Login.LOGIN_PAGE_LOGIN_TEXT)) and chrome.current_url == constants.STELLAR_BURGERS_LOGIN_PAGE
