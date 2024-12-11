import allure
import logging
from datetime import datetime

class AllureLogger(logging.Handler):
    """
    Custom logging handler that emits log messages to Allure report.

    Usage:
    logger = logging.getLogger(__name__)
    allure_handler = AllureLogger()
    logger.addHandler(allure_handler)
    logger.info("This is an info message")
    """

    def emit(self, record: logging.LogRecord) -> None:
        """
        Emit a log record to Allure report.

        Args:
            record (logging.LogRecord): The log record to emit.
        """

        now = datetime.now()  # current date and time
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        if record.levelno >= logging.INFO:
            with allure.step(f'{date_time} LOG ({record.levelname}): {record.getMessage()}'):
                pass