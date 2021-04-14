from tests.todo import TaskTest, TaskListTest
from tests.moneycat import MoneyCatAuthTest, MoneyCatRegistrationTest, MoneyCatConverterTest, MoneyCatSettingsTest
from tests.todo import TaskTest, TaskListTest, SortTest

CHROME_BIN = './bin/mac_m1/chromedriver'
FIREFOX_BIN = './bin/mac_m1/geckodriver'
SELENIUM_BIN = 'bin/selenium.jar'

TESTS = [
    MoneyCatConverterTest,
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
