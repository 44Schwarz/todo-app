from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    path('projects/', views.all_projects),
    url(r'projects/(?P<project_id>\d+)', views.detail),
]
