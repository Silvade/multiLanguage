import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    addButtons = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    countOfAddButtons = len(addButtons)
    assert countOfAddButtons == 1, f'Expected one of add to basket button, but found {countOfAddButtons} buttons.'
