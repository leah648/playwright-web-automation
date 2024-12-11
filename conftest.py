import configparser
import logging
import pytest
import allure
from slugify import slugify
from playwright.sync_api import Page
from utils.allure_logger import AllureLogger

logger = logging.getLogger()

@pytest.fixture(scope='session')
def config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT']

@pytest.fixture
def user(config):
    return config['User']

@pytest.fixture
def password(config):
    return config['Password']

@pytest.fixture
def application_url(config):
    return config['ApplicationURL']

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict) -> dict:
    """
    Fixture to configure browser type launch arguments for the entire session.

    Args:
        browser_type_launch_args (dict): Existing browser type launch arguments.

    Returns:
        dict: Updated browser type launch arguments.
    """
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 600,
        "args": ["--start-maximized"]
    }

@pytest.fixture
def browser_context_args(
    browser_context_args: dict,
    tmpdir_factory: pytest.TempdirFactory
) -> dict:
    """
    Fixture to configure browser context arguments for each test case.

    Args:
        browser_context_args (dict): Existing browser context arguments.
        tmpdir_factory (pytest.TempdirFactory): Factory for creating temporary directories.

    Returns:
        dict: Updated browser context arguments.
    """
    context_args = {
        **browser_context_args,
        "no_viewport": True,
        "record_video_dir": tmpdir_factory.mktemp('videos'),
        "accept_downloads": True
    }
    
    return context_args


def pytest_runtest_makereport(item, call) -> None:
    """
    Custom hook to attach screenshots and videos to Allure report.

    Args:
        item: The test item.
        call: The call information.

    Returns:
        None
    """
    if call.when == "call":
        if call.excinfo is not None and "page" in item.funcargs:
            page: Page = item.funcargs["page"]
            try:
                allure.attach(
                    page.screenshot(type='png'),
                    name=f"{slugify(item.nodeid)}.png",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                logger.error(f"Error attaching screenshot: {e}")

            try:
                video_path = page.video.path()
                page.context.close()  # Ensure video is saved
                allure.attach(
                    open(video_path, 'rb').read(),
                    name=f"{slugify(item.nodeid)}.webm",
                    attachment_type=allure.attachment_type.WEBM
                )
            except Exception as e:
                logger.error(f"Error attaching video: {e}")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Configures the logging settings for pytest.

    This function sets up the logging configuration for pytest, ensuring that log messages
    are captured and sent to the Allure report. It sets the logging level to INFO and adds
    the custom AllureLogger handler if it is not already present.

    Args:
        config: The pytest configuration object.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    allure_logger = AllureLogger()
    if allure_logger not in logger.handlers:
        logger.addHandler(allure_logger)






