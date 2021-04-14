import os

import unittest
from .pages.auth import AuthPage
from testutils import SeleniumTest


class MoneyCatAuthTest(SeleniumTest):
    def setUp(self):
        super(MoneyCatAuthTest, self).setUp()
        self.account = AuthPage(self.driver)
        self.account.open()
        self.login_form = self.account.form
        self.clear = None

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_success(self):
        self.assertEqual(
            self.account.Actions.sign_in(
                self.login_form,
                os.environ.get("LOGIN"),
                os.environ.get("PASS")
            ),
            "Личный кабинет"
        )
