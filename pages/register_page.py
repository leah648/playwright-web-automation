from playwright.sync_api import Page
from pages.base_page import BasePage

class RegisterPage(BasePage):
    """
    RegisterPage class to handle interactions with the registration page.

    Attributes:
        username_input: Locator for the username input field.
        password_input: Locator for the password input field.
        confirm_password_input: Locator for the confirm password input field.
        register_button: Locator for the register button.
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

    def register(self, username: str, password: str):
        """
        Registers a new user by filling out the registration form and clicking the register button.

        Args:
            username (str): The username to enter in the form.
            password (str): The password to enter in the form.
        """
        self.logger.info(f"Fill username {username} on username input")
        self.username_input.fill(username)
        self.logger.info(f"Fill password {password} on password input")
        self.password_input.fill(password)
        self.logger.info(f"Fill password {password} on Confirm Password input")
        self.confirm_password_input.fill(password)
        self.logger.info(f"Click Register button")
        self.register_button.click()