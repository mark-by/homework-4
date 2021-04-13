import testutils
from selenium.webdriver.common.by import By


class SellForm(testutils.Component):
    class Selectors:
        has_sell = '.opened-rate__btn-wrapper.sell .opened-rate__available'
        sell_button = '.opened-rate__btn.sell'
        buy_button = '.opened-rate__btn.buy'
        input = '[id=rate-amount-input]'
        message = '[class=message]'

    def wallet_status(self) -> float:
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.has_sell)
        return float(self.driver.find_element_by_css_selector(self.Selectors.has_sell).text)

    def fill_input(self, amount):
        self._fill_input(By.CSS_SELECTOR, self.Selectors.input, amount)

    def wait_for_message(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.message)

    def sell(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.sell_button)
        self.driver.find_element_by_css_selector(self.Selectors.sell_button).click()

    def buy(self):
        self._wait_clickable(By.CSS_SELECTOR, self.Selectors.buy_button)
        self.driver.find_element_by_css_selector(self.Selectors.buy_button).click()
