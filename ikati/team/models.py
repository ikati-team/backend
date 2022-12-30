from django.db import models
from django.conf import settings


class Team(models.Model):
    """Teams with users"""
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, through="TeamMember")
    description = models.TextField()
    public_message = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    """User in team representation"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_member')
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.team} - {self.user}"


class TextNote(models.Model):
    """A note on a team's  board"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField(auto_now=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "text note"
        verbose_name_plural = "text notes"


class Invite(models.Model):
    target = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.target} - {self.team}"
