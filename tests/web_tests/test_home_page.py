from pages.careers_page import CareersPage


def test_only_one_logo_on_top_bar(quandl_home):
    """In home page top bar, there is only one visible logo"""
    num_logos = quandl_home.top_bar.logo_count
    assert num_logos == 1, "There are more than one logos in the main screen"


def test_top_bar_logo_links_to_home_page(quandl_home):
    """In home page, Quandl logo on the top bar takes the user back to home page"""

    quandl_home.top_bar.click_on_logo()
    assert quandl_home.is_loaded(), "Home page was not loaded after user clicks on top bar logo"


def test_footer_has_careers_link(browser, quandl_home):
    """In home page, There should be a link to careers page in the footer"""
    quandl_home.footer.navigate_to_careers()
    career_page = CareersPage(browser)
    assert career_page.is_loaded(), "After clicking on the careers link , the careers page was not loaded"

