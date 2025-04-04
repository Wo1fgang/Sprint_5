import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Login
from tests import login_action


@pytest.mark.parametrize('login_button', [Login.PERSONAL_ACCOUNT, Login.ENTER_ACCOUNT])
def test_login_personal_account_header_button(chrome, main_page, login_page, login_button):
    element_visible = expected_conditions.visibility_of_element_located
    wait = WebDriverWait(chrome, 4)
    chrome.get(main_page)
    wait.until(element_visible(login_button)).click()  # parametrized logins
    login_action.login_on_login_page(chrome)

    assert wait.until(element_visible(Login.WHEN_LOGGED_IN_PERSONAL_ACCOUNT_PAGE_SETTINGS)).is_displayed()
