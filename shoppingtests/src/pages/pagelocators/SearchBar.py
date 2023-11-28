from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.pages.pagelocators.SearchBarLocator import SearchBarLocator

class SearchBar(SearchBarLocator):
    def __init__(self,driver):
        self.sl = SeleniumHelpers(driver)

    def verify_search_bar_displayed(self, text=None):
        text = 'beanie' if not text else text
        self.sl.wait_and_input_text(self.SEARCH_BAR,text)
