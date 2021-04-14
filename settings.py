
from tests.moneycat import MoneyCatAuthTest, MoneyCatSettingsTest, MoneyCatMainTest
from tests.todo import TaskTest, TaskListTest, SortTest

CHROME_BIN = './bin/mac_m1/chromedriver'
FIREFOX_BIN = './bin/mac_m1/geckodriver'
SELENIUM_BIN = 'bin/selenium.jar'

TESTS = [
    # TaskTest,
    # TaskListTest,
    # MoneyCatAuthTest,
    MoneyCatMainTest,
    MoneyCatAuthTest,
    MoneyCatSettingsTest,
    TaskListTest,
    TaskTest,
    SortTest
]

BROWSERS = [
    'CHROME',
    'FIREFOX',
]
