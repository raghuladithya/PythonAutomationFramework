from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import allure
from Utils import utils as utils
from Pages.loginPage import LoginPage
from Pages.Homepage import Homepage
from Pages.Advancetracking import Advancetracking

@pytest.mark.usefixtures("test_setup")
class Testadvancedtracking():

    def test_login(self):
        browser = self.browser
        browser.get(utils.URL)
        time.sleep(5)

        login = LoginPage(browser)
        login.click_app()
        time.sleep(5)
        allure.attach(self.browser.get_screenshot_as_png(), name="login", attachment_type=allure.attachment_type.PNG)
        login.enter_username(utils.Username)
        allure.attach(self.browser.get_screenshot_as_png(), name="username", attachment_type=allure.attachment_type.PNG)
        login.enter_password(utils.Password)
        allure.attach(self.browser.get_screenshot_as_png(), name="Password", attachment_type=allure.attachment_type.PNG)
        login.click_login()
        time.sleep(5)

    def test_advancedtracking(self):
        browser = self.browser
        advancetracking = Advancetracking(browser)
        advancetracking.click_Advancedtracking()
        allure.attach(self.browser.get_screenshot_as_png(), name="Advancetracking", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        advancetracking.enter_trackingnumber(utils.trackingnumber)
        allure.attach(self.browser.get_screenshot_as_png(), name="trackingnumber", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        advancetracking.click_search()
        allure.attach(self.browser.get_screenshot_as_png(), name="search", attachment_type=allure.attachment_type.PNG)
        time.sleep(5)

    def test_logout(self):
        browser = self.browser
        homePage = Homepage(browser)
        homePage.click_logout()

