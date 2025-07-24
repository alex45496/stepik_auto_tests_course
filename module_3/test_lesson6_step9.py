# Запуск автотестов для разных языков интерфейса

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.chrome.options import Options as Chrome_Options


# Задать язык для браузера Google
options = Chrome_Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
browser = webdriver.Chrome(options=options)


# Задать язык для браузера FireFox
# options = Firefox_Options()
# options.set_preference("intl.accept_languages", 'ru')
# browser = webdriver.Firefox(options=options)


link = "http://selenium1py.pythonanywhere.com/"
browser.get(link)
browser.find_element(By.CSS_SELECTOR, "#login_link")
time.sleep(2)
browser.quit()
