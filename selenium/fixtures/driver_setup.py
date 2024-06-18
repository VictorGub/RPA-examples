import logging

import pytest

from utils.browser import Browser
from utils.helpers.common_actions import CommonActions
from utils.helpers.config_provider import settings_config


@pytest.fixture()
def base_driver_setup(request):
    test_name = request.node.test_name_
    logging.info("Start test: %s", test_name)
    browser = Browser()
    driver = browser.get_browser()
    driver.get(settings_config["base_site_url"])
    request.cls.driver = driver
    yield
    if request.node.rep_setup.failed or request.node.rep_call.failed:
        CommonActions.create_screenshot(driver, test_name)
    driver.quit()
