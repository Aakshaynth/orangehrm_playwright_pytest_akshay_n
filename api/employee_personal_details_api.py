import requests
from conftest import test_data

class EmployeePersonalDetailsAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_employee_personal_details(self, emp_number: str, session_cookie:str):
        url = f"{self.base_url}/{emp_number}/personal-details"
        headers = {
            "Accept": "application/json",
            "Cookie": f"orangehrm={session_cookie}"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()