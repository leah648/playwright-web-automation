from playwright.sync_api import Page
from pages.base_page import BasePage

class SecuredAreaPage(BasePage):
    """
    SecuredAreaPage class to handle interactions with the secured area page.

    Attributes:
        contact_button: Locator for the contact button.
    """
    
    def __init__(self, page: Page):
        """
        Initializes the SecuredAreaPage with the given Playwright Page object.

        Args:
            page (Page): The Playwright Page object.
        """
        super().__init__(page)
        self.contact_button = page.get_by_role("link", name="Contact")

    def click_contact(self):
        """
        Clicks the contact button to navigate to the contact page.
        """
        self.logger.info(f"Open Contact form by clicking Contact link on Bar")
        self.contact_button.click()