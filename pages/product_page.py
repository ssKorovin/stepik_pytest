from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def go_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.GO_TO_BASKET)
        basket.click()

    def is_correct_book(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert book_name == ""

    def is_product_page(self):
        assert self.browser.current_url != "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019", "Not product page!"