import logging
import allure
from playwright.sync_api import Page
from playwright.sync_api import expect
import pytest
from enums.notifications import Notifications
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.contact_page import ContactPage
from pages.secured_area_page import SecuredAreaPage



@pytest.mark.sanity
@allure.parent_suite('Sanity')
@allure.suite("Full Flows")
@allure.feature("User Registration and Contact")
@allure.story("Register, login, and send a notification")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("User Registration, Login, and Contact Message Sending Flow")
def test_register_login_and_send_contact_message(
    page: Page, user: str, password: str, application_url: str
):
    """
    Test the user registration, login, and contact message sending flow.

    This test covers the following steps:
    1. Go to the registration page.
    2. Register a new user and verify successful registration.
    3. Login with the new user and verify successful login.
    4. Navigate to the contact page.
    5. Send a contact message and verify success.

    Args:
        page (Page): The Playwright Page object.
        user (str): The username for registration and login.
        password (str): The password for registration and login.
        application_url (str): The base URL of the application.
    """
    
    register_page = RegisterPage(page)
    login_page = LoginPage(page)
    secured_area_page = SecuredAreaPage(page)
    contact_page = ContactPage(page)
    logger = logging.getLogger()

    with allure.step("Go to registration page"):
        page.goto(f"{application_url}/register")
        logger.info("Navigated to registration page")

    with allure.step("Register a new user and verify successful registration"):
        register_page.register(user, password)
        
        logger.info("Verify there are no errors")
        assert not register_page.is_error_notification_displayed(), (
            "Unexpected error notification displayed during registration"
        )
        
        logger.info("Verify user was redirected to login page")
        expect(page, "User was not redirected to login page").to_have_url(
            f"{application_url}/login"
        )
        
        logger.info("Verify correct success message appears")
        assert login_page.is_success_notification_displayed(
            Notifications.REGISTRATION_SUCCESS.value
        ), "Registration success notification not displayed"

    with allure.step("Login with the new user and verify successful login"):
        login_page.login(user, password)
        
        logger.info("Verify there are no errors")
        assert not login_page.is_error_notification_displayed(), (
            "Unexpected error notification displayed during login"
        )
        
        logger.info("Verify user was redirected to secure page")
        expect(page, "User was not redirected to secured area").to_have_url(
            f"{application_url}/secure"
        )

        logger.info("Verify correct success message")
        assert secured_area_page.is_success_notification_displayed(
            Notifications.LOGIN_SUCCESS.value
        ), "Login success notification not displayed"

    with allure.step("Navigate to contact page"):
        secured_area_page.click_contact()
        
        logger.info("Verify user was redirected to contact page")
        expect(page, "User was not redirected to contact page").to_have_url(
            f"{application_url}/contact"
        )

    with allure.step("Send a contact message and verify success"):
        contact_page.send_contact_message(
            user, 
            "test@gmail.com", 
            "This is a test message."
        )
        assert contact_page.is_success_notification_displayed(
            Notifications.MESSAGE_SENT_SUCCESS.value
        ), "Message send success notification not displayed"