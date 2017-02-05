from selenium.webdriver.common.by import By

# element locators can be separated . the main advantage of doing this is re-usability
# Things like top bar seems to  appear in multiple pages, so this would be common place to store its elements.

# ------------------------- Widgets / Common ----------------------------------------------
class TopBarLocators(object):
    TOP_BAR = (By.CLASS_NAME, "application-header")
    DROP_DOWN_MENU = (By.ID, "ember693")
    DOCS_AND_HELP = (By.ID, "ember665")
    DOCS_AND_HELP_DROPDOWN = (By.ID, "ember696")
    SIGN_IN = (By.CLASS_NAME, "qa-top-bar-log-in")
    LOGO = (By.CLASS_NAME, "quandl-logo")


class FooterLocators(object):
    CAREERS_LINK = (By.CSS_SELECTOR, ".fat-footer .qa-footer-jobs")


class SignupFormLocators(object):
    FORM = (By.CLASS_NAME, "qa-about-signup")
    TITLE = (By.CSS_SELECTOR, ".qa-about-signup h3")
    NAME = (By.CLASS_NAME, "qa-name div input")
    EMAIL = (By.CLASS_NAME, "qa-email div input")
    PASSOWRD = (By.CLASS_NAME, "qa-password div input")
    ERROR_MESSAGE = (By.CLASS_NAME, "qa-error-message")
    SIGUN_UP_BTN = (By.CLASS_NAME, "button.qa-submit")

# ------------------------- Pages -----------------------------------------------------------

class HomePageLocators(object):
    HOME_HERO = (By.CSS_SELECTOR, "main.display .home-hero")


class CareersPageLocators(object):
    CAREERS_HERO = (By.CSS_SELECTOR, "div.careers-hero")