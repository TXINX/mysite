from django.conf.urls import url
from . import views

urlpatterns =\
[
    url(r'^blog/$', views.posts, name='blog'),
    url(r'^re/$', views.refresh, name='refresh'),
    url(r'^$', views.main_page, name='index'),
    url(r'^blog/(?P<index>[0-9]*)/$', views.post, name='blog'),
]