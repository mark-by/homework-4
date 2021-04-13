import testutils
from .components import SignInFrom

class Authorization(testutils.Page):
  base_url = "https://softree.group"
  path = "signin"

  class Actions:
    @staticmethod
    def sign_in(form: SignInFrom, username, password) -> str:
      form.fill_login(username)
      form.next()
      form.fill_password(password)
      form.submit()
      return form.get_user_email()

  @property
  def form(self):
    return SignInFrom(self.driver)
