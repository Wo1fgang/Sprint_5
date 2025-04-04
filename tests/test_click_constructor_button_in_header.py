from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import Constructor


def test_click_personal_account_in_header(chrome, main_page, login_page):
    chrome.get(login_page)
    element_visible = expected_conditions.visibility_of_element_located
    wait = WebDriverWait(chrome, 4)
    wait.until(element_visible(Constructor.MAIN_PAGE_CONSTRUCTOR_LINK)).click()

    assert chrome.current_url == main_page
