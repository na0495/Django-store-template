from django.urls import path

from .views import *

# -------------------------------------------------

urlpatterns = [
    path('category/list/', CategoryList.as_view(), name='category-list'),
    path('category/create/', CreateCategory.as_view(), name='category-create'),
    path('product/list/', ProductList.as_view(), name='product-list'),
    path('product/create/', CreateProduct.as_view(), name='product-create'),
    path('product/filter/', ProductFilter.as_view(), name='product-filter'),
    path('cart/list/', CartList.as_view(), name='cart-list'),
    path('cart/list/user/', CartListForUser.as_view(), name='cart-list-user'),
    path('cart/create/', CreateCart.as_view(), name='cart-create'),
    path('cart/add/<int:pk>/', AddNewItemIntoCart.as_view(), name='add-item-into-cart'),
    path(
        'cart/remove/<int:pk>/',
        RemoveItemFromCart.as_view(),
        name='remove-item-from-cart',
    ),
]
