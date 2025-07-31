from django.shortcuts import render
from .models import Product

def product_list(request):
    in_stock_items = Product.objects.filter(in_stock=True)
    out_of_stock_items = Product.objects.filter(in_stock=False)
    return render(request, 'inventory_app/product_list.html', {
        'in_stock_items': in_stock_items,
        'out_of_stock_items': out_of_stock_items
    })

def in_stock_products(request):
    products = Product.objects.filter(in_stock=True)
    return render(request, 'products/in_stock.html', {'products': products})

def out_of_stock_products(request):
    products = Product.objects.filter(in_stock=False)
    return render(request, 'products/out_of_stock.html', {'products': products})