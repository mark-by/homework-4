from tests.moneycat import MoneyCatAuthTest, MoneyCatSettingsTest, MoneyCatMainTest, MoneyCatRegistrationTest, MoneyCatConverterTest
from tests.todo import TaskTest, TaskListTest, SortTest

CHROME_BIN = './bin/mac_m1/chromedriver'
FIREFOX_BIN = './bin/mac_m1/geckodriver'
SELENIUM_BIN = 'bin/selenium.jar'

TESTS = [
    MoneyCatRegistrationTest,
    MoneyCatConverterTest
    MoneyCatMainTest,
    MoneyCatAuthTest,
    MoneyCatSettingsTest,
    TaskListTest,
    TaskTest,
    SortTest
]
