from django.db.models import Sum
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Product, Order, OrderProduct


def home(request: HttpRequest):
    return HttpResponse(render(request, 'home.html', {}))


def products(request: HttpRequest):
    products_list = Product.objects.filter(is_active=True)
    products_list = products_list.order_by('count')

    return HttpResponse(render(request, 'products.html', {
        'products': products_list
    }))


def get_product_for_view(id: int):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404('Товар не найден')

    if not product.is_active:
        raise Http404('Товар не доступен')

    return product


def product_view(request: HttpRequest, product_id: int):
    try:
        products = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404('Товар не найден')

    return HttpResponse(render(request, 'product.html', {
        'product': products
    }))


def add_to_basket_view(request: HttpRequest, product_id: int):
    product = get_product_for_view(id=product_id)

    if product.count < 1:
        return redirect('product', id=product_id)

    basket: list = request.session.get('basket', [])

    found_item = next(
        (item for item in basket if item['product_id'] == product_id),
        None,
    )

    if found_item is not None:
        found_item['quantity'] = found_item['quantity'] + 1
    else:
        basket.append({
            'product_id': product_id,
            'quantity': 1
        })

    request.session['basket'] = basket

    return redirect('basket')


def basket_view(request: HttpRequest):
    items = request.session.get('basket', [])

    for item in items:
        item['product'] = Product.objects.get(id=item['product_id'])

    total_price = sum(item['product'].price * item['quantity']
                      for item in items)

    return HttpResponse(render(request, 'basket.html', {
        'items': items,
        'total_price': total_price,
    }))


def basket_clear_view(request: HttpRequest):
    request.session.update({'basket': []})

    return redirect('basket')


@require_http_methods(["POST"])
def order_view(request: HttpRequest):
    if not request.user.is_authenticated:
        login_page = redirect('login')
        login_page['Location'] += '?next=/order'
        return login_page

    if request.method == 'POST':
        order = Order()
        order.user = request.user
        order.save()

        basket = request.session.get('basket', [])
        for item in basket:
            order_product = OrderProduct(order=order)
            order_product.product = Product.objects.get(id=item['product_id'])
            order_product.quantity = item['quantity']
            order_product.price = order_product.product.price
            order_product.save()

        request.session.update({'basket': []})

        return redirect('get_order', id=order.id)


@require_http_methods(["GET"])
def get_order_view(request: HttpRequest, id: int):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        raise Http404('Заказ не найден')

    return HttpResponse(render(request, 'order.html', {
        'order': order,
        'products': OrderProduct.objects.filter(order=order),
    }))