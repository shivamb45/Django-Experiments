from django.conf.urls import url
from home import views
urlpatterns = [
url(r'^forms',views.formsPage,name="formsPage"),
url(r'^$',views.index,name="indexPage")
]
