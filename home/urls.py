
from django.contrib import admin
from django.urls import path
from Html import views

urlpatterns = [
    path('python', views.index),
    path('',views.index),
]