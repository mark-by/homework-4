from selenium.webdriver.common.by import By

from testutils import Component


class TaskListSettings(Component):
    container = 'div[class^="ListMenu_base"]'

    class Selectors:
        hide_completed = 'button:nth-child(1)'
        sort_by_date = 'button:nth-child(3)'
        sort_by_name = 'button:nth-child(4)'
        sort_by_priority = 'button:nth-child(5)'
        edit = 'button:nth-child(7)'
        delete = 'button:nth-child(8)'

    def hide_completed(self):
        self.__press_button(self.Selectors.hide_completed)

    def delete(self):
        self.__press_button(self.Selectors.delete)

    def __press_button(self, selector):
        button_selector = self.container + ' ' + selector
        self._wait_clickable(By.CSS_SELECTOR, button_selector)
        element = self.driver.find_element_by_css_selector(button_selector)
        element.click()


