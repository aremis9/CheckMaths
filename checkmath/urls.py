"""checkmath URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import genmath
import precal
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='main/index.html'),
        name='home'),
    # url(r'^contact/$', TemplateView.as_view(template_name='main/contact.html'),
    #     name='home'),
    path('contact/', views.contact, name="contact"),
    path('genmath/', include('genmath.urls')),
    path('precal/', include('precal.urls')),
    path('bscal/', include('bscal.urls'))
]
