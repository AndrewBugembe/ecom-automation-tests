from shoppingtests.src.pages.pagelocators.OrderReceivedPageLocator import OrderReceivedLocator
from shoppingtests.src.pages.pagelocators.seleniumlocator import SeleniumHelpers
class OrderReceived(OrderReceivedLocator):
    def __init__(self, driver):
        self.sl = SeleniumHelpers(driver)

    def get_order_received_confirmation(self):
        self.sl.wait_until_element_contains_text(self.ORDER_RECEIVED_NOTIFICATION, "Order received")

    def verify_order_number(self):
        self.sl.wait_and_get_text(self.GET_ORDER_NUM)