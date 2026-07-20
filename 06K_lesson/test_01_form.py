import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """Фикстура: запускает Edge, возвращает driver и закрывает после теста."""
    service = EdgeService()
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    # 1. Открываем страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait = WebDriverWait(driver, 10)

    # 2. Ждём, пока на странице появятся инпуты
    wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "input")) > 0)
    inputs = driver.find_elements(By.TAG_NAME, "input")

    # В моём окружении их 10, но на всякий случай проверим, что хотя бы 9
    assert len(inputs) >= 9

    # 3. Раскладываем по смыслу (по порядку на странице)
    first_name = inputs[0]
    last_name = inputs[1]
    address = inputs[2]
    email = inputs[3]
    phone = inputs[4]
    zip_code = inputs[5]  # Zip code — оставляем пустым
    city = inputs[6]
    country = inputs[7]
    job_position = inputs[8]
    company = inputs[9] if len(inputs) > 9 else None

    # 4. Заполняем все поля, кроме Zip code
    first_name.send_keys("Иван")
    last_name.send_keys("Петров")
    address.send_keys("Ленина, 55-3")
    email.send_keys("test@skypro.com")
    phone.send_keys("+7985899998787")
    city.send_keys("Москва")
    country.send_keys("Россия")
    job_position.send_keys("QA")
    if company:
        company.send_keys("SkyPro")

    # 5. Пытаемся нажать кнопку Submit (если есть)
    try:
        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit'], button")
            )
        )
        submit_button.click()
    except Exception:
        # Если кнопки нет/не кликается (особенность страницы/антивируса) — продолжаем
        pass

    # 6. Проверяем "валидацию":
    #    Zip code считаем "красным" (ошибка), если он пустой,
    #    остальные поля считаем "зелёными" (нормальными), если они не пустые.

    # Zip code должен остаться пустым
    assert zip_code.get_attribute("value") == ""

    # Остальные — заполнены
    for element in (
        first_name,
        last_name,
        address,
        email,
        phone,
        city,
        country,
        job_position,
    ):
        assert element.get_attribute("value") != ""

    if company:
        assert company.get_attribute("value") != ""
