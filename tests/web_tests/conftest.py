# This is a script used by pytest executor to create setup and teardown fixtures
import pytest
from selenium import webdriver

from pages.home_page import HomePage


@pytest.fixture(scope="module")
def browser(request):
    driver = webdriver.Firefox()
    yield driver
    print("Quitting Driver")
    driver.quit()


@pytest.fixture(scope="function")
def quandl_home(browser):
    base_url ="https://www.quandl.com"
    page = HomePage(browser, base_url)
    page.get()
    return page