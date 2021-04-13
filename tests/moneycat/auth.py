import os

from .utils import TestCase
from .pages.auth import AuthPage

class MoneyCatAuthTest(TestCase):
  def test_login(self):
    account = AuthPage(self.driver)
    account.open()

    login_form = account.form
    
    self.assertEqual(
      account.Actions.sign_in(
        login_form,
        os.environ.get("LOGIN"),
        os.environ.get("PASS")
      ),
      os.environ.get("LOGIN")
    )
