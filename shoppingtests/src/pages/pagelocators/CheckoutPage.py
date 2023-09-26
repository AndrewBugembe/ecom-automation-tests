from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.pages.pagelocators.CheckoutLocator import CheckoutLocator

class Checkout(CheckoutLocator):
    def __init__(self, driver):
        self.sl = SeleniumHelpers(driver)

    def click_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)