from django.db import models
from django.conf import settings


class Skill(models.Model):
    """Skills specified in user's profile"""
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "skill"
        verbose_name_plural = "skills"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Comment(models.Model):
    """User's profile comment"""
    author = models.ManyToManyField(settings.AUTH_USER_MODEL)
    mark = models.PositiveSmallIntegerField()
    text = models.TextField()


class SoshialNetwork(models.Model):
    """Link to a specified social network"""
    class Type(models.TextChoices):
        GIHUB = "github", "Github"
        GILAB = "gitlab", "Gitlab"
        LINKEDIN = "linkedin", "LinkedIn"

    type = Type
    link = models.URLField()

    class Meta:
        verbose_name = "social network"
        verbose_name_plural = "social networks"


class Profile(models.Model):
    """User's profile"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT)
    city = models.CharField(max_length=100,help_text="City where you live")
    biography = models.TextField(help_text="Tell everyone about yourself")
    skill = models.ManyToManyField(Skill, help_text="things you can do, techs you know")
    soshial_network = models.ManyToManyField(SoshialNetwork)
    preferenced_role = ''  # WIP нужно сделать команды и прописать там роли
    comments = models.ForeignKey(
        Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
