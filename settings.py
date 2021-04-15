from tests.todo import TaskTest, TaskListTest, SortTest
from tests.moneycat import MoneyCatAuthTest, MoneyCatRegistrationTest, MoneyCatConverterTest, MoneyCatSettingsTest,\
    MoneyCatMainTest

CHROME_BIN = 'bin/mac_m1/chromedriver'
FIREFOX_BIN = 'bin/mac_m1/geckodriver'
SELENIUM_BIN = 'bin/selenium.jar'

TESTS = [
    MoneyCatMainTest,
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
