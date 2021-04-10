import os
import unittest
from .pages import AccountPage, TodoPage
from .utils import get_driver
import time


class TodoTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        account = AccountPage(self.driver)
        account.open()
        login_form = account.form
        account.Actions.sign_in(login_form, os.environ.get("LOGIN"), os.environ.get("PASS"))
        self.page = TodoPage(self.driver)
        self.page.open()
        self.clear = None

    def tearDown(self) -> None:
        if self.clear is not None:
            self.clear()

        self.driver.quit()

    def test_change_description(self):
        description_content = 'Some description'
        task_list = self.page.task_list
        task_list.fill_description(description_content)
        self.driver.refresh()
        self.assertEqual(description_content, task_list.get_description())
        self.clear = lambda: task_list.clear_description()
        task_list.clear_description()

    def test_change_title(self):
        title_content = 'Some title'
        task_list = self.page.task_list
        task_list.fill_title(title_content)
        self.driver.refresh()
        self.clear = lambda: task_list.clear_title()
        self.assertEqual(title_content, task_list.get_title())
        task_list.clear_title()

