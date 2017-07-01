from django.shortcuts import render
from . import forms
from . import models
# Create your views here.

def index(req):
    return render(req,'templates/app/index.html')
def formPage(req):
    msg = "Hello Form needs to be filled first"
    form = forms.GenericForm()

    if req.method == 'POST':
        enteredData = req.POST
        name = enteredData['name']
        email = enteredData['email']
        tmp = models.GenericUser()
        tmp.name = name
        tmp.email = email
        tmp.save()
        print(tmp.created_on)
        msg = "User saved !"
        contextVar = {'msg':msg,'db':tmp}
        return render(req,'templates/app/formPage.html',context=contextVar)

    contextVar = {'msg':msg,'form':form}
    return render(req,'templates/app/formPage.html',context=contextVar)
