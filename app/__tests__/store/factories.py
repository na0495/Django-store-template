import factory
from store.models import Cart, Product, Category, CartItem
from faker import Factory as FakerFactory

from __tests__.accounts.factories import UserFactory

faker = FakerFactory.create()


class CategoryFactory(factory.django.DjangoModelFactory):
    """Category factory"""

    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'category{0}'.format(n))


class ProductFactory(factory.django.DjangoModelFactory):
    """Product factory"""

    class Meta:
        model = Product

    name = factory.Sequence(lambda n: 'product{0}'.format(n))
    description = factory.LazyAttribute(lambda o: faker.text())
    price = factory.LazyAttribute(lambda o: faker.random_int(min=1, max=100))
    quantity = factory.LazyAttribute(lambda o: faker.random_int(min=1, max=100))
    category = factory.SubFactory(CategoryFactory)


class CartItemFactory(factory.django.DjangoModelFactory):
    """CartItem factory"""

    class Meta:
        model = CartItem

    product = factory.SubFactory(ProductFactory)
    quantity = factory.LazyAttribute(lambda o: faker.random_int(min=1, max=100))


class CartFactory(factory.django.DjangoModelFactory):
    """Cart factory"""

    class Meta:
        model = Cart

    user = factory.SubFactory(UserFactory)
    items = factory.RelatedFactory(CartItemFactory)
    created_at = factory.LazyAttribute(lambda o: faker.date_time_between(start_date='-30d', end_date='now'))
