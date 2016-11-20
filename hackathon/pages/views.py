"""
Hackathon #hackRussia
"""

from django.shortcuts import render, redirect

from profiles.forms import EditForm, SignupForm
from profiles.models import Profile


def index(request):
    return render(request, "index.html")


def get_started(request):
    if request.user.is_authenticated:
        return redirect("offers:index")
    else:
        return redirect("login")
