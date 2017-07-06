from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import School,Student
# Create your views here.
def index(req):
    return render(req,'app/index.html',{'title':'Advanced Topic','heading':'Welcome to Advanced Sections of Django','isLinkActive':'','paragraph':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

class CBV(View):
    def get(self,request):
        return render(request,'app/index.html',{'title':'Class Based View','heading':'Class Based View - View','isLinkActive':'active','paragraph':'This page is Generated using Simplest Class based View - "View". '})

class TBV(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,**kwargs):
        contex_var = super().get_context_data(**kwargs)
        contex_var['heading'] = 'Template Based View Page'
        contex_var['paragraph'] = 'This Page is generated by TemplateBasedView'
        contex_var['title'] = 'Template View usage'
        return contex_var

class SchoolListView(ListView):
    # generally returns the context_object_name as model lower case name and adds underscore _list
    context_object_name = 'schools'
    model = School
    template_name = 'app/school_list.html'

    def get_context_data(self,**kwargs):
        context_var = super(SchoolListView,self).get_context_data(**kwargs)
        context_var['title'] = 'List View Example Page'
        return context_var


class SchoolDetailView(DetailView):
    # genrally returns the context_object_name as model ka lowercase name
    context_object_name = 'school_detail'
    model = School
    template_name = 'app/school_detail.html'

    def get_context_data(self,**kwargs):
        context_var = super(SchoolDetailView,self).get_context_data(**kwargs)
        context_var['title'] = 'List View Example Page'
        return context_var

class SchoolCreateView(CreateView):

    model = School
    fields = ('name','location','principal')
    def get_context_data(self,**kwargs):
        context_var = super(SchoolCreateView,self).get_context_data(**kwargs)
        context_var['title'] = 'Create View Example Page'
        return context_var
