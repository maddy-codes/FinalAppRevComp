from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("uploaded", views.uploaded, name="uploaded"),
    path('download', views.download, name='download'),
    path('accmaker', views.accmaker, name='accmaker'),
    path('uploadedacc', views.uploadedacc, name='uploadedacc'),
    path('downloadacc', views.downloadacc, name='downloadacc'),
    path('goats',views.goats, name='goatspage'),
    #path('loancalc',loancalc.views.loancalc, name='loancalc')
]

