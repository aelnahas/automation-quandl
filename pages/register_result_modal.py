from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from common.page_object import PageObject
from pages.locators import RegisterModalLocators


class RegisterResultModal(PageObject):

    @property
    def api_key(self):
        return self.find_element(RegisterModalLocators.API_KEY).text

    def dismiss(self):
        self.click_element(RegisterModalLocators.MODAL_CONTINUE)

    def is_successful_registration(self):
        try:
            WebDriverWait(self._webdriver, 10, 1).until(visibility_of_element_located(RegisterModalLocators.API_KEY))
            return True

        except TimeoutException:
            return False


