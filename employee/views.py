from django.db.models import Q
from django.http import HttpResponseRedirect

from employee.models import Employee
from employee.forms import EmployeeForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .utils import button_class


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
        employees = Employee.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(employees, 2)
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
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = Employee(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                mobile=form.cleaned_data["mobile"],
                address=form.cleaned_data["address"],
                about=form.cleaned_data["about"],
            )
            employee.save()
            return redirect('employee_index')

    context = {
        "form": form,
    }
    return render(request, "employee_add.html", context)


def employee_detail(request, pk=None):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee.name = form.cleaned_data["name"]
            employee.email = form.cleaned_data["email"]
            employee.mobile = form.cleaned_data["mobile"]
            employee.address = form.cleaned_data["address"]
            employee.about = form.cleaned_data["about"]
            if request.FILES:
                employee.image = request.FILES['image']
            employee.save()

            # return HttpResponseRedirect('/employee/')
            return redirect('employee_detail', pk)
    else:
        form = EmployeeForm(instance=employee)

    context = {
        "employee": employee,
        "form": form,
    }
    return render(request, "employee_detail.html", context)
