from .auth import MoneyCatAuthTest
from .pages.finance import FinancePage


class MoneyCatFinanceTest(MoneyCatAuthTest):
    def test_sell_success(self):
        finance = FinancePage(self.driver)
        sell_form = finance.sell_form

        finance.Actions.open_card(finance.currency_list)
        before = finance.Actions.get_wallet_status(sell_form)

        amount = 10
        finance.Actions.fill_sell_form(sell_form, amount)
        finance.Actions.click_sell_button(sell_form)
        finance.Actions.wait_message(sell_form)

        after = finance.Actions.get_wallet_status(sell_form)

        self.assertEqual(before - after, amount)
