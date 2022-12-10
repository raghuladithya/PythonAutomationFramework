class consignee():

    def __init__(self, browser):
        self.browser = browser

        self.myconsignee_tab_cssselector = "#navConsignee > a"
        self.mycontainer_tab_id="navMyContainerConsignee"
        self.atconsignee_section_xpath="//div[(text()='AT CONSIGNEE')]"
        self.download_button_id="btnDownload"

    def click_consgineetab(self):
        consigneetab = self.browser.find_element_by_css_selector(self.myconsignee_tab_cssselector)
        consigneetab.click()

    def click_containertab(self):
        mycontainer = self.browser.find_element_by_id(self.mycontainer_tab_id)
        mycontainer.click()

    def click_atconsignee(self):
        consigneeclick = self.browser.find_element_by_xpath(self.atconsignee_section_xpath)
        consigneeclick.click()

    def click_download(self):
        download = self.browser.find_element_by_id(self.download_button_id)
        download.click()