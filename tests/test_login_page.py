import pytest
from pages.login_page import LoginPage

# Test: Verify login functionality
# Purpose: Ensures user can log in successfully with valid credentials
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order(1)
def test_verify_user_able_to_login_successfully_with_valid_credentials(page, credentials, test_data):
    # Step 1: Create LoginPage object
    login = LoginPage(page)

    # Step 2: Navigate to login page
    login.goto(test_data["base_url"])

    # Step 3: Perform login using credentials fixture
    login.login(credentials["username"], credentials["password"])

    # Step 4: Verify login success (Dashboard visible)
    login.verify_successfull_login()
    
    # Step 5: Verify current URL matches expected dashboard URL
    login.verify_current_url(test_data["dashboard_url"])