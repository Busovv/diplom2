from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from main.models import Order
from .forms import RegisterForm


def profile_view(request: HttpRequest):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return HttpResponse(render(request, 'profile.html', {'orders': orders}))


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(render(request, 'profile.html', {}))
        else:
            return HttpResponse(render(
                request, 'registration/register.html', {'form': form}
            ))
