from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    LoginPage class to handle interactions with the login page.

    Attributes:
        username_input: Locator for the username input field.
        password_input: Locator for the password input field.
        login_button: Locator for the login button.
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
        
    def login(self, username: str, password: str):
        """
        Logs in the user by filling out the login form and clicking the login button.

        Args:
            username (str): The username to enter in the form.
            password (str): The password to enter in the form.
        """
        self.logger.info(f"Fill username {username} on username input")
        self.username_input.fill(username)
        self.logger.info(f"Fill password {password} on password input")
        self.password_input.fill(password)
        self.logger.info(f"Click login button")
        self.login_button.click()
    


