from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    contextVar = {'title' : 'HomePage for Playing with Forms','desc':'Hello!','desc2': 'goto /forms','dev_name':'Shivam Bharadwaj','url':'home/forms'}
    return render(req,'home/index.html',context=contextVar)
def formsPage(req):
    return "Under Construction"
