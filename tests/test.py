import json
import time

from page_objects import base_page
from locators import MainLocator, ProjectsLocator


def test_open_main_page_go_to_projects(browser, load_env):
    base_url, projects_url = load_env

    base_page.open_page(browser, base_url)
    base_page.find_element_and_click(browser, MainLocator.projects_link)
    base_page.wait_for_visible(browser, ProjectsLocator.projects_main)

    assert projects_url == browser.current_url
    print(browser.current_url)

    base_page.wait_for_visible(browser, ProjectsLocator.project_item_title)
    el_project_item_title = base_page.find_elements(browser, ProjectsLocator.project_item_title)
    projects_count = len(el_project_item_title)

    assert projects_count >= 7
    print(projects_count)

    # expected_project_name = base_page.get_project_list()

    data = {'projects': []}

    for el in el_project_item_title:
        actual_project_name = el.text

        data['projects'].append(actual_project_name)
        # print(data)

        with open('/home/igor/PycharmProjects/mos/env/actual_projects_list.json', 'w', encoding='utf8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)

            print(el.text)

# assert expected_project_name == actual_project_name
# print({expected_project_name: actual_project_name})
