import os

from .utils import TestCase
from .pages.finance import FinancePage
from .pages.auth import AuthPage


class MoneyCatAuthTest(TestCase):
    def test_sell_success(self):
        account = AuthPage(self.driver)
        account.open()

        finance = FinancePage(self.driver)
        sell_form = finance.sell_form

        account.Actions.sign_in(account.form, os.environ.get("LOGIN"), os.environ.get("PASS"))

        finance.Actions.open_card(finance.currency_list)
        before = finance.Actions.get_wallet_status(sell_form)

        amount = 10
        finance.Actions.fill_sell_form(sell_form, amount)
        finance.Actions.click_sell_button(sell_form)
        finance.Actions.wait_message(sell_form)

        after = finance.Actions.get_wallet_status(sell_form)

        self.assertEqual(before - after, amount)
