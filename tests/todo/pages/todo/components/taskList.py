from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from testutils import Component


class TaskList(Component):

    class Selectors:
        title = '[placeholder="Добавить название"]'
        description = '[placeholder="Добавить описание"]'
        create_task = '[placeholder="Создать задачу"]'

    def fill_description(self, content):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.description, content, True)

    def clear_description(self):
        self._clear_input(By.CSS_SELECTOR, self.Selectors.description, True)

    def get_description(self) -> str:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.description)
        return self.driver.find_element_by_css_selector(self.Selectors.description).text

    def fill_title(self, content):
        self._clear_input(By.CSS_SELECTOR, self.Selectors.title, False)
        self._fill_input(By.CSS_SELECTOR, self.Selectors.title, content, True)

    def clear_title(self):
        self._clear_input(By.CSS_SELECTOR, self.Selectors.title, True)

    def get_title(self) -> str:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.title)
        return self.driver.find_element_by_css_selector(self.Selectors.title).text
