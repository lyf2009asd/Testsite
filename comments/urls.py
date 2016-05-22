from django.conf.urls import url
from django.contrib import admin
from .views import (
    comment_thread,
)
urlpatterns = [
    url(r'^(?P<id>\d+)/$', comment_thread, name="thread"),
    # url(r'^(?P<id>\d-]+)/$', views.posts_detail, name="comment_delete")
]