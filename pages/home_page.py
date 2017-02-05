from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from common.page_object import PageObject, PageNotLoaded
from pages.footer import Footer
from pages.locators import HomePageLocators
from pages.top_bar import TopBarNav


class HomePage(PageObject):
    """ Quandl's page object """

    def is_loaded(self):
        """A Top Bar Navigation is loaded if the top bar element is visible"""
        return self._is_loaded_helper(HomePageLocators.HOME_HERO)

    def _check_page(self, page_object, name):

        if not page_object.is_loaded():
            raise PageNotLoaded("{} was not loaded on home page")

    @property
    def top_bar(self):
        """The top bar navigation page object"""
        # since top bar is seen on the
        top_bar = TopBarNav(self._webdriver)
        self._check_page(top_bar, "Top bar navigation")
        return top_bar

    @property
    def footer(self):
        footer = Footer(self._webdriver)
        self._check_page(footer, "Footer")
        return footer
