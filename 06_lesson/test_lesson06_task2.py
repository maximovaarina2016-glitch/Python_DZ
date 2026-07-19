import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    # Неявное ожидание лучше минимизировать, полагаясь на явные ожидания ниже
    yield driver
    driver.quit()


def test_lesson06_task2(browser):
    wait = WebDriverWait(browser, 10)

    # --- Блок первого пользователя ---
    browser.get("https://www.gitflic.ru/")
    
    # Ждем готовности DOM и наличия футера перед работой с куками
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

    # Устанавливаем куки авторизации
    browser.add_cookie({
        "name": "SESSION",
        "value": "MTI2NzQzMGEtNTAxYi00ZjAxLWI4YzAtMTBlZWY5MjFlZTg2",
        "domain": ".gitflic.ru",  # Точка позволяет использовать куку на субдоменах
    })
    browser.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": ".gitflic.ru",
    })

    # Переходим на страницу профиля
    browser.get("https://gitflic.ru/user/karoline_max")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".user-profile__name")))
    url_user1 = browser.current_url

    # Сбрасываем только сессию пользователя, оставляя согласие на куки
    browser.delete_cookie("SESSION")
    browser.refresh()

    # --- Блок второго пользователя ---
    browser.get("https://www.gitflic.ru/")
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

    browser.add_cookie({
        "name": "SESSION",
        "value": "MWM0NTdjOWEtZDRmMS00YWZhLWI4ZTctNDhjYjcyNzk2OTA0",
        "domain": ".gitflic.ru",
    })
    browser.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": ".gitflic.ru",
    })

    browser.get("https://gitflic.ru/user/arina_yudushkina")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".user-profile__name")))
    url_user2 = browser.current_url

    # Проверка. Сообщение об ошибке выведет pytest автоматически.
    assert (
        "karoline_max" in url_user1 and "arina_yudushkina" in url_user2
    ), f"Проверка провалена. URL1: {url_user1}, URL2: {url_user2}"