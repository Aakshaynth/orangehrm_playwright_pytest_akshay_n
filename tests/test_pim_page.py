import pytest
from conftest import test_data_updater
from pages.pim_page import PIMPage
from pages.side_panel import SidePanel
from utilities.test_data_generator import TestDataGenerator

# Test: Verify a new Employee can be added into the system,
# Purpose: To validate the Add Employee functionality
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order(2)
def test_verify_user_able_to_successfully_add_a_new_employee(login_logout, test_data, test_data_updater):
    page = login_logout
    pim_page = PIMPage(page)
    side_panel = SidePanel(page)
    test_data_generator = TestDataGenerator()

    # Step 1: Navigate to PIM section via side panel
    side_panel.click_menu("PIM")

    # Step 2: Click on 'Add Employee' button
    pim_page.click_topbar_menu("Add Employee")

    # Step 3: Fill in employee details
    fn = test_data_generator.generate_random_string_with_int(5)
    first_name = test_data["employee_data"]["first_name"]+fn
    pim_page.enter_first_name(first_name)
    test_data_updater({"employee_data": {"first_name": first_name}})
    ln = test_data_generator.generate_random_string_with_int(5)
    last_name = test_data["employee_data"]["last_name"]+ln
    pim_page.enter_last_name(last_name)
    test_data_updater({"employee_data": {"last_name": last_name}})
    emp_id = test_data_generator.generate_random_string_with_int(5) # Generate and store the random employee ID
    pim_page.enter_employee_id(emp_id)
    test_data_updater({"employee_data": {"employee_id": emp_id}})  # Store the generated employee ID for later use

    # Step 4: Upload profile picture
    pim_page.upload_profile_picture("config\\dummy_user.png")

    # Step 4: Save the new employee
    pim_page.save_employee()

    # Step 5: Verify the success toast message appears
    pim_page.verify_toast_message(test_data["employee_data"]["added_success_toast"])

# Test: Verify user can edit a Employee detail
# Purpose: To validate the Edit Employee functionality
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order(3)
def test_verify_user_able_to_successfully_edit_an_employee(login_logout, test_data, test_data_updater):
    page = login_logout
    pim_page = PIMPage(page)
    side_panel = SidePanel(page)

    # Step 1: Navigate to PIM section via side panel
    side_panel.click_menu("PIM")

    # Step 2: Click on 'Employee List' button
    pim_page.click_topbar_menu("Employee List")

    # Step 3: Search for the employee by name & ID
    pim_page.fill_data_in_input_field_by_label("Employee Name", f"{test_data['employee_data']['first_name']} {test_data['employee_data']['last_name']}")
    pim_page.fill_data_in_input_field_by_label("Employee Id", test_data["employee_data"]["employee_id"])
    pim_page.click_search_button()

    # Step 4: Click on the edit button for the employee with the specified ID
    pim_page.click_edit_button_based_on_employee_id(test_data["employee_data"]["employee_id"])

    # Step 5: Navigate to the 'Job' section in the edit employee page
    pim_page.click_menu_in_edit_employee_navigation("Job")

    # Step 6: Update the job title and employment status
    pim_page.select_dropdown_option("Job Title", f"{test_data['employee_data']['jobtitle']}")
    pim_page.select_dropdown_option("Employment Status", f"{test_data['employee_data']['employment_status']}")

    # Step 7: Save the updated employee information
    pim_page.save_employee()

    # Step 8: Verify the success toast message appears
    pim_page.verify_toast_message(test_data["employee_data"]["updated_success_toast"])

    # Step 9: Verify the updated job title and employment status is
    pim_page.click_menu_in_edit_employee_navigation("Job")
    updated_job_title = pim_page.fetch_input_value_by_label("Job Title", test_data["employee_data"]["jobtitle"])
    assert updated_job_title == test_data["employee_data"]["jobtitle"]
    updated_employment_status = pim_page.fetch_input_value_by_label("Employment Status", test_data["employee_data"]["employment_status"])
    assert updated_employment_status == test_data["employee_data"]["employment_status"]

    # 10 Capture the employee ID and store it in test data for future use
    emp_number = pim_page.test_capture_emp_id_and_store()
    emp_number = int(emp_number)
    test_data_updater({"employee_data": {"employee_number": emp_number}})  # Store the captured employee number for later use

# Test: Verify a Existing employee detail can deleted
# Purpose: To validate Delete employee record functionality
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order(5)
def test_verify_user_able_to_successfully_delete_an_employee(login_logout, test_data, test_data_updater):
    page = login_logout
    pim_page = PIMPage(page)
    side_panel = SidePanel(page)

    # Step 1: Navigate to PIM section via side panel
    side_panel.click_menu("PIM")

    # Step 2: Click on 'Employee List' button
    pim_page.click_topbar_menu("Employee List")

    # Step 3: Search for the employee by name & ID
    pim_page.fill_data_in_input_field_by_label("Employee Name", f"{test_data['employee_data']['first_name']} {test_data['employee_data']['last_name']}")
    pim_page.fill_data_in_input_field_by_label("Employee Id", test_data["employee_data"]["employee_id"])
    pim_page.click_search_button()

    # Step 4: Click on the delete button for the employee with the specified ID
    pim_page.click_delete_button_based_on_employee_id(test_data["employee_data"]["employee_id"],"Delete")

# Test: Verify Deleted employee details are not displayed anymore in application UI
# Purpose: To validate Delete employee record removal from UI
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order(6)
def test_verify_deleted_employee_is_longer_displayed_in_employee_list(login_logout, test_data):
    page = login_logout
    pim_page = PIMPage(page)
    side_panel = SidePanel(page)

    # Step 1: Navigate to PIM section via side panel
    side_panel.click_menu("PIM")

    # Step 2: Click on 'Employee List' button
    pim_page.click_topbar_menu("Employee List")

    # Step 3: Search for the employee by name & ID
    pim_page.fill_data_in_input_field_by_label("Employee Name", f"{test_data['employee_data']['first_name']} {test_data['employee_data']['last_name']}")
    pim_page.fill_data_in_input_field_by_label("Employee Id", test_data["employee_data"]["employee_id"])
    pim_page.click_search_button()

    # Step 4: Verify toast message displayed as No data found
    pim_page.verify_toast_message("No Records Found")