import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from .pages import AccountPage


class AuthTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self) -> None:
        self.driver.quit()

    def test(self):
        account = AccountPage(self.driver)
        account.open()
