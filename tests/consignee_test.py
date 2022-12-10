from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import allure
from Pages.loginPage import LoginPage
from Pages.Homepage import Homepage
from Pages.consignee import consignee
from Utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class Testconsignee():


    def test_login(self):
        browser = self.browser
        browser.get(utils.URL)
        time.sleep(5)

        login = LoginPage(browser)
        login.click_app()
        allure.attach(self.browser.get_screenshot_as_png(), name="login", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        login.enter_username(utils.Username)
        allure.attach(self.browser.get_screenshot_as_png(), name="username", attachment_type=allure.attachment_type.PNG)
        login.enter_password(utils.Password)
        allure.attach(self.browser.get_screenshot_as_png(), name="Password", attachment_type=allure.attachment_type.PNG)
        login.click_login()
        time.sleep(5)

    def test_consignee(self):
        browser = self.browser

        Consginee = consignee(browser)
        Consginee.click_consgineetab()
        allure.attach(self.browser.get_screenshot_as_png(), name="Consigneetab", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        Consginee.click_containertab()
        allure.attach(self.browser.get_screenshot_as_png(), name="mycontainer", attachment_type=allure.attachment_type.PNG)
        time.sleep(10)
        Consginee.click_atconsignee()
        allure.attach(self.browser.get_screenshot_as_png(), name="atconsignee", attachment_type=allure.attachment_type.PNG)
        time.sleep(10)
        Consginee.click_download()
        allure.attach(self.browser.get_screenshot_as_png(), name="download", attachment_type=allure.attachment_type.PNG)
        time.sleep(10)


    def test_logout(self):
        browser = self.browser
        homePage = Homepage(browser)
        homePage.click_logout()