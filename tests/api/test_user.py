import pytest


from src.models.user import UserLoginResponse, UserResponse, UsersResponse, DeletedUserResponse, \
    UserNotFoundErrorResponse, BadRequestResponse
from src.variables import API_USERNAME


# --------------positive test cases--------------------- #

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


# --------------negative test cases--------------------- #

@pytest.mark.api
def test_get_not_existing_user(authenticated_user_client):
    user_client = authenticated_user_client
    user_id = 9999999999
    response = user_client.get_user(user_id=user_id)
    assert response.status_code == 404
    error_message = UserNotFoundErrorResponse.model_validate(response.json())
    assert str(user_id) in error_message.message


@pytest.mark.api
def test_update_not_existing_user(authenticated_user_client):
    user_client = authenticated_user_client
    user_id = 9999999999
    response = user_client.partially_update_user_fields(user_id=user_id)
    assert response.status_code == 404
    error_message = UserNotFoundErrorResponse.model_validate(response.json())
    assert str(user_id) in error_message.message


@pytest.mark.api
def test_delete_not_existing_user(authenticated_user_client):
    user_client = authenticated_user_client
    user_id = 9999999999
    response = user_client.delete_user(user_id=user_id)
    assert response.status_code == 404
    error_message = UserNotFoundErrorResponse.model_validate(response.json())
    assert str(user_id) in error_message.message


@pytest.mark.api
def test_handle_400_error(authenticated_user_client):
    user_client = authenticated_user_client
    response = user_client.custom_http_response(status_code=400)
    assert response.status_code == 400
    error_message = BadRequestResponse.model_validate(response.json())
    assert error_message.status == 400
    assert error_message.message == 'Bad Request'


@pytest.mark.api
@pytest.mark.parametrize('delay', [1000, 2000, 3000, 4000, 5000])
def test_delayed_get_user(authenticated_user_client, delay):
    user_client = authenticated_user_client
    response = user_client.get_user(user_id=1, delay=delay)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() * 1000  >= delay


@pytest.mark.api
def test_empty_response_body(authenticated_user_client, generate_url_with_empty_resp):
    user_client = authenticated_user_client
    test_url = generate_url_with_empty_resp
    response = user_client.perform_get_request(path=test_url.replace('https://dummyjson.com', ''))
    assert response.status_code == 200
    assert response.text == ''


