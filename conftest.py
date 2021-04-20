import json

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# def pytest_addoption(parser):
#     parser.addoption("--url", "-U", action="store", default="https://www.mos.ru/")
# parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
#
#
# @pytest.fixture
# def url(request):
#     return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """
    # ignore SSL certificate

    option = webdriver.ChromeOptions()
    option.add_argument('--ignore-certificate-errors')

    # /ignore SSL certificate

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=option)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


@pytest.fixture(scope='module')
def load_env():
    env = json.load(open('./env/env.json'))
    base_url = env['base_url']

    return base_url
