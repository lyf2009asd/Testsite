from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts_list, name="posts_list"),
    url(r'^create/$', views.posts_create, name="posts_create"),
    url(r'^(?P<id>\d+)/$', views.posts_detail, name="posts_detail"),
    url(r'^(?P<id>\d+)/edit/$', views.posts_update, name="posts_update"),
    url(r'^(?P<id>\d+)/delete/$', views.posts_delete, name="posts_delete"),
]