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

    def test_homepage_assert(self):
        browser = self.browser
        homepage = browser.find_element_by_css("#navHome > a")
        homepage.click()
        time.sleep(5)
        Agecalculator = browser.find_element_by_xpath("//*[@class='btn btn-success w-100']")
        Agecalculator.send_keys(2000)
        time.sleep(5)
        calculate = browser.find_element_by_id("btnGenerate")
        calculate.click()
        time.sleep(5)
        element= browser.find_element_by_id("modalConfirmation-btnOk")
        assert element == "22yrs 0months 0 days"


    def test_logout(self):
        browser = self.browser
        homePage = Homepage(browser)
        homePage.click_logout()