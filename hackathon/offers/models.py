"""
Hackathon #hackRussia
"""

from django.db import models
from profiles.models import Profile


class Offer(models.Model):
    offeror = models.ForeignKey(Profile, related_name="offeror")
    offeree = models.ForeignKey(Profile, related_name="offeree")

    # title = models.CharField(max_length=255)
    terms = models.TextField()

    seen = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    accepted_date = models.DateTimeField(null=True)

    def __str__(self):
        return "Договор #" + str(self.id)
