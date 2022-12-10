from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import allure
from Utils import utils as utils
from Pages.loginPage import LoginPage
from Pages.Homepage import Homepage
from Pages.myfinance import myfinance

@pytest.mark.usefixtures("test_setup")
class Testmyfinance():

    def test_login(self):
        browser = self.browser
        browser.get(utils.URL)
        time.sleep(5)

        login = LoginPage(browser)
        login.click_app()
        time.sleep(5)
        allure.attach(self.browser.get_screenshot_as_png(), name="login", attachment_type=allure.attachment_type.PNG)
        login.enter_username(utils.Username)
        allure.attach(self.browser.get_screenshot_as_png(),name="username",attachment_type=allure.attachment_type.PNG)
        login.enter_password(utils.Password)
        allure.attach(self.browser.get_screenshot_as_png(), name="username", attachment_type=allure.attachment_type.PNG)
        login.click_login()
        time.sleep(5)

    def test_myfinance(self):
        browser = self.browser
        myfinancepage = myfinance(browser)
        myfinancepage.click_myfinancetab()
        time.sleep(5)
        allure.attach(self.browser.get_screenshot_as_png(), name="myfinance", attachment_type=allure.attachment_type.PNG)
        myfinancepage.click_myinvoicetab()
        time.sleep(5)
        allure.attach(self.browser.get_screenshot_as_png(), name="myinvoice", attachment_type=allure.attachment_type.PNG)
        myfinancepage.click_download()
        allure.attach(self.browser.get_screenshot_as_png(), name="download", attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

    def test_logout(self):
        browser = self.browser
        homePage = Homepage(browser)
        homePage.click_logout()