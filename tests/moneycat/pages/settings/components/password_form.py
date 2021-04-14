from testutils import Component
from selenium.webdriver.common.by import By


class PasswordForm(Component):
    container = '[data-test-id=settings__window]'

    class Selectors:
        password = 'input[name="oldPassword"]'
        new_password = 'input[name="newPassword"]'
        repeat_password = 'input[name="repeatPassword"]'
        submit = 'input[type="submit"]'
        errors = 'p[class="field__error"]'
        success_msg = 'div[class="message-content"]'

    def clear_input(self):
        self._clear_input(By.CSS_SELECTOR, self.Selectors.password)
        self._clear_input(By.CSS_SELECTOR, self.Selectors.new_password)
        self._clear_input(By.CSS_SELECTOR, self.Selectors.repeat_password)

    def fill_form(self, old_pass, new_pass, repeat_pass):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.password, old_pass, True)
        self._fill_input(By.CSS_SELECTOR, self.Selectors.new_password, new_pass, True)
        self._fill_input(By.CSS_SELECTOR, self.Selectors.repeat_password, repeat_pass, True)

    def submit(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.submit)
        self.driver.find_element_by_css_selector(self.Selectors.submit).click()

    @property
    def errors(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.errors)
        return self.driver.find_element_by_css_selector(self.Selectors.errors)

    @property
    def success_msg(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.success_msg)
        return self.driver.find_element_by_css_selector(self.Selectors.success_msg)

    @property
    def password(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.password)
        return self.driver.find_element_by_css_selector(self.Selectors.password)
