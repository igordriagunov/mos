import time

from page_objects import BasePage, MainPage, ProjectsPage


def test_open_main_page_go_to_projects(browser, load_env):
    base_url = load_env

    MainPage(browser).open_main_page(base_url)
    MainPage(browser) \
        .check_projects_link_visible() \
        .click_on_projects()


def test_projects_page_check_projects(browser):
    ProjectsPage(browser).check_projects_elements_visible()

