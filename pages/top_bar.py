from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from common.page_object import PageObject
from .locators import TopBarLocators, HomePageLocators


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
    def drop_down_menu(self):
        """The drop down menu if found"""
        try:
            return self.find_element(TopBarLocators.DROP_DOWN_MENU)

        except NoSuchElementException:
            return None

    def _find_visible_logos(self):
        """Find all visible logos in the top bar, due to responsive layout there is a potential that the page
           loads more than one visible logo at a time
            :returns: a list of all logos that are visible on the top bar
        """
        # find the log within the top bar, so first locate the top bar then use it as a context to find the logo.
        elements = self.find_element(TopBarLocators.TOP_BAR).find_elements(*TopBarLocators.LOGO)
        logos = [logo for logo in elements if logo.is_displayed()]
        return logos

    def click_on_logo(self):
        """Clicks on the Quandl logo, waits until the home page is loaded"""
        logos = self._find_visible_logos()
        assert len(logos) == 1, "There are more than one displayed logos"
        logos[0].click()
        WebDriverWait(self._webdriver, 10, 1).until(visibility_of_element_located(HomePageLocators.HOME_HERO),
                                                    message="clicked on the Quandl logo but home page was not loaded")

    def navigate_to_docs_and_help(self):
        """A Function to navigate ot the docs & help."""
        drop_down_menu = self.drop_down_menu

        # check if the responive layout has rendered the drop down hamburger menu ( i.e. screen is small enough )
        if drop_down_menu:
            drop_down_menu.click()
            self.find_element(TopBarLocators.DOCS_AND_HELP_DROPDOWN).click()

        # the link is fully exposed, i.e. the web browser has a screen large enough
        else:
            self.find_element(TopBarLocators.DOCS_AND_HELP).click()