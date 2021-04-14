from selenium.webdriver.common.by import By

from testutils import Component
from datetime import datetime, timedelta


class DatePicker(Component):
    class Selectors:
        day = lambda month, day, year: f'button[data-test-id="date-{month}/{day}/{year}"]'

    def choose_day(self, from_today=0):
        date = datetime.now() + timedelta(days=from_today)
        selector = self.Selectors.day(date.month, date.day, date.year)
        self._wait_visible(By.CSS_SELECTOR, selector)
        self._wait_clickable(By.CSS_SELECTOR, selector)
        self._find(selector).click()
        self._dis_wait_visible(By.CSS_SELECTOR, selector)
