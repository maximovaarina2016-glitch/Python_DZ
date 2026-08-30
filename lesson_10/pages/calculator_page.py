from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """
    Класс-обертка для страницы медленного калькулятора.

    Attributes:
        driver: Экземпляр Selenium WebDriver.
        url: URL адрес тестируемой страницы.
        wait: Явное ожидание WebDriverWait с таймаутом 45 секунд.
    """

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_VALUE = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        """
        Инициализация объекта страницы.

        Args:
            driver: Объект webdriver.Chrome().
            url: Строка с URL-адресом страницы.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 45)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает целевую страницу в текущем окне браузера.

        Returns:
            None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установить задержку вычислений равной 45 секундам")
    def set_delay(self) -> None:
        """
        Устанавливает задержку выполнения операций на странице в 45 секунд.

        Ожидает появления поля ввода, очищает его и отправляет значение "45".

        Returns:
            None
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys("45")

    @allure.step("Ввести выражение 7 + 8 =")
    def enter_expression(self) -> None:
        """
        Последовательно нажимает кнопки для выражения '7 + 8 ='.

        Returns:
            None
        """
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            xpath = f"//span[text()='{button}']"
            self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Дождаться отображения результата '15'")
    def get_result(self) -> str:
        """
        Ожидает появления результата '15' и возвращает текст из экрана калькулятора.

        Returns:
            str: Текстовое значение результата вычисления.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_VALUE, "15")
        )
        result_element = self.driver.find_element(*self.RESULT_VALUE)
        return result_element.text
