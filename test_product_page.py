from pages.base_page import BasePage
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.is_product_page()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.go_to_basket()
    browser.implicitly_wait(10000)