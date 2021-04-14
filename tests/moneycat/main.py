from .utils import TestCase
from .pages.main import MainPage


class MoneyCatFinanceTest(TestCase):
    def setUp(self):
        super().setUp()
        self.main = MainPage(self.driver)
        self.sell_form = self.main.sell_form
        self.header_form = self.main.header

    def test_sell_ok(self):
        self.main.currency_list.open_first_currency()
        before = self.sell_form.wallet_status()

        amount = 1
        self.sell_form.fill_input(amount)
        self.sell_form.sell()
        self.sell_form.wait_for_message()

        after = self.sell_form.wallet_status()

        self.assertEqual(before - after, amount)

    def test_sell_zero(self):
        self.main.currency_list.open_first_currency()
        before = self.sell_form.wallet_status()

        amount = 0
        self.sell_form.fill_input(amount)
        self.sell_form.sell()
        self.sell_form.wait_for_message()

        after = self.sell_form.wallet_status()

        self.assertEqual(before - after, amount)

    def test_sell_no_exist_currency(self):
        # try to buy euro by japan currency
        self.main.currency_list.open_last_currency()
        before = self.sell_form.wallet_status()

        amount = 1
        self.sell_form.fill_input(amount)
        self.sell_form.sell()
        self.sell_form.wait_for_message()

        after = self.sell_form.wallet_status()

        self.assertEqual(before - after, 0)

    def test_header_open_by_click_logo(self):
        self.header_form.click_logo()
        visible = self.main.currency_list.is_currency_card_visible()
        self.assertEqual(visible, True)

    def test_header_open_by_click_settings(self):
        is_settings_page = self.header_form.click_account()
        self.assertEqual(is_settings_page, True)

    def test_header_open_drop_down_menu(self):
        drop_down_menu_visible = self.header_form.click_avatar()
        self.assertEqual(drop_down_menu_visible, True)

    def test_header_settings_drop_down_menu(self):
        self.header_form.click_avatar()
        is_settings_page = self.header_form.click_settings_in_drop_down_menu()
        self.assertEqual(is_settings_page, True)

    def test_header_exit_from_drop_down_menu(self):
        self.header_form.click_avatar()
        is_auth_page = self.header_form.click_exit_in_drop_down_menu()
        self.assertEqual(is_auth_page, True)

    def test_header_bag(self):
        is_bag_page = self.header_form.click_bag()
        self.assertEqual(is_bag_page, True)

    def test_header_history(self):
        is_history_page = self.header_form.click_history()
        self.assertEqual(is_history_page, True)
