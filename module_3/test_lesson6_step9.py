# Запуск автотестов для разных языков интерфейса

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# Задать язык для браузера Google
# options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
# browser = webdriver.Chrome(options=options)


# Задать язык для браузера FireFox
options = Options()
options.set_preference("intl.accept_languages", 'ru')
browser = webdriver.Firefox(options=options)


link = "http://selenium1py.pythonanywhere.com/"
browser.get(link)
browser.find_element(By.CSS_SELECTOR, "#login_link")
time.sleep(2)
browser.quit()
