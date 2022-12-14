"""login_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import imp
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from api.views import Login, Logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('api.urls','api'))),
    path('api_generate_token/', views.obtain_auth_token),
    path('Login/',Login.as_view(), name = 'Login'),
    path('Logout/',Logout.as_view(), name = 'Logout')
  
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
