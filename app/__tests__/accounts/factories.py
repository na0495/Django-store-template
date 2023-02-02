import factory
from accounts.models import User
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    """User factory"""

    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    first_name = factory.LazyAttribute(lambda o: faker.first_name())
    last_name = factory.LazyAttribute(lambda o: faker.last_name())
    phone_number = factory.LazyAttribute(lambda o: faker.phone_number())
    password = factory.PostGenerationMethodCall('set_password', 'password')
