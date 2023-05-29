from shoppingtests.src.pages.pagelocators.MyAccountLocators import MyAccountSignedOutLocator

from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.helpers.url_helper import base_url


class MyAccountSignedOut(MyAccountSignedOutLocator):
    # endpoint = "/my-account/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumHelpers(self.driver)

    def go_to_my_account(self):
        url = base_url()
        my_account_url = url + "/my-account/"
        self.driver.get(my_account_url)

    def input_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME, username)



    def input_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)



    def click_login(self):
        self.sl.wait_and_click(self.CLICK_LOGIN)
