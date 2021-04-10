from selenium.webdriver import Remote


class Component(object):
    locators = {}
    container = ''

    def __init__(self, driver: Remote):
        self.driver = driver
