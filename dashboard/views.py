from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from department.models import Department
from employee.models import Employee
from project.models import Project
from task.models import Task


def dashboard_index(request):
    total = {}
    total['employee'] = Employee.objects.all().count()
    total['department'] = Department.objects.all().count()
    total['project'] = Project.objects.all().count()
    total['task'] = Task.objects.all().count()

    context = {
        "total": total,
    }

    return render(request, 'dashboard_index.html', context)


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
