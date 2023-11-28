from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.pages.pagelocators.HeaderLocator import HeaderLocator

class Header(HeaderLocator):

    def __init__(self, driver):
        self.sl = SeleniumHelpers(driver)

    def click_cart_right_header_icon(self):
        self.sl.wait_and_click(self.CART_RIGHT_HEADER_ICON)

    def wait_until_cart_view_count(self, count):
        # expected_text = str(count) + ' item'
        self.sl.wait_until_element_contains_text(self.CART_VIEW_COUNT, str(count))

    def verify_cart_title_displayed(self):
        self.sl.wait_and_get_text(self.CART_TITLE)