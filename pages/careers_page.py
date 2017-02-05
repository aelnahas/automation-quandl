from common.page_object import PageObject
from pages.locators import CareersPageLocators


class CareersPage(PageObject):
    """The careers page"""

    def is_loaded(self):
        return self._is_loaded_helper(CareersPageLocators.CAREERS_HERO) and self.title == "Careers at Quandl"
