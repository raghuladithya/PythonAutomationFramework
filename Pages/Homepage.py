class Homepage():

    def __init__(self, browser):
        self.browser = browser

        self.logout_button_xpath="//*[@id='menuLeft']/li[7]/a/p"


    def click_logout(self):
        Logout = self.browser.find_element_by_xpath(self.logout_button_xpath)
        Logout.click()

