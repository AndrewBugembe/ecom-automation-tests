import pytest
from shoppingtests.src.pages.pagelocators.MyAccountWhenSignedOutPage import MyAccountSignedOut
from shoppingtests.src.pages.pagelocators.MyAccountWhenSignedInPage import MyAccountSignedIn
from shoppingtests.src.utilities.genericUtilities import get_random_email_password


@pytest.mark.usefixtures('init_driver')
class TestNewUser:

    @pytest.mark.tf2
    def test_register_new_user(self):
        # go to my account page
        random_info = get_random_email_password()
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        user_registered = MyAccountSignedIn(self.driver)


        # fill in the username
        my_account.input_register_email(random_info['email'])

        # fill in password
        my_account.input_register_password(random_info['password'])

        # click submit
        my_account.click_register()

        # verify registration successful message
        user_registered.verify_user_is_signed_in()



