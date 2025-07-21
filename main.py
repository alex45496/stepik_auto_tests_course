# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/text_input_task.html")

# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
textarea.send_keys("get()")

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
submit_button.click()

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
