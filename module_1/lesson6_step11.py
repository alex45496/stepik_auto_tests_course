from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    last_name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    email.send_keys("test@test.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    browser.quit()