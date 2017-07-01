from django.conf.urls import url
from ProTwo import views

urlpatterns = [
url(r'^help',views.help,name="protwohelp"),
url(r'^$',views.index,name="protwoindex"),
url(r'^staticimg',views.showImg,name="showImgPage")
]
