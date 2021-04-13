import os

from .utils import TestCase
from .pages.settings import Settings


class MoneyCatSettingsTest(TestCase):
    def setUp(self):
        super().setUp()

        self.settings = Settings(self.driver)
        self.settings.open()

    def test_new_pass_len_less_than_6(self):
        errors = self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass="lolkek",
            new_pass="12345",
            repeat_pass="12345",
        )
        self.assertTrue(errors)

    def test_valid_pass(self):
        errors = self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass="lolkek",
            new_pass="keklol",
            repeat_pass="keklol",
        )
        self.assertFalse(errors)
        self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass="keklol",
            new_pass="lolkek",
            repeat_pass="lolkek",
        )

    def test_new_pass_len_more_than_30(self):
        errors = self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass="lolkek",
            new_pass="BSiaIwOqsSGNKCu9JGcZWFUEGGq5CID",
            repeat_pass="BSiaIwOqsSGNKCu9JGcZWFUEGGq5CID",
        )
        self.assertTrue(errors)
        self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass="keklol",
            new_pass="lolkek",
            repeat_pass="lolkek",
        )

    def test_invalid_symbols(self):
        errors = self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass="lolkek",
            new_pass="невалидный",
            repeat_pass="невалидный",
        )
        self.assertTrue(errors)

    def test_pass_not_cmp(self):
        errors = self.settings.update_pass(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
            old_pass="lolkek",
            new_pass="kekkek",
            repeat_pass="kekkkk",
        )
        self.assertTrue(errors)

    # def test_change_avatar(self):
    #     pass

    # def test_avatar_invalid_size(self):
    #     pass

    def test_check_user_data(self):
        email = self.settings.open_avatar_form(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.avatar_form,
        ).text
        self.assertEqual(email, os.environ.get("LOGIN"))

    def test_open_pass_form(self):
        self.assertTrue(self.settings.open_pass_form(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.password_form,
        ))

    def test_open_avatar_form(self):
        self.assertTrue(self.settings.open_avatar_form(
            menu_form=self.settings.menu_form,
            pass_form=self.settings.avatar_form,
        ))
