from django import forms

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
        widget=forms.Select(attrs={
            "class": "form-control m-input m-input--air m-input--pill",
        }),
        choices=Statuses
    )

    class Meta:
        model = Employee
        fields = ['name', 'email', 'mobile', 'address', 'about', 'image', 'status']
