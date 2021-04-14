from selenium.webdriver import Remote, DesiredCapabilities


class CurrentBrowser:
    def __init__(self):
        self.browser = None
        self.driver = None

    def set(self, browser):
        self.browser = browser
        self.driver = self.__get_driver(browser)

    def get(self):
        return self.driver

    @staticmethod
    def __get_driver(browser):
        return Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
