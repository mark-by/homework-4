import os

import unittest
from .utils import get_driver
from .pages.auth import AuthPage


class MoneyCatAuthTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
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

    # def test_login_nonexist(self):
    #     account = AuthPage()
    #     account.open()
    #
    #     login_form = account.form
    #
    #     self.assertEqual(
    #         account.Actions.sign_in(
    #             login_form,
    #             "mkoijnbhu@ygv",
    #             os.environ.get("PASS")
    #         ),
    #         os.environ.get("LOGIN")
    #     )
    #
    # def test_login_wrong_password(self):
    #     account = AuthPage()
    #     account.open()
    #
    #     login_form = account.form
    #
    #     self.assertEqual(
    #         account.Actions.sign_in(
    #             login_form,
    #             os.environ.get("LOGIN"),
    #             os.environ.get("PASS") + "1"
    #         ),
    #         os.environ.get("LOGIN")
    #     )
