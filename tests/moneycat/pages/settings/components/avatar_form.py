from testutils import Component
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AvatarForm(Component):
    container = '[data-test-id=settings__window]'

    class Selectors:
        email = 'p[id="username"]'
        submit = 'input[type="submit"]'
        errors = 'div[id="message-content"]'
        success_msg = 'div[class="message-content"]'

    def upload_file(self, path_to_file: str) -> None:
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.submit)
        submit = self.driver.find_element_by_css_selector(self.Selectors.submit)
        submit.click()
        submit.send_keys(path_to_file + Keys.RETURN)

    @property
    def email(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.email)
        return self.driver.find_element_by_css_selector(self.Selectors.email)

    @property
    def success_msg(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.success_msg)
        return self.driver.find_element_by_css_selector(self.Selectors.success_msg)

    @property
    def errors(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.errors)
        return self.driver.find_element_by_css_selector(self.Selectors.errors)
