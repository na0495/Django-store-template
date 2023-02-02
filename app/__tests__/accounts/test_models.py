import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_user_model(user):
    assert user.username == 'cool_user'
    assert str(user) == 'cool_user'


@pytest.mark.django_db
def test_get_full_name_test(user):
    assert user.get_full_name() == 'Cool User'
