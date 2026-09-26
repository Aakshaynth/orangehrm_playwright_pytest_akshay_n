from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page:Page):
        self.page = page

        # Locators for login elements
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("//button[normalize-space()='Login']")
        self.dashboard_page_header = page.locator("h6.oxd-topbar-header-breadcrumb-module")

    # Method: Navigate to login page
    # Purpose: Opens the OrangeHRM login URL
    def goto(self, base_url: str):
        self.page.goto(base_url, timeout=60000)  # Set a timeout of 60 seconds for navigation

    # Method: Perform login
    # Purpose: Enters username & password, clicks login button
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    # Method: Verify successful login
    # Purpose: Confirms login worked by checking Dashboard text
    def verify_successfull_login(self):
        expect(self.dashboard_page_header).to_contain_text("Dashboard")

    # Method: Verify current URL
    # Purpose: Confirms that the browser navigated to the expected page
    def verify_current_url(self, dashboard_url: str):
        expect(self.page).to_have_url(dashboard_url)