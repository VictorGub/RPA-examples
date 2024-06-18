import pytest

from utils.base_test import BaseTest


@pytest.mark.usefixtures("auto_login")
class AutoLoginTest(BaseTest):
    pass
