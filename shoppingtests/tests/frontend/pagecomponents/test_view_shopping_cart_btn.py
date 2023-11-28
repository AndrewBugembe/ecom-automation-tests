
import pytest
from shoppingtests.src.pages.pagelocators.HomePage import HomePage
from shoppingtests.src.pages.pagelocators.Header import Header

@pytest.mark.usefixtures("init_driver")
class TestViewCartBtn:
    @pytest.mark.tf15
    def test_view_cart_btn_on_home_page(self):
        home_page = HomePage(self.driver)
        home_page.go_to_homepage()

        # locate and click button
        home_page.verify_cart_btn_displayed()

        # verify button clicked
        cart_title = Header(self.driver)
        cart_title.verify_cart_title_displayed()

        # assert text == "Cart", f"Expected text is Cart, displayed text is {text}"

