import pytest


from src.models.user import UserLoginResponse, UserResponse, UsersResponse, DeletedUserResponse
from src.variables import API_USERNAME


@pytest.mark.api
def test_user_can_be_authorized(user_client):
    response = user_client.login_user()
    assert response.status_code == 200
    user = UserLoginResponse.model_validate(response.json())
    assert user.username == API_USERNAME
    assert user.accessToken != ''


@pytest.mark.api
def test_get_current_authenticated_user(authenticated_user_client):
    response = authenticated_user_client.get_current_authentication()
    assert response.status_code == 200
    user = UserResponse.model_validate(response.json())
    assert user.username == API_USERNAME


@pytest.mark.api
@pytest.mark.parametrize('user_id', [1, 50, 100])
def test_get_single_user(authenticated_user_client, user_id):
    user_client = authenticated_user_client
    response = user_client.get_user(user_id)
    assert response.status_code == 200
    test_user = UserResponse.model_validate(response.json())
    assert test_user.id_ == user_id


@pytest.mark.api
def test_get_all_users(authenticated_user_client):
    user_client = authenticated_user_client
    response = user_client.get_all_users()
    assert response.status_code == 200
    users = UsersResponse.model_validate(response.json())
    assert len(users.users) == 30
    assert users.total > 0
    assert users.limit == 30


@pytest.mark.api
def test_add_user(authenticated_user_client):
    user_client = authenticated_user_client
    user_name = 'TestFirstName-1'
    last_name = 'TestLastName-1'
    age = 100
    response = user_client.create_user(first_name=user_name, last_name=last_name, age=age)
    assert response.status_code == 201
    user = UserResponse.model_validate(response.json())
    assert user.firstName == user_name
    assert user.lastName == last_name
    assert user.age == age

@pytest.mark.api
def test_full_user_update(authenticated_user_client):
    user_client = authenticated_user_client
    user_name = 'TestFirstName-2'
    last_name = 'TestLastName-2'
    age = 10
    user_id = 5
    response = user_client.update_full_user_fields(first_name=user_name, last_name=last_name, age=age, user_id=user_id)
    assert response.status_code == 200
    user = UserResponse.model_validate(response.json())
    assert user.firstName == user_name
    assert user.lastName == last_name
    assert user.age == age


@pytest.mark.api
def test_partial_user_update(authenticated_user_client):
    user_client = authenticated_user_client
    user_name = 'TestFirstName-3'
    user_id = 6
    response = user_client.partially_update_user_fields(user_id=user_id, first_name=user_name)
    assert response.status_code == 200
    user = UserResponse.model_validate(response.json())
    assert user.firstName == user_name


@pytest.mark.api
@pytest.mark.parametrize('user_id', [1, 50, 100])
def test_delete_user(authenticated_user_client, user_id):
    user_client = authenticated_user_client
    response = user_client.delete_user(user_id)
    assert response.status_code == 200
    user = DeletedUserResponse.model_validate(response.json())
    assert user.isDeleted is True
    assert user.id_ == user_id
