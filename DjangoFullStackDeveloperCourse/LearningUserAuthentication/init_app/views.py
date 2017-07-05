from django.shortcuts import render
from django.http import HttpResponse
from init_app.forms import UserForm,UserProfileInfoForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(req):
    return render(req,'init_app/index.html')
@login_required
def special(req):
    return HttpResponse('You are logged in')

def registeredMethod(req):
    registered = False

    if req.method == 'POST':
        user_form = UserForm(data = req.POST)
        profile_form = UserProfileInfoForm(data = req.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_image' in req.FILES:
                profile.profile_image = req.FILES['profile_image']
            profile.save()

            registered = True
        else:
            print("Not a POST Request")
            print(profile_form.errors,user_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(req,'init_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
