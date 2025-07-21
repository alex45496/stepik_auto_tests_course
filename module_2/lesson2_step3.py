from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Вычислить значение
    value1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    value2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
    value = str(int(value1) + int(value2))

    #!!!!!!!!!!!!!!!!
    # Выбрать значение
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value)

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()
