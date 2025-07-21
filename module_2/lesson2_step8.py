from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys("Petrov")
    email = browser.find_element(By.NAME, 'email')
    email.send_keys("test@test.ru")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'file.txt')

    # Прикрепляем файл
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()