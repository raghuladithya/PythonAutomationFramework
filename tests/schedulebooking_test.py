from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import allure
from Utils import utils as utils
from Pages.loginPage import LoginPage
from Pages.Homepage import Homepage
from Pages.schedulebooking import scheduleBooking

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

    def test_Schedulebooking(self):
        browser = self.browser
        schedulebooking = scheduleBooking(browser)
        schedulebooking.click_Multipleschedule()
        allure.attach(self.browser.get_screenshot_as_png(), name="Multipleschedule",attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        schedulebooking.click_GenerateSchedule()
        allure.attach(self.browser.get_screenshot_as_png(), name="GenerateSchedule",attachment_type=allure.attachment_type.PNG)
        time.sleep(5)
        schedulebooking.click_ConfirmationSchedule()
        allure.attach(self.browser.get_screenshot_as_png(), name="confirmationschedule",attachment_type=allure.attachment_type.PNG)
        time.sleep(10)
        schedulebooking.click_downloadbtn()
        allure.attach(self.browser.get_screenshot_as_png(), name="downloadbtn",attachment_type=allure.attachment_type.PNG)
        time.sleep(5)


    def test_logout(self):
        browser = self.browser
        homePage = Homepage(browser)
        homePage.click_logout()
