from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$', views.index),
  url(r'^process$', views.process),
  url(r'^(?P<id>\d+)/remove$', views.remove),
  url(r'^(?P<id>\d+)/like$', views.like)
  ]