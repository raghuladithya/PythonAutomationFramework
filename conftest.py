import pytest
import time

def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="chrome", help="Type in browser n(me e.g.chrome OR firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        browser = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        browser = webdriver.Firefox(GeckoDriverManager().install())
    browser.maximize_window()
    request.cls.browser = browser
    time.sleep(5)
    yield
    browser.quit()