from django.conf.urls import url
from app import views
urlpatterns = [
url(r'^$',views.index,name="welcomePage"),
url(r'formPage',views.formPage,name="formPageDisplay")
]
