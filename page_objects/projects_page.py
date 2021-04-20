from page_objects import BasePage
from locators import ProjectsLocator


class ProjectsPage(BasePage):

    def check_projects_elements_visible(self):
        # self.wait_for_visible(ProjectsLocator.project)
        self.wait_for_visible(ProjectsLocator.projects_block)
        return ProjectsPage(self.driver)
