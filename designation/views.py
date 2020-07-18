from .models import Designation
from .forms import DesignationForm

from django.shortcuts import get_object_or_404, redirect, render


def designation_index(request):
    data = Designation.objects.all()
    form = DesignationForm()
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['id']:
                model_data = Designation.objects.get(id=form.cleaned_data['id'])
                model_data.name = form.cleaned_data["name"]
                model_data.status = form.cleaned_data["status"]
                model_data.save()
            else:
                input_data = Designation(
                    name=form.cleaned_data["name"],
                    status=form.cleaned_data["status"],
                )
                input_data.save()
            return redirect('designation_index')

    context = {
        "form": form,
        "data": data,
    }

    return render(request, 'designation_index.html', context)


def designation_delete(request, pk=None):
    data = get_object_or_404(Designation.objects.all(), pk=pk)

    data.delete()
    return redirect('designation_index')
