from django.conf.urls import url
from app.views import CBV,TBV,SchoolListView,SchoolDetailView,SchoolCreateView


app_name = 'app'

urlpatterns = [
url(r'^cbv/$',CBV.as_view(),name='ViewBasedPage'),
url(r'^tbv/$',TBV.as_view(),name='TemplateBasedViewPage'),
url(r'^listview/$',SchoolListView.as_view(),name='ListViewPage'),
url(r'^detailview/<pk>$',SchoolDetailView.as_view(),name='DetailViewPage'),
url(r'^school/(?P<pk>[-\w]+)$',SchoolDetailView.as_view(),name='Detail'),
url(r'^create/',SchoolCreateView.as_view(),name='createSchool'),
]
