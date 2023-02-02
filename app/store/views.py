from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from .models import Cart, CartItem, Category, Product
from .serializers import (
    CartSerializer,
    CategorySerializer,
    DisplayCartSerializer,
    DisplayProductSerializer,
    ProductSerializer,
)

# ---------------------
# Store APIs views ----
# ---------------------


class CustomThrottle(UserRateThrottle):
    # limit the rate throttle to 2 request per second
    rate = '2/second'


# ----------
# Category -
# ----------


class CategoryList(generics.ListAPIView):
    """List available categories"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class CreateCategory(generics.CreateAPIView):
    """Create category for store"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


# ----------
# Product --
# ----------
class CreateProduct(generics.CreateAPIView):
    """Create product in the store"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class ProductList(generics.ListAPIView):
    """Product list in the store, user is only allowed to have only 2 request per second"""

    queryset = Product.objects.all()
    serializer_class = DisplayProductSerializer
    permission_classes = (AllowAny,)
    throttle_classes = (CustomThrottle,)


class ProductFilter(generics.ListAPIView):
    """Product filter, in order to filter by category, you should add '?category=<category_id>' in the url"""

    queryset = Product.objects.all()
    serializer_class = DisplayProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category is not None:
            return Product.objects.filter(category=category)
        return None


# ------
# Cart -
# ------
class CartList(generics.ListAPIView):
    """List all carts on the store"""

    queryset = Cart.objects.all()
    serializer_class = DisplayCartSerializer
    permission_classes = (IsAuthenticated,)


class CartListForUser(generics.ListAPIView):
    """List all carts on the store, for a specific user"""

    queryset = Cart.objects.all()
    serializer_class = DisplayCartSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


class CreateCart(generics.CreateAPIView):
    """To create a cart wtih pre-existing items send a list of items in the request body"""

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)


class AddNewItemIntoCart(generics.RetrieveUpdateAPIView):
    """This Api allow user to add new item into cart, by providing product id and quantity"""

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        cart = self.get_object()
        product = Product.objects.get(id=request.data['product'])
        quantity = request.data['quantity']
        # create new cart item
        cart_item = CartItem.objects.create(product=product, quantity=quantity)
        # add cart item into cart
        cart.items.add(cart_item)
        return self.retrieve(request, *args, **kwargs)


class RemoveItemFromCart(generics.RetrieveUpdateAPIView):
    """This Api allow user to remove item from cart, by providing item id wanted to remove"""

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        cart = self.get_object()
        item = CartItem.objects.get(id=request.data['item'])
        # remove cart item from cart
        cart.items.remove(item)
        # delete cart item
        item.delete()
        return self.retrieve(request, *args, **kwargs)
