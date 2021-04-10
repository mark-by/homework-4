from selenium.webdriver import Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Component(object):
    container = ''

    def __init__(self, driver: Remote):
        self.driver = driver

    def _fill_input(self, by, selector, content, send_enter=False):
        self._wait_clickable(by, selector)
        description = self.driver.find_element(by, selector)
        description.click()
        description.send_keys(content)
        if send_enter:
            description.send_keys(Keys.ENTER)

    def _clear_input(self, by, selector, send_enter=False):
        self._wait_clickable(by, selector)
        description = self.driver.find_element(by, selector)
        description.click()
        description.clear()
        if send_enter:
            description.send_keys(Keys.ENTER)

    def _wait_visible(self, by, selector):
        self._wait(expected_conditions.presence_of_element_located, by, selector)

    def _wait_clickable(self, by, selector):
        self._wait(expected_conditions.element_to_be_clickable, by, selector)

    def _wait(self, condition: expected_conditions, by, selector, *args):
        WebDriverWait(self.driver, 30, 0.1).until(
            condition((by, selector), *args)
        )

    def _wait_not(self, condition, by, selector, *args):
        WebDriverWait(self.driver, 30, 0.1).until_not(
            condition((by, selector), *args)
        )


