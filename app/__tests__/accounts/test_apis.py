import pytest
from django.urls import reverse
from rest_framework import status
from accounts.models import User

# -------------------------
# User Api's unit test ----
# -------------------------


@pytest.mark.django_db
def test_user_register(client):
    """Test user register"""
    url = reverse('user_register')
    data = {
        'username': 'testuser',
        'first_name': 'test',
        'last_name': 'user',
        'phone_number': '1234567890',
        'gender': 'M',
        'password': 'Hard@pasudo1.',
        'password2': 'Hard@pasudo1.',
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

    # check if the user with the data user name exsit
    user = User.objects.get(username=data['username'])
    assert user is not None
    assert user.first_name == data['first_name']

    # login the user
    url = reverse('token_obtain_pair')
    data = {'username': 'testuser', 'password': 'Hard@pasudo1.'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['access'] is not None
    assert response.data['refresh'] is not None


@pytest.mark.django_db
def test_user_login(client, user):
    """Test user login"""
    url = reverse('token_obtain_pair')
    data = {'username': user.username, 'password': 'password'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['refresh'] is not None
    assert response.data['access'] is not None


@pytest.mark.django_db
def test_user_login_wrong_password(client, user):
    """Test user login with wrong password"""
    url = reverse('token_obtain_pair')
    data = {'username': user.username, 'password': 'wrong_password'}
    response = client.post(url, data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert (
        response.data['detail'] == 'No active account found with the given credentials'
    )


@pytest.mark.django_db
def test_register_with_not_matching_password(client):
    """Test user register with not matching password"""
    url = reverse('user_register')
    data = {
        'username': 'testuser',
        'first_name': 'test',
        'last_name': 'user',
        'phone_number': '1234567890',
        'password': 'Hard@pasudo1.',
        'password2': 'Hard@pasudo2.',
        'gender': 'M',
    }
    response = client.post(url, data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
