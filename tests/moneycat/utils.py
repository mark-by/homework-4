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
        self.driver.quit()
