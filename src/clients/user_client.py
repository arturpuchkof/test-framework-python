import requests

from src.clients.base_client import BaseClient
from src.models.user import CreateUserPayload, UpdateUserPayload, GenerateApiRequest
from src.variables import API_USERNAME, API_PASSWORD


class UserClient(BaseClient):

    def login_user(self, username: str = API_USERNAME, password: str = API_PASSWORD) -> requests.Response  :
        return self.perform_post_request(path='/user/login', data={'username': username, 'password': password})

    def get_current_authentication(self) -> requests.Response:
        return self.perform_get_request(path='/user/me')

    def get_all_users(self) -> requests.Response :
        return self.perform_get_request(path='/users')

    def get_user(self, user_id: int, delay: int = None):
        return self.perform_get_request(path=f'/users/{user_id}', delay=delay)

    def search_user(self, search_query: str):
        return self.perform_get_request(path=f'/users/search/?q={search_query}')

    def create_user(self, first_name: str = None, last_name: str = None, age: int = None):
        payload = CreateUserPayload(firstName=first_name, lastName=last_name, age=age)
        return self.perform_post_request(path='/users/add', data=payload.model_dump())

    def update_full_user_fields(self, first_name: str , last_name: str, age: int, user_id: int):
        payload = CreateUserPayload(firstName=first_name, lastName=last_name, age=age)
        return self.perform_put_request(path=f'/users/{user_id}', data=payload.model_dump())

    def partially_update_user_fields(self, user_id: int, first_name: str = None, last_name: str = None, age: int = None):
        payload = UpdateUserPayload(firstName=first_name, lastName=last_name, age=age)
        return self.perform_patch_request(path=f'/users/{user_id}', data=payload.model_dump(exclude_none=True))

    def delete_user(self, user_id: int):
        return self.perform_delete_request(path=f'/users/{user_id}')

    def generate_api_with_empty_body_response(self):
        payload = GenerateApiRequest()
        return self.perform_post_request(path='/c/generate', data=payload.model_dump())

    def custom_http_response(self, status_code: int):
        return self.perform_get_request(path=f'/http/{status_code}')
