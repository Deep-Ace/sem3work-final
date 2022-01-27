from django.urls import path
from accounts import views

urlpatterns = [
    path('userLogin', views.userLogin, name='userLogin'),
    path('userRegister', views.userRegister, name='userRegister'),
    path('dashboard', views.dashboard, name='dashboard'),
]
