from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets

from django.contrib.auth.models import User
from user_profile.serializers import UserSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpecifiedUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        name = self.request.query_params.get('username')
        queryset = User.objects.filter(username=name)
        return queryset
2