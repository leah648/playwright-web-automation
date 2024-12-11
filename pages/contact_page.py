from playwright.sync_api import Page
from pages.base_page import BasePage

class ContactPage(BasePage):
    """
    ContactPage class to handle interactions with the contact page.

    Attributes:
        name_input: Locator for the name input field.
        email_input: Locator for the email input field.
        address_textarea: Locator for the address textarea.
        send_button: Locator for the send button.
        notification_success_notification: Locator for the success notification notification.
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
        self.message_textarea = page.locator("textarea[name=\"address\"]")
        self.send_button = page.get_by_role("link", name="Send")

    def send_contact_message(self, name: str, email: str, address: str):
        """
        Fills out and sends the contact form.

        Args:
            name (str): The name to enter in the form.
            email (str): The email to enter in the form.
            address (str): The address to enter in the form.
        """
        self.logger.info(f"Fill name {name} on name input")
        self.name_input.fill(name)
        self.logger.info(f"Fill email {email} on email input")
        self.email_address_input.fill(email)
        self.logger.info(f"Fill address {address} on address input")
        self.message_textarea.fill(address)
        self.send_button.click()
    


