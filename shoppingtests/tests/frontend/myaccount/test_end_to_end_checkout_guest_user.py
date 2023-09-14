import pytest
from shoppingtests.src.pages.pagelocators.HomePage import HomePage
@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:
    @pytest.mark.tf3
    def test_end_to_end_checkout_guest_user(self):
        home_page = HomePage(self.driver)
        home_page.go_to_homepage()


        # click add to cart

        # click cart
        # add coupon
        # click submit order
        # verify order is placed



