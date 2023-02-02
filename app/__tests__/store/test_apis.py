from unicodedata import category
import pytest
from django.urls import reverse
from rest_framework import status
from accounts.models import User
from store.models import CartItem, Product, Category, Cart


# ----------------------------
# Category Api's unit test ---
# ----------------------------


@pytest.mark.django_db
def test_category_list(client, category_one, category_two):
    """Test category list"""
    url = reverse('category-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == Category.objects.count()


@pytest.mark.django_db
def test_create_category(client, user, category_one, category_two):
    """Test create category"""
    client.force_authenticate(user=user)
    url = reverse('category-create')
    data = {'name': 'Test Category'}
    response = client.post(url, data, format='json')
    # import pdb ; pdb.set_trace()
    assert response.status_code == status.HTTP_201_CREATED
    assert Category.objects.count() == 3
    assert Category.objects.get(name='Test Category')


# ---------------------------
# Product Api's unit test ---
# ---------------------------


@pytest.mark.django_db
def test_product_list(client, product_one, product_two):
    """Test product list"""
    url = reverse('product-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == Product.objects.count()


@pytest.mark.django_db
def test_create_product(client, user, product_one, product_two):
    """Test create product"""
    client.force_authenticate(user=user)
    url = reverse('product-create')
    data = {
        'name': 'Test Product',
        'description': 'Test Description',
        'category': product_one.category.id,
        'price': '10.00',
        'quantity': '10',
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Product.objects.count() == 3
    assert Product.objects.get(name='Test Product')


@pytest.mark.django_db
def test_product_filter(client, product_one, category_one):
    """Test product filter"""
    url = reverse('product-filter') + '?category={}'.format(category_one.id)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == Product.objects.filter(category=category_one).count()


@pytest.mark.django_db
def test_product_filter_with_no_query(client, product_one, category_one):
    """Test product filter"""
    url = reverse('product-filter')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0


# ------------------------
# Cart Api's unit test ---
# ------------------------


@pytest.mark.django_db
def test_cart_list(client, user, cart_one, cart_two):
    """Test cart list"""
    client.force_authenticate(user=user)
    url = reverse('cart-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == Cart.objects.count()


@pytest.mark.django_db
def test_create_cart(client, user, cart_item_one, cart_item_two):
    """Test create cart"""
    client.force_authenticate(user=user)
    url = reverse('cart-create')
    data = {'user': user.id, 'items': [cart_item_one.id, cart_item_two.id]}
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Cart.objects.get(user=user)
    assert Cart.objects.get(user=user).items.count() == 2


@pytest.mark.django_db
def test_add_item_to_cart(client, user, cart_two, product_two):
    """Test add product to cart"""
    client.force_authenticate(user=user)
    # add id of the cart into the url pk
    url = reverse('add-item-into-cart', kwargs={'pk': cart_two.id})
    data = {'user': user.id, 'product': product_two.id, 'quantity': '10'}
    response = client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert Cart.objects.get(user=user).items.get(product=product_two) is not None
    assert Cart.objects.get(user=user).items.count() == 2
    # import pdb ; pdb.set_trace()


@pytest.mark.django_db
def test_remove_item_from_cart(client, user, cart_one, cart_item_one, cart_item_two):
    """Test remove item from cart"""
    client.force_authenticate(user=user)
    url = reverse('remove-item-from-cart', kwargs={'pk': cart_one.id})
    data = {'item': cart_item_two.id}
    assert Cart.objects.get(user=user).items.count() == 2
    response = client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert Cart.objects.get(id=cart_one.id).items.count() == 1
    # check if the item is removed
    assert CartItem.objects.filter(id=cart_item_one.id) is not None


@pytest.mark.django_db
def test_list_cart_for_a_specific_user(client, user, cart_one, cart_two):
    """Test list cart for a specific user"""
    client.force_authenticate(user=user)
    url = reverse('cart-list-user')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == Cart.objects.filter(user=user).count()
