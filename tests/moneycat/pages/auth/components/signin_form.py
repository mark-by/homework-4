from testutils import Component
from selenium.webdriver.common.by import By


class SignInForm(Component):
    container = '[data-test-id=modal]'

    class Selectors:
        login = 'input[type="email"]'
        password = 'input[type="password"]'
        next_button = '[data-test-id="next-button"]'
        submit_button = 'input[type="submit"]'
        user_email_header = 'p[id="account"]'
        redirect_to_signin = 'a[class="signin-link"]'

    def go_to_signin(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.redirect_to_signin)
        return self.driver.find_element_by_css_selector(self.Selectors.redirect_to_signin).click()

    def get_user_email(self) -> str:
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.user_email_header)
        return self.driver.find_element_by_css_selector(self.Selectors.user_email_header).text

    def fill_login(self, username):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.login, username)

    def next(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.next_button)
        self.driver.find_element_by_css_selector(self.Selectors.next_button).click()

    def fill_password(self, password):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.password, password)

    def submit(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.submit_button)
        self.driver.find_element_by_css_selector(self.Selectors.submit_button).click()
