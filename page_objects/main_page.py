from page_objects import BasePage
from locators import MainLocator


class MainPage(BasePage):

    def open(self, url):
        self.open_main_page(url)
        return MainPage(self.driver)

    def check_projects_link_visible(self):
        self.wait_for_visible(MainLocator.projects_link)
        return MainPage(self.driver)

    def click_on_projects(self):
        self.click(MainLocator.projects_link)
        return MainPage(self.driver)
