from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.wait import WebDriverWait

from common.page_object import PageObject
from pages.locators import CareersPageLocators


class CareersPage(PageObject):

    def is_loaded(self):
        return self._is_loaded_helper(CareersPageLocators.CAREERS_HERO) and self.title == "Careers at Quandl"
