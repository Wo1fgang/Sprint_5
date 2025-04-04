from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Constructor


def test_click_personal_account(chrome, main_page):
    element_visible = expected_conditions.visibility_of_element_located
    wait = WebDriverWait(chrome, 4)
    chrome.get(main_page)
    wait.until(
        element_visible(Constructor.SAUCE_SECTION_CHANGE_BUTTON)).click()

    assert wait.until(element_visible(Constructor.SAUCE_ACTIVE_SECTION)).is_displayed()
