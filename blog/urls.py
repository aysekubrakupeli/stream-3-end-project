from django.conf.urls import url
from .views import blogposts, viewpost, newpost, editpost, addcomment, like_count_blog

urlpatterns = [
    url(r'^posts$', blogposts, name="posts"),
    url(r'^posts/(\d+)$', viewpost, name="viewpost"),
    url(r'^posts/new/$', newpost, name="newpost"),
    url(r'^posts/(\d+)/edit/', editpost, name="editpost"),
    url(r'^posts/(\d+)/comments/add$', addcomment, name="addcomment"),
    url(r'^posts/(?P<slug>[-_\w]*)/$', viewpost, name='post_detail'),
    url(r'^posts/?post_id=(\d+)$', like_count_blog, name='like_count_blog'),
    ]