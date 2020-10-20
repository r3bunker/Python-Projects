from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profiles_console', views.profiles_console, name='profiles_console'),
    path('<int:pk>/details/', views.details, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('confirmdelete/', views.confirmed, name='confirmed'),
    path('createUser/', views.createUser, name='createUser'),
]
