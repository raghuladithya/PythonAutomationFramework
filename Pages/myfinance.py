class myfinance():

    def __init__(self, browser):
        self.browser = browser

        self.myfinance_tab_css = "#navMyFinance > a > p"
        self.myinvoice_tab_css = "#navMyInvoice > p"
        self.download_button_css = "btnDownloadOutstandingInvoice"

    def click_myfinancetab(self):
        myfinancetab = self.browser.find_element_by_css_selector(self.myfinance_tab_css)
        myfinancetab.click()

    def click_myinvoicetab(self):
        myinvoicetab = self.browser.find_element_by_css_selector(self.myinvoice_tab_css)
        myinvoicetab.click()

    def click_download(self):
        download = self.browser.find_element_by_id(self.download_button_css)
        download.click()