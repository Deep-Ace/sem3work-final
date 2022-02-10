from django.contrib import admin
from django.urls import path
from ecom import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about', views.about, name='about'),
]
