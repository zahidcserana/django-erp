from django.shortcuts import render


def dashboard_index(request):
    return render(request, 'dashboard_index.html')


def user_login(request):
    return render(request, 'login.html')
