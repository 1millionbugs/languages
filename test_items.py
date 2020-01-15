import time
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_cart_presented(browser):
    browser.get(link)
    time.sleep(30)
    button_add_to_cart = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert button_add_to_cart, \
        f"Button add to cart is not presented"