from shoppingtests.src.pages.pagelocators.MyAccountSignedOutLocators import MyAccountSignedOutLocator

from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers

from shoppingtests.src.configs.hosts_config import MainConfigs
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):


    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumHelpers(self.driver)

    def go_to_my_account(self):
        url = MainConfigs.get_base_url()
        endpoint = "/my-account/"
        my_account_url = url + endpoint
        logger.info(f"Getting into my {my_account_url}")
        self.driver.get(my_account_url)


    def input_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME, username)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)


    def click_login(self):
        logger.debug("clicking login button")
        self.sl.wait_and_click(self.CLICK_LOGIN)

    def click_register(self):
        logger.debug("clicking register button")
        self.sl.wait_and_click(self.CLICK_REGISTER)

    def wait_till_error_displayed(self, exp_err):
        self.sl.wait_until_error_is_displayed(self.ERROR_DISPLAYED, exp_err)
