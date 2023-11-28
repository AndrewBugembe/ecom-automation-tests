from selenium.webdriver.common.by import By

class HeaderLocator:

    CART_VIEW_COUNT = (By.CSS_SELECTOR, "count")
    CART_RIGHT_HEADER_ICON = (By.ID, "site-header-cart")
    CART_TITLE = (By.CSS_SELECTOR, "#post-7 > header > h1")
    # site - header - cart
    # cart - contents

