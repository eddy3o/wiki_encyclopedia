from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(r'wiki/<entry>', views.wiki, name="wiki"),
    #re_path(r'^results/$', views.results, name="results")

    re_path(r'^results/$', views.results, name="results")
]
