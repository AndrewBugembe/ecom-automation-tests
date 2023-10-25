
from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.configs.hosts_config import MainConfigs
from shoppingtests.src.pages.pagelocators.HomePageLocators import HomePageLocator

class HomePage(HomePageLocator):
    expected_menu = ["Home", "Cart", "Checkout", "My account", "Sample Page"]
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumHelpers(driver)
    def go_to_homepage(self):
        base_url = MainConfigs.get_base_url()
        self.driver.get(base_url)

    def click_add_first_to_cart_btn(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)

    # def click_view_cart_btn(self):
    #     self.sl.wait_and_click(self.VIEW_CART_BTN)

    def get_visible_products(self):
        error_txt = "Can not get products from homepage"
        return self.sl.wait_and_get_elements(self.PRODUCT_NAME,error=error_txt)

    def verify_site_heading_displayed(self):
        return self.sl.wait_and_get_text(self.SITE_HEADING)

    def get_menu_displayed(self):
        menu_items = self.sl.wait_and_get_elements(self.MENU_LIST)
        menu_list = [ item.text for item in menu_items]
        return menu_list

    def assert_menu_displayed(self):
        displayed_menu = self.get_menu_displayed()
        for menu in self.expected_menu:
            assert menu in displayed_menu, f"{menu} is not in expected list {displayed_menu}"

    def verify_shopping_dropdown_displayed(self,drop_down=None):
        drop_down = 'Default sorting' if not drop_down else drop_down

        self.sl.wait_and_select_dropdown(self.DROPDOWN_BTN, to_select=drop_down, select_by="visible_text")
