from django.shortcuts import render
from playground import forms

# Create your views here.

def index(req):
    contextVar = {'heading' : 'Welcome to playground for Django Forms','msg':'goto /formDisplay for real fun.'}
    return render(req,'playground/index.html',context=contextVar)

def form_page(req):
    formObj = forms.FormNames()
    if req.method == 'POST':
        print("Got some Data")
        formData = forms.FormNames(req.POST)
        print(str(formData))
        if formData.is_valid():
            print("Validated")
            print("Name - {}\nemail -{}\ntext-{}\n".format(formData.cleaned_data['name'],formData.cleaned_data['email'],formData.cleaned_data['text']))
    return render(req,'playground/form_page.html',{'forms_object':formObj})
