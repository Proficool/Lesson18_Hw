from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

def test_dropdown():
    # Настройка WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    try:
        # Открываем сайт
        driver.get("http://omayo.blogspot.com/")

        # Находим выпадающий список с ID "drop1"
        dropdown = Select(driver.find_element(By.ID, "drop1"))

        # Выбираем опцию "doc 3"
        dropdown.select_by_visible_text("doc 3")

        # Проверяем, что выбранная опция действительно установлена на "doc 3"
        selected_option = dropdown.first_selected_option
        assert selected_option.text == "doc 3", f"Expected 'doc 3', but got '{selected_option.text}'"
        print("Test passed")

    finally:
        # Закрываем браузер
        driver.quit()

# Вызов функции
test_dropdown()