from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation(driver):
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    sleep(3)

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form").click()

    assert (
        "/forms/post" in driver.current_url
    ), "URL не изменился на /forms/post"

    driver.back()
    sleep(5)

    assert (
        driver.current_url - -"https://httpbin.org/"
    ), "Не удалось вернуться на исходный URL"
    sleep(3)

    driver.quit()
