class LoginPage():

    def __init__(self,browser):
        self.browser = browser


        self.username_textbox_id = "registeredEmail"
        self.password_textbox_id = "password"
        self.login_button_xpath = "//*[@id='formLogin']/div[4]/div[1]/button"
        self.app_menu_xpath = "//*[@id='navbarSupportedContent']/ul/li[5]/a"

    def click_app(self):
        app = self.browser.find_element_by_xpath(self.app_menu_xpath)
        app.click()

    def enter_username(self, username):
        email = self.browser.find_element_by_id(self.username_textbox_id)
        email.send_keys(username)

    def enter_password(self,password):
        passwordtab = self.browser.find_element_by_id(self.password_textbox_id)
        passwordtab.send_keys(password)

    def click_login(self):
        Loginbtn = self.browser.find_element_by_xpath(self.login_button_xpath)
        Loginbtn.click()

