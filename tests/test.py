import json
import time

import pytest

# from page_objects import BasePage, MainPage
from page_objects.base_page import BasePage
from page_objects.main_page import MainPage
from page_objects.projects_page import ProjectsPage

from locators import MainLocator, ProjectsLocator, ProjectBlago


# @pytest.mark.skip
def test_open_main_page_go_to_projects(browser, load_env):
    main_url, projects_url, project_blago_url = load_env

    MainPage(browser) \
        .open_main_page(main_url) \
        .click_projects_link()

    assert projects_url == browser.current_url  # можно добавить проверики здесь, если позволяет стиль написания кода
    print(browser.current_url)

    # можно продолжить цепочку действий с объектом страницы ProjectsPage.make_some_action()...


def test_check_projects_list(browser, load_env):
    main_url, projects_url, project_blago_url = load_env

    ProjectsPage(browser). \
        check_projects_count(). \
        check_projects_names()
