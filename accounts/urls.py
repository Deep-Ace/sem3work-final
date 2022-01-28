from django.urls import path
from accounts import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [ 
    # User Related Views
    path('userLogin', views.userLogin, name='userLogin'),
    path('userRegister', views.userRegister, name='userRegister'),
    path('logout', views.logout, name='logout'),
    path('resetPass', views.resetPass, name='resetPass'),
    path('userDashboard', views.userDashboard, name='userDashboard'),

    # Important Function Defined
    path('afterlogin', views.afterlogin_view, name='afterlogin'),

    # path('adminclick', views.adminclick_view),
    # Admin Related Views
    path('adminDashboard', views.adminDashboard,name='adminDashboard'),
    path('logoutadmin', views.logoutadmin, name='logoutadmin'),
    path('admin-products', views.admin_products_view,name='admin-products'),
    path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('update-product/<int:pk>', views.update_product_view,name='update-product'),
]
