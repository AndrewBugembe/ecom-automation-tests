import pytest
from shoppingtests.src.pages.pagelocators.HomePage import HomePage
@pytest.mark.usefixtures("init_driver")
class TestShoppingDropdown:
    @pytest.mark.tf10
    def test_shopping_dropdown_displayed(self):
        # go to home page
        home_page = HomePage(self.driver)
        home_page.go_to_homepage()

        # locate the dropdown
        home_page.verify_shopping_dropdown_displayed()

