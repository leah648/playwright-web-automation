Playwright Web Automation
This project leverages Playwright for web automation, pytest for testing, Allure for reporting, and Poetry for dependency management.

Table of Contents
Installation
Usage
Tests
Allure Reports
Project Structure
Contributing
License
Installation
Clone the repository:
git clone https://github.com/leah648/playwright-web-automation
cd playwright_web_automation

Install Poetry: Follow the instructions on Poetry’s official website to install Poetry.
Install dependencies:
poetry install

Install Playwright browsers:
poetry run playwright install

Usage
To run the tests, use the following command:

poetry run pytest

Allure Reports
To generate and view Allure reports:

Run tests with Allure:
poetry run pytest --alluredir=allure-results

Generate and serve the Allure report:
allure serve allure-results

Project Structure
playwright_web_automation/
├── tests/
│   ├── test_register_login_and_send_contact_message.py
│   └── ...
├── pages/
│   ├── base_page.py
│   ├── register_page.py
│   ├── login_page.py
│   ├── secured_area_page.py
│   └── contact_page.py
├── enums/
│   └── notification.py
├── utils/
│   └── allure_logger.py
├── conftest.py
├── config.ini
├── pyproject.toml
└── README.md

Contributing
Contributions are welcome! Feel free to submit issues, fork the repository, and send pull requests.

License
This project is licensed under the MIT License.

