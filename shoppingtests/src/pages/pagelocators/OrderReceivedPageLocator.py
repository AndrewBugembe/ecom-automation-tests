from selenium.webdriver.common.by import By

class OrderReceivedLocator:

    ORDER_RECEIVED_NOTIFICATION = (By.CSS_SELECTOR, "header h1.entry-title")
    GET_ORDER_NUM = (By.CSS_SELECTOR, "li.order strong")