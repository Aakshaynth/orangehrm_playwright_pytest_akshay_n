import requests
from conftest import test_data

class EmployeeListAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_employee_list(self, session_cookie:str):
        url = f"{self.base_url}"
        headers = {
            "Accept": "application/json",
            "Cookie": f"orangehrm={session_cookie}"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()