"""
Hackathon #hackRussia
"""

from django.conf.urls import url

from offers import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^(?P<id>[0-9]+)/$", views.show, name="show"),
    url(r"^new/$", views.new, name="new"),
    url(r"^(?P<id>[0-9]+)/edit/$", views.edit, name="edit"),
    url(r"^(?P<id>[0-9]+)/accept/$", views.accept, name="accept"),
]
