from common.page_object import PageObject
from pages.locators import SignupPageLocators


class SignupPage(PageObject):
    """This is the signup page that is presented to the user if they click on
        sign in and then create new account"""

    @property
    def username(self):
        return self.find_element(SignupPageLocators.USERNAME).text

    @username.setter
    def username(self, username):
        self.send_keys(SignupPageLocators.USERNAME, username)

    @property
    def email(self):
        return self.find_element(SignupPageLocators.EMAIL).text

    @email.setter
    def email(self, email):
        self.send_keys(SignupPageLocators.EMAIL, email)

    @property
    def password(self):
        return self.find_element(SignupPageLocators.PASSWORD).text

    @password.setter
    def password(self, password):
        self.send_keys(SignupPageLocators.PASSWORD, password)

    @property
    def confirm_password(self):
        return self.find_element(SignupPageLocators.CONFIRM_PASSWORD).text

    @confirm_password.setter
    def confirm_password(self, confirm_password):
        self.send_keys(SignupPageLocators.CONFIRM_PASSWORD, confirm_password)

    def signup(self):
        self.find_element(SignupPageLocators.SIGN_UP_BTN).click()