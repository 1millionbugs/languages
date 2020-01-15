import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_cart_presented(browser):
    browser.get(link)
    time.sleep(30)
    button_add_to_cart = len(browser.find_elements(By.CSS_SELECTOR, "button[type='submit']"))
    assert button_add_to_cart > 0, "Button add to cart is not presented"