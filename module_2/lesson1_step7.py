from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычислить значение
    x = browser.find_element(By.CSS_SELECTOR, '#treasure').get_attribute('valuex')
    value = calc(int(x))

    # Ввести значение
    field_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    field_answer.send_keys(value)

    # Выбрать checkbox
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
