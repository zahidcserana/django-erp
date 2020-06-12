from django.db.models import Q
from django.http import HttpResponseRedirect

from .models import Department
from .forms import DepartmentForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, redirect, render


def department_index(request):
    data = Department.objects.all()
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['id']:
                model_data = Department.objects.get(id=form.cleaned_data['id'])
                model_data.name = form.cleaned_data["name"]
                model_data.status = form.cleaned_data["status"]
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

    return render(request, 'designation_index.html', context)


def department_delete(request, pk=None):
    data = get_object_or_404(Department.objects.all(), pk=pk)

    data.delete()
    return redirect('department_index')
