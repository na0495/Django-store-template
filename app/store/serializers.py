from rest_framework import serializers
from .models import Cart, Product, Category, CartItem

# ----------------------
# Store serializers ---
# ----------------------


class CategorySerializer(serializers.ModelSerializer):
    """Category serializer"""

    class Meta:
        model = Category
        fields = ('id', 'name')


# ----------------------


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'category')


class DisplayProductSerializer(serializers.ModelSerializer):
    """Display product serializer"""

    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'category')


# ----------------------


class DisplayCartItemSerializer(serializers.ModelSerializer):
    """CartItem serializer"""

    product = DisplayProductSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity')


class CartItemSerializer(serializers.ModelSerializer):
    """CartItem serializer"""

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'quantity')


# ----------------------


class CartSerializer(serializers.ModelSerializer):
    """Cart serializer"""

    class Meta:
        model = Cart
        fields = ('id', 'user', 'items')


class DisplayCartSerializer(serializers.ModelSerializer):
    """Display cart serializer"""

    items = DisplayCartItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'items', 'total', 'user', 'created_at', 'updated_at')

    def get_total(self, obj):
        total = 0
        for item in obj.items.all():
            total += item.product.price * item.quantity
        return total
