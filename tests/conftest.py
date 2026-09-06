import pytest

from src.clients.user_client import UserClient


@pytest.fixture(scope='session')
def user_client():
    user_client = UserClient()
    return user_client


@pytest.fixture(scope='session')
def authorize_user(user_client):
    response = user_client.login_user()
    token = response.json()['accessToken']
    user_client.update_authorization_token(token=token)
    return user_client
