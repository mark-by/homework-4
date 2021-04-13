import testutils
from selenium.webdriver.common.by import By


class CurrencyList(testutils.Component):
    class Selectors:
        currency_card = '[class=rate-card]'

    def open_first_currency(self):
        self._wait_visible(By.CSS_SELECTOR, self.Selectors.currency_card)
        self.driver.find_element_by_css_selector(self.Selectors.currency_card).click()
