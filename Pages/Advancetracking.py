class Advancetracking():

    def __init__(self, browser):
        self.browser = browser

        self.Advtracking_input_id="containerNumber"
        self.search_button_id="btnSubmitFormAdvancedTracking"
        self.AdvancedTracking_menu_css = "#navAdvancedTracking > a > p"


    def click_Advancedtracking(self):
        Advtracking = self.browser.find_element_by_css_selector(self.AdvancedTracking_menu_css)
        Advtracking.click()

    def enter_trackingnumber(self,trackingnumber):
        advtrackingnumber = self.browser.find_element_by_id(self.Advtracking_input_id)
        advtrackingnumber.send_keys(trackingnumber)


    def click_search(self):
        searchbtn = self.browser.find_element_by_id(self.search_button_id)
        searchbtn.click()