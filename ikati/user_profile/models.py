from django.db import models
from django.conf import settings


class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "skill"
        verbose_name_plural = "skills"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ManyToManyField(settings.AUTH_USER_MODEL)
    mark = models.PositiveSmallIntegerField()
    text = models.TextField()


class SoshialNetwork(models.Model):
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
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT)
    biography = models.TextField()
    skill = models.ManyToManyField(Skill)
    Soshial_network = models.ManyToManyField(SoshialNetwork)
    preferenced_role = ''  # WIP нужно сделать команды и прописать там роли
    comments = models.ForeignKey(
        Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
