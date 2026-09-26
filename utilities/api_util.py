class Assertions:

    @staticmethod
    def assert_in_response(test_data: dict, response: dict):
        """
        Assert that employee details from test_data ARE present in the API response list.
        Handles both dict and string elements in response["data"].
        """
        found = False
        for emp in response.get("data", []):
            if isinstance(emp, dict):
                first_name = emp.get("firstName") or ""
                last_name = emp.get("lastName") or ""
                employee_id = emp.get("employeeId") or ""

                if (
                    test_data["employee_data"]["first_name"] == first_name and
                    test_data["employee_data"]["last_name"] == last_name and
                    test_data["employee_data"]["employee_id"] == employee_id
                ):
                    found = True
                    break

            elif isinstance(emp, str):
                # If API returns raw strings instead of dicts
                if test_data["employee_data"]["first_name"] == emp \
                   or test_data["employee_data"]["last_name"] == emp \
                   or test_data["employee_data"]["employee_id"] == emp:
                    found = True
                    break

        assert found, f"Expected employee {test_data['employee_data']} not found in response"

    @staticmethod
    def assert_not_in_response(test_data: dict, response: dict):
        """
        Assert that employee details from test_data are NOT present in the API response list.
        Handles both dict and string elements in response["data"].
        """
        for emp in response.get("data", []):
            if isinstance(emp, dict):
                first_name = emp.get("firstName") or ""
                last_name = emp.get("lastName") or ""
                employee_id = emp.get("employeeId") or ""

                assert test_data["employee_data"]["first_name"] != first_name, \
                    f"Unexpected match: {test_data['employee_data']['first_name']} equals {first_name}"
                assert test_data["employee_data"]["last_name"] != last_name, \
                    f"Unexpected match: {test_data['employee_data']['last_name']} equals {last_name}"
                assert test_data["employee_data"]["employee_id"] != employee_id, \
                    f"Unexpected match: {test_data['employee_data']['employee_id']} equals {employee_id}"

            elif isinstance(emp, str):
                assert test_data["employee_data"]["first_name"] != emp, \
                    f"Unexpected match: {test_data['employee_data']['first_name']} equals {emp}"
                assert test_data["employee_data"]["last_name"] != emp, \
                    f"Unexpected match: {test_data['employee_data']['last_name']} equals {emp}"
                assert test_data["employee_data"]["employee_id"] != emp, \
                    f"Unexpected match: {test_data['employee_data']['employee_id']} equals {emp}"
