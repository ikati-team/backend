from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    """Skills specified in user's profile"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = "skill"
        verbose_name_plural = "skills"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Profile(models.Model):
    """User's profile"""
    user = models.OneToOneField(
        User, related_name='profile',
        on_delete=models.PROTECT)
    city = models.CharField(max_length=100, help_text="City where you live",  blank=True, default='')
    biography = models.TextField(help_text="Tell everyone about yourself",  blank=True, default='')
    skill = models.ManyToManyField(Skill, help_text="things you can do, techs you know", blank=True, null=True)
    preference_role = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


class SocialNetwork(models.Model):
    """Link to a specified social network"""
    class Type(models.TextChoices):
        GITHUB = "github", "Github"
        GITLAB = "gitlab", "Gitlab"
        LINKEDIN = "linkedin", "LinkedIn"

    type = models.CharField(max_length=30, choices=Type.choices)
    link = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_network')

    class Meta:
        verbose_name = "social network"
        verbose_name_plural = "social networks"

    def __str__(self):
        return f"{self.profile} - {self.type}"


class Comment(models.Model):
    """User's profile comment"""
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profile')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.PositiveSmallIntegerField()
    text = models.TextField()

    def __str__(self):
        return f"{self.author.username} - {self.target}"
