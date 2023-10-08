from django.urls import path
from . import views

urlpatterns = [
    path('home', views.homepage, name="home"),
    path('hotwheels', views.hotwheels, name="hotwheels"),
    path('maisto', views.maisto, name="maisto"),
    path('majorette', views.majorette, name="majorette"),
    path('tomica', views.tomica, name="tomica"),
    path('matchbox', views.homepage, name="matchbox"),
    path('others', views.homepage, name="others"),
]
