"""sem3work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.urls import path
# from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('adminlogin/', auth_views.LoginView.as_view(template_name='accounts/adminlogin.html'), name='adminlogin'),

     # path('adminlogin', LoginView.as_view(template_name='accounts/adminlogin.html'),name='adminlogin'),
    path('admin/', admin.site.urls),
    # path('adminlogin/', auth_views.LoginView.as_view(template_name='accounts/adminlogin.html'), name='adminlogin'),
   
    path('', include('ecom.urls')),
    path('', include('accounts.urls')),
    path('', include('store.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
