import distutils.util
import logging
import os.path
import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from project_constants import project_path
from utils.helpers.config_provider import settings_config
from utils.helpers.singleton import singleton


@singleton
class Browser:
    def __init__(self):
        self.os_type = platform.system().lower()
        logging.info("OS: %s", self.os_type)
        self.download_path = os.path.join(project_path, "output_test_files")

    @staticmethod
    def set_chrome_options(options):
        logging.info("Set Chrome Options")
        options.add_argument("--headless")
        options.add_argument("--kiosk")
        options.add_argument("--no-sandbox")
        options.add_argument("--verbose")
        options.add_argument("--lang=en")
        options.add_argument("--enable-logging")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-proxy-server")
        options.add_argument("--disable-setuid-sandbox")

    def set_browser(self):
        browser = settings_config["browser"]
        logging.info("Browser: %s", browser)
        if browser == "chrome":
            chrome_options = Options()
            chrome_options.add_experimental_option(
                "prefs",
                {
                    "download.default_directory": self.download_path,
                    "download.prompt_for_download": False,
                    "download.directory_upgrade": True,
                    "safebrowsing.enabled": True,
                },
            )
            if distutils.util.strtobool(settings_config["chrome_headless_mode"]):
                chrome_options.add_argument("--headless")
            if "linux" in self.os_type:
                self.set_chrome_options(chrome_options)
            # Run browser
            driver = webdriver.Chrome(options=chrome_options)
            # Set browser window size
            driver.set_window_size(1920, 1080)
            return driver
        return None

    def get_browser(self):
        return self.set_browser()

    @staticmethod
    def close_browser(driver):
        logging.info("Close browser")
        driver.quit()

    @staticmethod
    def open_web_page(driver, url):
        logging.info("Open web page: %s", str(url))
        driver.get(url)

    @staticmethod
    def refresh_browser(driver):
        logging.info("Refresh page")
        driver.refresh()
