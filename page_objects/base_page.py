import json

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from common.Alert import Alert


# def __init__(self, driver):
#     self.driver = driver
# self.alert = Alert(self.driver)
class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def open_page(self, url):
        self.browser.get(url)

    def find_element_and_click(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT

        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']

        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']

        elif 'class' in selector.keys():
            by = By.CLASS_NAME
            selector = selector['class']

        return self.browser.find_element(by, selector).click()

    def find_element(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT

        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']

        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']

        elif 'class' in selector.keys():
            by = By.CLASS_NAME
            selector = selector['class']

        return self.browser.find_element(by, selector)

    def find_elements(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT

        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']

        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']

        elif 'class' in selector.keys():
            by = By.CLASS_NAME
            selector = selector['class']

        return self.browser.find_elements(by, selector)

    def click(self, selector):
        ActionChains(self.browser).move_to_element(self.find_element(self.browser, selector)).click().perform()

    def input_text(self, selector, value):
        element = self.find_element_and_click(self.browser, selector)
        element.clear()
        element.send_keys(value)

    def wait_for_visible(self, selector, link_text=None, wait=5):
        return WebDriverWait(self.browser, wait).until(
            EC.visibility_of(self.find_element(selector)))

    def get_element_text(self, selector):
        return self.browser.find_element(selector).text

    def move_cursor_to_element(self, selector):
        ActionChains(self.browser).move_to_element(self.find_element(self.browser, selector)).perform()
