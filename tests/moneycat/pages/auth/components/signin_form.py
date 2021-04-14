from testutils import Component
from selenium.webdriver.common.by import By


class SignInForm(Component):
    container = '[data-test-id=modal]'

    class Selectors:
        login = 'input[type="email"]'
        password = 'input[type="password"]'
<<<<<<< HEAD
        submit_button = 'input[type="submit"]'
        account_header = 'p[id="account"]'
        href_to_signin = 'a[class="signin-link"]'
        error_message = 'p[class="field__error"]'
        href_to_signup = 'a[class="signup-link"]'
        registration_title = 'h2[class="modal__title"]'

    def go_to_signin(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.href_to_signin)
        return self.driver.find_element_by_css_selector(self.Selectors.href_to_signin).click()

    def get_account_header(self) -> str:
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.account_header)
        return self.driver.find_element_by_css_selector(self.Selectors.account_header).text

    def get_error_message(self) -> str:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.error_message)
        return self.driver.find_element_by_css_selector(self.Selectors.error_message).text
=======
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
>>>>>>> master

    def fill_login(self, username):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.login, username)

<<<<<<< HEAD
=======
    def next(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.next_button)
        self.driver.find_element_by_css_selector(self.Selectors.next_button).click()

>>>>>>> master
    def fill_password(self, password):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.password, password)

    def submit(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.submit_button)
        self.driver.find_element_by_css_selector(self.Selectors.submit_button).click()
<<<<<<< HEAD

    def click_signup_href(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.href_to_signup)
        self.driver.find_element_by_css_selector(self.Selectors.href_to_signup).click()

    def get_registration_title(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.registration_title)
        return self.driver.find_element_by_css_selector(self.Selectors.registration_title).text
=======
>>>>>>> master
