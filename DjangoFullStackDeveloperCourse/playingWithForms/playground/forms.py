from django import forms

class FormNames(forms.Form):
    name = forms.CharField(max_length=264,label="Name of User")
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
