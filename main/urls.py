from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.products, name='products'),
    path('product/<slug:product_id>', views.product_view, name='product'),
    path(
        'product/<int:product_id>/add/',
        views.add_to_basket_view,
        name='add_to_basket'
    ),
    path('basket/', views.basket_view, name='basket'),
    path('basket/clear/', views.basket_clear_view, name='basket_clear'),
    path('order/', views.order_view, name='order'),
]