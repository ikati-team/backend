from rest_framework import permissions, viewsets

from django.contrib.auth.models import User
from user_profile.serializers import UserSerializer, CreateUserSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.AllowAny]
