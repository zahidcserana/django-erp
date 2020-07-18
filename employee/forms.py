from django import forms
from django.contrib.auth.models import User

from department.models import Department
from designation.models import Designation
from employee.models import Employee

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Enter Username"
        })
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Email"
        })
    )
    password = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.PasswordInput(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Password"
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class EmployeeForm(forms.ModelForm):
    mobile = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Mobile"
        })
    )
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
            "placeholder": "Address"
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
        fields = ['mobile', 'address', 'about', 'image', 'status', 'department', 'designation']
