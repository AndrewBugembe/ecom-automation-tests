import pytest
from shoppingtests.src.pages.pagelocators.HomePage import HomePage

pytestmark = [pytest.mark.homepage]

@pytest.mark.usefixtures("init_driver")
class TestProductsDisplayed:

    @pytest.fixture(scope="class")
    def setup(self, request):
        request.cls.home_page = HomePage(self.driver)
        self.home_page.go_to_homepage()
        yield
    @pytest.mark.tf4
    def test_verify_products_displayed(self, setup):

        # verify number of products
        expected_num_of_prods = 16
        displayed_products = self.home_page.get_visible_products()
        assert len(displayed_products) == expected_num_of_prods, "Unexpected number of products displayed"

    @pytest.mark.tf5
    def test_site_heading_displayed(self, setup):
        expected_heading = "Shop"
        site_heading = self.home_page.verify_site_heading_displayed()
        assert site_heading == expected_heading, f" Expected site heading should be {expected_heading}" \
                                                    f"Expected site heading displayed is {site_heading}"

    @pytest.mark.tf6
    def test_site_menu_displayed(self, setup):
        site_menu = self.home_page.assert_menu_displayed()


