import os
import unittest

from tests.todo.pages import AccountPage, TodoPage
from tests.todo.utils import get_driver


class TaskTest(unittest.TestCase):
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
            self.clear = None

        self.driver.quit()

    def test_create_task(self):
        task_name = 'Some task name'
        task_list = self.page.task_list

        task_list.create_task(task_name)
        tasks = task_list.get_tasks()
        task = tasks[0]
        self.clear = lambda: task.delete()
        self.assertEqual(task_name, task.get_text())

    def test_change_task(self):
        task_name = 'New task change'
        new_task_name = 'Changed task name'

        task_list = self.page.task_list
        task_list.create_task(task_name)
        self.driver.refresh()
        task = task_list.get_tasks()[0]
        self.assertEqual(task_name, task.get_text())
        task.rename_task(new_task_name)
        self.driver.refresh()
        task = task_list.get_tasks()[0]
        self.assertEqual(new_task_name, task.get_text())