from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def dashboard_index(request):
    return render(request, 'dashboard_index.html')


def user_login(request):
    return render(request, 'login.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        post = User.objects.filter(username=username)
        if post:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_index')
        else:
            return render(request, 'user_login.html', {})
    return render(request, 'user_login.html', {})


def profile(request):
    if request.session.has_key('username'):
        posts = request.session['username']
        query = User.objects.filter(username=posts)
        return render(request, 'profile.html', {"query": query})
    else:
        return render(request, 'user_login.html', {})


def user_logout(request):
    logout(request)
    return render(request, 'user_login.html', {})
