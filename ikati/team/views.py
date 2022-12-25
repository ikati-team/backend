from rest_framework import permissions, viewsets

from team.models import Team,  TeamMember
from team.serializers import TeamSerializer, TeamMemberSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]