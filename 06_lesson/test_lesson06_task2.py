from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_lesson06_task2():

    driver = webdriver.Chrome()

    driver.get("https://www.gitflic.ru/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "footer"))
    )

    # Karoline_max
    # kJDXZjr!Zmn4TT6

user1 = driver.add_cookie
    ({
        "name": "SESSION",
        "value": "MTI2NzQzMGEtNTAxYi00ZjAxLWI4YzAtMTBlZWY5MjFlZTg2",
        "domain": "gitflic.ru",
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.get("https://gitflic.ru/user/karoline_max")
    user1_header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".user-profile__name"))
    )
    url_user1 = driver.current_url
    print(f"Первый пользователь загружен: {url_user1}")

    driver.delete_all_cookies()
    driver.refresh()

    driver.get("https://www.gitflic.ru/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "footer"))
    )

    # Arina_yudushkina
    # CQ7-mFizBD79Qx5
    user2 = driver.add_cookie({
        "name": "SESSION",
        "value": "MWM0NTdjOWEtZDRmMS00YWZhLWI4ZTctNDhjYjcyNzk2OTA0",
        "domain": "gitflic.ru",
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.get("https://gitflic.ru/user/arina_yudushkina")

    user2_header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".user-profile__name"))
    )

    url_user2 = driver.current_url
    print(f"Второй пользователь загружен: {url_user2}")

    if url_user1 != url_user2 and "karoline_max" in url_user1 and "arina_yudushkina" in url_user2:
        assert True
        print("Проверка пройдена: открыты страницы разных пользователей.")
    else:
        raise AssertionError(f"Проверка провалена. URL1: {url_user1}, URL2: {url_user2}")

    driver.quit()
