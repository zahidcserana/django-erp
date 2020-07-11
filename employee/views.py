from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect

from employee.models import Employee
from employee.forms import EmployeeForm, UserForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect


def employee_index(request):
    search = request.GET.get('search')
    name = request.GET.get('name')
    status = request.GET.get('status')
    designation = request.GET.get('designation')
    if search is not None:
        employees = Employee.objects.filter(
            (Q(name__icontains=name) | Q(email__icontains=name)) & Q(status__icontains=status) &
            Q(designation__icontains=designation)
        )
        # conditions = dict()
        # conditions.update(name__icontains=name)
        # conditions.update(status__icontains=status)
        # conditions.update(designation__icontains=designation)
        # employees = Employee.objects.filter(**conditions)
    else:
        employees = Employee.objects.all().select_related('user')

    # print(employees[0].user.email)
    page = request.GET.get('page', 1)

    paginator = Paginator(employees, 10)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'employee_index.html', {'data': data})


# def employee_index(request):
#     employees = Employee.objects.all()
#     paginator = Paginator(employees, 1)  # Show 25 contacts per page
#
#     page = request.GET.get('page')
#     contacts = paginator.get_page(page)
#     return render(request, 'employee_index.html', {'contacts': contacts})


# def employee_add(request):
#     form = EmployeeForm()
#     context = {
#         "form": form,
#     }
#     return render(request, "employee_add.html", context)


def employee_add(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        employee_form = EmployeeForm(data=request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            if request.FILES:
                employee.image = request.FILES['image']
            employee.save()
            return redirect('employee_index')
    else:
        user_form = UserForm()
        employee_form = EmployeeForm()
    context = {
        "add": True,
        'user_form': user_form,
        "form": employee_form,
        'user_image': 'https://www.w3schools.com/howto/img_avatar.png'
    }
    return render(request, "employee_add.html", context)


def employee_detail(request, pk=None):
    employee = Employee.objects.get(id=pk)
    user = User.objects.get(id=employee.user_id)
    if request.method == 'POST':
        # form = EmployeeForm(request.POST, request.FILES)
        employee_form = EmployeeForm(request.POST, instance=employee)
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            if request.FILES:
                employee.image = request.FILES['image']
            employee.save()

            # return HttpResponseRedirect('/employee/')
            return redirect('employee_detail', pk)
    else:
        user_form = UserForm(instance=user)
        employee_form = EmployeeForm(instance=employee)
    user_image = 'https://www.w3schools.com/howto/img_avatar.png'
    if employee.image:
        user_image = employee.image.url

    context = {
        "add": False,
        "employee": employee,
        "form": employee_form,
        'user_form': user_form,
        "user_image": user_image,
    }
    return render(request, "employee_detail.html", context)
