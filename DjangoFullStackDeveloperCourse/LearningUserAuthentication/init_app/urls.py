from django.conf.urls import url
from init_app import views


app_name = 'init_app'

urlpatterns = [
url(r'^register/',views.registeredMethod,name='registerURL'),
]
