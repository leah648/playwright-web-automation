import logging
from playwright.sync_api import Page
from playwright.sync_api import expect

class BasePage:
    """
    BasePage class to provide common functionality for all page objects.

    Attributes:
        page (Page): The Playwright Page object.
        logger (Logger): Logger for logging notifications.
        timeout (int): Timeout value for waiting for elements.
        success_notification_selector (str): CSS selector for success notifications.
        error_notification_selector (str): CSS selector for error notifications.
    """
    
    def __init__(self, page: Page, timeout: int = 5000):
        """
        Initializes the BasePage with the given Playwright Page object and timeout.

        Args:
            page (Page): The Playwright Page object.
            timeout (int): Timeout value for waiting for elements. Default is 5000 milliseconds.
        """
        self.page = page
        self.logger = logging.getLogger()
        self.timeout = timeout
        self.success_notification_selector = "#flash"
        self.error_notification_selector = ".alert-danger"
        
    def is_success_notification_displayed(self, text: str) -> bool:
        try:
            self.page.wait_for_selector(self.success_notification_selector, timeout=self.timeout)
            message = self.page.inner_text(self.success_notification_selector)
            if message == text:
                self.logger.info(f"Success message displayed: {message}")
                return True
            else:
                self.logger.warning(f"Success message text mismatch: expected '{text}', got '{message}'")
                return False
        except TimeoutError:
            self.logger.error("Success message not displayed within the expected time.")
            return False
        except Exception as e:
            self.logger.error(f"An error occurred while checking success message: {e}")
            return False
    
    def is_error_notification_displayed(self) -> bool:
        try:
            self.page.wait_for_selector(self.error_notification_selector, timeout=self.timeout)
            return True
        except TimeoutError:
            self.logger.debug("Error message not displayed within the expected time.")
            return False
        except Exception as e:
            self.logger.error(f"An error occurred while checking error message: {e}")
            return False
    
    def click_element(self, element) -> bool:
        """
        Clicks on the given element if it is visible.

        Args:
            element: The element to be clicked.

        Returns:
            bool: True if the element was clicked successfully, False otherwise.
        """
        try:
            expect(element).to_be_visible()
            element.click()
        except TimeoutError:
            self.logger.error(f"Element {element} not found or not visible.")
            return False
        return True

    def fill_element(self, element, text: str) -> bool:
        """
        Fills the given element with the specified text if it is visible.

        Args:
            element: The element to be filled.
            text (str): The text to fill into the element.

        Returns:
            bool: True if the element was filled successfully, False otherwise.
        """
        try:
            expect(element).to_be_visible()
            element.fill(text)
        except TimeoutError:
            self.logger.error(f"Element {element} not found or not visible.")
            return False
        return True

