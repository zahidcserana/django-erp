from django import forms

from department.models import Department
from designation.models import Designation
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Your Name"
        })
    )
    mobile = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Your Mobile"
        })
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Your Email"
        })
    )
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Your Addrress"
        })
    )
    about = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": ""
        })
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            "class": "attachment_upload",
            "placeholder": "Select a file"
        })
    )
    Statuses = (('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'),)
    status = forms.ChoiceField(
        error_messages={
            'required': "Please Select a Status."
        },
        widget=forms.Select(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
        }),
        choices=Statuses
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="-Select-",
        widget=forms.Select(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
        })
    )
    designation = forms.ModelChoiceField(
        queryset=Designation.objects.all(),
        empty_label="-Select-",
        widget=forms.Select(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
        })
    )

    class Meta:
        model = Employee
        fields = ['name', 'email', 'mobile', 'address', 'about', 'image', 'status', 'department','designation']
