import pytest
import json
import os
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.header_panel import HeaderPanel


# Fixture: Playwright instance
# Purpose: Starts Playwright once per test session and provides access to browser engines.
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

# Fixture: Browser
# Purpose: Launches a Chromium browser once per session.
@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

# Fixture: Page
# Purpose: Creates a new browser context + page for each test function.
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    context.set_default_timeout(30000)
    context.set_default_navigation_timeout(30000)
    expect.set_options(timeout=60000)
    yield page
    context.close()

# Fixture: Test Data
# Purpose: Loads test data from JSON file for data-driven testing.
@pytest.fixture(scope="session")
def test_data() -> dict:
    file_path = "config/testdata.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

@pytest.fixture(scope="session")
def test_data_updater(test_data):
    file_path = "config/testdata.json"

    def update(new_data: dict):
        # Deep merge instead of shallow overwrite
        for key, value in new_data.items():
            if isinstance(value, dict) and key in test_data and isinstance(test_data[key], dict):
                test_data[key].update(value)
            else:
                test_data[key] = value

        with open(file_path, "w") as f:
            json.dump(test_data, f, indent=4)

    return update

# Fixture: Credentials
# Purpose: Loads demo login credentials from JSON.
# Note: For assignment simplicity, creds are in repo.
# In real projects, use env vars or secret managers.
@pytest.fixture(scope="session")
def credentials():
    with open("config/credentials.json") as f:
        return json.load(f)

# Fixture: Login + Logout
# Purpose: Provides a logged-in page for tests and ensures logout after each test.
@pytest.fixture(scope="function")
def login_logout(page, credentials, test_data, test_data_updater):
    login = LoginPage(page)
    login.goto(test_data["base_url"])
    login.login(credentials["username"], credentials["password"])
    login.verify_successfull_login()
    yield page

# Fixture: Session Cookie
# Purpose: Extracts the 'orangehrm' session cookie after login for authenticated API calls.
@pytest.fixture(scope="function")
def session_cookie(login_logout):
    cookies = login_logout.context.cookies()
    return next(c['value'] for c in cookies if c['name'] == 'orangehrm')
