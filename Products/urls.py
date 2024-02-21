from django.urls import path
from .views import ProductsDetailsView, ProductsView


app_name = 'products'

urlpatterns = [
    path('products/', ProductsView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductsDetailsView.as_view(), name='product_details')
]
