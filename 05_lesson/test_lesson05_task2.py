from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    driver.maximize_window()
    # Заполнение поля "custname" значением "Arina"
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Arina")
    previous_url = driver.current_url
    # Поиск кнопки отправки и клик на неё
    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_btn.click()

    # Проверка изменения URL после нажатия
    new_url = driver.current_url
    assert new_url != previous_url, "URL не изменился после отправки формы"

    driver.quit()
