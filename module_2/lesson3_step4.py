from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x: int):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Подтверждаем всплывающее окно
    browser.find_element(By.TAG_NAME, 'button').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    # Вычислить значение
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    value = calc(int(x))

    # Ввести значение
    field_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    field_answer.send_keys(value)

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    time.sleep(2)
    browser.quit()
