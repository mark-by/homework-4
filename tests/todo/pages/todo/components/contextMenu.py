from selenium.webdriver.common.by import By

from testutils import Component
from .taskPriorityMenu import TaskPriorityMenu


class ContextMenu(Component):
    container = '[class^="ContextMenu_base"]'

    class Selectors:
        date_button = '[class^="MenuButton_base"]:nth-child(1)'
        priority_button = '[class^="MenuButton_base"]:nth-child(2)'
        delete_button = '[class^="MenuButton_base"]:nth-child(4)'

    def open_date_menu(self):
        self.driver.find_element_by_css_selector(self.container).\
            find_element_by_css_selector(self.Selectors.date_button).click()

    def open_priority_menu(self) -> TaskPriorityMenu:
        self.driver.find_element_by_css_selector(self.container). \
            find_element_by_css_selector(self.Selectors.priority_button).click()
        return TaskPriorityMenu(self.driver)

    def delete(self):
        self.driver.find_element_by_css_selector(self.container). \
            find_element_by_css_selector(self.Selectors.priority_button).click()