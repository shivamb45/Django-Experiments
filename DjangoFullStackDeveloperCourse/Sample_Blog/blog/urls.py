from blog import views
from django.conf.urls import url

urlpatterns = [
url(r'^about/$',views.AboutView.as_view(),name="aboutPage"),
url(r'^$',views.PostListView.as_view(),name='homePage'),
url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name="post_detail"),
url(r'^post/new/$',views.CreatePostView.as_view(),name='createPostPage'),
url(r'^post/(?P<pk>\d+)/edit/$',views.UpdatePostView.as_view(),name='updatePostPage'),
url(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='deletePostPage'),
url(r'^drafts/$',views.DrafListView.as_view(),name='draftsListPage'),
url(r'^comment/on/post/(?P<pk>\d+)$',views.add_comment_to_post,name='postComment'),
url(r'^comment_approval/(?P<pk>\d+)$',views.comment_approve,name='comment_approve'),
url(r'^comment_remove/(?P<pk>\d+)$',views.comment_remove,name='comment_remove'),
url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
]
