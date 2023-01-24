from selenium.webdriver.common.by import By


class DomHelper(object):
    def __init__(self, driver):
        self.driver = driver

    ##Open Page##
    def open_Page(self, url):
        self.driver.get(url)

    ##DriverQuit##
    def driver_Quit(self):
        self.driver.quit()

    ##ClickButton##
    def click_button_ID(self, selector):
        click_Function = self.driver.find_element(By.ID, selector)
        click_Function.click()

    ##SendKeys##
    def send_keys_ID(self, selector, text):
        text_field = self.driver.find_element(By.ID, selector)
        text_field.clear()
        text_field.send_keys(text)

    ##TestEquals##
    def is_text_equal_XPATH(self, selector, text):
        text_equal = self.driver.find_element(By.XPATH, selector)
        assert text_equal.text in text
        print(text_equal.text)

    ##Displayed##
    def is_displayed_ID(self, selector):
        displayed = self.driver.find_element(By.ID, selector)
        assert displayed.is_displayed()
        print(displayed.text)
