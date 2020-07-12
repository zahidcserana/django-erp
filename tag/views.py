from .models import Tag
from .forms import TagForm

from django.shortcuts import get_object_or_404, redirect, render


def tag_index(request):
    data = Tag.objects.all()
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['id']:
                model_data = Tag.objects.get(id=form.cleaned_data['id'])
                model_data.name = form.cleaned_data["name"]
                model_data.save()
            else:
                input_data = Tag(
                    name=form.cleaned_data["name"],
                )
                input_data.save()
            return redirect('tag_index')

    context = {
        "form": form,
        "data": data,
    }

    return render(request, 'tag_index.html', context)


def tag_delete(request, pk=None):
    data = get_object_or_404(Tag.objects.all(), pk=pk)

    data.delete()
    return redirect('tag_index')
