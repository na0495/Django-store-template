from accounts.models import User
from django.db import models

# -------------------------
# E-commerce Models  ------
# -------------------------


class Category(models.Model):
    """Category model"""

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model"""

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    """Cart Item model"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"


class Cart(models.Model):
    """Cart model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
