from selenium.webdriver.support.wait import WebDriverWait

from common.page_object import PageObject
from pages.locators import SignupFormLocators


class SignupForm(PageObject):
    """A sign up form widget, can be seen on the home page"""

    def is_loaded(self):
        return self._is_loaded_helper(SignupFormLocators.FORM)

    @property
    def title(self):

        return self.find_element(SignupFormLocators.TITLE).text

    @property
    def name(self):
        return self.find_element(SignupFormLocators.NAME).text

    @property
    def email(self):
        return self.find_element(SignupFormLocators.EMAIL)

    @property
    def password(self):
        return self.find_element(SignupFormLocators.PASSOWRD)

    @name.setter
    def name(self, username):
        self.send_keys(locator=SignupFormLocators.NAME, text=username)

    @email.setter
    def email(self, email):
        self.send_keys(SignupFormLocators.EMAIL, email)

    @password.setter
    def password(self, password):
        self.send_keys(SignupFormLocators.PASSOWRD, password)

    def submit(self):
        self.find_element(SignupFormLocators.SIGUN_UP_BTN).click()
