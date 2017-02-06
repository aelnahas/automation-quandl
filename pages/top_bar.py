import time
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located, presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from common.page_object import PageObject
from .locators import TopBarLocators, HomePageLocators, SigninLocators


class TopBarNav(PageObject):
    """Top Bar Navigation menu , shared across multiple pages"""

    def is_loaded(self):
        """A Top Bar Navigation is loaded if the top bar element is visible"""
        return self._is_loaded_helper(TopBarLocators.TOP_BAR)

    @property
    def logo_count(self):
        """returns the count of how many logo's are being displayed on the top bar"""
        return len(self._find_visible_logos())

    @property
    def user_menu(self):
        """The drop down menu if found"""
        return self.find_element(TopBarLocators.USER_MENU)

    def _find_visible_logos(self):
        """Find all visible logos in the top bar, due to responsive layout there is a potential that the page
           loads more than one visible logo at a time
            :returns: a list of all logos that are visible on the top bar
        """
        # find the log within the top bar, so first locate the top bar then use it as a context to find the logo.
        elements = self.find_element(TopBarLocators.TOP_BAR).find_elements(*TopBarLocators.LOGO)
        # filter out the ones that are actually visible
        logos = [logo for logo in elements if logo.is_displayed()]
        return logos

    def click_on_logo(self):
        """Clicks on the Quandl logo, waits until the home page is loaded"""

        # Make sure we only have one logo displayed
        logos = self._find_visible_logos()
        assert len(logos) == 1, "There are more than one displayed logos"
        logos[0].click()

        # Wait until the home screen is reloaded again, home hero is visible
        WebDriverWait(self._webdriver, 10, 1).until(visibility_of_element_located(HomePageLocators.HOME_HERO),
                                                    message="clicked on the Quandl logo but home page was not loaded")

    def navigate_to_signin(self):
        """Takes user to sigin in screen"""

        # first determine if the responsive layout displays the sign in button ( fullscreen )
        sign_in = self.find_element(TopBarLocators.SIGN_IN)
        if sign_in:
            sign_in.click()

        # the hamburger menu is visible instead try to click it
        else:
            user_menu = self.user_menu
            user_menu.click()
            self.click_element(TopBarLocators.SIGN_IN, context=user_menu)

        # in all cases need to give the web some time to load the sign in page, ( username field is visible )
        WebDriverWait(self._webdriver, 5, 0.5).until(visibility_of_element_located(SigninLocators.USERNAME),
                                                     message="Sign in page is not loaded or is missing username field")

    def retry_logouts(self):
        """Retry logouts until all 5 attempts are exhausted"""
        for count in range(5):
            elements = self.find_multi_elements(TopBarLocators.USER_MENU)

            for element in elements:
                if element.is_enabled() and element.is_displayed():
                    element.click()

                    logout = self.find_element(TopBarLocators.LOG_OUT, context=element)
                    if logout and logout.is_enabled() and logout.is_displayed():
                        logout.click()
                        return

            time.sleep(1)

    def logout(self):
        """logs the user out"""
        # first find the visible user menu
        # as a precaution make sure the user is logged in
        WebDriverWait(self._webdriver, 10, 1).until(presence_of_element_located(TopBarLocators.ACCOUNT_SETTINGS))

        self.retry_logouts()

        # wait until there is no account setting reference, which means we logged out
        WebDriverWait(self._webdriver, 10, 1).until(invisibility_of_element_located(TopBarLocators.ACCOUNT_SETTINGS),
                                                    message="Could not log out user")
