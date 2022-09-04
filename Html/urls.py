
from django.contrib import admin
from django.urls import path,include
from Html import views
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
urlpatterns = [
    path('',views.index,name='page'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]