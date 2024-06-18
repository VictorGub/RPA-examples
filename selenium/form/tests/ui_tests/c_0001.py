from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from form.pages.base_page import BasePage
from utils.base_test import BaseTest
from utils.helpers.common_actions import CommonActions

NAME = "John"
LAST_NAME = "Doe"
EMAIL = "test@example.com"
COMPANY = "Test"
DD_OPTION = "Development solutions"


class C0001(BaseTest):
    def test_c0001(self):
        website_page = BasePage(self.driver)
        website_page.driver.find_element(by=By.CSS_SELECTOR, value="input[name='Name_First']").send_keys(NAME)
        website_page.driver.find_element(by=By.CSS_SELECTOR, value="input[name='Name_Last']").send_keys(LAST_NAME)
        website_page.driver.find_element(by=By.CSS_SELECTOR, value="input[name='Email']").send_keys(EMAIL)
        website_page.driver.find_element(by=By.CSS_SELECTOR, value="input[name='SingleLine']").send_keys(COMPANY)
        select = Select(website_page.driver.find_element(by=By.CSS_SELECTOR, value="select[name='Dropdown']"))
        select.select_by_visible_text(DD_OPTION)
        CommonActions.create_screenshot(website_page.driver, "result")
