from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    options = Options()
    driver = webdriver.Firefox(options=options)

    try:
        driver.get("http://www.saucedemo.com/")
        driver.maximize_window()
        user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
        user_name.send_keys("standard_user")
        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.send_keys("secret_sauce")
        login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
        login_button.click()

        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "add-to-cart-sauce-labs-backpack")
            )
        )

        backpack = driver.find_element(
            By.NAME, "add-to-cart-sauce-labs-backpack"
        )
        backpack.click()
        shirt = driver.find_element(
            By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        shirt.click()
        onesie = driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie")
        onesie.click()
        shopping_cart_container = driver.find_element(
            By.ID, "shopping_cart_container"
        )
        shopping_cart_container.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        wait.until(EC.element_to_be_clickable((By.ID, "first-name")))

        first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.send_keys("Arina")
        last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.send_keys("Yudushkina")
        postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal_code.send_keys("173051")
        continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
        continue_button.click()

        total_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_text = total_element.text
        print(f"Получена итоговая стоимость: {total_text}")

    except AssertionError as e:
        print(f"\n Ошибка проверки {e}")
        raise

    finally:
        driver.quit()
