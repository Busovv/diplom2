from django.contrib.auth.views import LoginView
from django.urls import include, path

from .views import profile_view, sign_up


urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/register', sign_up, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
    path('accounts/login/', LoginView.as_view(), name='login'),
]
