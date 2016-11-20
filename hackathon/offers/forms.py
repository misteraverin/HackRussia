"""
Hackathon #hackRussia
"""

from django import forms
from offers.models import Offer


class NewForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ("offeree", "terms")


class EditForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ("terms",)
