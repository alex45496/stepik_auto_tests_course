from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ждём цену
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    # Нажать кнопку
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "book"))).click()

    # Прокрутить вниз
    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Вычислить значение
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    value = calc(int(x))
    # Ввести значение
    field_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    field_answer.send_keys(value)

    button.click()

finally:
    time.sleep(15)
    browser.quit()
