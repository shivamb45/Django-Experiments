from django.conf.urls import url
from app import views

#Templates_namespace
app_name = 'app'

# urlpatterns = [
# url(r'other/',views.other,name="otherKaPage"),
# url(r'relative_url_templates/',views.relative_url_templates,name="relative_url_templatesKaPage"),
# url(r'$',views.index,name="indexKaPage"),
# ]

urlpatterns = [
url(r'^other/$',views.other,name="otherKaPage"),
url(r'^relative/$',views.relative_url_templates,name="relativeKaPage")
]
