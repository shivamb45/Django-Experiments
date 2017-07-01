from django import forms
from app.models import GenericUser

class GenericForm(forms.ModelForm):
    class Meta:
        model = GenericUser()
        exclude = ['created_on']
