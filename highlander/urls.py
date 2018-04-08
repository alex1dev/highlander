
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
