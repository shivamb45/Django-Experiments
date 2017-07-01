from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return HttpResponse("This is index of First_APP")
def random(req):
    return HttpResponse("Random Page. Go Back Simon! ")
def templateEx(req):
    mydict = { 'insert_me' : 'hello world variable valuer'}
    return render(req,'index.html',context=mydict)
