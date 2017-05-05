from django.conf.urls import url
from . import views

urlpatterns =\
[
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^blog/$', views.ArticleListView.as_view(), name='blog'),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name="detail"),
    url(r'^blog/search/$', views.search, name='search'),

]