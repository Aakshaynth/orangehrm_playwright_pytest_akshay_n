from playwright.sync_api import Page

class SidePanel:
    def __init__(self, page: Page):
        self.page = page


    def click_menu(self, menu_option: str):
        menu_name= self.page.locator(f"//ul[@class='oxd-main-menu']//a/span[contains(normalize-space(),'{menu_option}')]")
        menu_name.click()