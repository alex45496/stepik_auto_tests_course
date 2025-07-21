from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычислить значение
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    value = calc(int(x))


    # Ввести значение
    field_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    field_answer.send_keys(value)

    check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    time.sleep(10)
    browser.quit()
