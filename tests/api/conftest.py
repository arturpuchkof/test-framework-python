import pytest

from src.clients.user_client import UserClient


@pytest.fixture
def user_client() -> UserClient:
    user_client = UserClient()
    return user_client


@pytest.fixture()
def authenticated_user_client() -> UserClient:
    user_client = UserClient()
    response = user_client.login_user()
    token = response.json()['accessToken']
    user_client.update_authorization_token(token)
    return user_client


@pytest.fixture()
def generate_url_with_empty_resp() -> str:
    user_client =  UserClient()
    response = user_client.generate_api_with_empty_body_response()
    return response.json()['url']