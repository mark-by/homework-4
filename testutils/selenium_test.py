import unittest
from .utils import CurrentBrowser


GlobalCurrentBrowser = CurrentBrowser()


class SeleniumTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = GlobalCurrentBrowser.get()

    def tearDown(self) -> None:
        self.driver.quit()
