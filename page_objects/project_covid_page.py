from locators import ProjectCovidLocator
from page_objects.base_page import BasePage
from page_objects.main_page import MainPage


class ProjectCovidPage(BasePage):
    def check_elements(self):
        self.wait_for_visible(ProjectCovidLocator.covid_block)
        return self
