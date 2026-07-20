import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Константы для удобства изменения данных теста
URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
DELAY_VALUE = "45"
EXPECTED_RESULT = "15"
CALCULATOR_DELAY_SECONDS = 45
WAIT_TIMEOUT_SECONDS = CALCULATOR_DELAY_SECONDS + 60


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    wait = WebDriverWait(driver, WAIT_TIMEOUT_SECONDS)

    yield driver, wait

    driver.quit()


def test_calculator(browser):

    driver, wait = browser

    driver.get(URL)

    delay_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys(DELAY_VALUE)

    actions_data = [
        ("7", 'button[data-key="7"]'),
        ("+", 'button[data-key="+"]'),
        ("8", 'button[data-key="8"]'),
        ("=", 'button[data-key="="]'),
    ]

    for _, selector in actions_data:
        btn = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        btn.click()

    result_field_locator = (By.CSS_SELECTOR, ".screen")

    wait.until(
        EC.text_to_be_present_in_element(result_field_locator, EXPECTED_RESULT)
    )

    screen_element = wait.until_not(
        EC.invisibility_of_element_located(result_field_locator)
    )

    actual_result = screen_element.text.strip()

    driver.save_screenshot("error.png")

    assert (
        actual_result == EXPECTED_RESULT
    ), f"Проверка провалена. Ожидалось число '{EXPECTED_RESULT}', но отобразилось '{actual_result}'."
