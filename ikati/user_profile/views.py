from rest_framework import permissions, viewsets

from django.contrib.auth.models import User
from .models import Profile
from user_profile.serializers import UserSerializer, CreateUserSerializer, AllSkillsSerializer, CreateUserProfileSerilizer
from .models import Skill


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllSkillsViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = AllSkillsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]


class CreateUserProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = CreateUserProfileSerilizer
    permission_classes = [permissions.AllowAny]

