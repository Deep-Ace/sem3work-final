from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [ 
    path('userLogin', views.userLogin, name='userLogin'),
    path('userRegister', views.userRegister, name='userRegister'),
    path('logout', views.logout, name='logout'),
    path('resetPass', views.resetPass, name='resetPass'),
    path('userDashboard', views.userDashboard, name='userDashboard'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),

    # path('adminclick', views.adminclick_view),
    
    path('adminDashboard', views.adminDashboard,name='adminDashboard'),
]
