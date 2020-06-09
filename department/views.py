from django.db.models import Q
from django.http import HttpResponseRedirect

from .models import Department
from .forms import DepartmentForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect


def department_index(request):
    data = Department.objects.all()
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['id']:
                model_data = Department.objects.get(id=form.cleaned_data['id'])
                model_data.name = form.cleaned_data["name"]
                model_data.save()
            else:
                input_data = Department(
                    name=form.cleaned_data["name"],
                    status=form.cleaned_data["status"],
                )
                input_data.save()
            return redirect('department_index')

    context = {
        "form": form,
        "data": data,
    }

    return render(request, 'department_index.html', context)


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


def department_add(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            input_data = Department(
                name=form.cleaned_data["name"],
                status=form.cleaned_data["status"],
            )
            input_data.save()
            return redirect('index')

    context = {
        "form": form,
    }
    return render(request, "add.html", context)
