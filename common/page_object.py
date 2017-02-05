# A common base page object to be used by all the page object
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class PageNotLoaded(Exception):
    pass

class PageObject(object):
    """
        The base page object, all pages will extend this page
    """
    def __init__(self, webdriver, base_url=None):
        self._webdriver = webdriver
        self._base_url = base_url

    def get(self, url=None):
        """retrieve the page or visit a link within the page
            :param url: a relative url to the page, if left empty, the
                method will just attempt to get the page using the base url
        """
        if self._base_url is None and url is None:
            raise ValueError("Both base_url and url are None. "
                              "At least one of the base_url or url should be a valid url string")

        elif self._base_url is None:
            self._webdriver.get(url)

        elif url is None:
            self._webdriver.get(self._base_url)

        else:
            self._webdriver.get(self._base_url + url)

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, new_url):
        self._base_url = new_url

    @property
    def title(self):
        return self._webdriver.title

    def _is_loaded_helper(self, element_locator):
        try:
            WebDriverWait(self._webdriver, 10, 1).until(visibility_of_element_located(element_locator))
            return True

        except TimeoutException:
            return False

    def is_loaded(self):
        """A method that would determine if the current page object is visible on the browser
            :returns: True if the page is load, False otherwise
        """
        raise NotImplemented("This method needs to be implemented in the specific page object instance")

    def find_element(self, locator, context=None):
        if context:
            return context.find_element(*locator)

        return self._webdriver.find_element(*locator)

    def find_multi_elements(self, locator, context=None):
        if context:
            return context.find_element(*locator)
        return self._webdriver.find_element(*locator)

    def click_element(self, locator):
        self.find_element(*locator).click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

