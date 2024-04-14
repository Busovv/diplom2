from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from main.models import Order
from .forms import CustomUserCreationForm


@login_required
def profile_view(request: HttpRequest):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return HttpResponse(render(request, 'profile.html', {'orders': orders}))


def sign_up(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            return HttpResponse(render(request, 'profile.html', {}))
        else:
            return HttpResponse(render(
                request, 'registration/register.html', {'form': form}
            ))
