import datetime
from unicodedata import category
import pytest
from __tests__.accounts.factories import UserFactory
from __tests__.store.factories import (
    CartFactory,
    CartItemFactory,
    ProductFactory,
    CategoryFactory,
)
from store.models import Cart, Product, Category
from accounts.models import User
from rest_framework.test import APIClient
from django.test import TestCase
import pytz

utc=pytz.UTC

# -------------------------

TestCase.databases = {"default"}

# -----------------------------
# setup database for testing --
# -----------------------------


@pytest.fixture()
def client():
    return APIClient()


# ---------------
# users setup ---
# ---------------


@pytest.fixture()
def user():
    return UserFactory(
        username='cool_user',
        password='password',
        first_name='Cool',
        last_name='User',
        is_active=True,
    )


@pytest.fixture()
def admin_user():
    return UserFactory(password='password', is_staff=True, is_active=True)


# --------------------
# categories setup ---
# --------------------


@pytest.fixture()
def category_one():
    return CategoryFactory(name='category_one')


@pytest.fixture()
def category_two():
    return CategoryFactory(name='category_two')


# ------------------
# products setup ---
# ------------------


@pytest.fixture()
def product_one(category_one):
    return ProductFactory(category=category_one, name='product_one')


@pytest.fixture()
def product_two(category_two):
    return ProductFactory(category=category_two)


@pytest.fixture()
def prodcut_three(category_one):
    return ProductFactory(category=category_one)


# --------------------
# Cart Items setup ---
# --------------------


@pytest.fixture()
def cart_item_one(product_one):
    return CartItemFactory(product=product_one, quantity=1)


@pytest.fixture()
def cart_item_two(product_two):
    return CartItemFactory(product=product_two, quantity=2)


@pytest.fixture()
def cart_item_three(product_one):
    return CartItemFactory(product=product_one, quantity=3)


# --------------
# cart setup ---
# --------------


@pytest.fixture()
def cart_one(cart_item_one, cart_item_two, user):
    cart = CartFactory(user=user)
    # add both cart items to the cart
    cart.items.add(cart_item_one)
    cart.items.add(cart_item_two)
    return cart


@pytest.fixture()
def cart_two(cart_item_three, user):
    cart = CartFactory(user=user)
    cart.items.add(cart_item_three)
    return cart


@pytest.fixture()
def outdated_cart(cart_item_one, user):
    cart = CartFactory(user=user)
    cart.items.add(cart_item_one)
    cart.created_at = utc.localize(datetime.datetime.now() - datetime.timedelta(days=65))
    return cart