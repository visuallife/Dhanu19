"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path("",views.main),
    path("shop/",views.buy),
    path("about/",views.about),
    path("shop/about",views.about),
    path("login/",views.login),
    path("shop/login",views.login),
    path("about/login",views.login),
    path("shop/about/login",views.login),
    path("shop/ar/",views.ar),
    path("shop/home",views.ar),
     path("about/home",views.about),
      path("about/login",views.about),



]
