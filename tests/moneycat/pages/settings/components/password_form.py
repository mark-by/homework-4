from testutils import Component
from selenium.webdriver.common.by import By


class PasswordForm(Component):
    container = '[data-test-id=settings__window]'

    class Selectors:
        password = 'input[name="oldPassword"]'
        new_password = 'input[name="newPassword"]'
        repeat_password = 'input[name="repeatPassword"]'
        submit = 'input[type="submit"]'
        error = 'p[class="field__error"]'

    def fill_form(self, old_pass, new_pass, repeat_pass):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.password)
        self._fill_input(By.CSS_SELECTOR, self.Selectors.password, old_pass, True)

        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.password)
        self._fill_input(By.CSS_SELECTOR, self.Selectors.new_password, new_pass, True)

        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.password)
        self._fill_input(By.CSS_SELECTOR, self.Selectors.repeat_password, repeat_pass, True)

    def submit(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.submit)
        self.driver.find_element_by_css_selector(self.Selectors.submit).click()

    @property
    def errors(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.error)
        return self.driver.find_element_by_css_selector(self.Selectors.error)

    @property
    def password(self):
        return self.driver.find_element_by_css_selector(self.Selectors.password)
