"""ProyectoBit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin, auth
from django.contrib.auth.views import logout_then_login,LoginView,LogoutView
from django.urls import path, include

from ProyectoBit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login,name='login'),
    path('mayores/login', views.mayores, name='mayor_login'),
    path('ninos/login', views.ninos, name='ninos_login'),
    path('adultos/login', views.adultos, name='adultos_login'),
    path('varones/login', views.varones, name='varones_login'),
    path('juveniles/login', views.juveniles, name='juveniles_login'),
    path('mujeres/login', views.mujeres, name='mujeres_login'),

    path('ninos/', views.ninos, name='ninos'),
    path('juveniles/', views.juveniles, name='juveniles'),
    path('varones/', views.varones, name="varones"),
    path('mujeres/', views.mujeres, name="mujeres"),
    path('adultos/', views.adultos, name="adultos"),
    path('mayores/', views.mayores, name="mayores"),


    path('', LoginView.as_view(template_name='DeportesUY/ninos.html'), name='log'),

    url(r'^logout/$', LogoutView.as_view(template_name='DeportesUY/index.html'), name='logout'),




]