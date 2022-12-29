from rest_framework import permissions, viewsets

from django.contrib.auth.models import User
from team.models import TeamMember, Team
from team.serializers import TeamSerializer
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


class CurrentUserTeamsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        name = self.request.user
        user = User.objects.get(username=name)
        team_membership = TeamMember.objects.filter(user=user)
        queryset = set()
        for i in team_membership:
            queryset.add(i.team)
        return queryset
