from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.pages.pagelocators.BannerLocators import BannerLocator

class Banner(BannerLocator):
    def __init__(self, driver):
        self.sl = SeleniumHelpers(driver)

    def verify_discount_banner_displayed(self):
        self.sl.wait_until_element_is_visible(self.DISCOUNT_BANNER)

    def verify_discount_banner_is_not_displayed(self):
        try:
            self.verify_discount_banner_displayed()
            raise Exception("The discount banner is displayed yet it should not be")
        except:
            pass


