import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = "https://the-internet.herokuapp.com/dynamic_loading/2"
driver.get(url)

    
start_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
)
start_button.click()

   
hello_world_element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "finish"))
)
    

actual_text = hello_world_element.text.strip()


if actual_text == "Hello World!":
    print("Проверка пройдена: Текст совпадает.")
else:
    print(f"Проверка провалена: Ожидалось 'Hello World!', получено '{actual_text}'")


screenshot_path = "screenshot_dynamic_loading.png"
driver.save_screenshot(screenshot_path)
print(f"Скриншот сохранен как {screenshot_path}")

time.sleep(2)

driver.quit()
