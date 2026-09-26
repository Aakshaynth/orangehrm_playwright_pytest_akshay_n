import pytest
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from pages.header_panel import HeaderPanel

# Test: Verify login functionality
# Purpose: Ensures user can log in successfully with valid credentials
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order(8)
def test_verify_user_able_to_logout_successfully_from_application(login_logout, test_data):
    # Step 1: Create LogoutPage object
    page = login_logout
    login_page = LoginPage(page)
    header_panel = HeaderPanel(page)

    # Step 2: Click Log out option from Header
    header_panel.log_out()

    # Step 3: Verify user redirected Login page
    login_page.verify_current_url(test_data["login_url"])

