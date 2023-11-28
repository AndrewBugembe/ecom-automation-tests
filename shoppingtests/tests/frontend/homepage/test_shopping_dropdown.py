import pytest
from shoppingtests.src.pages.pagelocators.HomePage import HomePage
from shoppingtests.src.pages.pagelocators.CartPage import CartPage

@pytest.mark.usefixtures("init_driver")
class TestShoppingDropdown:
    @pytest.mark.tf10
    def test_shopping_dropdown_displayed_on_home_page(self):
        # go to home page
        home_page = HomePage(self.driver)
        home_page.go_to_homepage()

        # locate the dropdown
        home_page.verify_shopping_dropdown_displayed()

    @pytest.mark.tf11
    def test_shopping_dropdown_displayed_on_cart_page(self):
        # go to cart page
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart_page()

        # locate the dropdown
        cart_page.verify_dropdown_btn_is_not_displayed()
