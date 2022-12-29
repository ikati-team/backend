from django.contrib import admin
from team.models import *


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    model = Team


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    model = TeamMember


@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    model = Invite


@admin.register(TextNote)
class TeamAdmin(admin.ModelAdmin):
    model = TextNote
