"""
Hackathon #hackRussia
"""

import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render, redirect

from offers.forms import NewForm, EditForm
from offers.models import Offer


@login_required
def index(request):
    return render(request, "offers/index.html", {
        "offeror_of": reversed(request.user.profile.offeror.all()),
        "offeree_of": reversed(request.user.profile.offeree.all())
    })


@login_required
def show(request, id):
    try:
        offer = Offer.objects.select_related("offeror", "offeree").get(pk=id)
    except Offer.DoesNotExist:
        return HttpResponseNotFound("Offer with this ID does not exist")

    # User is not a participant of this offer
    if request.user.profile not in (offer.offeror, offer.offeree):
        return HttpResponseForbidden(
            "You do not have enough permissions to view this offer")

    # User first time read this offer
    if not offer.seen and request.user.profile == offer.offeree:
        offer.seen = True
        offer.save()

    return render(request, "offers/show.html", {
        "offer": offer
    })


@login_required
def new(request):
    offer = Offer()

    if request.method == "POST":
        offer.offeror = request.user.profile
        form = NewForm(request.POST, instance=offer)

        if form.is_valid():
            form.save()
            messages.success(request, "Договор создан!")
            return redirect("offers:show", id=offer.id)
        else:
            messages.error(request, "Введите корректные данные!")
    else:
        form = NewForm(instance=offer)

    return render(request, "offers/new.html", {
        "form": form
    })


@login_required
def edit(request, id):
    try:
        offer = Offer.objects.select_related("offeror").get(pk=id)
    except Offer.DoesNotExist:
        return HttpResponseNotFound("Offer with this ID does not exist")

    # User is not a offeror of this offer
    if request.user.profile != offer.offeror:
        return HttpResponseForbidden(
            "You do not have enough permissions to edit this offer")

    if offer.accepted:
        messages.warning(request,
                         "Договор уже был принят! Вы не можете изменить его.")
        return redirect("offers:show", id=offer.id)

    if request.method == "POST":
        form = EditForm(request.POST, instance=offer)

        if form.is_valid():
            form.save()
            messages.success(request, "Договор обновлен!")
            return redirect("offers:show", id=offer.id)
        else:
            messages.error(request, "Введите корректные данные!")
    else:
        form = EditForm(instance=offer)

    return render(request, "offers/edit.html", {
        "offer": offer,
        "form": form
    })


@login_required
def accept(request, id):
    try:
        offer = Offer.objects.select_related("offeree").get(pk=id)
    except Offer.DoesNotExist:
        return HttpResponseNotFound("Offer with this ID does not exist")

    # User is not a offeree of this offer
    if request.user.profile != offer.offeree:
        return HttpResponseForbidden(
            "You do not have enough permissions to accept this offer")

    if offer.accepted:
        messages.warning(request, "Договор уже был принят вами!")
    else:
        offer.accepted = True
        offer.accepted_date = datetime.datetime.now()
        offer.save()
        messages.success(request, "Договор успешно принят!")

    return redirect("offers:show", id=offer.id)
