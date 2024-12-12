from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    LoginPage class to handle interactions with the login page.

    Attributes:
        username_input (Locator): Locator for the username input field.
        password_input (Locator): Locator for the password input field.
        login_button (Locator): Locator for the login button.
    """
    
    def __init__(self, page: Page):
        """
        Initializes the LoginPage with the given Playwright Page object.

        Args:
            page (Page): The Playwright Page object.
        """
        super().__init__(page)
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        
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
        self.fill_element(self.password_input, password)

    def click_login(self):
        """
        Clicks the login button to submit the form.
        """
        self.logger.info("Clicking the login button")
        self.click_element(self.login_button)
        
    def login(self, username: str, password: str):
        """
        Logs in the user by filling out the login form and clicking the login button.

        Args:
            username (str): The username to enter in the form.
            password (str): The password to enter in the form.
        """
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()