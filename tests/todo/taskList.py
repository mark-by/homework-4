from .utils import TodoTest


class TaskListTest(TodoTest):
    def _test_change_description(self):
        description_content = 'Some description'
        task_list = self.page.task_list
        task_list.fill_description(description_content)
        self.driver.refresh()
        self.control_bar.wait_self()
        self.control_bar.open_task_list(self.task_list_title)
        task_list.wait_description(description_content)
        self.assertEqual(description_content, task_list.get_description())

    def test_change_title(self):
        title_content = 'Some title'
        task_list = self.page.task_list
        task_list.fill_title(title_content)
        self.task_list_title = title_content
        self.driver.refresh()
        self.control_bar.wait_self()
        self.control_bar.open_task_list(self.task_list_title)
        task_list.wait_title(title_content)
        self.assertEqual(title_content, task_list.get_title())
