import os
from selenium.webdriver import Remote, DesiredCapabilities

from tests.todo.pages import AccountPage, TodoPage


def get_driver():
    browser = os.environ.get('BROWSER', 'CHROME')

    return Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )
