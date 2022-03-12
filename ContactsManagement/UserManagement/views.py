import email
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from UserManagement.forms import *

# Create your views here.

def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        user_login_form = UserLoginForm()
        return render(request, 'UserManagement/login.html', {'user_login_form': user_login_form})
    elif request.method == 'POST':
        user_login_form = UserLoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = authenticate(request, email=email, password=password)
        if user_obj is not None:
            login(request, user_obj)
            return redirect('/')
        return render(request, 'UserManagement/login.html', {'user_login_form': user_login_form, 'failure': True})


def UserRegister(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        user_register_form = UserRegisterForm()
        return render(request, 'UserManagement/register.html', {'user_register_form': user_register_form})
    elif request.method == 'POST':
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            user_obj = user_register_form.save(commit=False)
            user_obj.set_password(request.POST.get('password'))
            user_obj.save()
            login(request, user_obj)
            return redirect('/')
        return render(request, 'UserManagement/register.html', {'user_register_form': user_register_form})


def UserLogout(request):
    logout(request)
    return redirect('/')