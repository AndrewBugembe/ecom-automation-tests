import pytest
from shoppingtests.src.pages.pagelocators.HomePage import HomePage
from shoppingtests.src.pages.pagelocators.Header import Header
from shoppingtests.src.pages.pagelocators.CartPage import CartPage
from shoppingtests.src.configs.hosts_config import MainConfigs
@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:
    @pytest.mark.tf3
    def test_end_to_end_checkout_guest_user(self):
        home_page = HomePage(self.driver)
        header = Header(self.driver)
        cart_page = CartPage(self.driver)

        # go to home page

        home_page.go_to_homepage()

        # click add to cart
        home_page.click_add_first_to_cart_btn()
        import time; time.sleep(10)

        # wait for cart view count
        # header.wait_until_cart_view_count(1)

        # click view cart
        header.click_cart_right_header_icon()

        # verify items in cart
        product_name = cart_page.get_product_names_in_cart()
        assert len(product_name) == 1, f"Expected 1 product but got {len(product_name)}"

        # add coupon
        coupon_code = MainConfigs.get_coupon_code("FREE COUPON")
        cart_page.apply_coupon(coupon_code)

        # proceed to checkout
        cart_page.click_proceed_to_checkout()

        # verify order is placed



