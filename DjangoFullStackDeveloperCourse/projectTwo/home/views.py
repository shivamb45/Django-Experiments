from django.shortcuts import render
from django.http import HttpResponse
from home.models import Users
# Create your views here.

def index(req):
    varValues = {'desc': 'Sample Project two Using Templates static files and DB. goto /Users for more.',
    'title': 'Project 2',
    'heading': 'Project 2',
    'desc2':'ExploreUsers',
    'dev_name': 'Shivam',
    'url':'/users'}
    return render(req,'home/index.html',context=varValues)
def displayUsers(req):
    users = Users.objects.all()
    convar = {'userList':users}
    return render(req,'home/users.html',context=convar)
