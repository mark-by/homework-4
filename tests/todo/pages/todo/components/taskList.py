from selenium.webdriver.common.by import By
from .task import Task
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from testutils import Component


class TaskList(Component):

    class Selectors:
        title = '[placeholder="Добавить название"]'
        description = '[placeholder="Добавить описание"]'
        create_task = '[placeholder="Создать задачу"]'

    def create_task(self, title):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.create_task, title, True)

    def get_tasks(self):
        self._wait_visible(By.CSS_SELECTOR, Task.container)
        tasks = []
        for task in self.driver.find_elements(By.CSS_SELECTOR, Task.container):
            tasks.append(Task(self.driver, task))
        return tasks

    def wait_description(self, title):
        self._wait_text(By.CSS_SELECTOR, self.Selectors.description, title)

    def wait_title(self, title):
        self._wait_text(By.CSS_SELECTOR, self.Selectors.title, title)

    def wait_task_list(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.title)

    def fill_description(self, content):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.description, content, True)

    def clear_description(self):
        self._clear_input(By.CSS_SELECTOR, self.Selectors.description, True)

    def get_description(self) -> str:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.description)
        return self.driver.find_element_by_css_selector(self.Selectors.description).text

    def fill_title(self, content):
        self._clear_input(By.CSS_SELECTOR, self.Selectors.title, True)
        self._fill_input(By.CSS_SELECTOR, self.Selectors.title, content, True)

    def clear_title(self):
        self._clear_input(By.CSS_SELECTOR, self.Selectors.title, True)

    def get_title(self) -> str:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.title)
        return self.driver.find_element_by_css_selector(self.Selectors.title).text
