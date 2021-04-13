import testutils
from ..auth.components import SignInFrom
from .components import SellForm
from .components import CurrencyList


class FinancePage(testutils.Page):
    base_url = "https://softree.group"
    path = "signin"

    class Actions:
        @staticmethod
        def open_card(currency_list: CurrencyList):
            currency_list.open_first_currency()

        @staticmethod
        def fill_sell_form(sell_form: SellForm, amount):
            sell_form.fill_input(amount)

        @staticmethod
        def click_sell_button(sell_form: SellForm):
            sell_form.sell()

        @staticmethod
        def get_wallet_status(sell_form: SellForm) -> str:
            return sell_form.wallet_status()

        @staticmethod
        def wait_message(sell_form: SellForm):
            sell_form.wait_for_message()

    @property
    def currency_list(self):
        return CurrencyList(self.driver)

    @property
    def sell_form(self):
        return SellForm(self.driver)

