import sys
from multiprocessing import Process
from typing import List
import subprocess

import unittest

import settings
from tests.todo import AuthTest

TESTS = [AuthTest]


def run_tests(tests: List):
    suites = []
    for test in tests:
        suites.append(unittest.makeSuite(test))
    suite = unittest.TestSuite(suites)
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())


def init_grid():
    subprocess.call(['sh', './grid.sh', settings.SELENIUM_BIN])


def init_node():
    subprocess.call(['sh', './node.sh', settings.CHROME_BIN, settings.FIREFOX_BIN, settings.SELENIUM_BIN])


def run_selenium():
    grid = Process(target=init_grid)
    node = Process(target=init_node)
    grid.start()
    node.start()
    grid.join()
    node.join()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            run_tests(TESTS)
        elif sys.argv[1] == 'run_selenium':
            run_selenium()
    print("Usage: python manage.py [test, run_selenium]")



