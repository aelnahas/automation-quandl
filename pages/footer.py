from common.page_object import PageObject
from pages.locators import FooterLocators


class Footer(PageObject):
    """Footer containing various links, shared among many pages"""
    def is_loaded(self):
        return self._is_loaded_helper(FooterLocators.CAREERS_LINK)

    def navigate_to_careers(self):
        self.find_element(locator=FooterLocators.CAREERS_LINK).click()