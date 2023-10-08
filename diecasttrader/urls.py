"""
URL configuration for diecasttrader project.

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
from django.urls import path, include
from products.views import homepage
from products.views import hotwheels
from products.views import maisto
from products.views import majorette
from products.views import matchbox
from products.views import tomica
from products.views import others


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage),
    path('home/hotwheels/', hotwheels),
    path('home/maisto/', maisto),
    path('home/majorette/', majorette),
    path('home/matchbox/', matchbox),
    path('home/tomica/', tomica),
    path('home/others/', others),
]
