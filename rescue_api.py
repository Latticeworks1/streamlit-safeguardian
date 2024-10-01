import requests
from requests.auth import HTTPBasicAuth

class RescueAPI:
    def __init__(self, url="https://safeguardian-33b94228882a.herokuapp.com/"):
        self.url = url

    def _make_request(self, method, endpoint, data=None):
        try:
            response = requests.request(method, self.url + endpoint, json=data)
            if response.status_code == 200:
                json_response = response.json()
                if 'error' in json_response:
                    return json_response['error']
                else:
                    return json_response
            else:
                return f"Request failed with status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def post_victim(self, victim_info):
        assert isinstance(victim_info, dict), "victim_info should be a dictionary"

        return self._make_request("POST", "/victim/report", victim_info)['victim_number']

    def update_victim(self, victim_number, victim_info):
        assert isinstance(victim_number, str), "victim_number should be a string"
        assert isinstance(victim_info, dict), "victim_info should be a dictionary"

        return self._make_request("POST", f"/victim/update/{victim_number}", victim_info)
    
    def get_victim_from_id(self, victim_number):
        assert isinstance(victim_number, str), "victim_number should be a string"
        assert victim_number.startswith("-"), "victim_number should start with '-'"

        return self._make_request("GET", f"/victim/{victim_number}")

    def get_all_victims(self):
        return self._make_request("GET", "/victims/all")