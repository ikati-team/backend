"""ikati URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from user_profile.views import UserViewSet
from team.views import TeamViewSet, CreateTeamViewSet, CurrentUserInviteViewSet, CreateInviteViewSet
from search.views import CurrentUserViewSet, CurrentUserTeamsViewSet
from authentication.views import LoginView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'team_create', CreateTeamViewSet)
router.register(r'current_user', CurrentUserViewSet, basename='current_user')
router.register(r'current_user_teams', CurrentUserTeamsViewSet, basename='current_user_teans')
router.register(r'invites', CurrentUserInviteViewSet, basename='invites')
router.register(r'invites/create', CreateInviteViewSet, basename='invites_create')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
