from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button[value='Добавить в корзину']")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    GO_TO_BASKET = (By.CSS_SELECTOR, "a[class='btn btn-default']")