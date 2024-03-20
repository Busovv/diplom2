from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.products, name='products'),
    path('product/<slug:product_id>', views.product_view, name='product'),
    path(
        'product/<int:id>/add/',
        views.add_to_cart,
        name='add_to_basket'
    ),
]