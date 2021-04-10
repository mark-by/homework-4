from testutils import Component


class SignInFrom(Component):
    container = '[data-test-id=login-app-ready]'
    locator_login = 'input[name="username"]'
    locators = {
        'password': 'input[name="password"]',
        'next_button': '[data-test-id="next-button"]',
        'submit_button': '[data-test-id="submit-button"]',
        'user_email_header': '#PH_user-email',
    }

    def fill_login(self, username):
        login_input = self.driver.find_element_by_css_selector(self.locators['login'])
        login_input.click()
        login_input.send_keys(username)

    def next(self):
        self.driver.find_element_by_css_selector(self.locators['next-button'])