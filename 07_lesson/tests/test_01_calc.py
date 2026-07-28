import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


# Фикстура: запускает Chrome, возвращает driver и закрывает после теста.
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    # 1. Открываем страницу:
    # https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    # в Google Chrome.

def test_calculator(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    calc_page = CalculatorPage(driver, url)
    calc_page.open()
    calc_page.set_delay()
    calc_page.enter_expression()
    calc_page.get_result()
    assert calc_page.get_result() == "15"