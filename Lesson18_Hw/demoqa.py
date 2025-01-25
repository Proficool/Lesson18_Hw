from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_table():
    # Настройка WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    try:
        # Открытие сайта
        driver.get("https://demoqa.com/webtables")

        # Шаг 1: Нажимаем кнопку "Карандаш"
        driver.find_element(By.ID, "addNewRecordButton").click()

        # Шаг 2: Заполняем поля для добавления нового пользователя
        driver.find_element(By.ID, "firstName").send_keys("John")
        driver.find_element(By.ID, "lastName").send_keys("Doe")
        driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
        driver.find_element(By.ID, "age").send_keys("30")
        driver.find_element(By.ID, "salary").send_keys("50000")
        driver.find_element(By.ID, "department").send_keys("IT")

        # Нажимаем кнопку "Submit" для добавления данных
        driver.find_element(By.ID, "submit").click()
        #time.sleep(2)  # Задержка для обновления таблицы

        # Шаг 3: Редактируем запись с именем "John"
        # Используем XPath для поиска строки с именем "John"
        row = driver.find_element(By.XPATH, "//div[@role='row']//div[text()='John']/ancestor::div[@role='row']")
        # Кликаем на кнопку "Карандаш" в этой строке
        row.find_element(By.XPATH, ".//span[@title='Edit']").click()

        # Очищаем поля перед редактированием
        age_field = driver.find_element(By.ID, "age")
        salary_field = driver.find_element(By.ID, "salary")

        # Очищаем поле age
        age_field.send_keys(Keys.CONTROL + "a")
        age_field.send_keys(Keys.BACKSPACE)

        # Очищаем поле salary
        salary_field.send_keys(Keys.CONTROL + "a")
        salary_field.send_keys(Keys.BACKSPACE)

        # Проверяем, что поля очищены
        assert age_field.get_attribute("value") == "", "Поле age не очищено"
        assert salary_field.get_attribute("value") == "", "Поле salary не очищено"

        # Вводим новые данные
        age_field.send_keys("35")
        salary_field.send_keys("55000")
        driver.find_element(By.ID, "submit").click()

        # Проверяем обновление строки
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[@role='row']//div[text()='John']/ancestor::div[@role='row']"), "55000"
            )
        )
        updated_row = driver.find_element(By.XPATH, "//div[@role='row']//div[text()='John']/ancestor::div[@role='row']")
        assert "35" in updated_row.text, f"Ожидаемое значение '35', но в строке: {updated_row.text}"
        assert "55000" in updated_row.text, f"Ожидаемое значение '55000', но в строке: {updated_row.text}"
        print("Record updated successfully")
        
        # Шаг 4: Удаление записи
        delete_button = updated_row.find_element(By.XPATH, ".//span[@title='Delete']")
        delete_button.click()

        # Проверяем удаление записи
        rows = driver.find_elements(By.XPATH, "//div[@role='row']")
        for row in rows:
            assert "John" not in row.text, "Запись не была удалена"
        print("Record deleted successfully")

    finally:
        # Закрытие браузера
        driver.quit()

# Вызов функции
test_table()