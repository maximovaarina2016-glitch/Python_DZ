from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get("https://www.gitflic.ru/")

    # Karoline_max
    # kJDXZjr!Zmn4TT6

user1 = driver.add_cookie(
{
    "name": "SESSION",
    "value": "ZDg1NGJhNWQtMmU2Zi00OGY2LWJhMWItN2Y3MDYzZmUxYzEy",
    "domain": "gitflic.ru",
}
)

driver.add_cookie(
    {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
)

driver.refresh()

driver.maximize_window()
driver.get("https://gitflic.ru/user/karoline_max")
sleep(2)

url_user1 = driver.current_url

driver.delete_all_cookies()
driver.refresh()

    # Arina_yudushkina
    # CQ7-mFizBD79Qx5
user2 = driver.add_cookie(
    {
        "name": "SESSION",
        "value": "MWM0NTdjOWEtZDRmMS00YWZhLWI4ZTctNDhjYjcyNzk2OTA0",
        "domain": "gitflic.ru",
    }
)

driver.add_cookie(
    {"name": "cookiesAccepted", "value": "true", "domain": "gitflic.ru"}
)

driver.refresh()

driver.get("https://gitflic.ru/user/arina_yudushkina")
sleep(2)

url_user2 = driver.current_url

assert url_user1 != url_user2

driver.quit()
