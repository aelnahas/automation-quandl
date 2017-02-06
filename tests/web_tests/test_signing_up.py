from pages.register_result_modal import RegisterResultModal
from pages.signin_page import SigninPage
from pages.signup_form import SignupForm
from datetime import datetime

from pages.signup_page import SignupPage


def test_sigining_up_using_home_page_form(browser, quandl_home, logger):
    """A user should be able to sign up a new account , by filling the home page form"""

    logger.info("Fetching form at the bottom of the home page")
    form = SignupForm(browser)
    assert form.is_loaded(), "Form is not loaded on the home page"

    logger.info("Filling in user name, email and password")
    timestamp = datetime.now().strftime("%H%M")
    username = "qa_tester_{}".format(timestamp)
    form.name = username
    form.email = "{}@quandl.com".format(username)
    form.password = "password"
    form.submit()

    logger.info("Check if the successful registration modal is displayed")
    registration_modal = RegisterResultModal(browser)
    assert registration_modal.is_successful_registration(), "Could not create a new account"

    logger.info("Dismiss the modal and logout the new user")
    registration_modal.dismiss()
    quandl_home.logout()


def test_signingup_using_sign_in_button(browser, quandl_home, logger):
    "A user should be able to sign up to a new account, if the click on signin then signup"

    logger.info("Bring up the sign in page")
    quandl_home.navigate_to_sign_in()
    logger.info("Create a new account")
    SigninPage(browser).create_new_account()

    timestamp = datetime.now().strftime("%H%M_signin_page")
    username = "qa_tester_{}".format(timestamp)

    logger.info("Entering new user info: name, email, and password")
    form = SignupPage(browser)
    form.username = username
    form.email = "{}@quandl.com".format(username)
    form.password = "password"
    form.confirm_password = "password"
    form.signup()

    logger.info("Successful registration modal should be displayed")
    registration_modal = RegisterResultModal(browser)
    assert registration_modal.is_successful_registration(), "Could not create a new account"

    logger.info("Dismiss the modal and sign out the new user")
    registration_modal.dismiss()
    quandl_home.logout()

