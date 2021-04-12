import os
import unittest
import uuid

from selenium.webdriver import Remote, DesiredCapabilities

from tests.todo.pages import AccountPage, TodoPage


def get_driver():
    browser = os.environ.get('BROWSER', 'CHROME')

    return Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )


class TodoTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        account = AccountPage(self.driver)
        account.open()
        login_form = account.form
        account.Actions.sign_in(login_form, os.environ.get("LOGIN"), os.environ.get("PASS"))
        self.page = TodoPage(self.driver)
        self.page.open()
        self.control_bar = self.page.control_bar
        self.task_list_title = uuid.uuid4().hex
        self.control_bar.create_list(self.task_list_title)
        self.control_bar.open_task_list(self.task_list_title)
        self.page.task_list.wait_title(self.task_list_title)

        self.clear = None

    def tearDown(self) -> None:
        if self.clear is not None:
            self.clear()
            self.clear = None

        settings = self.page.task_list.settings
        settings.wait_self()
        settings.delete()
        settings.wait_until_disappear_self()
        self.page.task_list.wait_until_disappear_title(self.task_list_title)
        self.driver.refresh()
        self.control_bar.wait_self()

        self.driver.quit()
