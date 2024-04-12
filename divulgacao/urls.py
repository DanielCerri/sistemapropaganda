"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path('', home),
    path('tv/<int:pk>/', tv_detail, name='tv_detail'),
    path('tvs',tvscadastradas)
]
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', tvscadastradas),
    path('tv/<int:pk>/', tv_detail, name='tv_detail'),
    path('webm/<int:pk>/', tv_webm),
    path('mp4/<int:pk>/', tv_mp4),
    path('mov/<int:pk>/', tv_mov),
    path('mpeg/<int:pk>/', tv_mpeg),
    path('mkv/<int:pk>/', tv_mkv),
    path('tvs',tvscadastradas)
]
