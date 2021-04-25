import time

import pytest

from locators import ProjectBlagoLocator, ProjectCovidLocator, ProjectsLocator, MainLocator
from page_objects.main_page import MainPage
from page_objects.project_blago_page import ProjectBlagoPage
from page_objects.projects_page import ProjectsPage
from page_objects.project_covid_page import ProjectCovidPage


# @pytest.mark.skip
def test_open_main_page_go_to_projects(browser, load_env):
    main_url, projects_url, project_blago_url, project_covid_url = load_env

    MainPage(browser) \
        .open_main_page(main_url) \
        .click_projects_link()

    assert projects_url == browser.current_url  # можно добавить проверики здесь, если позволяет стиль написания кода
    print(browser.current_url)

    # можно продолжить цепочку действий с объектом страницы ProjectsPage.make_some_action()...


def test_check_projects_list(browser, load_env):
    main_url, projects_url, project_blago_url, project_covid_url = load_env

    project = ProjectsPage(browser) \
        .check_projects_count() \
        .check_projects_names() \
        .click_to_link_goto_project_blago()

    # можно "положить" результат выполнения шага в переменную и сдлеать какую либо проверку
    assert project_blago_url == project.browser.current_url
    print(project.browser.current_url)


def test_check_blago_page(browser, load_env):
    main_url, projects_url, project_blago_url, project_covid_url = load_env

    # объект класса любой страницы наследуется от BasePage и можно обращаться к "базовым" функциям
    # получается гибкая конструкция
    ProjectBlagoPage(browser).wait_for_visible(ProjectBlagoLocator.make_good_thing_button)
    ProjectBlagoPage(browser).wait_for_visible(ProjectBlagoLocator.how_to_work_service)
    ProjectBlagoPage(browser).wait_for_visible(ProjectBlagoLocator.want_to_help_button)
    ProjectBlagoPage(browser).move_cursor_to_element(ProjectBlagoLocator.how_to_work_service)
    time.sleep(2)
    ProjectBlagoPage(browser).move_cursor_to_element(ProjectBlagoLocator.how_to_work_service)
    time.sleep(2)
    ProjectBlagoPage(browser).move_cursor_to_element(ProjectBlagoLocator.want_to_help_button)
    time.sleep(2)
    ProjectsPage(browser).open_page(projects_url)


# @pytest.mark.skip
def test_check_covid_page(browser, load_env):
    main_url, projects_url, project_blago_url, project_covid_url = load_env

    ProjectsPage(browser).find_element_and_click(ProjectsLocator.project_covid_link)
    ProjectCovidPage(browser).check_elements() \
        .move_cursor_to_element(ProjectCovidLocator.covid_block)
    MainPage(browser).open_main_page(main_url)


def test_calendar(browser):
    MainPage(browser).find_element(MainLocator.calendar)
    MainPage(browser).move_cursor_to_element(MainLocator.calendar)
