"""Defines url patterns for learning logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
        #Home page
        url(r'^$', views.index, name='index'),
    ]
