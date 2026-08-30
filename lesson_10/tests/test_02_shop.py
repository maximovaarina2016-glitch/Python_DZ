import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.shop_page import MainShopPage, CartPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура: запускает Firefox, настраивает окно и закрывает браузер после теста.

    :yield: Экземпляр веб-драйвера.
    """
    drv = webdriver.Firefox()
    drv.implicitly_wait(3)
    drv.maximize_window()
    yield drv
    drv.quit()


@allure.title("Полная покупка трех товаров в магазине SauceDemo")
@allure.description("""
Тест-кейс имитирует стандартный пользовательский сценарий покупки:
1. Авторизация под стандартным пользователем.
2. Добавление трех разных товаров в корзину.
3. Переход в корзину и начало процедуры Checkout.
4. Ввод данных доставки.
5. Проверка корректности расчета итоговой суммы ($58.29).
6. Завершение заказа и проверка статуса успешной покупки.
""")
@allure.feature("E-commerce: Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_full_purchase_flow(driver):
    """
    Энд-ту-энд тест процесса покупки от логина до подтверждения заказа.
    """
    shop_page = MainShopPage(driver)

    with allure.step("Шаг 1: Авторизация"):
        shop_page.open_profile_page()
        shop_page.authorization("standard_user", "secret_sauce")

    with allure.step("Шаг 2: Добавление товаров в корзину"):
        shop_page.add_products_to_cart()

    with allure.step("Шаг 3: Переход в корзину и инициализация чекаута"):
        cart_page = shop_page.go_to_cart()
        # Явное ожидание кликабельности кнопки оформления (Explicit Wait)
        WebDriverWait(cart_page.driver, 10).until(
            EC.element_to_be_clickable(CartPage.CHECKOUT_BUTTON)
        ).click()

    with allure.step("Шаг 4: Заполнение данных доставки"):
        cart_page.fill_checkout_form("Arina", "Yudushkina", "173501")
        cart_page.continue_to_overview()

    with allure.step("Шаг 5: Проверка итоговой суммы"):
        actual_total = cart_page.get_total_text()
        assert (
            actual_total == "Total: $58.29"
        ), f"Ожидалось 'Total: $58.29', но получено '{actual_total}'"

    with allure.step("Шаг 6: Завершение заказа"):
        cart_page.finish_order()
        assert cart_page.is_order_complete(), "Заказ не был успешно завершен."
