import requests

from src.models.headers import DefaultHeaders
from src.variables import BASE_URL


class BaseClient:
    def __init__(self, base_url: str = BASE_URL, headers: DefaultHeaders = DefaultHeaders()):
        self._base_url = base_url
        self._headers = headers
        self._client = requests.Session()


    def perform_get_request(self, path: str) -> requests.Response:
        return self._client.get(self._base_url + path, headers=self._headers.model_dump())


    def perform_post_request(self, path: str, data: dict) -> requests.Response:
        return self._client.post(self._base_url + path, headers=self._headers.model_dump(), json=data)


    def perform_put_request(self, path: str, data: dict) -> requests.Response:
        return self._client.put(self._base_url + path, headers=self._headers.model_dump(), json=data)


    def perform_patch_request(self, path: str, data: dict) -> requests.Response:
        return self._client.patch(self._base_url + path, headers=self._headers.model_dump(), json=data)


    def perform_delete_request(self, path: str) -> requests.Response:
        return self._client.delete(self._base_url + path, headers=self._headers.model_dump())


    def update_authorization_token(self, token:str):
        self._headers.authorization = f'Bearer {token}'