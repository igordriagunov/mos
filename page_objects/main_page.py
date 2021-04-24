from page_objects.base_page import BasePage
from page_objects.projects_page import ProjectsPage

from locators import MainLocator, ProjectsLocator


class MainPage(BasePage):

    def open_main_page(self, url):
        self.open_page(url)
        return MainPage(self.browser)

    def click_projects_link(self):
        self.find_element_and_click(MainLocator.projects_link)
        self.wait_for_visible(ProjectsLocator.projects_main)
        return ProjectsPage(self.browser)
