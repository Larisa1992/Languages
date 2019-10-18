import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store',
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    
    options = Options()
    options.add_argument("--lang={}".format(browser_language))
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    print("\nstart chrome browser for language {}".format(browser_language))
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
