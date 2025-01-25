# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager


# def test_login_and_add_to_cart():
#     # Настройка WebDriver
#     options = Options()
#     options.add_argument("--start-maximized")
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.implicitly_wait(10)
#     try:
#         # Шаг 1: Перейти на страницу логина
#         driver.get("https://www.saucedemo.com")

#         # Шаг 2: Ввести данные для авторизации
#         login = driver.find_element(By.ID, "user-name")
#         password = driver.find_element(By.ID, "password")
#         button = driver.find_element(By.ID, "login-button")

#         login.send_keys("standard_user")
#         password.send_keys("secret_sauce")
#         button.click()
        

#         # Шаг 3: Добавить товар в корзину

#         driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
#         driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()
#         driver.find_element(By.ID, "checkout").click()
#         driver.find_element(By.ID, "first-name").send_keys("Vitaliy")
#         driver.find_element(By.ID, "last-name").send_keys("Popkov")
#         driver.find_element(By.ID, "postal-code").send_keys("220085")
#         driver.find_element(By.ID, "continue").click()
#         driver.find_element(By.ID, "finish").click()
#         shopping_complete_msg = driver.find_element(By.CLASS_NAME, "complete-text")
#         assert shopping_complete_msg.text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"


#     finally:
#         # Закрытие браузера
#         driver.quit()

# # Вызов функции
# test_login_and_add_to_cart()
   
 #   '''УЛУЧШЕННЫЙ'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Данные для тестирования с параметризацией
@pytest.mark.parametrize("username,password,first_name,last_name,postal_code,expected_msg", [
    ("standard_user", "secret_sauce", "Vitaliy", "Popkov", "220085", "Your order has been dispatched, and will arrive just as fast as the pony can get there!"),
    # Добавьте другие тестовые данные, если необходимо
])
def test_login_and_add_to_cart(username, password, first_name, last_name, postal_code, expected_msg):
    # Настройка WebDriver
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    try:
        # Шаг 1: Перейти на страницу логина
        driver.get("https://www.saucedemo.com")

        # Шаг 2: Ввести данные для авторизации
        login = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        button = driver.find_element(By.ID, "login-button")

        login.send_keys(username)
        password_field.send_keys(password)
        button.click()

        # Шаг 3: Добавить товар в корзину
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()
        driver.find_element(By.ID, "checkout").click()

        # Шаг 4: Заполнить данные для оформления заказа
        driver.find_element(By.ID, "first-name").send_keys(first_name)
        driver.find_element(By.ID, "last-name").send_keys(last_name)
        driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()

        # Шаг 5: Проверить сообщение об успешном оформлении заказа
        shopping_complete_msg = driver.find_element(By.CLASS_NAME, "complete-text")
        assert shopping_complete_msg.text == expected_msg

    finally:
        # Закрытие браузера
        driver.quit()

