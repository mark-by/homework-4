from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Remote, ActionChains

from testutils import Component
from .taskPriorityMenu import TaskPriorityMenu
from .contextMenu import ContextMenu


class Task(Component):
    container = '[class^="Task_base"]'

    class Selectors:
        text = '[class^="Task_text"] [class^="EditableText"] p'
        checkbox = 'input[type="checkbox"]'
        priority_button = '[class^="Task_priority"] [class^="PickerButton_base"]'

    def __init__(self, driver: Remote, element: WebElement):
        super().__init__(driver)
        self.element = element

    def rename_task(self, name):
        self._clear_input_element(self.element)
        self.element.send_keys(name + Keys.RETURN)

    def get_text(self) -> str:
        return self.element.find_element_by_css_selector(self.Selectors.text).text

    def toggle(self):
        self.element.find_element_by_css_selector(self.Selectors.checkbox).click()

    def open_priority_menu(self) -> TaskPriorityMenu:
        self.element.find_element_by_css_selector(self.Selectors.priority_button).click()
        return TaskPriorityMenu(self.driver)

    def open_context_menu(self) -> ContextMenu:
        ActionChains(self.driver).context_click(self.element).perform()
        return ContextMenu(self.driver)

    def delete(self):
        context_menu = self.open_context_menu()
        context_menu.wait_self()
        context_menu.delete()
