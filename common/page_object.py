# A common base page object to be used by all the page object
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
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

        # if only the url is present then go to that url
        elif self._base_url is None:
            self._webdriver.get(url)

        # only base url is present, go to the base url
        elif url is None:
            self._webdriver.get(self._base_url)

        # both are present, combine then and then go to that url
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
        """A helper method that determines if a pages is loaded based on the presence of an element

            :param element_locator: the element locator, this should be some pivotal element in that page
            :return True: if the page is loaded, i.e. element is found and visible. False otherwise
        """
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
        """Find an element , will filter out only those that are actually visible by the user

            :param locator: a selenium locator that can be used to find the element, e.g. (By.ID, "some_id")
            :param context: can be used if user needs to find a nested element. in that case pass in the element
                    as a context, if left as None, the method will just use the webdriver ( top of the html tree )
                    to find the element

            :return WebElement: if there is atleast one displayed element matching locator pattern. If there are more
                    than one, then method will return the first.
                    If no elements are found, or none are displayed, the method will return None.
        """
        elements = self.find_multi_elements(locator=locator, context=context)

        # return only the menu that is displayed and enabled, i.e. one that is actually clickable
        for element in elements:
            try:
                # return the first element that is displayed and is enabled.
                if element.is_displayed() and element.is_enabled():
                    return element
            except StaleElementReferenceException:
                pass

        # either no user menu elements were found at all, or none were clickable
        return None

    def find_multi_elements(self, locator, context=None):
        """Find a list of elements with same locator within this page
            :param locator: a selenium web element locator, of the format (By.<locator_type>, "search pattern")
            :param context: if a context is passed, find_element will use the context to find the element within it.
                    This is useful if the page needs to use a web element as a context to find a nested element for
                    example.
            :returns: the list of the matching web elements. note if no match is found , the function will return
                        an empty list
        """
        if context is None:
            context = self._webdriver

        return context.find_elements(*locator)

    def click_element(self, locator, context=None):
        """find the element then click it"""
        if context is None:
            context = self._webdriver

        # wait until element is clickable before attempting to click
        WebDriverWait(context, 5, 0.5).until(element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text, context=None):
        """Find an editable element and change the text"""
        element = self.find_element(locator=locator, context=context)
        # clear first then send the new text
        element.clear()
        element.send_keys(text)

