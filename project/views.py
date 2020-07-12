from .models import Project
from .forms import ProjectForm

from django.shortcuts import get_object_or_404, redirect, render


def project_index(request):
    data = Project.objects.all()
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['id']:
                model_data = Project.objects.get(id=form.cleaned_data['id'])
                model_data.name = form.cleaned_data["name"]
                model_data.status = form.cleaned_data["status"]
                model_data.save()
            else:
                input_data = Project(
                    name=form.cleaned_data["name"],
                    status=form.cleaned_data["status"],
                )
                input_data.save()
            return redirect('project_index')

    context = {
        "form": form,
        "data": data,
    }

    return render(request, 'project_index.html', context)


def project_delete(request, pk=None):
    data = get_object_or_404(Project.objects.all(), pk=pk)

    data.delete()
    return redirect('project_index')
