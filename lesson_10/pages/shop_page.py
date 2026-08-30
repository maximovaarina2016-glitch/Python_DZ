from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainShopPage:
    """
    Page Object Model для главной страницы магазина SauceDemo.
    """

    BASE_URL = "https://www.saucedemo.com/"
    LOGIN_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    ADD_sauce_labs_backpack_BUTTON = (
        By.NAME,
        "add-to-cart-sauce-labs-backpack",
    )
    ADD_sauce_labs_bolt_t_shirt_BUTTON = (
        By.NAME,
        "add-to-cart-sauce-labs-bolt-t-shirt",
    )
    ADD_to_cart_sauce_labs_onesie_BUTTON = (
        By.NAME,
        "add-to-cart-sauce-labs-onesie",
    )

    # Список локаторов товаров для массового добавления в корзину
    PRODUCTS_TO_ADD = [
        ADD_sauce_labs_backpack_BUTTON,
        ADD_sauce_labs_bolt_t_shirt_BUTTON,
        ADD_to_cart_sauce_labs_onesie_BUTTON,
    ]

    def __init__(self, driver):
        """
        Инициализация объекта главной страницы.

        :param driver: Экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Открыть главную страницу магазина")
    def open_profile_page(self) -> None:
        """
        Открывает URL целевой страницы.

        :return: None
        """
        self.driver.get(self.BASE_URL)

    @allure.step("Авторизоваться пользователем {username}")
    def authorization(
        self, username: str = "standard_user", password: str = "secret_sauce"
    ) -> "MainShopPage":
        """
        Выполняет ввод учетных данных и нажатие кнопки входа.

        :param username: Логин пользователя.
        :param password: Пароль пользователя.
        :return: Экземпляр текущей страницы после авторизации.
        """
        login_input = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_INPUT)
        )
        login_input.send_keys(username)

        password_input = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD_INPUT)
        )
        password_input.send_keys(password)

        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()
        return self

    @allure.step("Добавить товары из списка в корзину")
    def add_products_to_cart(self) -> "MainShopPage":
        """
        Последовательно нажимает на кнопки добавления каждого товара из PRODUCTS_TO_ADD.

        :return: Экземпляр текущей страницы.
        """
        for locator in self.PRODUCTS_TO_ADD:
            with allure.step(
                f"Нажать кнопку добавления товара по локатору {locator}"
            ):
                self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    @allure.step("Перейти в корзину покупок")
    def go_to_cart(self) -> "CartPage":
        """
        Нажимает на иконку корзины и возвращает объект страницы корзины.

        :return: Объект класса CartPage.
        """
        cart_btn = (By.ID, "shopping_cart_container")
        self.wait.until(EC.element_to_be_clickable(cart_btn)).click()
        from .shop_page import CartPage

        return CartPage(self.driver)


class CartPage:
    """
    Page Object Model для страницы корзины и оформления заказа.
    """

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
        """
        Инициализация объекта страницы корзины.

        :param driver: Экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step(
        "Заполнить форму оформления данными: {first_name} {last_name}, {postal_code}"
    )
    def fill_checkout_form(
        self,
        first_name: str = "Arina",
        last_name: str = "Yudushkina",
        postal_code: str = "173501",
    ) -> "CartPage":
        """
        Заполняет поля формы оформления заказа.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс.
        :return: Экземпляр текущей страницы.
        """
        first_name_input = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_NAME_INPUT)
        )
        first_name_input.clear()
        first_name_input.send_keys(first_name)

        last_name_input = self.wait.until(
            EC.element_to_be_clickable(self.LAST_NAME_INPUT)
        )
        last_name_input.clear()
        last_name_input.send_keys(last_name)

        postal_code_input = self.wait.until(
            EC.element_to_be_clickable(self.POSTAL_CODE_INPUT)
        )
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)
        return self

    @allure.step("Нажать кнопку Continue")
    def continue_to_overview(self) -> "CartPage":
        """
        Переходит на экран обзора заказа.

        :return: Экземпляр текущей страницы.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()
        return self

    @allure.step("Завершить оформление заказа")
    def finish_order(self) -> "CartPage":
        """
        Подтверждает заказ на финальном экране.

        :return: Экземпляр текущей страницы.
        """
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()
        return self

    @allure.step("Получить текст итоговой суммы")
    def get_total_text(self) -> str:
        """
        Возвращает текстовое значение общей стоимости заказа.

        :return: Строка вида 'Total: $XX.XX'.
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_VALUE)
        )
        return total_element.text

    @allure.step("Проверить соответствие итоговой суммы ожидаемой")
    def verify_total_amount(self) -> "CartPage":
        """
        Проверяет через ожидание, что в элементе отображается ожидаемая сумма.

        :return: Экземпляр текущей страницы.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.TOTAL_VALUE, self.EXPECTED_TOTAL
            )
        )
        return self

    @allure.step("Проверить наличие сообщения об успешном завершении заказа")
    def is_order_complete(self) -> bool:
        """
        Проверяет наличие подтверждающего текста на странице завершения.

        :return: True, если сообщение найдено, иначе False.
        """
        header = self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        )
        return "Thank you for your order!" in header.text
