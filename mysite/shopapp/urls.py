from django.urls import path
from .views import (
    ShopIndexView,
    GroupsListView,
    ProductsListView,
    ProductDetailsView,
    OrdersListView,
    create_product,
    OrderDetailView,
)

app_name = 'shopapp'

urlpatterns = [
    path('', ShopIndexView.as_view(), name='index'),
    path('groups/', GroupsListView.as_view(), name='groups_list'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='products_details'),
    path('products/create/', create_product, name='product_create'),
    path('orders/', OrdersListView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_details'),
]
