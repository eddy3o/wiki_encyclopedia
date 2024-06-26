from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("wiki/", views.wiki, name="wiki")
    path(r'wiki/<entry>', views.wiki, name="wiki")
    # url(r'^(?P<username>\w+)/$', views.profile_page,),
]
