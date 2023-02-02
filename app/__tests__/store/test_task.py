import pytest
from store.tasks import delete_outdated_cart
from store.models import Cart
import datetime
import pytz


utc=pytz.UTC

@pytest.mark.django_db
def test_delete_outdated_cart(user, cart_one):
    """
    Test that the delete_outdated_cart task works as expected
    """
    # create a cart that is older than 60 days
    outdated = utc.localize(datetime.datetime.now() - datetime.timedelta(days=65))
    cart = Cart.objects.create(user=user)
    cart.created_at = outdated
    cart.save()
    assert Cart.objects.count() == 2
    cart.refresh_from_db()
    # run the task
    delete_outdated_cart()
    # check that the cart is deleted
    assert Cart.objects.filter(pk=cart.pk).exists() is False
    assert Cart.objects.count() == 1