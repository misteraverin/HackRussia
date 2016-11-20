"""
Hackathon #hackRussia
"""

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from profiles.forms import EditForm, SignupForm
from profiles.models import Profile


# @login_required
# def index(request):
#     profiles = Profile.objects.select_related("user").all()
#
#     return render(request, "profiles/index.html", {
#         "profiles": profiles
#     })


@login_required
def show(request, id):
    try:
        profile = Profile.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponseNotFound("User with this ID does not exist")

    return render(request, "profiles/show.html", {
        "profile": profile
    })


@login_required
def me(request):
    return render(request, "profiles/show.html", {
        "profile": request.user.profile
    })


@login_required
def edit(request):
    if request.method == "POST":
        form = EditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Профиль обновлен!")
            return redirect("profiles:me")
        else:
            messages.error(request, "Введите корректные данные!")
    else:
        form = EditForm(instance=request.user)

    return render(request, "profiles/edit.html", {
        "form": form
    })


def signup(request):
    if request.user.is_authenticated:
        messages.warning(request, "Вы уже авторизованы")
        redirect("index")

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"]
            )

            login(request, user)
            return redirect("get-started")
        else:
            messages.error(request, "Введите корректные данные!")
    else:
        form = SignupForm()

    return render(request, "profiles/signup.html", {
        "form": form
    })
