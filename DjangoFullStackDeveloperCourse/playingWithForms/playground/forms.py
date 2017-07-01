from django import forms
from django.core import validators

""" Custom Validor Method for name to start with S. It is required to have a parameter named as value """
def custom_name_initial_valdator(value):
    if value[0].lower != 's':
        raise forms.ValidationError("Name should start with Letter S")

class FormNames(forms.Form):
    name = forms.CharField(max_length=264,label="Name of User",validators=[custom_name_initial_valdator])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    """This Method is detected by django for respective field. This is by far the most basic method
    cleaning and validation of data supplied to form"""
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError(" Bot activity suspected !")
        return botcatcher
