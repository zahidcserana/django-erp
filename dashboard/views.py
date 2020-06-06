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
            username = request.POST['username']
            request.session['username'] = username
            return redirect('dashboard_index')
            # return redirect("profile")
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


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'user_login.html', {})
