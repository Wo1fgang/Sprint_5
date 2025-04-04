from selenium import webdriver
import pytest
import constants


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def main_page():
    return constants.STELLAR_BURGERS_MAIN_PAGE


@pytest.fixture
def login_page():
    return constants.STELLAR_BURGERS_LOGIN_PAGE