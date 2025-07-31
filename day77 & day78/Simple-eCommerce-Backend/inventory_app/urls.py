from django.contrib import admin
from django.urls import path
from inventory_app.views import product_list, in_stock_products, out_of_stock_products, in_stock_products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='product_list'),
    path('in-stock/', in_stock_products, name='in_stock'),
    path('out-of-stock/', out_of_stock_products, name='out_of_stock'),
]
