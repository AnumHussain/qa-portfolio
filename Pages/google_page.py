from selenium.webdriver.common.by import By


class GooglePage:
    URL = "https://www.google.com"
    SEARCH_BOX = (By.NAME, "q")


    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def search(self, text):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.send_keys(text)
        search_box.submit()