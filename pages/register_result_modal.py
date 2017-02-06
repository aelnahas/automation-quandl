from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from common.page_object import PageObject
from pages.locators import RegisterModalLocators


class RegisterResultModal(PageObject):
    """A Modal that gets displayed when the user has successfully created a new account"""

    @property
    def api_key(self):
        return self.find_element(RegisterModalLocators.API_KEY).text

    def dismiss(self):
        """Dismiss the Modal by click the continue button"""
        self.click_element(RegisterModalLocators.MODAL_CONTINUE)
        WebDriverWait(self._webdriver, 10, 1)\
            .until(invisibility_of_element_located(RegisterModalLocators.REGISTER_SUCCESS))

    def is_successful_registration(self):
        """A function that determines whether if the user registration was successful

            :returns True: if the api key appears on the modal.
        """
        try:
            WebDriverWait(self._webdriver, 5, 0.5).until(visibility_of_element_located(RegisterModalLocators.API_KEY))
            return True

        except TimeoutException:
            return False


