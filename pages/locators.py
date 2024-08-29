from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn.btn-default:nth-child(1)")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    MASSAGES = (By.CSS_SELECTOR, ".alert")
    CORRECT_PRODUCT_NAME = (By.TAG_NAME, "h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    CORRECT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")


class BasketPageLocators:
    INSCRIPTION_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
