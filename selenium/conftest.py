import platform

import pytest

from utils.helpers.common_actions import CommonActions
from utils.helpers.config_provider import settings_config

# pylint: disable=W0212, C0103

pytest_plugins = "fixtures.driver_setup"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_{}".format(report.when), report)
    report.description = str(item.function.__doc__)


def pytest_runtest_setup(item):
    """
    Setup test_name_ global pytest variable
    """
    test_name = item.name.replace("test_", "")
    setattr(item, "test_name_", test_name)


def is_master(config):
    """
    :param config: config
    :return: True when xdist master node
    """
    return not hasattr(config, "slaveinput")


def pytest_configure(config):
    if is_master(config):
        if settings_config["clean_screenshot_folder"]:
            CommonActions.clean_screenshot_folder()
