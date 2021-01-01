from django.conf.urls import url, include
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.index),
    path('delete/<str:name>', views.delete)
]