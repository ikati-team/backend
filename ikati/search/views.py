from rest_framework import permissions, viewsets

from django.contrib.auth.models import User
from user_profile.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CurrentUserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        name = self.request.user
        queryset = User.objects.filter(username=name)
        return queryset
