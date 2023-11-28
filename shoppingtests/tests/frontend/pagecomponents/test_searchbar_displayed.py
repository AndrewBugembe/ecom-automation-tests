import pytest
from shoppingtests.src.pages.pagelocators.HomePage import HomePage
from shoppingtests.src.pages.pagelocators.CartPage import CartPage
from shoppingtests.src.pages.pagelocators.CheckoutPage import CheckoutPage
from shoppingtests.src.pages.pagelocators.SearchBar import SearchBar
@pytest.mark.usefixtures("init_driver")
class TestSearchBar:
    @pytest.mark.tf12
    def test_verify_search_bar_displayed_on_home_page(self):
        # go to home page
        home_page = HomePage(self.driver)
        home_page.go_to_homepage()

        # verify search bar is displayed
        home_page.verify_search_bar_displayed()

    @pytest.mark.tf13
    def test_verify_search_bar_displayed_on_cart_page(self):
        # go to cart page
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart_page()

        # verify search  bar is displayed
        search_bar = SearchBar(self.driver).verify_search_bar_displayed()

    @pytest.mark.tf14
    def test_verify_search_bar_displayed_on_checkout_page(self):

        # go to checkout page
        checkout = CheckoutPage(self.driver)
        checkout.go_to_checkout_page()

        # verify search bar is displayed
        search_bar = SearchBar(self.driver).verify_search_bar_displayed()
