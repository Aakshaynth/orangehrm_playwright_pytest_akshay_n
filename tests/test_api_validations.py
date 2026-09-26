from api.employee_list_api import EmployeeListAPI
from api.employee_personal_details_api import EmployeePersonalDetailsAPI
import pytest
from utilities.api_util import Assertions

# Test: Verify Employees details added are accurate by comparing both UI & API data
# Purpose: Ensure consistency among Front End & Back End data
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order(4) 
def test_verify_employee_details_consistency_ui_vs_api(test_data, session_cookie):
    
    # Step 1: Retrieve the employee number from test data (used as input for API call)
    emp_number = test_data["employee_data"]["employee_number"]

    # Step 2: Initialize the API client with the base URL from test data
    api = EmployeePersonalDetailsAPI(base_url=test_data["api"]["base_url"])

    # Step 3: Call the API to fetch employee personal details using emp_number and session cookie
    response = api.get_employee_personal_details(emp_number, session_cookie)

    # Step 4: Validate that the API response matches expected employee details from test data which was used to create the employee in the UI
    assert response["data"]["empNumber"] == emp_number
    assert response["data"]["firstName"] == test_data["employee_data"]["first_name"]
    assert response["data"]["lastName"] == test_data["employee_data"]["last_name"]
    assert response["data"]["employeeId"] == test_data["employee_data"]["employee_id"]

# Test: Verify Employee data deleted from UI, are remobed from Employee list API response also
# Purpose: Ensure Delete functionality validation among UI & API
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order(7)
def test_verify_employee_details_deleted_are_not_displayed_in_employee_list_api_response(test_data, session_cookie):

    # Step 1: Initialize the API client with the base URL from test data
    api = EmployeeListAPI(base_url=test_data["api"]["base_url"])

    # Step 2: Call the API to fetch employee personal details using emp_number and session cookie
    response = api.get_employee_list(session_cookie)

    # Step 3: Validate that the API response doesnt matches expected employee list from test data which was deleted from the UI
    Assertions.assert_not_in_response(test_data, response)