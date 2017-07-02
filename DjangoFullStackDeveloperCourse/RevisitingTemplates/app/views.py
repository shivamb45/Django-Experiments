from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req,'app/index.html',{'title':'Welcome Page'})

def other(req):
    return render(req,'app/other.html',{'title':'Other ka Page'})

def relative_url_templates(req):
    return render(req,'app/relative_url_templates.html',{'title':'Relative Ka Paege'})

def filterPage(req):
    import datetime
    contextVar = {'heading':"the heading text",'p':datetime.datetime.now(),'someNumber':123456}
    return render(req,'app/filter.html',context=contextVar)
