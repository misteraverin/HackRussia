"""
Hackathon #hackRussia
"""

from django.conf.urls import url

from profiles import views

urlpatterns = [
    # url(r"^$", views.index, name="index"),
    url(r"^(?P<id>[0-9]+)/$", views.show, name="show"),
    url(r"^me/$", views.me, name="me"),
    url(r"^me/edit/$", views.edit, name="edit"),
]
