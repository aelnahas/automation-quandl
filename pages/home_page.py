from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from common.page_object import PageObject, PageNotLoaded
from pages.footer import Footer
from pages.locators import HomePageLocators, TopBarLocators
from pages.signin_page import SigninPage
from pages.top_bar import TopBarNav


class HomePage(PageObject):
    """ Quandl's page object """

    def is_loaded(self):
        """A Top Bar Navigation is loaded if the top bar element is visible"""
        return self._is_loaded_helper(HomePageLocators.HOME_HERO)

    def _check_page(self, page_object, name):
        """A helper method to check if a part of the page has not loaded correctly"""
        if not page_object.is_loaded():
            raise PageNotLoaded("{} was not loaded on home page".format(name))

    @property
    def top_bar(self):
        """The top bar navigation page object"""
        # check to see if the top bar is loaded, return the page object if it is
        top_bar = TopBarNav(self._webdriver)
        self._check_page(top_bar, "Top bar navigation")
        return top_bar

    @property
    def footer(self):
        """The footer page object found on the home page"""
        # check to see if the footer is visible and return it if so
        footer = Footer(self._webdriver)
        self._check_page(footer, "Footer")
        return footer

    def navigate_to_sign_in(self):
        self.top_bar.navigate_to_signin()

    def sign_in(self, username, password):
        """helper method to go straight to signing in"""
        self.top_bar.navigate_to_signin()
        sign_in = SigninPage(self._webdriver)
        sign_in.username = username
        sign_in.password = password
        sign_in.log_in()


    def logout(self):
        """Log out of a user account"""
        self.top_bar.logout()