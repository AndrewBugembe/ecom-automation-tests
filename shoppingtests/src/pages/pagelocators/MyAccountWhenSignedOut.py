from shoppingtests.src.pages.pagelocators.MyAccountLocators import MyAccountSignedOutLocator

from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.helpers.url_helper import base_url
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):
    # endpoint = "/my-account/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumHelpers(self.driver)

    def go_to_my_account(self):
        url = base_url()
        my_account_url = url + "/my-account/"
        logger.info(f"Geting into my {my_account_url}")
        self.driver.get(my_account_url)


    def input_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME, username)


    def input_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)


    def click_login(self):
        logger.debug("we been debugging")
        self.sl.wait_and_click(self.CLICK_LOGIN)

    def wait_till_error_displayed(self, exp_err):
        self.sl.wait_until_error_is_displayed(self.ERROR_DISPLAYED, exp_err)
