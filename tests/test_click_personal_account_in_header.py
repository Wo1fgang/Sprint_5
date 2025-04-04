from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Login


def test_click_personal_account_in_header(chrome, main_page):
    element_visible = expected_conditions.visibility_of_element_located
    wait = WebDriverWait(chrome, 4)
    chrome.get(main_page)
    wait.until(element_visible(Login.PERSONAL_ACCOUNT)).click()

    assert wait.until(element_visible(Login.PURPLE_LOGIN_BUTTON_ON_LOGIN_PAGE)).is_displayed()
