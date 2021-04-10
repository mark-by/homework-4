from testutils import Page
from .components import SignInFrom


class AccountPage(Page):
    base_url = 'https://account.mail.ru'

    @property
    def form(self):
        return SignInFrom(self.driver)
