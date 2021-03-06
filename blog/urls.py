from django.conf.urls import url
from .views import blogposts, viewpost, newpost, editpost, addcomment, likepost, unlikepost

urlpatterns = [
    url(r'^posts$', blogposts, name="posts"),
    url(r'^posts/(\d+)$', viewpost, name="viewpost"),
    url(r'^posts/new/$', newpost, name="newpost"),
    url(r'^posts/(\d+)/edit/', editpost, name="editpost"),
    url(r'^posts/(\d+)/comments/add$', addcomment, name="addcomment"),
    url(r'^posts/(\d+)/like/', likepost, name="likepost"),
    url(r'^posts/(\d+)/unlike/', unlikepost, name="unlikepost"),
    ]