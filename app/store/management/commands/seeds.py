from django.core.management import BaseCommand
from accounts.models import User
from store.models import Product, Category

import random
import string
import datetime


def random_char(y):
    return "".join(random.choice(string.ascii_letters) for x in range(y))


class Command(BaseCommand):
    help = 'Seeds the database with data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding the database...'))

        # Create users
        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            {
                'username': 'admin',
                'first_name': 'Admin',
                'last_name': 'Admin',
                'phone_number': '+1-555-555-5555',
                'gender': 'M',
                'password': 'admin1234',
            },
            {
                'username': 'user',
                'first_name': 'User',
                'last_name': 'User',
                'phone_number': '+1-555-555-5555',
                'gender': 'M',
                'password': 'user1234',
            },
        ]

        for user in users:
            username_check = User.objects.filter(username=user['username']).exists()
            if not username_check:
                User.objects.create(**user)
        self.stdout.write(self.style.SUCCESS('Users created!'))

        # Create categories
        self.stdout.write(self.style.SUCCESS('Creating categories...'))

        for i in range(10):
            Category.objects.get_or_create(name=random_char(10))
            i += 1
        self.stdout.write(self.style.SUCCESS('Categories created!'))

        # Create products
        self.stdout.write(self.style.SUCCESS('Creating products...'))

        for i in range(100):
            Product.objects.get_or_create(
                name=random_char(10),
                description=random_char(100),
                price=random.randint(1, 100),
                category=Category.objects.get(id=random.randint(1, 10)),
                quantity=random.randint(1, 100),
            )
            i += 1
        self.stdout.write(self.style.SUCCESS('Products created!'))
