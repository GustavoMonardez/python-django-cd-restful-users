from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r"^users$", views.index),
    url(r"^users/new$", views.new),
    url(r"^users/(?P<user>\d+)/edit$", views.edit),
    url(r"^users/(?P<user>\d+)$", views.show),
    url(r"^users/create$", views.create),
    url(r"^users/(?P<user>\d+)/destroy$", views.destroy),
    url(r"^users/update$", views.update),
    url(r"^users/go_back$", views.go_back)
]