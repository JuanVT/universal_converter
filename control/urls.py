"""universal_converter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from control.views import (
    home,
    volume_converter,
    length_converter,
    time_converter,
    currency_converter,
    temperature_converter,
    weight_converter,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^volume_converter/$', volume_converter, name='volume_converter'),
    url(r'^length_converter/$', length_converter, name='length_converter'),
    url(r'^time_converter/$', time_converter, name='time_converter'),
    url(r'^currency_converter/$', currency_converter, name='currency_converter'),
    url(r'^temperature_converter/$', temperature_converter, name='temperature_converter'),
    url(r'^weight_converter/$', weight_converter, name='weight_converter'),
    url(r'^speed_converter/$', speed_converter, name='speed_converter'),
]
