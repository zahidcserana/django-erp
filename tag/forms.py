from django import forms

from .models import Tag


class TagForm(forms.ModelForm):
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

    class Meta:
        model = Tag
        fields = ['id', 'name']
