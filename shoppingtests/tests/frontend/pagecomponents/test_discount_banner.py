import pytest
from shoppingtests.src.pages.pagelocators.HomePage import HomePage
from shoppingtests.src.pages.pagelocators.Banner import Banner
from shoppingtests.src.pages.pagelocators.CartPage import CartPage
from shoppingtests.src.pages.pagelocators.CheckoutPage import CheckoutPage

@pytest.mark.usefixtures("init_driver")
class TestDiscountBanner:
    @pytest.mark.tf7
    def test_verify_discount_banner_displayed_on_homepage(self):
        # go to home page
        HomePage(self.driver).go_to_homepage()
        # verify discount banner displayed
        Banner(self.driver).verify_discount_banner_displayed()

    @pytest.mark.tf8
    def test_verify_discount_banner_displayed_on_cart_page(self):
        # go to cart page
        CartPage(self.driver).go_to_cart_page()

        # verify discount banner displayed
        Banner(self.driver).verify_discount_banner_displayed()

    @pytest.mark.tf9
    def test_verify_discount_banner_displayed_on_checkout_page(self):
        # go to checkout page
        CheckoutPage(self.driver).go_to_checkout_page()

        # verify discount banner displayed
        Banner(self.driver).verify_discount_banner_displayed()