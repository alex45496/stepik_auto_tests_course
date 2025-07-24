# Conftest.py и передача параметров в командной строке

# См. файл conftest.py, фикстура browser_2

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser_2):
    browser_2.get(link)
    browser_2.find_element(By.CSS_SELECTOR, "#login_link")
