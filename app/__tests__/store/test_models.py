import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_category_str(category_one):
    assert category_one.__str__() == 'category_one'


@pytest.mark.django_db
def test_get_product_str(product_one):
    assert product_one.__str__() == 'product_one'


@pytest.mark.django_db
def test_get_cart_str(cart_one):
    assert cart_one.__str__() == str(cart_one.id)


@pytest.mark.django_db
def test_get_cart_item_str(cart_item_one, product_one):
    assert cart_item_one.__str__() == f"{product_one.name} - 1"
