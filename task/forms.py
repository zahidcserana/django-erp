from django import forms

from .models import Task
from tag.models import Tag
from project.models import Project


class TaskForm(forms.ModelForm):
    id = forms.IntegerField(
        required=False
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Your Name"
        })
    )
    Statuses = (('ACTIVE', 'Active'), ('HOLD', 'Hold'), ('IN_PROGRESS', 'In Progress'), ('COMPLETE', 'Complete'), ('ARCHIVE', 'archive'), ('INACTIVE', 'Inactive'))
    status = forms.ChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
        }),
        choices=Statuses
    )
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        empty_label="-Select-",
        widget=forms.Select(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
        })
    )
    project = forms.ModelChoiceField(
        queryset=Project.objects.all(),
        empty_label="-Select-",
        widget=forms.Select(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
        })
    )

    class Meta:
        model = Task
        fields = ['id', 'project', 'tag', 'description', 'status']
