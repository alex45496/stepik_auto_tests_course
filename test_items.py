from selenium.webdriver.common.by import By


def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button_add_basket = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(button_add_basket) > 0, 'button not found'
