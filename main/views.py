from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Product


def home(request: HttpRequest):
    return HttpResponse(render(request, 'home.html', {}))


def products(request: HttpRequest):
    products_list = Product.objects.filter(is_active=True)
    products_list = products_list.order_by('count')

    return HttpResponse(render(request, 'products.html', {
        'products': products_list
    }))