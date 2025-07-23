# Установка Firefox и Selenium-драйвера geckodriver
# Инструкция по переустановке firefox - https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04#:%7E:text=Installing%20Firefox%20via%20Apt%20(Not%20Snap)&text=You%20add%20the%20Mozilla%20Team,%2C%20bookmarks%2C%20and%20other%20data
# Установка geckodriver - https://selenium-python.com/install-geckodriver
# Релизы geckodriver - https://github.com/mozilla/geckodriver/releases

from selenium import webdriver
import time

# Инициализируем драйвер браузера
driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")

time.sleep(5)
