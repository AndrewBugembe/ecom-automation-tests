from selenium.webdriver.common.by import By

class CartPageLocator:

    VIEW_PRODUCTS_IN_CART = (By.CSS_SELECTOR, "tr.cart_item td.product-name")
    ADD_COUPON = (By.ID, "coupon_code")
    CLICK_ADD_COUPON_BTN = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.checkout-button')
    # tr.cart_item td.product-name