from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainShopPage:
    BASE_URL = "https://www.saucedemo.com/"
    LOGIN_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    ADD_sauce_labs_backpack_BUTTON =(
        By.NAME, 'add-to-cart-sauce-labs-backpack')
    ADD_sauce_labs_bolt_t_shirt_BUTTON =(
            By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_to_cart_sauce_labs_onesie_BUTTON =(
            By.NAME, "add-to-cart-sauce-labs-onesie")
    
    def __init__(self, driver):
        self.driver.get = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_profile_page(self):
        self.driver.get(self.BASE_URL)

    def authorization (self, username="standard_user", password="secret_sauce"):
        login_input = self.wait.until(EC.element_to_be_clickable(
            self.LOGIN_INPUT
        ))
        login_input.send_keys(username)

        password_input = self.wait.until(EC.element_to_be_clickable(
            self.PASSWORD_INPUT
        ))
        password_input.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable(
            self.LOGIN_BUTTON
        ))
        login_button.click()
        return self
    
    def add_products_to_cart(self):
        for locator in self.PRODUCTS_TO_ADD:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def go_to_cart(self):
        cart_btn = (By.ID, "shopping_cart_container")
        self.wait.until(EC.element_to_be_clickable(cart_btn)).click()
        from .cart_page import CartPage
        return CartPage(self.driver)
    
class CartPage:
    SHOPPING_CART_BUTTON = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    TOTAL_VALUE = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    EXPECTED_TOTAL = "Total: $58.29"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_checkout_form(self, first_name="Arina", last_name="Yudushkina", postal_code="173501"):
        first_name_input = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT))
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_INPUT))
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        postal_code_input = self.wait.until(EC.element_to_be_clickable(self.POSTAL_CODE_INPUT))
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)
        return self

    def continue_to_overview(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()
        return self

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()
        return self

    def get_total_text(self):
        total_element = self.wait.until(EC.visibility_of_element_located(self.TOTAL_VALUE))
        return total_element.text

    def verify_total_amount(self):
        self.wait.until(
            EC.text_to_be_present_in_element(self.TOTAL_VALUE, self.EXPECTED_TOTAL)
        )
        return self

    def is_order_complete(self):
        header = self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))
        return "Thank you for your order!" in header.text