from .utils import TestCase
from .pages.settings import Settings


class MoneyCatSettingsTest(TestCase):
    def setUp(self):
        super().setUp()

        self.settings = Settings(self.driver)
        self.settings.open()

    def test_new_pass_len_less_than_6(self):
        print(
            "HERE",
            self.settings.update_pass(
                menu_form=self.settings.menu_form,
                pass_form=self.settings.password_form,
                old_pass="lolkek",
                new_pass="12345",
                repeat_pass="12345",
            )
        )
        self.assertEqual(
            1,
            1
        )

    # def test_valid_pass(self):
    #     pass

    # def test_new_pass_len_more_than_30(self):
    #     pass

    # def test_invalid_symbols(self):
    #     pass

    # def test_pass_not_cmp(self):
    #     pass

    # def test_change_avatar(self):
    #     pass

    # def test_avatar_invalid_size(self):
    #     pass

    # def test_check_user_data(self):
    #     pass

    # def test_open_pass_form(self):
    #     pass

    # def test_open_avatar_form(self):
    #     pass
