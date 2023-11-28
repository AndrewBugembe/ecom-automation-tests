from selenium.webdriver.common.by import By

class CartPageLocator:

    VIEW_PRODUCTS_IN_CART = (By.CSS_SELECTOR, "tr.cart_item td.product-name")
    ADD_COUPON = (By.ID, "coupon_code")
    CLICK_ADD_COUPON_BTN = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.checkout-button')
    DROPDOWN_BTN = (By.CSS_SELECTOR, "#main > div:nth-child(2) > form > select")
    SEARCH_BAR = (By.ID, 'woocommerce-product-search-field-0')