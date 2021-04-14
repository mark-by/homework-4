import os

from .utils import TestCase
from .pages.converter import ConverterPage


class MoneyCatConverterTest(TestCase):
    def test_converter_first_field(self):
        self.account.Actions.sign_up(
            self.signup_form,
            str(time.time()) + "@mail.ru",
            os.environ.get("PASS"),
            os.environ.get("PASS")
        )

        self.assertEqual(
            self.signup_form.get_account_header(),
            "Личный кабинет"
        )

    # def test_converter_second_field(self):

    # def test_converter_unexceptable_symbols(self):
