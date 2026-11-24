from selenium.webdriver.common.by import By


class WebFormPage:

    TXT_INPUT = (By.NAME, "my-text")
    BTN_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    LBL_MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        self.driver = driver

    def fill_text(self, value):
        self.driver.find_element(*self.TXT_INPUT).send_keys(value)

    def submit(self):
        self.driver.find_element(*self.BTN_SUBMIT).click()

    def get_message(self):
        return self.driver.find_element(*self.LBL_MESSAGE).text