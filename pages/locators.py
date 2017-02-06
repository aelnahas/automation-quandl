from selenium.webdriver.common.by import By

# This is script containing all locators used. The idea is to keep them in a common script to avoid duplicating them


# ------------------------- Widgets / Common ----------------------------------------------
class TopBarLocators(object):
    TOP_BAR = (By.CLASS_NAME, "application-header")
    DOCS_AND_HELP = (By.ID, "ember665")
    DOCS_AND_HELP_DROPDOWN = (By.ID, "ember696")
    SIGN_IN = (By.CLASS_NAME, "qa-top-bar-log-in")
    LOGO = (By.CLASS_NAME, "quandl-logo")
    LOG_OUT = (By.CLASS_NAME, "qa-logout")
    USER_MENU = (By.CLASS_NAME, "qa-user-menu")
    ACCOUNT_SETTINGS = (By.CLASS_NAME, "qa-account-settings")


class FooterLocators(object):
    CAREERS_LINK = (By.CSS_SELECTOR, ".fat-footer .qa-footer-jobs")


class SignupFormLocators(object):
    FORM = (By.CLASS_NAME, "qa-about-signup")
    TITLE = (By.CSS_SELECTOR, ".qa-about-signup h3")
    NAME = (By.CSS_SELECTOR, ".qa-name div input")
    EMAIL = (By.CSS_SELECTOR, ".qa-email div input")
    PASSOWRD = (By.CSS_SELECTOR, ".qa-password div input")
    ERROR_MESSAGE = (By.CLASS_NAME, "qa-error-message")
    SIGUN_UP_BTN = (By.CSS_SELECTOR, "button.qa-submit")


class RegisterModalLocators(object):
    REGISTER_SUCCESS = (By.CSS_SELECTOR, "section.register-success")
    API_KEY = (By.CSS_SELECTOR, ".modal.register-success .api-key")
    MODAL_CONTINUE = (By.CLASS_NAME, "qa-continue")


# ------------------------- Pages -----------------------------------------------------------
class HomePageLocators(object):
    HOME_HERO = (By.CSS_SELECTOR, "main.display .home-hero")


class CareersPageLocators(object):
    CAREERS_HERO = (By.CSS_SELECTOR, "div.careers-hero")


class SigninLocators(object):
    USERNAME = (By.CLASS_NAME, "qa-login-username")
    PASSWORD = (By.CLASS_NAME, "qa-login-password")
    LOGIN_BTN = (By.CLASS_NAME, "qa-login")
    CREATE_NEW_LINK = (By.CLASS_NAME, "qa-register")


class SignupPageLocators(object):
    """This locator is for the sign up page that gets loaded if the user chooses to create a new account from
        the sign in page
    """
    USERNAME = (By.CSS_SELECTOR, "input.qa-username")
    EMAIL =  (By.CSS_SELECTOR, "input.qa-email")
    PASSWORD = (By.CSS_SELECTOR, "input.qa-password")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input.qa-password-confirmation")
    SIGN_UP_BTN = (By.CSS_SELECTOR, "button.qa-sign-up-free")