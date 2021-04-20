from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from common.Alert import Alert


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # self.alert = Alert(self.driver)

    def open_main_page(self, url):
        return self.driver.get(url)

    def find_element_and_click(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        # elif 'xpath' in selector.keys():
        #     by = By.XPATH
        #     selector = selector['xpath']
        return self.driver.find_element(by, selector).click()

    def element(self, selector: dict, link_text: str = None):
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

        return self.driver.find_element(by, selector)

    def elements(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            selector = selector['css']
        return self.driver.find_elements(by, selector)

    def click(self, selector):
        ActionChains(self.driver).move_to_element(self.element(selector)).click().perform()

    def input(self, selector, value):
        element = self.element(selector)
        element.clear()
        element.send_keys(value)

    def wait_for_visible(self, selector, link_text=None, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.element(selector, link_text)))

    def get_element_text(self, selector):
        return self.element(selector).text
