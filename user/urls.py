from django.contrib import admin
from django.urls import path

from django.conf.urls import include

from . import views

urlpatterns = [
    path('<provider>/login/callback', views.social_login),
    path('', include('allauth.urls')),
]
