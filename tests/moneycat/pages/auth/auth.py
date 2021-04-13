from testutils import Page
from .components import SignInForm

class Authorization(testutils.Page):
  base_url = "https://softree.group"
  path = "signup"

class AuthPage(Page):
    base_url = "https://softree.group"
    path = "signin"

    class Actions:
        @staticmethod
        def sign_in(form: SignInForm, username, password) -> str:
            form.go_to_signin()
            form.fill_login(username)
            form.fill_password(password)
            form.submit()
            return form.get_user_email()

    @property
    def form(self):
        return SignInForm(self.driver)
