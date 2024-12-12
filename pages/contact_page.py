from playwright.sync_api import Page
from pages.base_page import BasePage

class ContactPage(BasePage):
    """
    ContactPage class to handle interactions with the contact page.

    Attributes:
        name_input (Locator): Locator for the name input field.
        email_address_input (Locator): Locator for the email input field.
        message_textarea (Locator): Locator for the address textarea.
        send_button (Locator): Locator for the send button.
    """
    
    def __init__(self, page: Page):
        """
        Initializes the ContactPage with the given Playwright Page object.

        Args:
            page (Page): The Playwright Page object.
        """
        super().__init__(page)
        self.name_input = page.locator('label:has-text("Name") + input')
        self.email_address_input = page.locator('label:has-text("Email") + input')
        self.message_textarea = page.locator('textarea[name="address"]')
        self.send_button = page.get_by_role("link", name="Send")

    def fill_name(self, name: str):
        """
        Fills the name input field.

        Args:
            name (str): The name to enter in the form.
        """
        self.logger.info(f"Filling name: {name}")
        self.name_input.fill(name)

    def fill_email(self, email: str):
        """
        Fills the email input field.

        Args:
            email (str): The email to enter in the form.
        """
        self.logger.info(f"Filling email: {email}")
        self.fill_element(self.email_address_input, email)

    def fill_address(self, address: str):
        """
        Fills the address textarea.

        Args:
            address (str): The address to enter in the form.
        """
        self.logger.info(f"Filling address: {address}")
        self.fill_element(self.message_textarea, address)

    def click_send(self):
        """
        Clicks the send button to submit the form.
        """
        self.logger.info("Clicking the send button")
        self.click_element(self.send_button)

    def send_contact_message(self, name: str, email: str, address: str):
        """
        Fills out and sends the contact form.

        Args:
            name (str): The name to enter in the form.
            email (str): The email to enter in the form.
            address (str): The address to enter in the form.
        """
        self.fill_name(name)
        self.fill_email(email)
        self.fill_address(address)
        self.click_send()