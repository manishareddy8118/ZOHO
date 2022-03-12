from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'base.html')
    return redirect(reverse('UserManagement:login'))
    