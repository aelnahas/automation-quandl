# This is a script used by pytest executor to create setup and teardown fixtures
import pytest
from selenium import webdriver
import logging
from pages.home_page import HomePage


@pytest.fixture(autouse=True)
def _environment(request, browser):

    for key, value in browser.capabilities.items():
        request.config._environment.append(("Browser.{}".format(key), "{}".format(value)))


@pytest.fixture(scope="session")
def logger():
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger()


@pytest.fixture(scope="session")
def browser(request, logger):
    driver = webdriver.Firefox()
    driver.maximize_window()
    logger.info("Starting {} Browser".format(driver.name))

    def tear_down():
        logger.info("Quitting {} Browser".format(driver.name))
        driver.quit()

    request.addfinalizer(tear_down)
    return driver


@pytest.fixture(scope="function")
def quandl_home(browser, logger):
    logger.info("Navigating back to quandl home page")
    base_url ="https://www.quandl.com"
    page = HomePage(browser, base_url)
    page.get()
    return page
