class scheduleBooking():

    def __init__(self, browser):
        self.browser = browser

        self.Multipleschedule_btn_id = "btnMultipleSchedule"
        self.GenerateSchedule_btn_id = "btnGenerate"
        self.Confirmationschedule_btn_id = "modalConfirmation-btnOk"
        self.downloadbtn_btn_id ="btnDownload"

    def click_Multipleschedule(self):
        Multipleschedule = self.browser.find_element_by_id(self.Multipleschedule_btn_id)
        Multipleschedule.click()

    def click_GenerateSchedule(self):
        Generateschedule = self.browser.find_element_by_id(self.GenerateSchedule_btn_id)
        Generateschedule.click()

    def click_ConfirmationSchedule(self):
        confirmationSchedule = self.browser.find_element_by_id(self.Confirmationschedule_btn_id)
        confirmationSchedule.click()

    def click_downloadbtn(self):
        downloadbtn = self.browser.find_element_by_id(self.downloadbtn_btn_id)
        downloadbtn.click()