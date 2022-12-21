from django.db import models
from django.conf import settings


class TextNote(models.Model):
    """A note on a team's board"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "text note"
        verbose_name_plural = "text notes"


class Team(models.Model):
    """Teams with users"""
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    description = models.TextField()
    public_message = models.CharField(max_length=200)
    notes = models.ManyToManyField(TextNote)
