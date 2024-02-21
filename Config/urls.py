
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Products/', include('Products.urls', namespace='products')),
    path('accounts/', include('Accounts.urls', namespace='accounts')),
    # path('orders/', include('Orders.urls', namespace='orders'))
]
