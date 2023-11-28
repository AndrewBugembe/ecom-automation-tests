import pytest
from shoppingtests.src.pages.pagelocators.HomePage import HomePage

@pytest.mark.usefixtures("init_driver")
class TestWebsiteTitle:
    @pytest.mark.tf16
    def test_website_title_displayed_on_home_page(self):
        # go to home page
        home_page = HomePage(self.driver)
        home_page.go_to_homepage()

        # locate website title
        expected_heading = 'shopping'
        displayed_heading = home_page.verify_website_title_displayed()

        # verify expected website title is displayed
        assert displayed_heading == expected_heading, \
            f"Displayed website title on home page is not as expected. " \
        f"Expected: {expected_heading}, Actual: {displayed_heading}"



