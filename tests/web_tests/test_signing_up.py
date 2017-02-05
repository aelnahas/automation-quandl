from pages.signup_form import SignupForm
from datetime import datetime


def test_signingup_using_home_page_form(browser, quandl_home):
    """A user should be able to sign up using the form displayed at the bottom of the home page"""
    form = SignupForm(browser)
    # the timestamp is needed only for demo. In order to be able to repeat this test you would need to create
    # a new user each time, time stamping it may help in that regard
    timestamp = datetime.now().strftime("%H%M")
    username = "qa_tester_{}".format(timestamp)
    form.name = username
    form.email = "{}@qandl.com".format(username)
    form.password = "abcd1234ABCD!@#$"
