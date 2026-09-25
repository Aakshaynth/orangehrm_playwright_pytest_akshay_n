from playwright.sync_api import Page, expect

class PIMPage:
    def __init__(self, page: Page):
        self.page = page

    #Locators for PIM page elements
        self.add_employee_button = page.locator("//button[normalize-space()='Add Employee']")
        self.first_name_input = page.locator("//input[@placeholder='First Name']")
        self.last_name_input = page.locator("//input[@placeholder='Last Name']")
        self.employee_id_input = page.locator("//label[contains(normalize-space(),'Employee Id')]/parent::div/following-sibling::div/input")
        self.upload_input = page.locator("input[type='file']")
        self.save_button = page.locator("//button[contains(normalize-space(),'Save')]")
        self.toast_message = page.locator(".oxd-toast-content")
        self.employee_search_button = page.locator("//button[contains(normalize-space(.),'Search')]")
        self.employee_edit_button = page.locator("//div[@class='oxd-table-card'][1]//div[@class='oxd-table-cell-actions']/button/i[contains(@class,'bi-pencil-fill')]")


    def click_topbar_menu(self, menu_option: str):
        menu = self.page.locator(f"//nav[@aria-label='Topbar Menu']//a[contains(text(),'{menu_option}')]")
        menu.click()

    def enter_first_name(self, first_name: str):
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name: str):
        self.last_name_input.fill(last_name)

    def enter_employee_id(self, employee_id: str):
        self.employee_id_input.fill(employee_id)

    def upload_profile_picture(self, file_path: str):
        self.upload_input.set_input_files(file_path)

    def save_employee(self):
        self.save_button.click()

    def verify_employee_added_successfully_toast(self):
        expect(self.toast_message).to_be_visible()
        expect(self.toast_message).to_contain_text("Successfully Saved") #Assertion to check if the toast message contains the expected text

    def fill_data_in_input_field_by_label(self, label: str, value: str):
        input_field = self.page.locator(f"//label[normalize-space(text())='{label}']/parent::div/following-sibling::div//input")
        input_field.fill(value)

    def click_search_button(self):
        self.employee_search_button.click()

    def click_edit_button_based_on_employee_id(self, employee_id: str):
        edit_button = self.page.locator(f"//div[@class='oxd-table-card'][.//div[normalize-space(text())='{employee_id}']]//button/i[contains(@class,'bi-pencil-fill')]")
        edit_button.click()

    def click_menu_in_edit_employee_navigation(self, menu_option: str):
        menu = self.page.locator(f"//div[@class='orangehrm-edit-employee-navigation']//div[@role='tab']/a[contains(normalize-space(.),'{menu_option}')]")
        menu.click()

    def select_dropdown_option(self, dropdown_label: str, option_text: str):
        dropdown_by_label = self.page.locator(f"//label[normalize-space()='{dropdown_label}']/following::div[contains(@class,'oxd-select-text-input')]")
        dropdown_by_label.click()
        dropdown_option = self.page.locator(f"//div[@role='listbox']//span[normalize-space()='{option_text}']")
        dropdown_option.click()