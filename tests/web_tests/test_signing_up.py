from pages.register_result_modal import RegisterResultModal
from pages.signin_page import SigninPage
from pages.signup_form import SignupForm
from datetime import datetime

from pages.signup_page import SignupPage


def test_signingup_using_sign_in_button(browser, quandl_home):
    "A user should be able to sign up to a new account, if the click on signin then signup"
    quandl_home.navigate_to_sign_in()
    SigninPage(browser).create_new_account()

    timestamp = datetime.now().strftime("%H%M_signin_page")
    username = "qa_tester_{}".format(timestamp)

    form = SignupPage(browser)
    form.username = username
    form.email = "{}@quandl.com".format(username)
    form.password = "password"
    form.confirm_password = "password"
    form.signup()

    registration_modal = RegisterResultModal(browser)
    assert registration_modal.is_successful_registration(), "Could not create a new account"
    registration_modal.dismiss()

