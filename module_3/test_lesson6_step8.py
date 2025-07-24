# Плагин для перезапуска упавших тестов - pytest-rerunfailures

# для запуска используется следующая команда:
# pytest -v --tb=line --reruns 1 --browser_name=chrome ./module_3/test_lesson6_step8.py

# --reruns n — это количество перезапусков
# --tb=line", чтобы сократить лог с результатами теста


from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")

