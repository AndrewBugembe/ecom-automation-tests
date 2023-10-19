from selenium.webdriver.common.by import By

class HomePageLocator:

   ADD_TO_CART_BTN = (By.CSS_SELECTOR, "a.add_to_cart_button")
   PRODUCT_NAME = (By.CSS_SELECTOR, "ul.products li.product")
   SITE_HEADING = (By.CSS_SELECTOR, "header.woocommerce-products-header h1.page-title")
   MENU_LIST = (By.CSS_SELECTOR, "div.menu ul.nav-menu li")
   DROPDOWN_BTN = (By.CSS_SELECTOR, "#main > div:nth-child(2) > form > select")