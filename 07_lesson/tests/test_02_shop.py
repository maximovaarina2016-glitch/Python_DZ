import pytest
from selenium import webdriver
from pages.shop_page import MainShopPage
from pages.shop_page import CartPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()
def test_shop(driver):
    shop_page = MainShopPage(driver, "https://www.saucedemo.com/")
    shop_page.authorization("standard_user", "secret_sauce")
    shop_page.get_add_product()
    cart_page = CartPage(driver, "")
    cart_page.get_checkout()
    cart_page.get_form("Arina", "Yudushkina", "173501")
    cart_page.get_continue()
    total_text = cart_page.get_result()
    assert total_text == "Total: $58.29"