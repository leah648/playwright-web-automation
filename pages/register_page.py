from playwright.sync_api import Page
from pages.base_page import BasePage

class RegisterPage(BasePage):
    """
    RegisterPage class to handle interactions with the registration page.

    Attributes:
        username_input (Locator): Locator for the username input field.
        password_input (Locator): Locator for the password input field.
        confirm_password_input (Locator): Locator for the confirm password input field.
        register_button (Locator): Locator for the register button.
    """
    
    def __init__(self, page: Page):
        """
        Initializes the RegisterPage with the given Playwright Page object.

        Args:
            page (Page): The Playwright Page object.
        """
        super().__init__(page)
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password", exact=True)
        self.confirm_password_input = page.get_by_label("Confirm Password")
        self.register_button = page.get_by_role("button", name="Register")

    def fill_username(self, username: str):
        """
        Fills the username input field.

        Args:
            username (str): The username to enter in the form.
        """
        self.logger.info(f"Filling username: {username}")
        self.username_input.fill(username)

    def fill_password(self, password: str):
        """
        Fills the password input field.

        Args:
            password (str): The password to enter in the form.
        """
        self.logger.info(f"Filling password: {password}")
        self.password_input.fill(password)

    def fill_confirm_password(self, password: str):
        """
        Fills the confirm password input field.

        Args:
            password (str): The password to enter in the form.
        """
        self.logger.info(f"Filling confirm password: {password}")
        self.confirm_password_input.fill(password)

    def click_register(self):
        """
        Clicks the register button to submit the form.
        """
        self.logger.info("Clicking the register button")
        self.register_button.click()

    def register(self, username: str, password: str):
        """
        Registers a new user by filling out the registration form and clicking the register button.

        Args:
            username (str): The username to enter in the form.
            password (str): The password to enter in the form.
        """
        self.fill_username(username)
        self.fill_password(password)
        self.fill_confirm_password(password)
        self.click_register()
