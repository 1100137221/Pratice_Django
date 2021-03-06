"""mysite URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from weather.views import weather
from rate.views import rate
from home.views import home

from rest_framework.routers import DefaultRouter
from rate.views import RateViewSet
from weather.views import WeatherViewSet
router = DefaultRouter()
router.register(r'rate', RateViewSet)
router.register(r'weather', WeatherViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^weather/$', weather),
    url(r'^rate/$', rate),
    url(r'^api/', include(router.urls)),
    url('', home),
]
