from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.pages.pagelocators.BannerLocators import BannerLocator

class Banner(BannerLocator):
    def __init__(self, driver):
        self.sl = SeleniumHelpers(driver)

    def verify_discount_banner_displayed(self):
        self.sl.wait_until_element_is_visible(self.DISCOUNT_BANNER)