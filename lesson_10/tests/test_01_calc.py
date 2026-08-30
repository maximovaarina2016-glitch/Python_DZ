import pytest
import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """
    Фикстура инициализации драйвера.

    Запускает браузер Chrome перед тестом и закрывает его после завершения.

    Yields:
        webdriver.Chrome: Активный экземпляр браузера.
    """
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()


@allure.title("Проверка работы медленного калькулятора")
@allure.description("""
Тест проверяет корректность сложения чисел при наличии искусственной задержки.
Шаги теста:
1. Установка задержки обработки запросов на 45 секунд.
2. Ввод математического выражения '7 + 8 ='.
3. Проверка того, что итоговый результат равен '15'.
""")
@allure.feature("Функциональное тестирование UI")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    """Основной сценарий тестирования функционала калькулятора."""
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    calc_page = CalculatorPage(driver, url)

    calc_page.open()
    calc_page.set_delay()
    calc_page.enter_expression()

    with allure.step("Проверить, что полученный результат равен '15'"):
        assert calc_page.get_result() == "15"
