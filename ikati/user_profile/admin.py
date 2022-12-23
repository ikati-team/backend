from django.contrib import admin
from user_profile.models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    model = SocialNetwork


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    model = Skill
