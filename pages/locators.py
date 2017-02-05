from selenium.webdriver.common.by import By

# element locators can be separated . the main advantage of doing this is re-usability
# Things like top bar seems to  appear in multiple pages, so this would be common place to store its elements.


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
    NAME = (By.CLASS_NAME, "qa-name div input")
    EMAIL = (By.CLASS_NAME, "qa-email div input")
    PASSOWRD = (By.CLASS_NAME, "qa-password div input")
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
    USERNAME = (By.CLASS_NAME, "qa-username")
    EMAIL =  (By.CLASS_NAME, "qa-email")
    PASSWORD = (By.CLASS_NAME, "qa-password")
    CONFIRM_PASSWORD = (By.CLASS_NAME, "qa-password-confirmation")
    SIGN_UP_BTN = (By.CLASS_NAME, "qa-sign-up-free")