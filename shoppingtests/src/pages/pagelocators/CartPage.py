from shoppingtests.src.pages.pagelocators.CartPageLocator import CartPageLocator
from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
from shoppingtests.src.configs.hosts_config import MainConfigs
class CartPage(CartPageLocator):
    endpoint = '/cart'
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumHelpers(driver)


    def go_to_cart_page(self):

        base_url = MainConfigs.get_base_url()
        cart_url = base_url + self.endpoint
        self.driver.get(cart_url)

    def get_product_names_in_cart(self):
        products_in_cart = self.sl.wait_and_get_elements(self.VIEW_PRODUCTS_IN_CART)

        product_names = [i.text for i in products_in_cart]
        return product_names

    def add_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.ADD_COUPON, str(coupon_code))

    def click_add_coupon_btn(self):
        self.sl.wait_and_click(self.CLICK_ADD_COUPON_BTN)

    def apply_coupon(self, coupon_code):
        self.add_coupon(coupon_code)
        self.click_add_coupon_btn()

    def click_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)

    def verify_search_bar_displayed(self, text=None):
        text = 'beanie' if not text else text
        self.sl.wait_and_input_text(self.SEARCH_BAR, text)

    def verify_dropdown_btn_is_not_displayed(self):
        # drop_down = 'Default sorting' if not drop_down else drop_down
        # assert not self.sl.wait_and_select_dropdown(self.DROPDOWN_BTN, to_select=drop_down, select_by="visible_text")
        assert not self.sl.wait_until_element_is_visible(self.DROPDOWN_BTN)


