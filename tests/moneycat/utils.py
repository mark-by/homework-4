import os
import unittest
import uuid

import selenium.webdriver as webdriver

from .pages.auth import AuthPage


def get_driver():
    browser = os.environ.get('BROWSER', 'CHROME')

    return webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(webdriver.DesiredCapabilities, browser).copy()
    )


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        account = AuthPage(self.driver)
        account.open()
        login_form = account.form
        account.Actions.sign_in(login_form, os.environ.get("LOGIN"), os.environ.get("PASS"))

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
