import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_parametrize_language_browser(browser):
    browser.get(link)
    time.sleep(30)
    button_basket = browser.find_elements_by_css_selector(".btn-add-to-basket")

    assert len(button_basket) == 1, "кнопка не одна"
    
    
