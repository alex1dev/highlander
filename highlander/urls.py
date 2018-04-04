"""highlander URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from club import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', views.index, name='index'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^example', views.example, name='example'),
    url(r'^hotel', views.hotel, name='hotel'),
    url(r'^landscapes', views.landscapes, name='landscapes'),
    url(r'^login', views.ulogin, name='login'),
    url(r'^logout', views.ulogout, name='logout'),
    url(r'^register', views.register, name='register'),
    url(r'^booking', views.booking, name='booking'),
    url(r'^congrat', views.congrat, name='congrat'),
]
