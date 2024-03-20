from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect

from .models import Product


def home(request: HttpRequest):
    return HttpResponse(render(request, 'home.html', {}))


def products(request: HttpRequest):
    products_list = Product.objects.filter(is_active=True)
    products_list = products_list.order_by('count')

    return HttpResponse(render(request, 'products.html', {
        'products': products_list
    }))


def product_view(request: HttpRequest, product_id: int):
    try:
        products = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404('Товар не найден')

    return HttpResponse(render(request, 'product.html', {
        'product': products
    }))


def add_to_cart(request: HttpRequest, product_id: int):
    request.session['cart'] = request.session.get('cart', []) + [
        {
            'product_id': product_id
            'quantity': 1
        }

    ]
    return redirect('products')