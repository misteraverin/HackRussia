"""
Hackathon #hackRussia
"""

from django.conf.urls import include, url
from django.contrib import admin

from pages.views import index, get_started
from profiles.views import signup

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^get-started/", get_started, name="get-started"),
    url(r"^pages/", include("pages.urls", namespace="index")),

    url(r"^offers/", include("offers.urls", namespace="offers")),
    url(r"^profiles/", include("profiles.urls", namespace="profiles")),

    url(r"^", include("django.contrib.auth.urls")),
    url(r"^signup/$", signup, name="signup"),
    url(r"^admin/", admin.site.urls),
]
