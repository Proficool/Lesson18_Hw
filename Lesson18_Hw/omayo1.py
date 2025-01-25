from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_textbox1():
    # Настройка WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    try:
        # Открываем сайт
        driver.get("https://omayo.blogspot.com/")

        # Находим текстовое поле с ID "textbox1"
        textbox = driver.find_element(By.ID, "textbox1")

        # Очищаем текстовое поле, т.к. оно заполнено при открытии страницы
        textbox.clear()
    

        # Вводим текст "Selenium Test"
        input_text = "Selenium Test"
        textbox.send_keys(input_text)

        # Проверяем, что текст отобразился в поле
        result_text = textbox.get_attribute("value")
        assert result_text == input_text, f"Expected '{input_text}', but got '{result_text}'"
        print("Test passed")

    finally:
        # Закрываем браузер
        driver.quit()

# Вызов функции
test_textbox1()