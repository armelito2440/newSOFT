# sendemail/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index


urlpatterns = [
   path('index/',views.index, name='/index'),
]