
from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.configs.hosts_config import MainConfigs

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumHelpers(driver)
    def go_to_homepage(self):
        base_url = MainConfigs.get_base_url()
        self.driver.get(base_url)