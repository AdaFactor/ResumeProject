from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User


def login_view(request, context={}):
    if request.user.is_authenticated:
        return redirect('/')

    return render(request, 'AuthenApp/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def authen_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        context = {'login_error': True}
        return login_view(request, context)


def new_user_view(request):
    new = {
        'username': request.POST['username'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        're_password': request.POST['re-password'],
    }
    if new['password'] == new['re_password']:
        user = User.objects.create_user(
            username=new['username'],
            email=new['email'],
            password=new['password']
        )
        login(request, user)

    return redirect('index')
