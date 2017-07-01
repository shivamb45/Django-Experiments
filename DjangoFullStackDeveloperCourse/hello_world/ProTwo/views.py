from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return HttpResponse("<em>Hello Emphasized text</em>")
def help(req):
    cont = {'desc':'this is a sample help text'}
    return render(req,'ProTwo/help.html',context=cont)
def showImg(req):
    return render(req,'ProTwo/staticimg.html')
