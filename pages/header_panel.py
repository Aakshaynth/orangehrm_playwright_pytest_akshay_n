from playwright.sync_api import Page

class HeaderPanel:
    def __init__(self, page: Page):
        self.page = page

        self.user_dropdown = page.locator("//span[@class='oxd-userdropdown-tab']")
        self.logout_option = page.locator("//a[normalize-space()='Logout']")

    def log_out(self):
        self.user_dropdown.click()
        self.logout_option.click()
            