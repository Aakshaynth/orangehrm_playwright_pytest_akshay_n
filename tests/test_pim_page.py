import pytest
from pages.pim_page import PIMPage
from pages.side_panel import SidePanel
from utilities.test_data_generator import TestDataGenerator

@pytest.mark.smoke
@pytest.mark.regression
def test_verify_user_able_to_successfully_add_a_new_employee(login_logout, test_data):
    page = login_logout
    pim_page = PIMPage(page)
    side_panel = SidePanel(page)
    test_data_generator = TestDataGenerator()

    # Step 1: Navigate to PIM section via side panel
    side_panel.click_menu("PIM")

    # Step 2: Click on 'Add Employee' button
    pim_page.click_topbar_menu("Add Employee")

    # Step 3: Fill in employee details
    pim_page.enter_first_name(test_data["employee_data"]["first_name"])
    pim_page.enter_last_name(test_data["employee_data"]["last_name"])
    pim_page.enter_employee_id(test_data_generator.generate_random_string_with_int(5))
    test_data["employee_data"]["employee_id"] = pim_page.employee_id_input.input_value()  # Store the generated employee ID for later use
    
    # Step 4: Upload profile picture
    pim_page.upload_profile_picture("config\\dummy_user.png")

    # Step 4: Save the new employee
    pim_page.save_employee()

    # Step 5: Verify the success toast message appears
    pim_page.verify_employee_added_successfully_toast()

@pytest.mark.only
def test_verify_user_able_to_successfully_edit_an_employee_with_random_data(login_logout, test_data):
    page = login_logout
    pim_page = PIMPage(page)
    side_panel = SidePanel(page)
    test_data_generator = TestDataGenerator()

    # Step 1: Navigate to PIM section via side panel
    side_panel.click_menu("PIM")

    # Step 2: Click on 'Employee List' button
    pim_page.click_topbar_menu("Employee List")

    