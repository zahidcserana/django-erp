from django import forms

from .models import Designation


class DesignationForm(forms.ModelForm):
    id = forms.IntegerField(
        required=False
    )
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Your Name"
        })
    )
    Statuses = (('ACTIVE', 'Active'),('INACTIVE', 'Inactive'),)
    status = forms.ChoiceField(
        widget=forms.Select(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
        }),
        choices=Statuses
    )

    class Meta:
        model = Designation
        fields = ['id', 'name', 'status']
