import os
import unittest
import uuid

import selenium.webdriver as webdriver
from testutils import SeleniumTest

from .pages.auth import AuthPage


class TestCase(SeleniumTest):
    def setUp(self):
        super().setUp()
        account = AuthPage(self.driver)
        account.open()
        login_form = account.form
        account.Actions.sign_in(login_form, os.environ.get("LOGIN"), os.environ.get("PASS"))

    def tearDown(self) -> None:
        self.driver.quit()
