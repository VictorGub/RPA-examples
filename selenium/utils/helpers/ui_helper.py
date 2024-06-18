from selenium.common.exceptions import (NoAlertPresentException, NoSuchElementException, StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class UIHelper:
    """
    All actions from selenium that are common
    """

    @staticmethod
    def wait_until_element_is_displayed(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout, ignored_exceptions=StaleElementReferenceException)
        try:
            wait.until(ec.visibility_of_element_located(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def wait_until_element_clickable(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout, ignored_exceptions=StaleElementReferenceException)
        try:
            element = wait.until(ec.element_to_be_clickable(locator))
            return element
        except (NoSuchElementException, TimeoutException) as err:
            raise Exception("Element isn't clickable") from err

    @staticmethod
    def wait_until_element_is_not_visible(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout, ignored_exceptions=StaleElementReferenceException)
        try:
            wait.until(ec.invisibility_of_element_located(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def wait_until_element_disappear(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout, ignored_exceptions=StaleElementReferenceException)
        try:
            wait.until_not(ec.presence_of_element_located(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def wait_until_element_appears(driver, locator, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout, ignored_exceptions=StaleElementReferenceException)
        try:
            wait.until(ec.presence_of_element_located(locator))
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @staticmethod
    def click(driver, locator, timeout=5):
        if not UIHelper.wait_until_element_is_displayed(driver, locator, timeout=timeout):
            raise Exception("Element is missing on the page")
        element = UIHelper.wait_until_element_clickable(driver, locator)
        element.click()

    @staticmethod
    def return_element(driver, locator, timeout=5):
        if UIHelper.wait_until_element_is_displayed(driver, locator, timeout=timeout):
            element = driver.find_element(*locator)
            return element
        raise Exception("Element is missing on the page")

    @staticmethod
    def return_elements(driver, locator, timeout=5):
        if UIHelper.wait_until_element_is_displayed(driver, locator, timeout=timeout):
            element = driver.find_elements(*locator)
            return element
        raise Exception("Element is missing on the page")

    @staticmethod
    def return_element_text(driver, locator, timeout=5):
        if UIHelper.wait_until_element_is_displayed(driver, locator, timeout=timeout):
            element = driver.find_element(*locator)
            return element.text
        raise Exception("Elements are missing on the page")

    @staticmethod
    def return_element_attribute(driver, locator, attribute, timeout=5):
        if UIHelper.wait_until_element_is_displayed(driver, locator, timeout=timeout):
            element = driver.find_element(*locator)
            return element.get_attribute(attribute)
        raise Exception("Element is missing on the page")

    @staticmethod
    def type_keys(driver, locator, value, clear_text=True, timeout=5):
        if not UIHelper.wait_until_element_is_displayed(driver, locator, timeout=timeout):
            raise Exception("Element is missing on the page")
        element = UIHelper.wait_until_element_clickable(driver, locator)
        if clear_text:
            element.clear()
        element.send_keys(value)

    @staticmethod
    def wait_until_alert_is_displayed(driver, timeout=5):
        wait = WebDriverWait(driver, timeout=timeout, ignored_exceptions=StaleElementReferenceException)
        return wait.until(ec.alert_is_present())

    @staticmethod
    def accept_alert(driver):
        try:
            alert = UIHelper.wait_until_alert_is_displayed(driver)
            alert.accept()
        except NoAlertPresentException as err:
            raise Exception("Alert is missing") from err

    @staticmethod
    def dismiss_alert(driver):
        try:
            alert = UIHelper.wait_until_alert_is_displayed(driver)
            alert.dismiss()
        except NoAlertPresentException as err:
            raise Exception("Alert is missing") from err

    @staticmethod
    def get_text_from_alert(driver):
        try:
            alert = UIHelper.wait_until_alert_is_displayed(driver)
            return alert.text
        except NoAlertPresentException as err:
            raise Exception("Alert is missing") from err

    @staticmethod
    def scroll_to_element(driver, web_element):
        driver.execute_script("arguments[0].scrollIntoView()", web_element)

    @staticmethod
    def click_on_element(driver, web_element):
        driver.execute_script("return arguments[0].click()", web_element)

    @staticmethod
    def scroll_to_the_bottom(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @staticmethod
    def is_element_checked(driver, locator, timeout=5):
        if UIHelper.wait_until_element_is_displayed(driver, locator, timeout=timeout):
            return driver.find_element(*locator).is_selected()
        raise Exception("Element is missing on the page")

    @staticmethod
    def get_current_window(driver):
        return driver.window_handles[0]

    @staticmethod
    def get_new_window(driver):
        return driver.window_handles[1]

    @staticmethod
    def switch_to_window(driver, window):
        return driver.switch_to_window(window)
