import pytest
from shoppingtests.src.pages.pagelocators.MyAccountWhenSignedOutPage import MyAccountSignedOut

@pytest.mark.usefixtures('init_driver')
class TestLoginNegative:

    @pytest.mark.tf1
    def test_login_user_not_registered(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_username('lllllll')
        my_account.input_password('jhgfddss')
        my_account.click_login()
        error = "Error: The username lllllll is not registered on this site. If you are unsure of your username, try your email address instead."
        my_account.wait_till_error_displayed(error)
