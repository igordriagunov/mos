import json

from page_objects.base_page import BasePage
from page_objects.project_blago_page import ProjectBlagoPage
from locators import ProjectsLocator


class ProjectsPage(BasePage):

    def check_projects_count(self):
        self.wait_for_visible(ProjectsLocator.projects_main)
        self.wait_for_visible(ProjectsLocator.project_item_title)
        el_project_item_title = self.find_elements(ProjectsLocator.project_item_title)
        projects_count = len(el_project_item_title)

        assert projects_count >= 7  # можно добавить проверики здесь, если позволяет стиль написания кода
        print(projects_count)

        return ProjectsPage(self.browser)

    def check_projects_names(self):
        el_project_item_title = self.find_elements(ProjectsLocator.project_item_title)
        actual_project_list = {'projects': []}

        for el in el_project_item_title:
            actual_project_name = el.text

            actual_project_list['projects'].append(actual_project_name)
            # print(data)

            # чтение из файла и запись в файл можно вынести в отдельный класс/метод
            # если это часто используется и есть схожее поведение
            # в данном случае это "хардкод" , надеюсь на понимание =)
            with open('/home/igor/PycharmProjects/mos/env/actual_projects_list.json', 'w',
                      encoding='utf8') as json_file:
                json.dump(actual_project_list, json_file, ensure_ascii=False)

                # print(el.text)

        expected_projects_list = json.load(open('/home/igor/PycharmProjects/mos/env/expected_projects_list.json'))

        checking_match_in_lists = sorted(actual_project_list.items()) == sorted(expected_projects_list.items())
        # print(actual_project_list)
        # print('-------------')
        # print(expected_projects_list)
        # print('-------------')
        # print(checking_match_in_lists)

        assert checking_match_in_lists is True

        return ProjectsPage(self.browser)

    def click_to_link_goto_project_blago(self):
        self.find_element_and_click(ProjectsLocator.project_blago_link)
        return ProjectBlagoPage(self.browser)
