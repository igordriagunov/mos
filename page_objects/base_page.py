import json

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from common.Alert import Alert


# def __init__(self, driver):
#     self.driver = driver
# self.alert = Alert(self.driver)


def open_page(browser, url):
    browser.get(url)
    browser.implicitly_wait(5)


def find_element_and_click(browser, selector: dict, link_text: str = None):
    by = None
    if link_text:
        by = By.LINK_TEXT
    elif 'css' in selector.keys():
        by = By.CSS_SELECTOR
        selector = selector['css']
    elif 'xpath' in selector.keys():
        by = By.XPATH
        selector = selector['xpath']

    return browser.find_element(by, selector).click()


def find_element(browser, selector: dict, link_text: str = None):
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

    return browser.find_element(by, selector)


def find_elements(browser, selector: dict, link_text: str = None):
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

    return browser.find_elements(by, selector)


def click(browser, selector):
    ActionChains(browser).move_to_element(find_element(browser, selector)).click().perform()


def input_text(driver, selector, value):
    element = find_element_and_click(driver, selector)
    element.clear()
    element.send_keys(value)


def wait_for_visible(browser, selector, link_text=None, wait=5):
    return WebDriverWait(browser, wait).until(EC.visibility_of(find_element(browser, selector, link_text)))


def get_element_text(browser, selector):
    return browser.find_element(selector).text


# def get_project_list():
#     pl = json.load(open('/env/expected_projects_list.json'))
#     projects_list = pl['projects']
#
#     for project_name in projects_list:
#         print(project_name)
#
#         return project_name
