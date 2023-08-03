from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("uploaded", views.uploaded, name="uploaded"),
    path('download', views.download, name='download')
]

