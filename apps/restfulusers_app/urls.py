from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r"^users$", views.index),
    url(r"^users/new$", views.new),
    url(r"^users/<id>/edit$", views.edit),
    url(r"^users/<id>$", views.show),
    url(r"^users/create$", views.create),
    url(r"^users/<id>/destroy$", views.destroy),
    url(r"^users/<id>/update$", views.update)
]