import platform

from selenium import webdriver


class WebDriver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()

    def add_option(self, option):
        self.options.add_argument(option)

    def add_options(self, options):
        for option in options:
            self.options.add_argument(option)

    def create_driver(self):
        os_type = platform.system().lower()
        driver = ""
        # os - Windows
        if "windows" in os_type:
            driver = "chromedriver.exe"
        # os - Mac
        elif "darwin" in os_type:
            driver = "chromedriver"
        # os - Linux : 나중에 사용자가 있다면 추가
        elif "linux" in os_type:
            pass
        return webdriver.Chrome("../resources/" + driver, options=self.options)