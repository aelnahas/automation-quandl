from common.page_object import PageObject
from pages.locators import SigninLocators


class SigninPage(PageObject):


    @property
    def username(self):
        return self.find_element(SigninLocators.USERNAME).text

    @username.setter
    def username(self, username):
        self.send_keys(SigninLocators.USERNAME, username)

    @property
    def password(self):
        return self.find_element(SigninLocators.PASSWORD).text

    @password.setter
    def password(self, password):
        self.send_keys(SigninLocators.PASSWORD, password)

    def log_in(self):
        self.click_element(SigninLocators.LOGIN_BTN)

    def create_new_account(self):
        self.click_element(SigninLocators.CREATE_NEW_LINK)