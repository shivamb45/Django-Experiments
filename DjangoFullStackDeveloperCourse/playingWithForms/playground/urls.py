from django.conf.urls import url
from playground import views

urlpatterns = [
url(r'^$',views.index,name="IndexPageForms"),
url(r'formDisplay',views.form_page,name="formDisplayPage")
]
